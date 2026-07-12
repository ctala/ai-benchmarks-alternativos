#!/usr/bin/env python3
"""
Genera RECOMENDACIONES.md desde docs/data/models.json.

POR QUE EXISTE
--------------
RECOMENDACIONES.md se escribia a mano y NO estaba en regenerate_all.py. Resultado
(auditoria 12-jul-2026): 81 dias sin tocar, una seccion "### Hermes" duplicada por
un find-replace que nadie releyo, y recomendaba modelos que hoy estan **#86, #90,
#95 y #97 de 98**. Era el doc con forma de DECISION -- el que un emprendedor
efectivamente lee para elegir -- y era el unico que se pudria solo.

Ironia: models.json se regeneraba a diario y el doc que traduce esos datos a una
decision, nunca. Prioridad invertida.

QUE CAMBIA RESPECTO AL VIEJO
----------------------------
No recomienda "el #1 del ranking". Recomienda **el mas barato de los que empatan
en calidad** (ver bands.py): los modelos de la cima son estadisticamente
indistinguibles, asi que pagar mas por decimales de score es tirar plata.

Uso:
    python benchmarks/generate_recomendaciones.py        # stdout
    python benchmarks/generate_recomendaciones.py -i     # escribe RECOMENDACIONES.md
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bands import verdict, quality_bands, is_local  # noqa: E402

ROOT = Path(__file__).parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
OUT = ROOT / "RECOMENDACIONES.md"

CALLS = 3000  # ~100/dia

# Casos de negocio -> pilar del benchmark que los mide.
CASOS = [
    ("Agentes y automatizaciones (n8n, Hermes)", "Agentes",
     "El modelo decide y llama herramientas. Necesitás fiabilidad en tool calling."),
    ("Contenido y marketing (blog, SEO, copy)", "Contenido",
     "Texto largo en español neutro. El costo manda: es alto volumen."),
    ("Código y debugging", "Coding",
     "Generación y corrección de código."),
    ("Razonamiento y estrategia", "Razonamiento",
     "Análisis, decisiones, problemas con varios pasos."),
]

PRESUPUESTOS = [
    ("Menos de $10/mes", 10),
    ("Hasta $30/mes", 30),
    ("Hasta $100/mes", 100),
]


def fmt(v: dict, key: str = "best") -> str:
    c = v.get(key)
    if not c:
        return "—"
    return f"**{c['name']}** — ≈${c['cost_month']:,.0f}/mes (calidad {c['quality']:.2f}/10)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in-place", action="store_true")
    args = ap.parse_args()

    data = json.loads(MODELS_JSON.read_text())
    ranked = [m for m in data["models"] if m.get("ranked")]
    L = []
    A = L.append

    A("# Recomendaciones por Caso de Uso")
    A("")
    A(f"> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.")
    A(f"> **No editar a mano.** Última regeneración: {date.today().isoformat()} · "
      f"{len(ranked)} modelos con muestra sólida (≥50 runs).")
    A("")
    A("## Cómo leer esto (importante)")
    A("")
    A("**No recomendamos \"el #1 del ranking\".** Los modelos de la cima **empatan "
      "estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen "
      "de error de la medición. Ordenarlos por decimales de score finge una precisión que "
      "los datos no tienen.")
    A("")
    A("Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue "
      "es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que "
      "te estarías gastando de más si eligieras el más caro de ese mismo grupo.")
    A("")
    A(f"Todos los costos asumen **{CALLS:,} llamadas/mes** (≈100 por día). "
      "Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).")
    A("")
    A("---")
    A("")
    A("## Por tarea")
    A("")

    for titulo, pilar, nota in CASOS:
        v = verdict(ranked, pilar, calls_per_month=CALLS)
        if not v:
            continue
        A(f"### {titulo}")
        A("")
        A(f"_{nota}_")
        A("")
        A(f"- **Usá:** {fmt(v)}")
        if "priciest" in v:
            p = v["priciest"]
            A(f"- **Lo que te ahorrás:** {p['name']} cuesta ≈${p['cost_month']:,.0f}/mes "
              f"(**{p['times']}× más**) por apenas {p['quality_gap']:+.2f} de calidad — "
              f"dentro del margen de error.")
        if "open" in v:
            A(f"- **Mejor open-source:** {fmt(v, 'open')}")
        if "local" in v:
            A(f"- **Si tenés hardware propio:** {fmt(v, 'local')}")
        A(f"- _{v['band_size']} modelos empatan en calidad en este pilar._")
        A("")

    A("---")
    A("")
    A("## Por presupuesto")
    A("")
    A("Lo mejor que podés comprar con cada techo de gasto, a "
      f"{CALLS:,} llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.")
    A("")
    A("| Presupuesto | Modelo | Calidad | Costo real |")
    A("|---|---|---:|---:|")
    for etiqueta, techo in PRESUPUESTOS:
        cands = [m for m in ranked
                 if not is_local(m)
                 and m.get("cost_per_1k_calls_usd") is not None
                 and m["cost_per_1k_calls_usd"] * CALLS / 1000 <= techo
                 and m.get("quality_avg") is not None]
        if not cands:
            continue
        best = max(cands, key=lambda m: m["quality_avg"])
        cost = best["cost_per_1k_calls_usd"] * CALLS / 1000
        A(f"| {etiqueta} | **{best['name']}** | {best['quality_avg']:.2f} | ≈${cost:,.0f}/mes |")
    A("")

    # El dato que resume todo el proyecto.
    v = verdict(ranked, None, calls_per_month=CALLS)
    if v and "priciest" in v:
        b, p = v["best"], v["priciest"]
        A("---")
        A("")
        A("## El resumen de todo el benchmark")
        A("")
        A(f"**{v['band_size']} modelos empatan en calidad** en la cima del ranking global.")
        A("")
        A(f"El más barato de ese grupo — **{b['name']}** — sale **≈${b['cost_month']:,.0f}/mes**.")
        A(f"El más caro — **{p['name']}** — sale **≈${p['cost_month']:,.0f}/mes**.")
        A("")
        A(f"Eso es **{p['times']}× más caro** por una diferencia de calidad de "
          f"**{p['quality_gap']:+.2f} puntos**, que está dentro del margen de error.")
        A("")
        A("Si te llevás una sola cosa de este benchmark, que sea esta.")
        A("")

    out = "\n".join(L)
    if args.in_place:
        OUT.write_text(out)
        print(f"OK: RECOMENDACIONES.md regenerado ({len(CASOS)} casos, {len(ranked)} modelos)")
    else:
        print(out)


if __name__ == "__main__":
    main()
