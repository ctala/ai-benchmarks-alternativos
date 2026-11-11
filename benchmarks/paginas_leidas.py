#!/usr/bin/env python3
"""Un guardrail que deja de leer falla solo: cuenta las páginas que revisó contra el registro.
(11-nov-2026, change `motor-sitio` 2.3, regla de Cristian)

POR QUÉ EXISTE
--------------
Al poner el HTML de Astro (`dist`) en lugar del de Python (`docs/`), `check_ganadores` y
`check_cortes` leyeron cero filas, y `check_consistency` dejó 29 páginas sin verificar **en
verde**. Un guardrail cuyo lector no reconoce el HTML no falla: no encuentra nada que objetar.
Comparar `docs/` contra `dist` lo destapó una vez; no puede depender de que alguien se acuerde.

La regla: cada guardrail portado dice qué páginas leyó y falla si son menos de las que el
registro (`registro_paginas.py`) le asigna. Así, uno que en el futuro deje de leer, por un
cambio de plantilla o de ruta, falla solo.

Uso desde un guardrail:
    import paginas_leidas as pl
    esperadas = pl.esperadas(tipos={"ranking"})
    ... leer, y por cada página leída: leidas.add(url) ...
    fallos += pl.exigir("check_x", leidas, esperadas)
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))


def esperadas(tipos: set[str] | None = None, con_redirects: bool = False) -> set[str]:
    """Las URLs que el registro asigna: de esos tipos (todos si None), sin los redirects salvo
    que se pidan (un redirect no tiene contenido que revisar)."""
    import registro_paginas as rp
    return {e["url"] for e in rp.paginas()
            if (tipos is None or e["tipo"] in tipos) and (con_redirects or not e["redirect_a"])}


def url_de(base: Path, html: Path) -> str:
    """La URL pública de un `index.html` bajo `base` (`docs/` o `dist`)."""
    rel = html.parent.relative_to(base)
    return "/" if str(rel) == "." else f"/{rel.as_posix()}/"


def exigir(nombre: str, leidas: set[str], esperadas_: set[str]) -> list[str]:
    """Imprime cuántas leyó y devuelve el fallo si faltan páginas que le corresponden."""
    faltan = sorted(esperadas_ - leidas)
    print(f"  · {nombre}: {len(esperadas_ & leidas)} de {len(esperadas_)} página(s) que le asigna el registro")
    if not faltan:
        return []
    muestra = ", ".join(faltan[:5]) + (" …" if len(faltan) > 5 else "")
    return [f"{nombre} leyó {len(esperadas_) - len(faltan)} de {len(esperadas_)} páginas: "
            f"no revisó {len(faltan)} ({muestra}). Un guardrail que no lee no encuentra nada que objetar."]
