#!/usr/bin/env python3
"""Paridad: lo que compila Astro publica lo mismo que publica hoy Python, salvo lo declarado.
(11-nov-2026, change `motor-sitio`, design.md D9)

POR QUÉ EXISTE
--------------
El corte reemplaza `docs/` por lo que compila Astro. Si una página cambia de contenido sin que
nadie lo haya decidido, el corte lo publica en silencio. Acá se compara el `contrato-pagina`
de cada página migrada (`recomienda`, `ordena_por`, `filas` por tabla) contra el de `docs/`, y
toda diferencia tiene que estar DECLARADA:

  - un modelo que SALE de una comparación por familia: está en `fuera` del export, con su
    motivo de elegibilidad (R1 estricta, decisión de Cristian del 11-nov-2026);
  - un modelo que ENTRA: rankea, y solo puede entrar en una página donde salió alguno (ocupa
    el lugar del que salió);
  - una página que pasa a redirect: el registro la declara (`redirect_a`, con su motivo);
  - una congelada: su contrato tiene que ser idéntico al de hoy.

También las URLs: cada URL de `docs/` existe en `dist` o es `legado` en el registro.

Uso:
    python benchmarks/paridad_sitio.py --dist sitio/dist
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))
import contrato_pagina  # noqa: E402
import registro_paginas as rp  # noqa: E402


def _html(base: Path, url: str) -> Path:
    return base / url.strip("/") / "index.html" if url != "/" else base / "index.html"


def revisar(dist: Path, docs: Path, datos: Path, regs: list[dict], ranked_por_nombre: dict[str, bool]):
    fallos, declaradas = [], []
    por_url = {e["url"]: e for e in regs}
    for url in sorted(rp.urls_en_docs(docs)):
        e = por_url.get(url)
        if e is None:
            fallos.append(f"{url}: está en docs/ y no en el registro")
        elif e["motor"] == "astro" and not _html(dist, url).exists():
            fallos.append(f"{url}: se perdió (no está en dist)")

    for e in regs:
        if e["motor"] != "astro":
            continue
        fa, fd = _html(dist, e["url"]), _html(docs, e["url"])
        if not fa.exists() or not fd.exists():
            continue  # la URL perdida ya se reportó; una página nueva no tiene con qué compararse
        ca, cd = contrato_pagina.leer(fa.read_text(encoding="utf-8")), contrato_pagina.leer(fd.read_text(encoding="utf-8"))
        if ca is None:
            fallos.append(f"{e['url']}: la página compilada no declara contrato")
            continue
        if e["redirect_a"]:
            if ca.get("tipo") != "redirect":
                fallos.append(f"{e['url']}: el registro la declara redirect y compila como {ca.get('tipo')}")
            elif cd and cd.get("tipo") != "redirect":
                declaradas.append(f"{e['url']}: pasa a redirect → /{e['redirect_a']}/ ({e['motivo']})")
            continue
        if cd is None:
            fallos.append(f"{e['url']}: la versión de Python no declara contrato; no hay con qué comparar")
            continue
        if ca.get("ordena_por") != cd.get("ordena_por"):
            fallos.append(f"{e['url']}: ordena_por cambió: «{cd.get('ordena_por')}» → «{ca.get('ordena_por')}»")
        ra, rd = list(ca.get("recomienda") or []), list(cd.get("recomienda") or [])
        filas_a = [t.get("filas") for t in ca.get("tablas") or []]
        filas_d = [t.get("filas") for t in cd.get("tablas") or []]
        if e["congelada"]:
            if ra != rd or filas_a != filas_d:
                fallos.append(f"{e['url']}: está congelada y su contrato cambió (recomienda o filas)")
            continue
        jf = datos / "comparaciones" / f"{e['slug']}.json"
        fuera = {m["name"]: m for m in (json.loads(jf.read_text(encoding="utf-8"))["fuera"] if jf.exists() else [])}
        salen = [n for n in rd if n not in ra]
        entran = [n for n in ra if n not in rd]
        for n in salen:
            if n in fuera:
                declaradas.append(f"{e['url']}: sale {n} (R1: {fuera[n]['motivo']})")
            else:
                fallos.append(f"{e['url']}: sale {n} sin estar declarado en `fuera`")
        for n in entran:
            if not ranked_por_nombre.get(n):
                fallos.append(f"{e['url']}: entra {n}, que no rankea")
            elif not salen:
                fallos.append(f"{e['url']}: entra {n} sin que haya salido nadie")
            else:
                declaradas.append(f"{e['url']}: entra {n} (ocupa el lugar de uno que salió por R1)")
        if len(filas_a) != len(filas_d):
            fallos.append(f"{e['url']}: cambió el número de tablas ({len(filas_d)} → {len(filas_a)})")
        elif filas_a and filas_a[0] != len(ra):
            fallos.append(f"{e['url']}: la tabla declara {filas_a[0]} filas y recomienda {len(ra)}")
    return fallos, declaradas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=ROOT / "sitio" / "dist")
    ap.add_argument("--docs", type=Path, default=ROOT / "docs")
    ap.add_argument("--datos", type=Path, default=ROOT / "sitio" / "src" / "datos")
    ap.add_argument("--detalle", action="store_true", help="lista cada diferencia declarada")
    a = ap.parse_args()
    if not a.dist.is_dir():
        print(f"  ❌ no existe {a.dist}: correr `npm run build` en sitio/")
        return 1
    d = json.loads((a.docs / "data" / "models.json").read_text(encoding="utf-8"))
    ranked = {m["name"]: bool(m.get("ranked")) for m in d["models"] if m.get("ranked")}
    fallos, declaradas = revisar(a.dist, a.docs, a.datos, rp.paginas(), ranked)
    print("PARIDAD — docs/ (Python) contra dist (Astro)\n")
    print(f"  {len(declaradas)} diferencias declaradas (redirects y filas que salen por R1)")
    if a.detalle:
        for x in declaradas:
            print(f"     · {x}")
    for x in fallos:
        print(f"  ❌ {x}")
    if not fallos:
        print("  ✅ cada diferencia está declarada; ninguna URL se pierde")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
