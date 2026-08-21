#!/usr/bin/env python3
"""El `?v=` de app.js/style.css sale del CONTENIDO, no de que alguien se acuerde.

POR QUÉ EXISTE (21-ago-2026)
----------------------------
`docs/index.html` cargaba `app.js?v=20260813d`: un cache-bust escrito a mano y fechado
el **13 de agosto**. Entre esa fecha y hoy `app.js` cambió muchas veces —el wizard, los
enlaces a fichas, W16, la columna nueva— y cada uno de esos cambios llegó al navegador
de un visitante que ya había entrado **con el JavaScript viejo**, porque la URL no
cambió. Se descubrió probando la columna «Ficha» en local: el HTML era nuevo y el JS
era del 13.

Es el patrón conocido del repo con una vuelta cruel: no es una regla sin instrumento,
es un dato derivado que se mantenía a mano. El contenido ya sabe cuándo cambió — su
propio hash—, así que el token se calcula, no se recuerda.

Uso:
    python benchmarks/sync_cachebust.py           # actualiza si hace falta
    python benchmarks/sync_cachebust.py --check   # exit 1 si está desincronizado
"""

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "index.html"
ASSETS = ("app.js", "style.css")


def huella(nombre: str) -> str:
    f = DOCS / nombre
    return hashlib.sha256(f.read_bytes()).hexdigest()[:8] if f.exists() else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    html = INDEX.read_text()
    cambios, desync = [], []
    for asset in ASSETS:
        h = huella(asset)
        if not h:
            continue
        patron = re.compile(rf'({re.escape(asset)})\?v=([A-Za-z0-9._-]+)')
        m = patron.search(html)
        if not m:
            continue
        if m.group(2) != h:
            desync.append(f"{asset}: declara ?v={m.group(2)} y su contenido es {h}")
            html = patron.sub(rf'\1?v={h}', html)
            cambios.append(asset)

    if a.check:
        if desync:
            print("CACHE-BUST desincronizado:\n")
            for d in desync:
                print(f"  ❌ {d}")
            print("\n  El navegador de quien ya visitó el sitio seguirá con la versión")
            print("  vieja. Correr: python benchmarks/sync_cachebust.py")
            return 1
        print(f"  ✅ el `?v=` de {', '.join(ASSETS)} coincide con su contenido")
        return 0

    if cambios:
        INDEX.write_text(html)
        print(f"  ✅ cache-bust actualizado: {', '.join(cambios)}")
    else:
        print("  ✅ cache-bust ya estaba al día")
    return 0


if __name__ == "__main__":
    sys.exit(main())
