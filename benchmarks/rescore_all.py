#!/usr/bin/env python3
"""
Re-puntúa TODO el histórico desde las respuestas guardadas. Sin llamar a un solo modelo.

POR QUÉ
-------
El scorer de los tests de tipo `reasoning` era una bolsa de palabras: exigía que ≥60% de
las palabras de cada insight aparecieran LITERALMENTE en el texto. Eso no medía si el
modelo entendió; medía si usaba nuestro vocabulario.

Caso real, puntuado 1.7/10:

    "No se puede saber si la secuencia de emails funcionó. Tienes TRES INTERVENCIONES
     SIMULTÁNEAS... no hay datos de atribución que permitan separar su impacto."

Es exactamente el insight esperado ("correlación no implica causalidad", "otras variables
cambiaron en paralelo"), dicho impecable. Reprobó por no escribir esas palabras.

El spread que producía ese ruido (6.00 entre modelos) parecía discriminación. No lo era:
correlacionaba **-0.29** con string_precision. Estábamos ordenando modelos por su parecido
con nuestro diccionario. 2.544 runs de 10 suites arrastran ese error.

QUÉ CAMBIA
----------
1. `reasoning` → verificador semántico (benchmarks/verifier.py). Le pregunta a un LLM,
   por cada insight, "¿el texto afirma esta idea?". Verificable, admite sinónimos.
2. Tests con `expected_answer` → **el juez LLM ya no opina**. Probamos seis jueces sin
   conflicto de interés, de 14B a 671B: todos saturan (phi-4: 100% de techo, correlación
   0.00 con la trampa aritmética). Donde hay hechos, no hace falta una opinión.

POR QUÉ SE PUEDE HACER SIN GASTAR EN MODELOS
--------------------------------------------
Porque las respuestas están guardadas. Generar una respuesta es caro; puntuarla es
barato. Este script es la prueba de que esas dos cosas tienen que estar separadas:
corregir el scorer cuesta ~$1, no una noche entera de re-correr el benchmark.

AUDITORÍA
---------
El archivo original se copia a `results/_archive-pre-verificador/` ANTES de tocarlo.
Nunca se pierde cómo se puntuó antes. El export solo lee el nivel superior de results/,
así que el archivo no se cuenta dos veces.

Uso:
    python benchmarks/rescore_all.py --dry-run     # cuántos y cuánto cuesta
    python benchmarks/rescore_all.py               # hacerlo
"""
import argparse
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

RESULTS = ROOT / "benchmarks" / "results"
RESPONSES = RESULTS / "responses"
ARCHIVE = RESULTS / "_archive-pre-verificador"

PESO_RUBRICA = 0.3
PESO_JUEZ = 0.7
MARCADOR = "## Respuesta completa\n"


def indice_tests():
    from benchmarks.runner import ALL_TEST_SUITES
    return {(s, t["name"]): t for s, ts in ALL_TEST_SUITES.items() for t in ts}


def indice_modelos():
    from benchmarks.models import MODELS, OLLAMA_MODELS
    return {c["name"]: k for k, c in {**MODELS, **OLLAMA_MODELS}.items() if c.get("name")}


def leer_respuesta(stamp: str, model_key: str, suite: str, test: str) -> str | None:
    f = RESPONSES / stamp / f"{model_key}__{suite}__{test}.md"
    if not f.exists():
        return None
    t = f.read_text(encoding="utf-8")
    return t.split(MARCADOR, 1)[1].strip() if MARCADOR in t else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--suite", default=None,
                    help="Solo re-puntuar runs cuya suite empiece con este prefijo "
                         "(ej. agent_long_horizon). Sin esto, re-puntúa todas.")
    args = ap.parse_args()

    from benchmarks.config import OPENROUTER_API_KEY
    from benchmarks.scoring import (compute_final_score, score_content_quality,
                                    score_expected_answer, set_verifier)
    from benchmarks.verifier import Verifier

    TESTS = indice_tests()
    KEY = indice_modelos()

    # Inventario: qué runs se pueden re-puntuar (tienen respuesta en disco).
    trabajo = []
    for f in sorted(RESULTS.glob("benchmark_*.json")):
        m = re.search(r"benchmark_(\d{8}_\d{6}(?:_\d+)?)", f.name)
        if not m:
            continue
        stamp = m.group(1)
        if not (RESPONSES / stamp).is_dir():
            continue
        try:
            data = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        rows = data if isinstance(data, list) else data.get("results", [])
        pend = []
        for r in rows:
            if not isinstance(r, dict) or not r.get("success"):
                continue
            suite, tn = r.get("suite"), r.get("test_name")
            if args.suite and not str(suite or "").startswith(args.suite):
                continue
            t = TESTS.get((suite, tn))
            mk = KEY.get(r.get("model", ""))
            if not t or not mk or not t.get("expected_answer"):
                continue
            pend.append((r, t, mk))
        if pend:
            trabajo.append((f, data, stamp, pend))

    total = sum(len(p) for _, _, _, p in trabajo)
    reasoning = sum(1 for _, _, _, p in trabajo for _, t, _ in p
                    if t["expected_answer"].get("type") == "reasoning")
    calls = sum(len(t["expected_answer"].get("key_insights", []))
                for _, _, _, p in trabajo for _, t, _ in p
                if t["expected_answer"].get("type") == "reasoning")

    print(f"\n  {len(trabajo)} archivos · {total} runs con verdad verificable")
    print(f"  de esos, {reasoning} son tipo `reasoning` → {calls} verificaciones")
    print(f"  costo estimado: ~${calls * 0.00009:.2f}  (cero llamadas a los modelos)\n")
    if args.dry_run:
        print("  (correr sin --dry-run para hacerlo)")
        return 0

    V = Verifier(OPENROUTER_API_KEY)
    if V.score("Los costos suman 9.150.", ["los costos suman 9150"]) < 0:
        sys.exit("ERROR: el verificador no responde. No re-puntúo nada.")
    set_verifier(V)
    print(f"  Verificador: {V.model} — prueba OK\n")

    ARCHIVE.mkdir(exist_ok=True)
    hechos = fallidos = 0

    for f, data, stamp, pend in trabajo:
        def uno(item):
            r, t, mk = item
            resp = leer_respuesta(stamp, mk, r["suite"], r["test_name"])
            if not resp:
                return None
            try:
                answer = score_expected_answer(resp, t["expected_answer"])
            except RuntimeError:
                return None  # el verificador falló en este run: se deja como estaba
            content = score_content_quality(resp, t.get("criteria", {}))

            # QUÉ PESA EN UN TEST CON TRAMPA
            #
            # auto_quality era `content*0.4 + answer*0.6`. Pero `content` mide LARGO,
            # FORMATO, SECCIONES E IDIOMA. En un test cuya gracia es si cazaste que los
            # costos suman 9.150 y no 7.400, el formato es RUIDO — y al sacar el juez ese
            # 40% pasó a decidir la calidad. Resultado: los modelos que formatean lindo
            # subían solos. Gemini 2.5 Flash Lite (barato, rápido, prolijo) llegó a #1.
            #
            # Donde hay verdad verificable, la nota ES si la cazó. El formato no salva a
            # quien publicó un número falso con viñetas impecables.
            quality = answer
            sc = compute_final_score(quality, float(r.get("speed") or 0),
                                     float(r.get("latency") or 0),
                                     float(r.get("tool_calling") or 0),
                                     float(r.get("cost_usd") or 0))
            return r, content, answer, sc

        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for out in ex.map(uno, pend):
                if out is None:
                    fallidos += 1
                    continue
                r, content, answer, sc = out
                # Guardamos los COMPONENTES, no solo el compuesto. Si mañana queremos
                # re-pesar (¿el formato cuenta algo? ¿cuánto?), sale gratis: no hay que
                # volver a llamar al verificador ni, mucho menos, a los modelos.
                # Guardar solo el número final fue el error que nos obligó a pagar dos veces.
                r["content_score"] = round(content, 2)
                r["answer_score"] = round(answer, 2)
                r["auto_quality"] = round(answer, 2)
                r["quality"] = sc["quality"]
                r["final"] = sc["final"]
                # Misma marca de procedencia que estampa el runner. Sin esto no se puede
                # saber con qué fórmula se calculó `quality` — que es la causa raíz de
                # haber promediado escalas incompatibles durante meses.
                r["scoring"] = "verificable"
                r["rescored_by"] = "verificador-semantico"
                r["rescored_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                hechos += 1

        # El original, intacto, queda archivado ANTES de reescribir.
        if not (ARCHIVE / f.name).exists():
            shutil.copy(f, ARCHIVE / f.name)
        if isinstance(data, dict):
            data.setdefault("metadata", {})["rescore"] = {
                "scorer": "verificador-semantico (benchmarks/verifier.py)",
                "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "cambio": "reasoning: keywords → verificación semántica · "
                          "tests con expected_answer: sin juez LLM",
            }
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        print(f"  {f.name[:46]:<48} {len(pend):>4} runs", flush=True)

    print(f"\n  ♻️  {hechos} runs re-puntuados"
          f"{f' · {fallidos} sin respuesta guardada' if fallidos else ''}")
    print(f"  Originales archivados en {ARCHIVE.relative_to(ROOT)}/ (auditoría)")
    print("  Ahora: python benchmarks/export_for_pages.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
