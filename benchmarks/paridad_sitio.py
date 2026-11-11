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

AFIRMACIONES (sesión 2, rankings y variantes; Cristian, 11-nov-2026)
-------------------------------------------------------------------
Un ranking o una página de variantes afirma cosas en prosa: quién es la mejor compra, el grupo
de cabeza, el top 3, dónde queda cada familia frontier, qué tier recomendar y, suite por suite,
si el precio compra algo. La versión de Astro las genera del dato (`sitio_rankings.py`) y las
resume en `afirmaciones`; acá se leen las de `docs/` del HTML de Python y se comparan. Toda
diferencia necesita un motivo en `MOTIVOS_AFIRMACION` (por tipo de página y de afirmación); sin
motivo es rojo. El grupo de cabeza y la mejor compra salen de las mismas funciones en los dos
motores: no tienen motivo declarado y una diferencia ahí es un error.

FRASES RETIRADAS
----------------
`RETIRADAS` lista frases que `docs/` publica y que el dato ya no respalda, con su motivo. Cada
una tiene que estar en al menos una página de `docs/` de ese tipo (si no, la declaración sobra) y
en ninguna de `dist`.

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


import html as _h
import re

MOTIVOS_AFIRMACION = {
    ("ranking", "top3"): "regla del ruido: dentro del margen de error se muestra «≈» y va primero "
                         "el más barato (Cristian, 11-nov-2026)",
    ("ranking", "frontera"): "la frontera sale del campo `familia` y solo de rankeados en esta "
                             "página; antes eran siete nombres buscados por subcadena, sin mirar si "
                             "rankeaban (R1)",
    ("variantes", "veredicto"): "el tier recomendado es el más barato de los que no se separan del "
                                "mejor por el margen de error de la nota; antes, el más barato a "
                                "secas y un empate con umbral fijo de 0,30",
    ("variantes", "escalera"): "cada suite compara con su margen de error (`quality_ci95_by_suite`), "
                               "no con el umbral fijo de 0,25; con pocos tests por suite, el margen "
                               "es amplio",
}

# (tipo de página, frase visible, motivo). La frase se busca en el texto visible normalizado.
RETIRADAS = [
    ("ranking", "un modelo nuevo mueve a todos",
     "la referencia del puntaje está congelada desde v4.0: un modelo nuevo no mueve a los demás"),
    ("ranking", "Entrar es gratis",
     "CAR es de pago desde el 28-sep-2026 y está cerrada desde el 27-oct; el CTA va al go-link"),
    ("ranking", "con score global ≥ 6,8",
     "el piso de /mejor-llm-barato/ es de calidad (≥ 8,4 sobre `score_calidad`), no del score global"),
    ("ranking", "Ordenado por score global, filtrando solo modelos open source",
     "/mejor-llm-open-source/ ordena por la nota de calidad, no por el score global"),
    ("ranking", "Porque el score global pondera calidad, costo, velocidad y latencia",
     "los rankings ordenan por calidad sola: el precio no entra al orden (FAQ retirada)"),
    ("ranking", "Es la opción a vencer en esta dimensión",
     "valoración fija por puesto, sin dato que la respalde"),
    ("ranking", "Es la alternativa más sólida si el primero no encaja en tu stack",
     "valoración fija por puesto, sin dato que la respalde"),
    ("ranking", "Es una tercera opción competitiva",
     "valoración fija por puesto, sin dato que la respalde"),
    ("ranking", "puede valer la pena si ya integraste su ecosistema",
     "consejo fijo para todo modelo propietario, sin dato que lo respalde"),
    ("ranking", "casi la mitad de los modelos medidos resuelven la tarea perfecta",
     "la segunda tabla se publica por la correlación de puestos (< 0,70), que ahora se muestra"),
    ("ranking", "Mucha gente llega buscando GPT-5.6, Claude Opus/Fable o Grok",
     "nombres fijos de modelos que ya no rankean; la frontera sale del dato"),
    ("ranking", "8-12 turnos",
     "las conversaciones de `agent_long_horizon` van de 2 a 13 turnos; se cuenta del guion"),
    ("ranking", "no es solo \"el más inteligente\"",
     "afirmaba que el orden pondera costo y velocidad; el orden es por calidad sola"),
    ("variantes", "103 corridas",
     "cifra escrita a mano; las corridas salen del dato de cada tier"),
    ("variantes", "hay un caso donde el caro sí vale la pena",
     "se afirmaba siempre; ahora solo si la escalera encuentra una suite donde el caro se separa"),
    ("variantes", "rendidos por los tres",
     "«tres» fijo; el número de tiers sale del dato"),
    ("variantes", "escalera de precios de 10×",
     "cifra escrita a mano en la entrada; el múltiplo de precio sale del dato"),
    ("variantes", "la diferencia de precio entre ellas es de 12×",
     "cifra escrita a mano en la entrada; el múltiplo de precio sale del dato"),
    ("variantes", "cuestan prácticamente lo mismo",
     "afirmación de precio escrita a mano en la entrada; el múltiplo sale del dato"),
]


def _texto(html: str) -> str:
    html = re.sub(r"<(script|style|head)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return " ".join(_h.unescape(re.sub(r"<[^>]+>", " ", html)).split())


def afirmaciones_publicadas(html: str, tipo: str) -> dict:
    """Lo que afirma una página de Python, leído de su HTML (las marcas que emite su generador)."""
    if tipo == "ranking":
        g = re.search(r'data-grupo-cabeza="([^"]*)"', html)
        b = re.search(r'verdict-best">\s*<span[^>]*>[^<]*</span>\s*<strong>([^<]*)</strong>', html)
        if b is None:   # veredicto inconcluso: la mejor compra va en prosa, «el más barato es <strong>X</strong>»
            b = re.search(r'class="verdict verdict-open">.*?el más barato es\s*<strong>([^<]*)</strong>', html, re.S)
        sec = re.search(r"<h2>(?:Top 3 explicado|El grupo de cabeza)[^<]*</h2>(.*?)</section>", html, re.S)
        top3 = []
        for h in re.findall(r"<h3>([^<]*)</h3>", sec.group(1) if sec else ""):
            top3.append(re.sub(r"^\d+\.\s*", "", _h.unescape(h)).split(" — ")[0].strip())
        ul = re.search(r'<ul class="frontier-list">(.*?)</ul>', html, re.S)
        return {"grupo_cabeza": sorted(k for k in (g.group(1).split(",") if g else []) if k),
                "mejor_compra": _h.unescape(b.group(1)) if b else None,
                "top3": top3,
                "frontera": [_h.unescape(x) for x in re.findall(r"<li><strong>([^<]*)</strong>", ul.group(1) if ul else "")]}
    if tipo == "variantes":
        b = re.search(r'verdict-best">\s*<span[^>]*>[^<]*</span>\s*<strong>([^<]*)</strong>', html)
        c = re.search(r'verdict-costly">\s*<span[^>]*>[^<]*</span>\s*<strong>([^<]*)</strong>', html)
        esc = {}
        for label, ver in re.findall(r'<tr class="lad-[^"]*"><td><strong>([^<]*)</strong>.*?<td class="lad-verdict">([^<]*)</td>', html, re.S):
            ver = _h.unescape(ver)
            esc[_h.unescape(label)] = ("empatan_todos" if ver.startswith("Empatan —") else
                                       "empatan_arriba" if ver.startswith("Empatan") else
                                       "compra" if ver.startswith("El precio compra") else
                                       "al_reves" if ver.startswith("Va al revés") else "gana")
        lead = re.search(r'<p class="verdict-lead">(.*?)</p>', html, re.S)
        return {"veredicto": ({"empiece": _h.unescape(b.group(1)), "caro": _h.unescape(c.group(1)) if c else None,
                               "empatan_todos": bool(lead and "empatan en calidad" in lead.group(1))}
                              if b else None),
                "escalera": esc}
    return {}


def comparar_afirmaciones(url: str, tipo: str, antes: dict, ahora: dict):
    """(declaradas, fallos) de una página: cada afirmación que cambia, con su motivo o en rojo."""
    declaradas, fallos = [], []
    for k in sorted(set(antes) | set(ahora)):
        a, b = antes.get(k), ahora.get(k)
        if a == b:
            continue
        motivo = MOTIVOS_AFIRMACION.get((tipo, k))
        if k == "escalera" and isinstance(a, dict) and isinstance(b, dict):
            cambios = [f"{s}: {a.get(s)} → {b.get(s)}" for s in sorted(set(a) | set(b)) if a.get(s) != b.get(s)]
            det = "; ".join(cambios)
        else:
            det = f"{a} → {b}"
        if motivo:
            declaradas.append(f"{url}: {k} cambia ({det}). Motivo: {motivo}")
        else:
            fallos.append(f"{url}: la afirmación «{k}» cambia sin motivo declarado ({det})")
    return declaradas, fallos


def revisar_retiradas(dist: Path, docs: Path, regs: list[dict]):
    """(declaradas, fallos): cada frase retirada está en docs/ y en ningún dist de su tipo."""
    declaradas, fallos = [], []
    por_tipo: dict[str, list[dict]] = {}
    for e in regs:
        if e["motor"] == "astro" and not e["redirect_a"] and e["tipo"] in ("ranking", "variantes"):
            por_tipo.setdefault(e["tipo"], []).append(e)
    textos = {}
    for tipo, es in por_tipo.items():
        for e in es:
            fd, fa = _html(docs, e["url"]), _html(dist, e["url"])
            textos[(tipo, e["url"])] = (_texto(fd.read_text(encoding="utf-8")) if fd.exists() else "",
                                        _texto(fa.read_text(encoding="utf-8")) if fa.exists() else "")
    for tipo, frase, motivo in RETIRADAS:
        en_docs = [u for (t_, u), (d, _) in textos.items() if t_ == tipo and frase in d]
        en_dist = [u for (t_, u), (_, a) in textos.items() if t_ == tipo and frase in a]
        if not en_docs:
            fallos.append(f"frase retirada «{frase}»: no está en ninguna página de {tipo} de docs/ "
                          "(la declaración sobra o la frase está mal copiada)")
        if en_dist:
            fallos.append(f"frase retirada «{frase}»: sigue en dist ({', '.join(en_dist)})")
        if en_docs and not en_dist:
            declaradas.append(f"se retira «{frase}» de {len(en_docs)} página(s) de {tipo}. Motivo: {motivo}")
    return declaradas, fallos


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
        if e["tipo"] in ("ranking", "variantes"):
            sub = "rankings" if e["tipo"] == "ranking" else "variantes"
            jf = datos / sub / f"{e['slug']}.json"
            d = json.loads(jf.read_text(encoding="utf-8")) if jf.exists() else None
            if d is None:
                fallos.append(f"{e['url']}: sin datos exportados ({jf})")
                continue
            dec, fal = comparar_afirmaciones(e["url"], e["tipo"],
                                             afirmaciones_publicadas(fd.read_text(encoding="utf-8"), e["tipo"]),
                                             d.get("afirmaciones") or {})
            declaradas += dec
            fallos += fal
            if ra != rd:
                fallos.append(f"{e['url']}: recomienda cambió ({rd} → {ra})")
            if filas_a != filas_d:
                fallos.append(f"{e['url']}: cambiaron las filas de sus tablas ({filas_d} → {filas_a})")
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
    dec, fal = revisar_retiradas(dist, docs, regs)
    return fallos + fal, declaradas + dec


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
    print(f"  {len(declaradas)} diferencias declaradas (redirects, filas que salen por R1, afirmaciones "
          f"que cambian y frases retiradas)")
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
