#!/usr/bin/env python3
"""El registro de páginas: la única declaración de qué URLs tiene el sitio. (11-nov-2026)

POR QUÉ EXISTE
--------------
Change `motor-sitio` (DECISIONES, 11-nov-2026). El sitio tiene 204 URLs y las escriben nueve
generadores, cada uno con su propia lista. Nadie declaraba la URL como tal, así que una página
que nadie regeneraba seguía publicada y mostraba modelos que ya habían salido del ranking. Al
11-nov eran 24 de las 27 comparaciones de versión exacta.

Las entradas se DERIVAN de las configuraciones que ya existen (`COMPARISONS`, `RANKINGS`,
`FAMILIES`, `LANDINGS`, las fichas) y no se copian, para no tener dos listas. A mano solo se
declara lo que es decisión:

  - `MOTOR_ASTRO`: los tipos que ya compila Astro. El resto es `legado` (el HTML de Python se
    copia tal cual) hasta que su sesión lo migre.
  - `CONGELADAS`: fecha y motivo. Es la ÚNICA forma de que una página muestre un modelo fuera
    del ranking vigente (R1 de `check_registro.py`).
  - `REDIRECTS_VERSION`: las comparaciones de versión exacta que pasan a su familia.

Cada entrada: `url` ("/slug/"), `slug`, `tipo`, `familias`, `ocasion`, `motor`, `congelada`
({fecha, motivo} o None), `redirect_a` (slug o None), `generador`.

Uso:
    python benchmarks/registro_paginas.py            # resumen por tipo y motor
    python benchmarks/registro_paginas.py --json     # el registro entero
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "sitio" / "legado"
sys.path.insert(0, str(ROOT / "benchmarks"))
sys.path.insert(0, str(ROOT))

# Tipos que ya compila Astro (sesión 1: comparaciones y sus redirects; sesión 2: rankings y
# variantes). En el 1b entran `ficha`, `landing`, `home` y `proveedores`.
MOTOR_ASTRO = {"comparacion", "redirect", "ranking", "variantes"}

_MOTIVO_SIN_FAMILIA = ("Comparación de versión exacta: a un lado le falta su página de familia. "
                       "Se reevalúa cuando el change de comparaciones por familia la cree.")
CONGELADAS = {
    slug: {"fecha": "2026-11-11", "motivo": _MOTIVO_SIN_FAMILIA}
    for slug in (
        "gpt-5.6-vs-gpt-5.5", "gpt-5.6-luna-vs-terra", "gpt-5.6-terra-vs-sol",
        "gpt-5.6-luna-vs-sol", "grok-4.5-vs-grok-4.3", "glm-5.2-vs-glm-5.1",
        "glm-5.2-vs-claude-opus-4-8", "fable-5-vs-minimax-m3", "gpt-5.6-vs-minimax-m3",
        "nemotron-3-ultra-vs-deepseek-v4-flash", "diffusiongemma-vs-gemma-4",
    )
}
# Páginas de variantes con menos de dos tiers en el ranking vigente: no hay escalera que generar.
# Cristian (11-nov-2026) no las congela: «congelar es para conservar a propósito algo que vale la
# pena». Search Console, 16 meses: gpt-5.6-luna-terra-sol 1 clic y 15 impresiones; grok-4-1-vs-4-5,
# 0 y 10. Pasan a la comparación por familia (DECISIONES, 11-nov-2026).
REDIRECTS_VARIANTES = {
    "gpt-5.6-luna-terra-sol": "claude-vs-chatgpt",
    "grok-4-1-vs-4-5": "grok-vs-chatgpt",
}
MOTIVO_REDIRECT_VARIANTES = ("Página de variantes sin dos versiones en el ranking vigente: no hay "
                             "escalera que generar y pasa a su comparación por familia (DECISIONES 11-nov-2026).")

# Aprobadas por Cristian el 11-nov-2026 (design.md del change). Search Console, 16 meses:
# ninguna pasa de 6 clics; la que más, gpt-5.6-vs-claude-opus-4-8 (6 clics, 372 impresiones).
REDIRECTS_VERSION = {
    "fable-5-vs-gpt-5-5": "claude-vs-chatgpt",
    "fable-5-vs-gpt-5-6-sol": "claude-vs-chatgpt",
    "gpt-5.6-vs-fable-5": "claude-vs-chatgpt",
    "gpt-5.6-vs-claude-opus-4-8": "claude-vs-chatgpt",
    "gpt-5.6-vs-claude-sonnet-4-6": "claude-vs-chatgpt",
    "gpt-5.6-luna-vs-claude-haiku-4-5": "claude-vs-chatgpt",
    "gpt-5.6-terra-vs-claude-sonnet-4-6": "claude-vs-chatgpt",
    "gpt-5.6-sol-vs-claude-opus-4-8": "claude-vs-chatgpt",
    "fable-5-vs-opus-4-8": "claude-haiku-sonnet-opus",
    "fable-5-vs-claude-sonnet-4-6": "claude-haiku-sonnet-opus",
    "grok-4.3-vs-gpt-5-5": "grok-vs-chatgpt",
    "grok-4.5-vs-gpt-5-6": "grok-vs-chatgpt",
    "grok-4.5-vs-claude-sonnet-4-6": "grok-vs-claude",
    "gpt-5.6-vs-gemini-3.5-flash": "gemini-vs-chatgpt",
    "gpt-5.6-vs-deepseek-v4": "deepseek-vs-chatgpt",
    "gemini-3.5-flash-vs-gemini-2.5-flash": "gemini-flash-o-pro",
}
MOTIVO_REDIRECT_VERSION = ("Comparación de versión exacta reemplazada por su comparación por familia "
                           "(DECISIONES 11-nov-2026, «Motor del sitio»).")


def _entrada(slug: str, tipo: str, generador: str, familias=None, ocasion=None) -> dict:
    return {"url": f"/{slug}/" if slug else "/", "slug": slug, "tipo": tipo,
            "familias": familias or [], "ocasion": ocasion, "motor": None,
            "congelada": None, "redirect_a": None, "motivo": None, "generador": generador}


def _fichas() -> list[str]:
    """Las fichas que existen: las de los rankeados de hoy y las que ya se publicaron (una ficha
    publicada no se abandona; `generate_model_cards.py`, 4-nov-2026)."""
    import generate_model_cards as gmc
    d = json.loads((DOCS / "data" / "models.json").read_text(encoding="utf-8"))
    slugs = {gmc.slug(m) for m in d["models"] if m.get("ranked")}
    if (DOCS / "modelo").is_dir():
        slugs |= {p.name for p in (DOCS / "modelo").iterdir() if (p / "index.html").exists()}
    return sorted(slugs)


def paginas() -> list[dict]:
    import generate_comparison as gc
    import generate_manual_landings as gm
    import generate_rankings as gr
    import generate_variants as gv
    import generate_providers_page as gp

    out = [_entrada("", "home", "index.html (calculadora)")]
    for c in gc.COMPARISONS:
        out.append(_entrada(c["slug"], "comparacion", "generate_comparison",
                            familias=[c["a"]["name"], c["b"]["name"]]))
    for slug, cfg in gc.HUERFANAS_DECLARADAS.items():
        e = _entrada(slug, "redirect", "generate_comparison")
        e["redirect_a"], e["motivo"] = cfg["destino"], cfg["por_que"]
        out.append(e)
    for r in gr.RANKINGS:
        out.append(_entrada(r["slug"], "ranking", "generate_rankings", ocasion=r.get("pillar")))
    for f in gv.FAMILIES:
        out.append(_entrada(f["slug"], "variantes", "generate_variants", familias=[f["family"]]))
    for slug, _fn in gm.LANDINGS:
        out.append(_entrada(slug, "landing", "generate_manual_landings"))
    out.append(_entrada(gp.SLUG, "proveedores", "generate_providers_page"))
    for s in _fichas():
        out.append(_entrada(f"modelo/{s}", "ficha", "generate_model_cards"))

    for e in out:
        if e["slug"] in REDIRECTS_VERSION:
            e["tipo"], e["redirect_a"] = "redirect", REDIRECTS_VERSION[e["slug"]]
            e["motivo"] = MOTIVO_REDIRECT_VERSION
        if e["slug"] in REDIRECTS_VARIANTES:
            e["tipo"], e["redirect_a"] = "redirect", REDIRECTS_VARIANTES[e["slug"]]
            e["motivo"] = MOTIVO_REDIRECT_VARIANTES
        if e["slug"] in CONGELADAS:
            e["congelada"] = dict(CONGELADAS[e["slug"]])
        e["motor"] = "astro" if e["tipo"] in MOTOR_ASTRO else "legado"
    # Un redirect que apunta a otro redirect se resuelve al destino final: dos saltos pierden
    # señal y Google puede no seguir el segundo. Caso real: grok-4.3-vs-gpt-5.5 → grok-4.3-vs-gpt-5-5,
    # que el 11-nov pasó a redirigir a grok-vs-chatgpt.
    destino = {e["slug"]: e["redirect_a"] for e in out if e["redirect_a"]}
    for e in out:
        vistos = {e["slug"]}
        while e["redirect_a"] in destino and e["redirect_a"] not in vistos:
            vistos.add(e["redirect_a"])
            e["redirect_a"] = destino[e["redirect_a"]]
    return out


def urls_en_docs(docs: Path = DOCS) -> set[str]:
    """Las URLs que hoy publica `sitio/legado/` (cada `index.html`)."""
    return {"/" if p.parent == docs else f"/{p.parent.relative_to(docs).as_posix()}/"
            for p in docs.rglob("index.html")}


def errores(regs: list[dict]) -> list[str]:
    """Coherencia interna del registro (la usa `check_registro.py`)."""
    fallos, vistos = [], Counter(e["url"] for e in regs)
    fallos += [f"URL duplicada en el registro: {u}" for u, n in vistos.items() if n > 1]
    slugs = {e["slug"] for e in regs}
    for e in regs:
        if not e["tipo"]:
            fallos.append(f"{e['url']}: sin tipo")
        if e["redirect_a"] is not None:
            if e["redirect_a"] not in slugs:
                fallos.append(f"{e['url']}: redirige a /{e['redirect_a']}/, que no está en el registro")
            elif next(x for x in regs if x["slug"] == e["redirect_a"])["redirect_a"]:
                fallos.append(f"{e['url']}: redirige a otro redirect (/{e['redirect_a']}/)")
            if e["congelada"]:
                fallos.append(f"{e['url']}: no puede ser redirect y congelada a la vez")
        if e["congelada"] and not (e["congelada"].get("fecha") and e["congelada"].get("motivo")):
            fallos.append(f"{e['url']}: congelada sin fecha o sin motivo")
    for slug in list(CONGELADAS) + list(REDIRECTS_VERSION) + list(REDIRECTS_VARIANTES):
        if slug not in slugs:
            fallos.append(f"/{slug}/: declarada (congelada o redirect) pero ningún generador la crea")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    regs = paginas()
    if a.json:
        print(json.dumps(regs, ensure_ascii=False, indent=1))
        return 0
    print(f"Registro de páginas: {len(regs)} URLs")
    for (t, mo), n in sorted(Counter((e["tipo"], e["motor"]) for e in regs).items()):
        print(f"  {t:12} {mo:7} {n}")
    print(f"  congeladas: {sum(1 for e in regs if e['congelada'])} · "
          f"redirects: {sum(1 for e in regs if e['redirect_a'])}")
    f = errores(regs)
    for x in f:
        print(f"  ❌ {x}")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main())
