#!/usr/bin/env python3
"""
Genera el Top 10 Global del README desde docs/data/models.json.

POR QUE EXISTE
--------------
El top-10 del README se escribia a mano y quedaba desactualizado en silencio.
No era descuido: el score_global es un z-score normalizado contra la poblacion,
asi que al agregar UN modelo nuevo se recalculan TODOS los scores. Un README
escrito a mano queda obsoleto en el momento exacto en que se mide algo nuevo.

Julio 2026: el README publicaba Grok 4.5 = 6.99 mientras el sitio (generado
desde models.json) mostraba 5.84. Misma fuente, dos numeros publicos distintos.
Este script cierra ese agujero: el README pasa a derivarse de la fuente unica.

Solo rankea modelos con muestra solida (>=50 runs, campo `ranked`), igual que
las paginas pSEO. Ver MIN_RUNS_RANKED en export_for_pages.py.

Uso:
    python benchmarks/generate_readme_ranking.py        # imprime a stdout
    python benchmarks/generate_readme_ranking.py -i     # actualiza README.md in-place
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
README = ROOT / "README.md"

START = "<!-- AUTO-RANKING-START -->"
END = "<!-- AUTO-RANKING-END -->"

TOP_N = 10


def load_ranked() -> tuple[list[dict], dict]:
    if not MODELS_JSON.exists():
        raise FileNotFoundError(
            f"No existe {MODELS_JSON}. Corré `python benchmarks/export_for_pages.py` primero."
        )
    data = json.loads(MODELS_JSON.read_text())
    ranked = [
        m for m in data.get("models", [])
        if m.get("ranked") and m.get("score_global") is not None
    ]
    # Orden por CALIDAD: desde v4.1 el titular responde "¿qué modelo es mejor?".
    # El compuesto (score_global) va en su propia tabla, más abajo.
    ranked.sort(key=lambda m: -(m.get("score_calidad") or 0))
    return ranked, data


def fmt_cost(m: dict) -> str:
    c = m.get("cost_per_1k_calls_usd")
    return f"${c:,.2f}" if c is not None else "—"


def build_block(ranked: list[dict], data: dict) -> str:
    min_runs = data.get("thresholds", {}).get("ranked_min_runs", 50)
    ranked_count = data.get("ranked_count", len(ranked))

    lines = [
        START,
        "",
        f"> Auto-generado por `benchmarks/generate_readme_ranking.py` desde "
        f"`docs/data/models.json`. **No editar a mano** — el z-score se recalcula "
        f"con cada modelo nuevo y una tabla escrita a mano queda obsoleta sola.",
        "",
        "### Índice de calidad — ¿qué modelo responde mejor?",
        "",
        "Solo calidad. **El precio y la velocidad se muestran al lado, no van dentro del "
        "número** — un modelo caro no es peor, es caro, y mezclarlo esconde cuál es cuál.",
        "",
        "| # | Modelo | Calidad | $/1k calls | Latencia | Provider | Runs |",
        "|---|---|---:|---:|---:|---|---:|",
    ]
    for i, m in enumerate(ranked[:TOP_N], 1):
        lat = m.get("latency_avg_s")
        lines.append(
            f"| {i} | **{m['name']}** | **{(m.get('score_calidad') or 0):.2f}** | "
            f"{fmt_cost(m)} | {f'{lat:.0f}s' if lat is not None else '—'} | "
            f"{m.get('provider', '?')} | {m.get('runs', 0)} |"
        )

    por_valor = sorted(ranked, key=lambda m: -m["score_global"])[:TOP_N]
    lines += [
        "",
        "### Mejor valor — ¿qué me conviene pagar?",
        "",
        "Acá sí entra el precio: calidad (70%), costo (15%), velocidad (7,5%) y latencia "
        "(7,5%) para un perfil de emprendedor genérico. **Es otra pregunta, no un ranking "
        "mejor.**",
        "",
        "| # | Modelo | Valor | Calidad | $/1k calls | Provider |",
        "|---|---|---:|---:|---:|---|",
    ]
    for i, m in enumerate(por_valor, 1):
        lines.append(
            f"| {i} | **{m['name']}** | **{m['score_global']:.2f}** | "
            f"{(m.get('score_calidad') or 0):.2f} | {fmt_cost(m)} | {m.get('provider', '?')} |"
        )

    lines += [
        "",
        f"> **Piso de ranking: {min_runs} runs.** Solo compiten los {ranked_count} modelos con "
        f"muestra sólida. Con 3-12 runs la varianza permite liderar por azar, así que los "
        f"emergentes se listan aparte, en *En evaluación* de [MODELOS.md](MODELOS.md), con su "
        f"score marcado como indicativo.",
        "",
        f"> **Por qué dos tablas y no una.** Hasta v4.0 publicábamos un solo número que mezclaba "
        f"calidad con precio, y eso movía modelos sin avisar: Claude Opus 4.6 es **#5 en "
        f"calidad** y salía **#18**; Poolside Laguna XS es **#29 en calidad** y salía **#7**. "
        f"Las dos cifras eran verdad, pero bajo un rótulo que no lo decía. Separadas, cada una "
        f"responde su pregunta.",
        "",
        f"> **Ninguna de las dos es tu caso exacto.** Si corrés batch de noche, la latencia no te "
        f"importa y la tabla de valor la penaliza igual; si atendés usuarios en vivo, te importa "
        f"el doble. Ajustá los pesos en la [calculadora]"
        f"(https://benchmarks.cristiantala.com/) o mirá las tablas por caso de uso en "
        f"[MODELOS.md](MODELOS.md).",
        "",
        END,
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in-place", action="store_true", help="Actualiza README.md in-place")
    args = ap.parse_args()

    ranked, data = load_ranked()
    block = build_block(ranked, data)

    if not args.in_place:
        print(block)
        return

    content = README.read_text()
    if START in content and END in content:
        new_content = re.sub(
            rf"{re.escape(START)}.*?{re.escape(END)}", block, content, flags=re.DOTALL
        )
    else:
        raise SystemExit(
            f"ERROR: no encontré los marcadores {START} / {END} en README.md.\n"
            "Agregalos alrededor de la tabla del Top 10 para que este script la mantenga."
        )
    README.write_text(new_content)
    print(f"OK: README.md — top {min(TOP_N, len(ranked))} regenerado ({len(ranked)} modelos rankeados)")


if __name__ == "__main__":
    main()
