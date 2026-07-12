#!/usr/bin/env python3
"""
Genera tabla de modelos probados para MODELOS.md con links a:
1. MD por modelo en benchmarks/results/per-model/
2. Carpeta de responses individuales

El score mostrado es el `score_global` z-scoreado de docs/data/models.json,
exactamente el mismo que usa la calculadora web. No recalcula nada desde los
JSONs crudos para evitar discrepancias.

Uso:
    python benchmarks/generate_modelos_md_table.py        # imprime tabla a stdout
    python benchmarks/generate_modelos_md_table.py -i     # actualiza MODELOS.md in-place
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
RESULTS_DIR = ROOT / "benchmarks" / "results"
PER_MODEL_DIR = RESULTS_DIR / "per-model"
RESPONSES_DIR = RESULTS_DIR / "responses"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"


def model_id_to_per_model_filename(model_id: str) -> str:
    safe = model_id.replace("/", "_").replace(".", "_").replace(":", "_")
    return f"{safe}.md"


def load_models_export():
    """Devuelve (ranked, in_review).

    ranked     = muestra solida (>=50 runs) -> entra a los rankings.
    in_review  = tiene score pero muestra chica (<50 runs) -> se muestra aparte.

    La separacion importa: con 3-12 runs un modelo puede liderar por azar. Antes
    esta tabla mezclaba ambos y coronaba #1 a un modelo con 39 runs mientras las
    paginas pSEO (que si filtran >=50) mostraban otro ganador.
    """
    if not MODELS_JSON.exists():
        raise FileNotFoundError(
            f"No existe {MODELS_JSON}. Corré `python benchmarks/export_for_pages.py` primero."
        )
    data = json.loads(MODELS_JSON.read_text())
    scored = [m for m in data.get("models", []) if m.get("score_global") is not None]
    ranked = [m for m in scored if m.get("ranked")]
    in_review = [m for m in scored if not m.get("ranked")]
    return ranked, in_review


def find_response_dirs(model_id: str) -> list[str]:
    if not RESPONSES_DIR.exists():
        return []
    found = []
    safe_id = model_id.replace("/", "_").replace(":", "_")
    for ts_dir in sorted(RESPONSES_DIR.iterdir(), reverse=True):
        if not ts_dir.is_dir():
            continue
        for f in ts_dir.iterdir():
            if not f.name.endswith(".md"):
                continue
            stem = f.name.split("__")[0]
            mid_short = model_id.split("/")[-1].replace(".", "")
            if mid_short.lower() in stem.lower() or stem.lower() in mid_short.lower():
                found.append(ts_dir.name)
                break
    return found


def build_links(model_id: str) -> tuple[str, str]:
    fname = model_id_to_per_model_filename(model_id)
    md_path = PER_MODEL_DIR / fname
    link_md = f"[per-model](benchmarks/results/per-model/{fname})" if md_path.exists() else "—"
    response_dirs = find_response_dirs(model_id)
    link_resp = f"[responses](benchmarks/results/responses/{response_dirs[0]}/)" if response_dirs else "—"
    return link_md, link_resp


def row_for_model(m: dict, score_key: str = "score_global") -> str:
    mid = m.get("id", "?")
    score = m.get(score_key)
    score_str = f"**{score:.2f}**" if score is not None else "—"
    runs = m.get("runs", 0)
    os_label = "✅" if m.get("open_source") else "❌" if m.get("open_source") is False else "?"
    license_str = m.get("license") or ""
    ci = m.get("cost_input_per_M")
    co = m.get("cost_output_per_M")
    cost = f"${ci}/{co}" if ci is not None and co is not None else "—"
    link_md, link_resp = build_links(mid)
    return (
        f"| `{mid}` | {os_label} {license_str} | {cost} | {score_str} | {runs} | {link_md} | {link_resp} |"
    )


def table_header(title: str) -> list[str]:
    return [
        f"#### {title}",
        "",
        "| Modelo | OS | $ in/out | Score | Runs | Per-model MD | Responses |",
        "|---|---|---:|---:|---:|---|---|",
    ]


def build_global_table(models: list[dict]) -> str:
    lines = table_header("Score global (perfil emprendedor: calidad 70%, costo 15%, velocidad 7.5%, latencia 7.5%)")
    for m in sorted(models, key=lambda x: -(x.get("score_global") or -1)):
        lines.append(row_for_model(m, "score_global"))
    return "\n".join(lines)


def build_quality_table(models: list[dict]) -> str:
    lines = table_header("Mejor calidad pura (sin considerar costo ni velocidad)")
    for m in sorted(models, key=lambda x: -(x.get("quality_avg") or -1)):
        lines.append(row_for_model(m, "quality_avg"))
    return "\n".join(lines)


def build_suite_table(models: list[dict], suites: list[str], title: str) -> str:
    def score(m):
        by_suite = m.get("score_by_suite", {})
        vals = [by_suite.get(s) for s in suites if by_suite.get(s) is not None]
        return sum(vals) / len(vals) if vals else -1

    lines = table_header(title)
    for m in sorted(models, key=lambda x: -score(x)):
        s = score(m)
        if s < 0:
            continue
        # Mostramos el score compuesto como score_key temporal
        m["_tmp_score"] = s
        lines.append(row_for_model(m, "_tmp_score"))
        del m["_tmp_score"]
    return "\n".join(lines)


def build_cost_efficiency_table(models: list[dict]) -> str:
    """Ranking por relación calidad/costo usando score_global_linear con pesos viejos (60/20/10/10)."""
    import statistics
    import math

    def cost_score_log(c):
        if c <= 1e-6:
            return 10.0
        return max(0.0, min(10.0, 8.0 - 3.0 * math.log10(c / 0.001)))

    tested = list(models)  # ya vienen filtrados a muestra solida (>=50 runs)
    q_vals = [m.get("quality_avg", 0) for m in tested]
    c_vals = [cost_score_log(m.get("cost_per_1k_calls_usd", 0)) for m in tested]
    s_vals = [m.get("speed_score_avg", 0) for m in tested]
    l_vals = [m.get("latency_score_avg", 0) for m in tested]

    def zscore(vals, val):
        mu = statistics.mean(vals)
        sd = statistics.pstdev(vals)
        return (val - mu) / sd if sd > 0 else 0

    # Pesos viejos v2.9: quality 60%, cost 20%, speed 10%, latency 10%
    weights = {"q": 0.60, "c": 0.20, "s": 0.10, "l": 0.10}
    for m in tested:
        zq = zscore(q_vals, m.get("quality_avg", 0))
        zc = zscore(c_vals, cost_score_log(m.get("cost_per_1k_calls_usd", 0)))
        zs = zscore(s_vals, m.get("speed_score_avg", 0))
        zl = zscore(l_vals, m.get("latency_score_avg", 0))
        z = weights["q"] * zq + weights["c"] * zc + weights["s"] * zs + weights["l"] * zl
        m["_cost_eff_score"] = max(0.0, min(10.0, 5.5 + 3.3 * z))

    lines = table_header("Mejor relación calidad/costo (pesos v2.9: 60% quality, 20% costo, 10% speed, 10% latency)")
    for m in sorted(tested, key=lambda x: -x.get("_cost_eff_score", 0)):
        lines.append(row_for_model(m, "_cost_eff_score"))
        del m["_cost_eff_score"]
    return "\n".join(lines)


def build_in_review_table(models: list[dict]) -> str:
    """Modelos con score pero muestra insuficiente para rankear (<50 runs).

    Se publican por transparencia -- no se esconden -- pero fuera del ranking:
    su score es indicativo, no comparable de igual a igual.
    """
    lines = [
        "#### En evaluación — muestra parcial (<50 runs, NO rankeados)",
        "",
        "> Estos modelos tienen menos runs que el piso del ranking, así que su score es "
        "**indicativo, no comparable**: con pocas muestras la varianza permite que un modelo "
        "quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** "
        "en las tablas de arriba hasta completar la cobertura.",
        "",
        "| Modelo | OS | $ in/out | Score (indicativo) | Runs | Per-model MD | Responses |",
        "|---|---|---:|---:|---:|---|---|",
    ]
    for m in sorted(models, key=lambda x: -(x.get("score_global") or -1)):
        lines.append(row_for_model(m, "score_global"))
    return "\n".join(lines)


def build_table(ranked: list[dict], in_review: list[dict]) -> str:
    sections = [
        build_global_table(ranked),
        "",
        build_quality_table(ranked),
        "",
        build_suite_table(ranked, ["code_generation", "structured_output", "string_precision"], "Mejor coding"),
        "",
        build_suite_table(ranked, ["deep_reasoning", "reasoning"], "Mejor razonamiento"),
        "",
        build_suite_table(ranked, ["content_generation", "startup_content", "news_seo_writing"], "Mejor contenido/marketing"),
        "",
        build_cost_efficiency_table(ranked),
    ]
    if in_review:
        sections += ["", build_in_review_table(in_review)]
    return "\n".join(sections)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in-place", action="store_true", help="Actualiza MODELOS.md in-place")
    args = ap.parse_args()

    ranked, in_review = load_models_export()
    table = build_table(ranked, in_review)

    if args.in_place:
        modelos_md = ROOT / "MODELOS.md"
        content = modelos_md.read_text()
        START = "<!-- AUTO-TABLE-START -->"
        END = "<!-- AUTO-TABLE-END -->"
        new_block = (
            f"{START}\n\n"
            "> Auto-generado por `benchmarks/generate_modelos_md_table.py`.\n\n"
            "> **No existe un único 'mejor modelo'.** El score global combina calidad, costo, "
            "velocidad y latencia con pesos elegidos para emprendedores (70% calidad, 15% costo, "
            "7.5% velocidad, 7.5% latencia) — **es un punto de partida, no un veredicto**. "
            "Un modelo puede quedar bajo en el global y ser el correcto para vos: si tu caso es "
            "batch nocturno, la latencia no te importa y el ranking la está penalizando igual. "
            "Mirá las tablas por caso de uso, y para tus propios pesos usá la "
            "[calculadora](https://benchmarks.cristiantala.com/).\n\n"
            "> **Piso de ranking: 50 runs.** Los modelos con menos muestra van a *En evaluación* "
            "al final — su score es indicativo, no comparable.\n\n"
            f"{table}\n\n"
            f"{END}"
        )

        if START in content and END in content:
            new_content = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", new_block, content, flags=re.DOTALL)
        else:
            new_content = content.replace("## Probados", f"## Probados\n\n{new_block}\n\n#### Tabla manual (legacy):", 1)
        modelos_md.write_text(new_content)
        print(f"OK: MODELOS.md actualizado — {len(ranked)} rankeados (>=50 runs), "
              f"{len(in_review)} en evaluación (<50 runs)")
    else:
        print(table)


if __name__ == "__main__":
    main()
