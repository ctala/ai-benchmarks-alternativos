#!/usr/bin/env python3
"""Fecha cada página de `dist` por su contenido: `dateModified`, «Última actualización» y el
`lastmod` del sitemap cambian solo si cambió lo que la página dice. (11-nov-2026, motor-sitio 2.4)

POR QUÉ EXISTE
--------------
Los generadores ponían la fecha de hoy en cada regeneración. El 11-nov, 135 páginas amanecieron
con `lastmod` de ese día por commits que no les cambiaron una palabra, y las landings pasaban a
«Última actualización: hoy» cada vez que se corría `regenerate_all`. Un `lastmod` que siempre
dice hoy es un `lastmod` que Google deja de leer. Era la tarea 5.4 de `corte-v5-1`.

CÓMO
----
`sitio/fechas_contenido.json` (versionado) guarda por URL la huella del contenido
(`fechas.huella`: texto de <main> y JSON-LD, sin la fecha misma, sin cabecera, pie, CSS ni JS)
y la fecha en que cambió por última vez. En cada build, después de copiar el legado:

  · huella igual a la registrada → la página lleva la fecha registrada;
  · huella distinta o URL nueva   → hoy, y el registro se actualiza (hay que commitearlo).

Corre igual sobre las páginas de Astro y las del legado: las dos llegan a `dist` con la fecha de
hoy y salen con la de su último cambio.

LO QUE VERIFICA `--check` (bloqueante en el build y en el QA)
  F1  la fecha de cada página es la del registro, y la huella registrada es la de la página: un
      contenido que cambió sin fecha nueva, o una fecha nueva sin cambio de contenido, es rojo.
  F2  el `lastmod` de cada URL del sitemap es la fecha de su página.
  F3  regla de páginas leídas.

Uso:
    python benchmarks/fechar_dist.py --dist sitio/dist            # fecha y actualiza el registro
    python benchmarks/fechar_dist.py --dist sitio/dist --check    # solo verifica
    python benchmarks/fechar_dist.py --dist sitio/dist --sembrar  # primera vez (ver `sembrar`)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fechas  # noqa: E402

SITE = "https://benchmarks.cristiantala.com"
LASTMOD = re.compile(r"(<loc>([^<]+)</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)")


def paginas(dist: Path):
    import paginas_leidas as pl
    for f in sorted(dist.rglob("index.html")):
        h = f.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in h:
            continue
        yield pl.url_de(dist, f), f, h


def fechar_sitemap(texto: str, fecha_de_url: dict) -> str:
    def r(m):
        url = m.group(2).replace(SITE, "") or "/"
        return m.group(1) + fecha_de_url.get(url, m.group(3)) + m.group(4)
    return LASTMOD.sub(r, texto)


def sembrar(dist: Path, registro: dict, rama: str = "main") -> int:
    """Primera vez: una página cuyo contenido es el mismo que el publicado en `rama` conserva la
    fecha publicada (su `dateModified`, o el `lastmod` del sitemap publicado); la que cambió
    lleva hoy. Así el corte no estrena 184 páginas «modificadas hoy»."""
    sm = subprocess.run(["git", "show", f"{rama}:docs/sitemap.xml"], cwd=ROOT,
                        capture_output=True, text=True).stdout
    lastmod = {m.group(2).replace(SITE, "") or "/": m.group(3) for m in LASTMOD.finditer(sm)}
    n = 0
    for url, f, h in paginas(dist):
        rel = "docs" + (url if url != "/" else "/") + "index.html"
        pub = subprocess.run(["git", "show", f"{rama}:{rel}"], cwd=ROOT,
                             capture_output=True, text=True).stdout
        if pub and fechas.huella(pub) == fechas.huella(h):
            m = fechas.FECHA_MOD.search(pub)
            fecha = m.group(2) if m else lastmod.get(url, fechas.hoy())
            n += 1
        else:
            fecha = fechas.hoy()
        registro[url] = {"huella": fechas.huella(h), "modificada": fecha}
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, required=True)
    ap.add_argument("--registro", type=Path, default=fechas.REGISTRO)
    ap.add_argument("--check", action="store_true", help="solo verifica (F1-F3); no escribe nada")
    ap.add_argument("--sembrar", action="store_true", help="primera vez: fechas de lo publicado en main")
    a = ap.parse_args()
    import paginas_leidas as pl
    registro = fechas.leer_registro(a.registro)

    if a.check:
        fallos, leidas, fecha_url = [], set(), {}
        for url, f, h in paginas(a.dist):
            leidas.add(url)
            e = registro.get(url)
            m = fechas.FECHA_MOD.search(h)
            if not e:
                fallos.append(f"F1 · {url}: no está en el registro de fechas (¿no corrió el fechado?)")
                continue
            fecha_url = {**fecha_url, url: e["modificada"]}
            if e["huella"] != fechas.huella(h):
                fallos.append(f"F1 · {url}: el contenido cambió y la fecha no (registro: {e['modificada']})")
            if m and m.group(2) != e["modificada"]:
                fallos.append(f"F1 · {url}: publica dateModified {m.group(2)} y su último cambio de "
                              f"contenido es del {e['modificada']}")
            for u in fechas.ULTIMA.findall(h):
                if u[1] != e["modificada"]:
                    fallos.append(f"F1 · {url}: dice «Última actualización: {u[1]}» y su último cambio "
                                  f"de contenido es del {e['modificada']}")
        sm = a.dist / "sitemap.xml"
        if sm.exists():
            for m in LASTMOD.finditer(sm.read_text(encoding="utf-8")):
                url = m.group(2).replace(SITE, "") or "/"
                if url in fecha_url and m.group(3) != fecha_url[url]:
                    fallos.append(f"F2 · sitemap: {url} lleva lastmod {m.group(3)} y su página es del {fecha_url[url]}")
        else:
            fallos.append("F2 · falta sitemap.xml en el árbol")
        print(f"FECHAS POR CONTENIDO — {len(leidas)} página(s) de {a.dist}")
        fallos += pl.exigir("F3", leidas, pl.esperadas())
        if fallos:
            for x in fallos[:40]:
                print(f"  ❌ {x}")
            print(f"\n  ❌ {len(fallos)} fecha(s) que no dicen cuándo cambió la página.")
            return 1
        print("  ✅ cada dateModified, «Última actualización» y lastmod es la fecha del último cambio de contenido")
        return 0

    if a.sembrar:
        n = sembrar(a.dist, registro)
        print(f"registro sembrado: {n} página(s) conservan la fecha publicada en main; el resto, hoy")
    hoy = fechas.hoy()
    cambiadas, fecha_url = 0, {}
    for url, f, h in paginas(a.dist):
        fecha, cambio = fechas.fecha_de(url, h, registro, hoy)
        cambiadas += cambio
        fecha_url[url] = fecha
        nuevo = fechas.fechar(h, fecha)
        if nuevo != h:
            f.write_text(nuevo, encoding="utf-8")
    sm = a.dist / "sitemap.xml"
    if sm.exists():
        sm.write_text(fechar_sitemap(sm.read_text(encoding="utf-8"), fecha_url), encoding="utf-8")
    # Una URL que ya no se publica sale del registro: si vuelve, vuelve con fecha nueva.
    registro = {u: e for u, e in registro.items() if u in fecha_url}
    fechas.escribir_registro(registro, a.registro)
    print(f"fechas por contenido: {len(fecha_url)} página(s), {cambiadas} con contenido nuevo (fecha {hoy})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
