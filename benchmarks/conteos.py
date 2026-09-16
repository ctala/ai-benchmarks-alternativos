#!/usr/bin/env python3
"""Los conteos que se publican, definidos UNA sola vez.

POR QUÉ EXISTE (16-sep-2026)
----------------------------
«Ejecuciones» tenía **dos definiciones vivas, y las dos se publicaban**: los docs decían
48.822 (`sum(runs)`, lo atribuido a cada modelo del catálogo) y el sitio decía 68.667
(`total_runs_measured`, todo lo que se corrió de verdad, descartes incluidos). Ninguna de
las dos está mal; tenerlas juntas sí — y el pilar del blog tuvo que elegir una a mano.

Es el mismo patrón que ya costó caro con `suites.del_indice()`: dos definiciones del mismo
concepto conviviendo, y cada consumidor eligiendo la suya. Antes de escribir un criterio,
buscar si ya hay una función que lo responda; si no la hay, es ésta la que hay que ampliar.

La canónica es **`total_runs_measured`** —lo que la máquina ejecutó— porque es la que ya
sirven el sitio (`app.js`), `llms.txt`, las páginas pSEO y el README como «runs reales».
"""
from __future__ import annotations


def ejecuciones(data: dict) -> int:
    """Total de ejecuciones medidas del dataset (`docs/data/models.json`).

    El fallback suma los runs por modelo, y existe sólo para datasets viejos anteriores a
    que el export publicara el campo: da un número MENOR (no cuenta los descartados), así
    que si aparece en algo publicado es señal de que el dataset está desactualizado.
    """
    return int(data.get("total_runs_measured")
               or sum(m.get("runs", 0) or 0 for m in data.get("models", [])))
