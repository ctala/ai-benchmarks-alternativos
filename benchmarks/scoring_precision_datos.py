"""Scorer de la suite `precision_datos`: crédito parcial por ítem, comparación EXACTA.

POR QUÉ NO ALCANZAN LOS SCORERS DE `scoring.py` (9-nov-2026)
------------------------------------------------------------
- `exact_string` da 7 si coincide el 99 % de los caracteres: en una cadena de 120
  caracteres eso es un dígito cambiado en un RUT, y un RUT con un dígito cambiado es
  otra persona. Acá un carácter vale lo mismo que la cadena entera.
- `numeric` tolera ±3 % y su parser acepta `1.234,00` y `1,234.00` como el mismo
  número. Eso es justo lo que esta suite mide: convertir de formato sin cambiar el valor.
- `exact_vs_distractor` quita puntos y comas antes de comparar, así que no ve un
  separador regional mal puesto.

Cómo puntúa
-----------
`expected_answer = {"type": "precision_items", "items": [...]}`. Cada ítem es una cadena
o una lista de cadenas aceptables. La respuesta se lee como líneas; cada ítem cuenta si
alguna línea, EN ORDEN, es exactamente ese ítem (subsecuencia común más larga, así una
frase de cortesía antes o después no corre a todos los ítems, y dos líneas intercambiadas
no suman las dos).

    nota = 10 × ítems exactos / (ítems pedidos + líneas de datos sobrantes)

Las «líneas de datos sobrantes» cierran un atajo: sin ellas, devolver el catálogo
entero (60 líneas) contendría las dos pedidas en orden y sacaría 10, igual que dar las
dos CLABE, la vieja y la nueva. Una línea sobrante es una que no calza con ningún ítem,
tiene al menos un dígito (la cortesía sin cifras —«Aquí tienes:»— no se castiga) y no
ocupa el lugar de un ítem fallado (un ítem mal copiado ya cuesta su ítem; no se cobra
dos veces).

Lo único que se limpia antes de comparar es lo que no es el dato: espacios en los
bordes, comillas o backticks que envuelven la línea, negritas de markdown, una viñeta
o numeración de lista al inicio y las líneas de cerco de código. Se normaliza a Unicode
NFC (una «ñ» compuesta y una descompuesta son la misma letra). Nada más: ni mayúsculas,
ni puntos finales, ni separadores.
"""

from __future__ import annotations

import re
import unicodedata

_MARCADOR_LISTA = re.compile(r"^(?:[-*•·]|\d{1,3}[.)])\s+")
_CERCO = re.compile(r"^```[\w-]*$")


def _nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def _variantes(linea: str) -> set[str]:
    """Las formas de una línea que se aceptan como «el dato» (sin tocar el dato)."""
    base = _nfc(linea).strip()
    out = {base}
    for _ in range(2):
        nuevas = set()
        for v in out:
            w = v.strip()
            if w.startswith("**") and w.endswith("**") and len(w) > 4:
                nuevas.add(w[2:-2].strip())
            if len(w) >= 2 and w[0] == w[-1] and w[0] in "\"'`":
                nuevas.add(w[1:-1].strip())
            m = _MARCADOR_LISTA.match(w)
            if m:
                nuevas.add(w[m.end():].strip())
        out |= nuevas
    return out


def _lineas(response: str) -> list[set[str]]:
    lineas = []
    for raw in (response or "").splitlines():
        s = raw.strip()
        if not s or _CERCO.match(s):
            continue
        lineas.append(_variantes(s))
    return lineas


def _aceptables(item) -> set[str]:
    if isinstance(item, (list, tuple)):
        return {_nfc(x).strip() for x in item}
    return {_nfc(str(item)).strip()}


def items_exactos(response: str, items: list) -> int:
    """Cuántos ítems aparecen exactos y en orden (LCS sobre líneas)."""
    return _conteo(response, items)[0]


def _conteo(response: str, items: list) -> tuple[int, int]:
    """(ítems exactos en orden, líneas con dígitos que no calzan con ningún ítem)."""
    lineas = _lineas(response)
    objetivos = [_aceptables(i) for i in items]
    n, m = len(objetivos), len(lineas)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if objetivos[i] & lineas[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    # líneas que no calzan con NINGÚN ítem y traen alguna cifra
    todos = set().union(*objetivos) if objetivos else set()
    sin_calce = sum(1 for l in lineas
                    if not (l & todos) and any(ch.isdigit() for ch in min(l, key=len)))
    return dp[0][0], sin_calce


def score_precision_items(response: str, expected: dict) -> float:
    items = expected.get("items") or []
    if not items:
        raise ValueError("precision_items sin `items`: no hay contra qué comparar")
    n = len(items)
    aciertos, sin_calce = _conteo(response, items)
    sobrantes = max(0, sin_calce - (n - aciertos))
    return round(10.0 * aciertos / (n + sobrantes), 2)
