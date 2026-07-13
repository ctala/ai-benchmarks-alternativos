"""Re-juzga post-hoc un results JSON cuyas evaluaciones de juez fallaron.

Contexto (jun 2026): el bug del base_url hardcodeado en llm_judge.py hacía que
el juez fallara silenciosamente y el 100% de los tests quedara con score
automático (quality == auto_quality). Este script toma el JSON de resultados,
relee cada respuesta completa desde results/responses/<ts>/*.md, la evalúa con
el juez indicado y recalcula quality y final con la MISMA fórmula del runner:

    quality = auto_quality * 0.3 + judge_quality * 0.7
    final   = compute_final_score(quality, speed, latency, tool_calling, cost)

Uso:
    python benchmarks/rejudge.py <results.json> --judge-model phi4-spark [--dry-run]

Solo re-juzga entradas con success=True y quality == auto_quality (juez ausente).
Guarda backup <results.json>.pre-rejudge antes de escribir. Suites NIAH se
saltan (retrieval puro, no usan juez — igual que el runner).
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from benchmarks.llm_judge import LLMJudge, JUDGE_PRESETS, judge_score_to_10
from benchmarks.scoring import compute_final_score


def build_test_index():
    """Indexa los tests de todas las suites por (suite, test_name) → dict del test."""
    from benchmarks import runner as _r
    idx = {}
    # ALL_TEST_SUITES mapea suite_name → lista de tests (no módulo)
    for suite_name, tests in _r.ALL_TEST_SUITES.items():
        for t in tests:
            idx[(suite_name, t["name"])] = t
    return idx


def read_full_response(responses_root: Path, model_key: str, suite: str, test_name: str) -> str | None:
    """Lee la respuesta completa desde el .md guardado por el runner."""
    matches = list(responses_root.glob(f"*/{model_key}__{suite}__{test_name}.md"))
    if not matches:
        return None
    # tomar el más reciente si hay varios timestamps
    path = max(matches, key=lambda p: p.stat().st_mtime)
    text = path.read_text(encoding="utf-8")
    marker = "## Respuesta completa\n"
    return text.split(marker, 1)[1].strip() if marker in text else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results_json")
    ap.add_argument("--judge-model", default="phi4-spark")
    ap.add_argument("--model-key", default=None,
                    help="Key del modelo en MODELS (para ubicar responses). Default: inferido del filename de responses.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    preset = JUDGE_PRESETS[args.judge_model]
    # Un preset con api_key=None significa "usá la key de OpenRouter" (así lo resuelve
    # create_judge). Pasar el None crudo hace que el juez falle en TODAS las evaluaciones
    # y el script reporte alegremente "juez falló, se mantiene auto" 602 veces — que es
    # exactamente el silencio que este script existe para reparar.
    api_key = preset["api_key"]
    if api_key is None:
        from benchmarks.config import OPENROUTER_API_KEY
        api_key = OPENROUTER_API_KEY
    judge = LLMJudge(api_key=api_key, base_url=preset["base_url"],
                     judge_model=preset["model"], provider=preset["provider"])

    # Prueba de vida ANTES de recorrer 600 runs. Sin esto, un juez roto produce un
    # informe de 600 líneas que dice "todo bien, se mantiene auto" y no arregla nada.
    _p = judge.evaluate("Madrid es la capital de España.",
                        {"name": "_probe", "prompt": "¿Cuál es la capital de España?"}, "_probe")
    if _p.get("score_final", -1) < 0:
        sys.exit(f"ERROR: el juez «{args.judge_model}» no responde. No re-juzgo nada.")
    print(f"Juez: {preset['model']} — prueba OK ({_p.get('score_final')}/5)")

    path = Path(args.results_json)
    data = json.loads(path.read_text())
    results = data["results"]
    test_idx = build_test_index()
    responses_root = path.parent / "responses"

    pending = [r for r in results
               if r.get("success")
               and r.get("quality") == r.get("auto_quality")
               and not str(r.get("suite", "")).startswith("niah")]
    print(f"{len(results)} resultados | a re-juzgar: {len(pending)}")

    rejudged, missing_resp, judge_fail = 0, 0, 0
    for i, r in enumerate(pending, 1):
        suite, tname = r.get("suite", ""), r.get("test_name", "")
        test = test_idx.get((suite, tname))
        if test is None:
            print(f"  [{i}/{len(pending)}] {suite}/{tname}: test no encontrado en suites, skip")
            continue
        # ubicar el archivo de respuesta: el runner usa el key del modelo en el filename
        model_key = args.model_key
        resp = None
        if model_key:
            resp = read_full_response(responses_root, model_key, suite, tname)
        else:
            # inferir: probar con cualquier archivo que matchee __suite__test
            matches = list(responses_root.glob(f"*/*__{suite}__{tname}.md"))
            if matches:
                m = max(matches, key=lambda p: p.stat().st_mtime)
                text = m.read_text(encoding="utf-8")
                marker = "## Respuesta completa\n"
                resp = text.split(marker, 1)[1].strip() if marker in text else None
        if not resp:
            resp = r.get("response_preview") or None
            if not resp:
                missing_resp += 1
                continue
        jr = judge.evaluate(resp, test, suite)
        j10 = judge_score_to_10(jr)
        if j10 < 0:
            judge_fail += 1
            print(f"  [{i}/{len(pending)}] {suite}/{tname}: juez falló, se mantiene auto")
            continue
        auto_q = float(r.get("auto_quality") or 0)
        new_quality = auto_q * 0.3 + j10 * 0.7
        new_scores = compute_final_score(
            new_quality,
            float(r.get("speed") or 0),
            float(r.get("latency") or 0),
            float(r.get("tool_calling") or 0),
            float(r.get("cost_usd") or 0),
        )
        r["quality"] = new_scores["quality"]
        r["final"] = new_scores["final"]
        r["judge_quality"] = round(j10, 2)
        # mismos campos que escribe el runner (export_for_pages lee judge_score 0-5)
        r["judge_score"] = jr.get("score_final", -1)
        r["judge_justificacion"] = jr.get("justificacion", "")
        r["rejudged"] = True
        rejudged += 1
        print(f"  [{i}/{len(pending)}] {suite}/{tname}: auto={auto_q} juez={j10:.1f} → quality={r['quality']} final={r['final']}")

    meta = data.setdefault("metadata", {})
    meta["rejudge"] = {"judge_model": preset["model"], "base_url": preset["base_url"],
                       "rejudged": rejudged, "judge_fail": judge_fail, "missing_resp": missing_resp}
    print(f"\nre-juzgados: {rejudged} | juez falló: {judge_fail} | sin respuesta: {missing_resp}")

    if args.dry_run:
        print("(dry-run: no se escribió nada)")
        return
    shutil.copy(path, str(path) + ".pre-rejudge")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"escrito {path} (backup .pre-rejudge)")


if __name__ == "__main__":
    main()
