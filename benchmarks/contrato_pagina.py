#!/usr/bin/env python3
"""EL CONTRATO DE UNA PÁGINA: qué publica, según ella misma.

POR QUÉ EXISTE (17-ago-2026)
----------------------------
Cristian, después del cuarto arreglo seguido en el auditor: *"solucionemos de manera
definitiva lo de las páginas"*.

Los arreglos anteriores fueron todos el mismo arreglo. El auditor **adivinaba la
estructura del HTML con expresiones regulares**, y las 71 páginas tienen **ocho formas
distintas** —con o sin columna de puesto, de una a cinco tablas—. Cada regex cubría unas
y dejaba otras afuera:

    P2 mezclaba las filas de las dos tablas de una página y la declaraba desordenada
    P3 no miraba 10 páginas porque su tabla no lleva columna de puesto
    P1 correlacionaba filas de dos tablas distintas
    P4 contaba «cero filas» en páginas con 19 y 48
    P6 leía «vacío» toda celda que empezara con <strong>

Cinco síntomas, una causa: **el HTML publicado no dice qué es**. Y mientras el auditor
tenga que inferirlo, cada formato nuevo abre un punto ciego nuevo.

LA SOLUCIÓN
-----------
La página **declara** lo que publica, en un bloque JSON embebido que el generador emite y
el auditor lee. Se acaba la adivinanza:

    <script type="application/json" id="contrato-pagina">
    {"tipo": "ranking", "generador": "generate_rankings",
     "ordena_por": "Calidad en Agentes", "recomienda": ["Claude Opus 4.8", ...],
     "tablas": [{"rol": "principal", "ordena_por": "…", "filas": 8}, …]}
    </script>

No es metadata decorativa: es el **contrato** que la página promete cumplir, y el auditor
verifica contra los datos. Una página sin contrato falla — así un formato nuevo no puede
entrar en silencio, que es exactamente lo que venía pasando.

Es la misma idea que ya resolvió dos problemas en este repo: el registro de suites (la
lista existía tres veces y divergía) y `m["elegible"]` (76 condicionales decidiendo lo
mismo por su cuenta). Cuando el dato viaja declarado, nadie tiene que reconstruirlo.
"""

import json
import re

CLAVES = ("tipo", "generador", "recomienda")
TIPOS = ("ranking", "comparacion", "variantes", "landing", "explicativa", "redirect",
         # `ficha`: una página por modelo (`/modelo/<key>/`). Publica los números de UN
         # modelo y enlaza los oficiales al fabricante en vez de copiarlos.
         "ficha")

_RE = re.compile(
    r'<script type="application/json" id="contrato-pagina">\s*(\{.*?\})\s*</script>',
    re.S)


def emitir(tipo, generador, recomienda, ordena_por=None, tablas=None, nota=None):
    """El bloque que cada generador incrusta en su HTML.

    `recomienda` son los nombres de modelo que la página pone como opción para el lector
    — no todos los que menciona. Es lo que el auditor contrasta contra `elegible`: un
    retirado o un no-apto ahí es un problema, nombrarlo en una explicación no lo es.
    """
    assert tipo in TIPOS, f"tipo de página desconocido: {tipo}"
    c = {"tipo": tipo, "generador": generador, "recomienda": list(recomienda)}
    if ordena_por:
        c["ordena_por"] = ordena_por
    if tablas:
        c["tablas"] = tablas
    if nota:
        c["nota"] = nota
    return ('<script type="application/json" id="contrato-pagina">\n'
            + json.dumps(c, ensure_ascii=False) + "\n</script>")


def leer(html):
    """El contrato de una página, o None si no lo declara."""
    m = _RE.search(html)
    if not m:
        return None
    try:
        c = json.loads(m.group(1))
    except json.JSONDecodeError:
        return None
    return c if all(k in c for k in CLAVES) else None
