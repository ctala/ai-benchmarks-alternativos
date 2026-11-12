#!/usr/bin/env python3
"""Los validadores del registro de páginas: R0-R6. (11-nov-2026, change `motor-sitio`)

POR QUÉ EXISTE
--------------
Al 11-nov, 24 de las 27 comparaciones de versión exacta mostraban modelos que ya habían
salido del ranking, y ningún chequeo lo veía: cada generador tenía su lista y nadie
declaraba la página como tal. El motor nuevo declara cada URL en `registro_paginas.py`;
este script hace que esa declaración no sea una promesa.

  R0  el registro es coherente (sin duplicados, redirects a destinos que existen, una
      congelada siempre con fecha y motivo).
  R1  una página Astro muestra un modelo fuera del ranking vigente (`ranked` falso) sin estar
      congelada; o una congelada no muestra el aviso.
  R2  una cifra visible del HTML compilado no viene marcada con `data-cifra`. Quedan exentos los
      años, las fechas, los nombres de modelo (que van marcados con `data-modelo`) y `EXENTAS`.
  R3  una URL publicada (directorios de `sitio/legado/` y `sitio/legado/sitemap.xml`) no tiene entrada en el
      registro, o no existe en `dist` ni como página ni como redirect correcto.
  R4  un `index.html` de `dist` no tiene entrada en el registro.
  R6  `sitemap.xml` y `llms.txt` listan exactamente los destinos del registro: ningún redirect
      (Google no indexa lo que la página misma marca `noindex`) y ningún destino afuera. Se
      revisan los de `sitio/legado/` y, con `--dist`, también los copiados a `dist`. (motor-sitio 2.3)
  R5  un modelo fuera del ranking no tiene motivo registrado (o `ranked` contradice a su
      elegibilidad). Sin motivo, una página no puede decir por qué un modelo no está; es un
      error de datos (Cristian, 11-nov-2026). Corre siempre, con o sin build.

LO QUE LAS PLANTILLAS DEBEN EMITIR (el contrato con Astro):
  - `data-modelo="<key>"` en todo elemento que nombra a un modelo;
  - `data-cifra` en todo elemento cuyo texto es una cifra (celdas, `<Cifra>`, conteos);
  - `data-nombre` en un nombre que no es un solo modelo (la etiqueta de una familia, el id de
    una suite, «Phi-4»): R2 no lo lee como cifra;
  - `data-anterior="<key>"` en el pie «Versiones anteriores»: los modelos que salen de la tabla
    por R1, con su ficha. Ahí R1 exige lo contrario: que NO rankeen;
  - `data-congelada` en el aviso de una página congelada;
  - en un redirect, meta refresh 0 y canonical al destino, y `noindex, follow`.

Se mira lo COMPILADO y no la fuente: una cifra escrita en el código de una plantilla también sale.

Las páginas `legado` (el HTML de Python) siguen bajo los guardrails de hoy hasta que su sesión las
migre. Desde la tarea 2.2 (`COPIA_LEGADO`), `copiar_legado.py` las lleva a `dist` y R3 las busca
ahí: lo que no esté en `dist` el corte lo borraría. Sin `--dist`, R3 sigue mirando `sitio/legado/`.

Uso:
    python benchmarks/check_registro.py --dist sitio/dist   # dentro de `npm run build`
    python benchmarks/check_registro.py                     # sin build: solo R0 y R3 contra sitio/legado/
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))
import registro_paginas as rp  # noqa: E402

SITE = "https://benchmarks.cristiantala.com"
COPIA_LEGADO = True    # tarea 2.2: `dist` lleva también lo legado (copiar_legado.py)

# Texto con dígitos que no es una cifra del benchmark. Cada uno con su motivo.
EXENTAS: dict[str, str] = {}
# Términos con dígitos que son nombres, no cifras. Llegan en textos de los datos (la
# descripción de un pilar, el motivo de elegibilidad), donde no hay un componente que marcar.
TERMINOS: dict[str, str] = {
    "N8N": "nombre de producto (la descripción del pilar Agentes)",
    "v5": "nombre de la versión del examen (el motivo «histórico» de elegibilidad)",
    "B2B": "término de negocio (los casos de uso de un ranking: «newsletters B2B»)",
}

_MESES = "ene|feb|mar|abr|may|jun|jul|ago|sep|sept|oct|nov|dic"
_EXENTO_RE = re.compile(
    rf"\b(?:19|20)\d\d-\d\d-\d\d\b"                 # 2026-11-11
    rf"|\b\d{{1,2}}(?:-| de )(?:{_MESES})[a-z]*(?:-| de )(?:19|20)\d\d\b"   # 11-nov-2026, 11 de noviembre de 2026
    rf"|\b(?:19|20)\d\d\b",                         # años
    re.I)
_VACIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
           "source", "track", "wbr"}
_OCULTOS = {"head", "script", "style", "noscript", "template", "svg"}


class _Lector(HTMLParser):
    """Junta los modelos marcados, el aviso de congelada y el texto visible sin marcar."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila: list[tuple[str, bool, bool]] = []   # (tag, marcado, oculto)
        self.modelos: list[str] = []
        self.anteriores: list[str] = []
        self.congelada = False
        self.sueltos: list[str] = []
        self.refresh = self.canonical = self.robots = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "data-modelo" in a:
            self.modelos.append(a["data-modelo"] or "")
        if "data-anterior" in a:
            self.anteriores.append(a["data-anterior"] or "")
        if "data-congelada" in a:
            self.congelada = True
        if tag == "meta" and (a.get("http-equiv") or "").lower() == "refresh":
            self.refresh = a.get("content")
        if tag == "meta" and a.get("name") == "robots":
            self.robots = a.get("content")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag in _VACIOS:
            return
        padre_m = self.pila[-1][1] if self.pila else False
        padre_o = self.pila[-1][2] if self.pila else False
        marca = any(k in a for k in ("data-cifra", "data-modelo", "data-nombre", "data-anterior"))
        self.pila.append((tag, padre_m or marca,
                          padre_o or tag in _OCULTOS))

    def handle_endtag(self, tag):
        for i in range(len(self.pila) - 1, -1, -1):
            if self.pila[i][0] == tag:
                del self.pila[i:]
                return

    def handle_data(self, data):
        if not self.pila or self.pila[-1][1] or self.pila[-1][2]:
            return
        if re.search(r"\d", data):
            self.sueltos.append(" ".join(data.split()))


def leer(html: str) -> _Lector:
    p = _Lector()
    p.feed(html)
    return p


def cifras_sueltas(textos: list[str]) -> list[str]:
    out = []
    for t in textos:
        if t in EXENTAS:
            continue
        limpio = _EXENTO_RE.sub("", t)
        for term in TERMINOS:
            limpio = re.sub(rf"\b{re.escape(term)}\b", "", limpio)
        if re.search(r"\d", limpio):
            out.append(t[:90])
    return out


def publicadas(docs: Path) -> set[str]:
    urls = rp.urls_en_docs(docs)
    sm = docs / "sitemap.xml"
    if sm.exists():
        for loc in re.findall(r"<loc>([^<]+)</loc>", sm.read_text(encoding="utf-8")):
            ruta = loc.replace(SITE, "") or "/"
            if ruta.endswith("/"):
                urls.add(ruta)
    return urls


def revisar(dist: Path | None, docs: Path, regs: list[dict], ranked: dict[str, bool]) -> list[str]:
    fallos = [f"R0 · {x}" for x in rp.errores(regs)]
    por_url = {e["url"]: e for e in regs}

    def html_de(base: Path, url: str) -> Path:
        return base / url.strip("/") / "index.html" if url != "/" else base / "index.html"

    # R3 · lo publicado sigue existiendo
    for url in sorted(publicadas(docs)):
        e = por_url.get(url)
        if e is None:
            fallos.append(f"R3 · {url}: publicada y sin entrada en el registro")
            continue
        if dist is None:
            continue
        legado = e["motor"] == "legado" and not COPIA_LEGADO
        f = html_de(docs if legado else dist, url)
        if not f.exists():
            fallos.append(f"R3 · {url}: publicada y no existe en {'docs' if legado else 'dist'}")
    if dist is None:
        return fallos

    for e in regs:
        if e["motor"] != "astro":
            continue
        f = html_de(dist, e["url"])
        if not f.exists():
            fallos.append(f"R3 · {e['url']}: el registro la declara en Astro y no está en dist")
            continue
        p = leer(f.read_text(encoding="utf-8"))
        if e["redirect_a"]:
            destino = f"{SITE}/{e['redirect_a']}/"
            if not (p.refresh and p.refresh.replace(" ", "") == f"0;url={destino}"
                    and p.canonical == destino and p.robots and "noindex" in p.robots):
                fallos.append(f"R3 · {e['url']}: no redirige bien a {destino} "
                              "(meta refresh 0, canonical y noindex)")
            continue
        fuera = sorted({k for k in p.modelos if not ranked.get(k, False)})
        if fuera and not e["congelada"]:
            fallos.append(f"R1 · {e['url']}: muestra modelos fuera del ranking vigente sin estar "
                          f"congelada: {', '.join(fuera)}")
        vigentes = sorted({k for k in p.anteriores if ranked.get(k, False)})
        if vigentes:
            fallos.append(f"R1 · {e['url']}: lista como versión anterior a modelos que rankean: "
                          f"{', '.join(vigentes)}")
        if e["congelada"] and not p.congelada:
            fallos.append(f"R1 · {e['url']}: está congelada y no muestra el aviso (data-congelada)")
        for c in cifras_sueltas(p.sueltos):
            fallos.append(f"R2 · {e['url']}: cifra sin data-cifra: «{c}»")

    # R4 · nada compilado fuera del registro
    for f in sorted(dist.rglob("index.html")):
        rel = f.parent.relative_to(dist).as_posix()
        url = "/" if rel == "." else f"/{rel}/"
        if url not in por_url:
            fallos.append(f"R4 · {url}: está en dist y no en el registro")
    return fallos


def revisar_indices(base: Path, regs: list[dict]) -> list[str]:
    """R6: el sitemap y llms.txt de `base` listan exactamente los destinos del registro."""
    destinos = {e["url"] for e in regs if not e["redirect_a"]}
    redirects = {e["url"] for e in regs if e["redirect_a"]}
    fallos = []
    for nombre, patron in (("sitemap.xml", r"<loc>([^<]+)</loc>"),
                           ("llms.txt", r"\((https://benchmarks\.cristiantala\.com[^)\s]*)\)")):
        f = base / nombre
        if not f.exists():
            fallos.append(f"R6 · falta {base.name}/{nombre}")
            continue
        urls = {u.replace(SITE, "") or "/" for u in re.findall(patron, f.read_text(encoding="utf-8"))}
        urls = {u for u in urls if u.endswith("/")}
        if not urls:
            fallos.append(f"R6 · {nombre}: no leí ninguna URL (¿cambió el formato?)")
            continue
        for u in sorted(urls & redirects):
            fallos.append(f"R6 · {nombre} lista {u}, que el registro declara redirect")
        for u in sorted(urls - destinos - redirects):
            fallos.append(f"R6 · {nombre} lista {u}, que no está en el registro")
        for u in sorted(destinos - urls):
            fallos.append(f"R6 · {nombre} no lista {u}, que es un destino del registro")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, help="el sitio compilado (sitio/dist)")
    ap.add_argument("--docs", type=Path, default=ROOT / "sitio" / "legado")
    ap.add_argument("--models", type=Path, default=ROOT / "sitio" / "legado" / "data" / "models.json")
    a = ap.parse_args()
    if a.dist is not None and not a.dist.is_dir():
        print(f"  ❌ no existe {a.dist}: el build no produjo nada que validar")
        return 1
    d = json.loads(a.models.read_text(encoding="utf-8"))
    ranked = {m["key"]: bool(m.get("ranked")) for m in d["models"]}
    fallos = revisar(a.dist, a.docs, rp.paginas(), ranked)
    import elegibilidad
    fallos += [f"R5 · {x}" for x in elegibilidad.contradicciones(d["models"])]
    fallos += revisar_indices(a.docs, rp.paginas())
    if a.dist is not None:
        fallos += revisar_indices(a.dist, rp.paginas())
    print("REGISTRO DE PÁGINAS — R0-R6\n")
    if a.dist is None:
        print("  ⚠️  sin --dist: corrieron R0 y R3 contra sitio/legado/. R1, R2 y R4 miran lo compilado "
              "y corren dentro de `npm run build`.")
    for x in fallos:
        print(f"  ❌ {x}")
    if not fallos:
        print("  ✅ cada URL publicada está en el registro"
              + (", y lo compilado cumple R1-R4" if a.dist else ""))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
