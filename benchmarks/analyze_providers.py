#!/usr/bin/env python3
"""
El mismo modelo, servido por dos proveedores: ¿cuánto cambia?

POR QUÉ EXISTE
--------------
Durante meses el ranking mezcló proveedores: unos modelos medidos en OpenRouter, otros
en NVIDIA NIM, Groq, Ollama Cloud o la API directa del fabricante. Eso hacía que el
`score_global` midiera **modelo × infraestructura**, no el modelo — y que un mismo modelo
ocupara dos puestos distintos del ranking.

Al separarlos, lo que parecía ruido resultó ser el hallazgo más útil del dataset:

    Qwen 3.5 397B    NVIDIA NIM    calidad 8.17
                     Ollama Cloud  calidad 5.43   ← 2.7 puntos. El MISMO modelo.

Un emprendedor que elige "Qwen 3.5 397B" cree que eligió un modelo. Eligió la mitad de la
decisión. La otra mitad —por dónde lo llama— le puede costar casi 3 puntos de calidad,
3× la velocidad, o el doble de latencia. Nadie se lo está diciendo.

Este script produce esa comparación desde los datos que ya tenemos: las filas marcadas
`provider_variant` (fuera del ranking, conservadas a propósito) contra su fila canónica
en OpenRouter.

Uso:
    python benchmarks/analyze_providers.py            # tabla
    python benchmarks/analyze_providers.py --md       # markdown para publicar
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

MODELS_JSON = ROOT / "docs" / "data" / "models.json"

# Cómo se llama, en castellano, el camino por el que medimos cada modelo.
VIA = {
    "openrouter": "OpenRouter",
    "nvidia_nim": "NVIDIA NIM",
    "groq_direct": "Groq",
    "ollama_cloud": "Ollama Cloud",
    "minimax_direct": "API directa",
    "xiaomi_direct": "API directa",
    "openai_direct": "API directa",
    "claude_code": "Claude Code CLI",
    # Self-hosted: acá la velocidad es la de TU máquina, no la de un datacenter.
    # Compararla con la nube no significa nada; se etiqueta para que no se confunda.
    "llama_server": "local (Spark)",
    "llama_server_think": "local (Spark, reasoning)",
    "ollama": "local (Ollama)",
    "diffusion_cli": "local (difusión)",
}


def familia(nombre: str) -> str:
    """El modelo, sin el paréntesis que dice por dónde lo llamamos."""
    return re.sub(r"\s*\([^)]*\)", "", nombre).strip()


def cargar():
    from benchmarks.models import MODELS
    data = json.loads(MODELS_JSON.read_text())
    prov = {c["name"]: (c.get("provider") or "openrouter")
            for c in MODELS.values() if c.get("name")}
    return data["models"], prov


def parejas(models, prov, min_runs=50):
    """Modelos medidos por >1 camino, con muestra suficiente en cada uno."""
    grupos = {}
    for m in models:
        if m.get("quality_avg") is None or m.get("runs", 0) < min_runs:
            continue
        if m.get("retired"):
            continue
        grupos.setdefault(familia(m["name"]), []).append(m)
    return {k: v for k, v in grupos.items() if len(v) > 1}


def fmt(v, n=2, suf=""):
    return "—" if v is None else f"{v:.{n}f}{suf}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true", help="Salida markdown")
    args = ap.parse_args()

    models, prov = cargar()
    pares = parejas(models, prov)
    if not pares:
        print("No hay ningún modelo medido por más de un proveedor con muestra suficiente.")
        return 0

    filas = []
    for fam, ms in sorted(pares.items()):
        ms = sorted(ms, key=lambda m: -(m.get("quality_avg") or 0))
        mejor, peor = ms[0], ms[-1]
        dq = (mejor.get("quality_avg") or 0) - (peor.get("quality_avg") or 0)
        filas.append((dq, fam, ms))
    filas.sort(reverse=True)

    if args.md:
        print("| Modelo | Se llama por | Calidad | tok/s | TTFT | Δ calidad |")
        print("|---|---|---:|---:|---:|---:|")
        for dq, fam, ms in filas:
            for i, m in enumerate(ms):
                v = VIA.get(prov.get(m["name"], ""), prov.get(m["name"], "?"))
                d = f"**{dq:+.2f}**" if i == 0 and len(ms) > 1 else ""
                print(f"| {fam if i == 0 else ''} | {v} | {fmt(m.get('quality_avg'))} | "
                      f"{fmt(m.get('tokens_per_second'), 0)} | {fmt(m.get('latency_avg_s'), 1, 's')} | {d} |")
        return 0

    print("\n  EL MISMO MODELO, DISTINTO PROVEEDOR")
    print("  " + "─" * 68)
    print("  Ordenado por cuánto cambia la CALIDAD. Si el modelo fuera lo único que")
    print("  importa, esta columna sería cero en todas las filas.\n")
    for dq, fam, ms in filas:
        alerta = "  ⚠️" if dq >= 1.0 else ""
        print(f"  {fam}{alerta}")
        for m in ms:
            v = VIA.get(prov.get(m["name"], ""), "?")
            print(f"     {v:<17} calidad {fmt(m.get('quality_avg')):>5} │ "
                  f"{fmt(m.get('tokens_per_second'), 0):>4} tok/s │ "
                  f"TTFT {fmt(m.get('latency_avg_s'), 1, 's'):>6} │ {m['runs']:>3} runs")
        if dq >= 1.0:
            print(f"     └─ {dq:.2f} puntos de calidad separan al mismo modelo de sí mismo.")
        print()

    grandes = [f for f in filas if f[0] >= 1.0]
    print("  " + "─" * 68)
    print(f"  {len(filas)} modelos medidos por más de un camino · "
          f"{len(grandes)} cambian ≥1 punto de calidad según por dónde se llamen.")
    if grandes:
        dq, fam, _ = grandes[0]
        print(f"  El peor: {fam}, {dq:.2f} puntos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
