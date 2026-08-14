#!/usr/bin/env python3
"""Detecta CAMINOS DE MEDICIÓN paralelos al instrumentado.

POR QUÉ EXISTE (14-ago-2026)
----------------------------
El 13-ago escribí `tareas-agente/cotizar/correr.py`: un script propio que llamaba a los
modelos por HTTP, los puntuaba y guardaba resultados. Al hacerlo perdí de golpe TODOS los
guardrails, y volví a pisar cinco pozos que este repo ya tenía tapados:

  · `max_tokens=1500` → los 6 modelos devolvieron vacío   (resuelto en adapters.py, abril)
  · una respuesta vacía puntuaba 7/17                     (el runner distingue 3 estados)
  · corrida secuencial, ~75 min en vez de ~12             (Regla 0 del RUNBOOK, julio)
  · sin canario                                            (el gate se agregó ESE MISMO día)
  · sin guardar entrada ni salida                          (rompe `rescore` — ayer se
                                                            re-puntuaron 10.503 runs gracias
                                                            a que el runner sí las guarda)

Ninguno fue mala suerte. Todos son consecuencia de una sola decisión: **construir por
fuera.** Y la lección de esta semana —*una regla sin instrumento que la haga cumplir es una
regla que ya se rompió*— aplica un nivel más arriba: **un instrumento que se puede esquivar
escribiendo un script nuevo, se esquiva.**

Este chequeo es ese instrumento. Marca cualquier archivo que llame a una API de modelos y
no esté en la lista de caminos sancionados.

Uso:  python benchmarks/check_caminos.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Los ÚNICOS lugares por donde se mide. Todo lo demás que llame a un modelo es un desvío.
SANCIONADOS = {
    "providers/adapters.py",        # el adapter — thinking budget, timeouts, ruteo
    "providers/registry.py",
    "benchmarks/runner.py",         # el runner — canario, resume, 3 estados de vacío
    "benchmarks/config.py",
    "benchmarks/models.py",
    "benchmarks/llm_judge.py",
    "benchmarks/verifier.py",
    "benchmarks/canario.py",
    "benchmarks/check_endpoints.py",
    "benchmarks/rejudge.py",
    "benchmarks/rescore_all.py",
    "benchmarks/judge_bakeoff.py",
    "benchmarks/sync_prices.py",
    "benchmarks/variance_analysis.py",
    "benchmarks/generate_manual_landings.py",
    "benchmarks/check_caminos.py",  # este archivo los nombra
    # GENERA contenido, no mide: escribe posts desde INSIGHTS.md y no produce ningún
    # puntaje (verificado: cero menciones a quality/score). Llamar a un modelo para
    # PRODUCIR es legítimo; lo que no puede pasar por afuera es MEDIR.
    "scripts/generate_blog_post.py",
}

LLAMA_A_MODELO = re.compile(
    r'openrouter\.ai/api|api\.openai\.com|/chat/completions|anthropic\.com/v1/messages',
    re.I)


def main() -> int:
    desvios = []
    for p in ROOT.rglob("*.py"):
        rel = p.relative_to(ROOT).as_posix()
        if ".venv" in rel or "node_modules" in rel or rel in SANCIONADOS:
            continue
        try:
            if LLAMA_A_MODELO.search(p.read_text(encoding="utf-8", errors="ignore")):
                desvios.append(rel)
        except Exception:
            continue

    if desvios:
        print(f"  ❌ {len(desvios)} camino(s) de medición fuera del runner:\n")
        for d in desvios:
            print(f"     {d}")
        print("\n  Un script propio que llama a los modelos pierde de golpe: el gate del")
        print("  canario, el presupuesto de los thinking models, los tres estados de")
        print("  respuesta vacía, la paralelización y el guardado de entrada/salida.")
        print("  El 13-ago eso costó seis bugs y tres relanzamientos.")
        print("\n  Medí por `runner.py`, o por Harbor si es una tarea agéntica.")
        print("  Si el camino nuevo es legítimo, agregalo a SANCIONADOS con su razón.")
        return 1

    print(f"  ✅ ningún camino de medición fuera de los {len(SANCIONADOS)} sancionados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
