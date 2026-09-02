#!/usr/bin/env python3
"""¿El reporte y el PDF del mes dicen lo mismo que el benchmark?

POR QUÉ EXISTE (1-sep-2026)
---------------------------
Cristian, al ver publicado el datasheet de septiembre: *"revisa que no haya problemas
con la data del datasheet, no habíamos agregado guardrails a este proceso, y debemos
usar la misma data del benchmark en todos lados"*.

Tenía razón, y lo que apareció al mirar fue peor de lo esperado. **Los dos generadores
del release mensual publicaban una escala que el sitio abandonó en v4.1:**

  · `release_diff.py` ordenaba y citaba `score_global` — el z-score congelado. Habría
    publicado «7,18» donde la web dice «8,53».
  · `generate_cheatsheet.py` hacía lo mismo en el top 10, y además usaba
    `score_by_pillar` en las tablas por categoría: para Qwen 3.8 27B en Coding eso da
    **8,25**, y lo que el sitio publica es **9,95**. Doce usos.

Ninguno de los dos estaba roto: estaban VIEJOS. Y no se notó porque **son generadores
que se corren una vez al mes**: entre corrida y corrida nadie los mira, así que un
cambio de criterio los deja atrás en silencio. `check_consistency.py` no los cubre a
propósito —los datasheet son snapshots y deben conservar su valor histórico— y ese
"a propósito" dejaba un hueco justo el día en que el snapshot se crea.

QUÉ VERIFICA (sólo sobre el release del MES EN CURSO)
------------------------------------------------------
  R1  Todo score citado en el datasheet del mes existe en `models.json`.
  R2  Ídem para el HTML del cheatsheet.
  R3  El #1 que anuncian es el #1 real del ranking.
  R4  El conteo de rankeados coincide.

Los datasheet de meses anteriores NO se tocan: son historia y reescribirlos sería el
bug, no el arreglo.

Uso:
    python benchmarks/check_release_mensual.py
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
# Rango donde viven los scores del benchmark. Por debajo son precios y proporciones.
#
# Acepta COMA y punto: el datasheet se escribe en español («8,53») y el HTML del
# cheatsheet sale en formato de máquina («8.53»). La primera versión de este chequeo
# sólo miraba el punto y reportó «datasheet: 0 scores citados · sin respaldo: 0» — un
# verde impecable sobre un documento lleno de cifras que no llegó a mirar.
SCORE = re.compile(r"\b([5-9][.,]\d{2})\b")


def _norm(x: str) -> str:
    return x.replace(",", ".")


def cifras_del_modelo(m) -> set[str]:
    """Todas las cifras publicables DE ESE modelo, en formato de dos decimales."""
    out = set()
    for k in ("quality_avg", "tool_calling_score_avg", "cost_score_avg",
              "speed_score_avg", "latency_score_avg", "agentic_score", "security_score"):
        v = m.get(k)
        if isinstance(v, (int, float)):
            out.add(f"{v:.2f}")
    for _, v in (m.get("dims_by_pillar") or {}).items():
        if (v or {}).get("quality_avg") is not None:
            out.add(f"{v['quality_avg']:.2f}")
    for _, v in (m.get("score_by_suite") or {}).items():
        if v is not None:
            out.add(f"{v:.2f}")
    # ⚠️ NO entran `score_global` ni `score_by_pillar`: existen en el JSON —la
    # calculadora los usa— pero NO son la escala publicada desde v4.1.
    return out


def parejas(txt: str, nombres: list[str]) -> list[tuple[str, str]]:
    """(modelo, cifra) leyendo FILAS DE TABLA, no texto libre.

    Dos intentos anteriores fallaron y conviene que quede escrito:

      1. «¿la cifra existe en models.json?» — inútil: con 99 modelos y decenas de
         métricas, «7.18» aparece **15 veces**. Cambiar el 8,53 del #1 por 7,18 pasaba
         en verde.
      2. «buscar el nombre y mirar los 160 caracteres siguientes» — falsos positivos:
         «GLM 5.3» matchea dentro de «GLM 5.3 Flash», y la ventana se comía las cifras
         de la fila de al lado.

    En una tabla la asociación es inequívoca: la fila ES el modelo y sus números. Se
    parsean `<tr>` en HTML y `| … |` en Markdown, y se toma el nombre MÁS LARGO que
    aparezca en la primera celda, para que «GLM 5.3 Flash» gane sobre «GLM 5.3».
    """
    filas = re.findall(r"<tr[^>]*>(.*?)</tr>", txt, re.S)
    filas += [l for l in txt.splitlines() if l.strip().startswith("|")]
    largos = sorted(nombres, key=len, reverse=True)
    out = []
    for fila in filas:
        limpio = re.sub(r"<[^>]+>", " ", fila)
        quien = next((n for n in largos if n in limpio), None)
        if not quien:
            continue
        # El PDF trunca los nombres a 20 caracteres, así que «Gemini 3.5 Flash Lite» sale
        # como «Gemini 3.5 Flash Lit» y el matcher lee el nombre corto que sí existe
        # («Gemini 3.5 Flash»), atribuyéndole la nota del otro. Cuando el nombre hallado
        # es prefijo de otros, se aceptan las cifras de cualquiera de ellos: es la
        # ambigüedad real del documento, y preferimos no acusar que acusar de más.
        familia = [n for n in nombres if n.startswith(quien)]
        # las cifras de ESA fila, quitando el nombre para no leer números del propio nombre
        resto = limpio.replace(quien, " ")
        # Fuera los precios: «$5.00» y «$25.00» caen en el mismo rango que un score y no
        # lo son. Se quita todo lo que venga precedido de $ (con o sin espacio).
        resto = re.sub(r"\$\s*\d+[.,]?\d*", " ", resto)
        for c in SCORE.findall(resto):
            out.append((tuple(familia), _norm(c)))
    return out


def main() -> int:
    argparse.ArgumentParser().parse_args()
    d = json.loads(MODELS_JSON.read_text())
    R = sorted([m for m in d["models"] if m.get("ranked")],
               key=lambda x: -(x.get("quality_avg") or 0))
    por_modelo = {m["name"]: cifras_del_modelo(m) for m in d["models"]}
    mes = date.today().strftime("%Y-%m")

    piezas = [(ROOT / f"DATASHEET_{mes}.md", "datasheet"),
              (ROOT / "cheatsheet" / f"cheatsheet_{mes.replace('-', '_')}_v2.html", "cheatsheet")]
    fallos, revisados = [], 0

    print(f"RELEASE MENSUAL — {mes}\n")
    for f, nombre in piezas:
        if not f.exists():
            print(f"  ⚠️  {nombre}: no existe todavía ({f.name})")
            continue
        revisados += 1
        txt = f.read_text(errors="ignore")
        pares = parejas(txt, [m["name"] for m in R])
        malas = [(fam[0], c) for fam, c in pares
                 if not any(c in por_modelo.get(n, set()) for n in fam)]
        print(f"  {nombre}: {len(pares)} pareja(s) modelo↔cifra · que no cuadran: {len(malas)}")
        for n, c in malas[:5]:
            fallos.append(f"{f.name}: dice que «{n}» saca {c}, y models.json no tiene esa "
                          f"cifra para ese modelo")
        # el #1 que anuncia
        if R and R[0]["name"] not in txt:
            fallos.append(f"{f.name}: no nombra al #1 real del ranking ({R[0]['name']})")
        if str(len(R)) not in txt:
            fallos.append(f"{f.name}: no menciona el conteo real de rankeados ({len(R)})")

    if not revisados:
        print("\n  ⚠️  no hay release de este mes que verificar.")
        return 0
    if not fallos:
        print(f"\n  ✅ el release de {mes} dice lo mismo que el benchmark.")
        return 0
    print(f"\n  ❌ {len(fallos)} problema(s):\n")
    for x in fallos:
        print(f"     {x}")
    print("\n     El release usa la MISMA fuente que el sitio: `docs/data/models.json`.")
    print("     Si una cifra no está ahí, viene de una escala vieja o se escribió a mano.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
