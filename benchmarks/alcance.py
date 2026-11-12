#!/usr/bin/env python3
"""El alcance de cada veredicto: qué suites lo sostienen y qué no medimos. (12-nov-2026, motor-sitio 2.6)

POR QUÉ EXISTE
--------------
/claude-haiku-sonnet-opus/ decía «Los 5 tiers empatan en calidad» y «pagar más no compra calidad
que se pueda medir». Cristian (12-nov): en Claude Code la diferencia entre tiers se nota mucho, y
eso no lo medimos; y «Planificar da 9,20 en los cinco: eso es saturación, no empate». El veredicto
generalizaba más allá de lo medido. Desde ahora:

  1. no hay veredicto sin alcance: la frase dice «En nuestras N suites de [tipo de tarea]» y
     enlaza a la lista (`#que-mide`);
  2. un empate se dice «esta medición no los distingue»; y si todos los modelos de la página
     están dentro del margen del techo de una suite (el mejor rankeado en ella), esa suite está
     SATURADA y no discrimina;
  3. cada página con veredicto lleva «Qué mide esta página y qué no»: las suites, cada una con
     su enlace, y lo que no medimos, con el benchmark externo de cada eje
     (`benchmarks_externos.json`).

Una sola autoridad: qué suites cuentan sale de `suites.py` (`del_indice`, `pilar_del_promedio`);
el margen, de `bands._indistinguishable`; las tareas agénticas, del `agentico` de models.json.
`check_alcance.py` verifica lo compilado.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

import suites as S  # noqa: E402
from bands import SUITE, _indistinguishable  # noqa: E402

EXTERNOS = ROOT / "benchmarks" / "benchmarks_externos.json"
REPO = "https://github.com/ctala/ai-benchmarks-alternativos"
EJES_MINIMOS = ("codigo_agente", "agentes_herramientas", "preferencia", "precio_velocidad")
TIPO_PILAR = {"Coding": "programación", "Contenido": "contenido", "Razonamiento": "razonamiento",
              "Agentes": "agentes"}


def url_suite(s: str) -> str:
    return f"{REPO}/blob/main/benchmarks/tests/{s}.py"


def url_tarea(t: str) -> str:
    return f"{REPO}/tree/main/tareas-agente/{t}"


def externos() -> dict:
    return json.loads(EXTERNOS.read_text(encoding="utf-8"))


def tareas_agenticas(models: list[dict]) -> list[str]:
    """Las tareas Harbor que entran en la nota: las que rindieron los rankeados."""
    t = set()
    for m in models:
        if m.get("ranked"):
            t |= set(((m.get("agentico") or {}).get("tareas") or {}))
    return sorted(t)


def _nota(m, s):
    return (m.get("quality_by_suite") or {}).get(s)


def saturada(s: str, modelos: list[dict], ranked: list[dict]) -> bool:
    """¿Todos los modelos de la página están dentro del margen del techo de la suite?

    El techo es el mejor rankeado en esa suite. Si nadie de la página se separa de él, la suite
    no tiene con qué distinguirlos: no es un empate entre ellos, es una suite que no discrimina."""
    con = [m for m in ranked if _nota(m, s) is not None]
    if not con or not modelos or any(_nota(m, s) is None for m in modelos):
        return False
    techo = max(con, key=lambda m: _nota(m, s))
    mejor = max(modelos, key=lambda m: _nota(m, s))

    def junto(a, b):
        return a.get("key") == b.get("key") or _indistinguishable(a, b, SUITE + s)
    # Saturada = la página no los separa entre ellos Y todos quedan dentro del margen del mejor modelo de la suite (el techo). Si uno se separa de
    # otro dentro de la página, hay señal y no se tapa con «saturada».
    return all(junto(mejor, m) for m in modelos) and all(junto(techo, m) for m in modelos)


def frase(n_suites: int, tipo: str | None, n_tareas: int, una: str | None = None) -> str:
    """«En nuestras N suites de [tipo]» (sin el enlace: lo pone la plantilla)."""
    if una:
        return f"En nuestra suite «{una}»"
    partes = []
    if n_suites:
        partes.append(f"{n_suites} suites" + (f" de {tipo}" if tipo else " del examen"))
    if n_tareas:
        partes.append(f"{n_tareas} tareas agénticas")
    return "En nuestras " + " y ".join(partes)


def partes(n_suites: int, tipo: str | None, n_tareas: int, una: str | None = None) -> dict:
    """Lo mismo que `frase`, en piezas: la plantilla marca cada cifra (`Alcance.astro`)."""
    return {"n_suites": n_suites, "tipo": tipo, "n_tareas": n_tareas, "una": una}


def bloque(suites: list[str], tareas: list[str], modelos: list[dict], ranked: list[dict],
           tipo: str | None = None, una: str | None = None, programar: bool = False) -> dict:
    """`programar`: la página es de Claude y tiene que decir que no responde si conviene para
    programar con un agente (Cristian, 12-nov-2026), con el benchmark externo de ese eje."""
    ext = externos()
    filas = [{"id": s, "nombre": S.label(s), "decide": S.decide(s), "pilar": S.pilar_del_promedio(s),
              "url": url_suite(s), "saturada": saturada(s, modelos, ranked)} for s in suites]
    return {
        "frase": frase(len(suites), tipo, len(tareas), una),
        "partes": partes(len(suites), tipo, len(tareas), una),
        "n_suites": len(suites), "n_tareas": len(tareas),
        "suites": filas, "n_saturadas": sum(1 for f in filas if f["saturada"]),
        "saturadas": [f["nombre"] for f in filas if f["saturada"]],
        "tareas": [{"id": t, "url": url_tarea(t)} for t in tareas],
        "no_medimos": [{"eje": e, "que": ext["ejes"][e],
                        "benchmarks": [b for b in ext["benchmarks"] if b["eje"] == e]} for e in ext["ejes"]],
        "revisado": max(b["revisado"] for b in ext["benchmarks"]),
        "no_responde": ([{"nombre": b["nombre"], "url": b["url"]} for b in ext["benchmarks"]
                         if b["eje"] == "codigo_agente"] if programar else None),
    }


def es_de_claude(modelos: list[dict]) -> bool:
    return any(m.get("familia") == "claude" for m in modelos)


def indice(models: list[dict]) -> tuple[list[str], list[str]]:
    """Lo que entra en la nota de calidad: las suites del índice y las tareas agénticas."""
    return sorted(S.del_indice()), tareas_agenticas(models)


def de_pilar(p: str) -> list[str]:
    return sorted(s for s in S.del_indice() if S.pilar_del_promedio(s) == p)


def errores_externos(hoy: date | None = None, max_dias: int = 120) -> list[str]:
    """E1-E3 de `benchmarks_externos.json` (los usa `check_alcance.py`)."""
    hoy = hoy or date.today()
    d = externos()
    fallos = [f"E1 · falta el eje «{e}»" for e in EJES_MINIMOS if e not in d["ejes"]]
    for e in d["ejes"]:
        if not any(b["eje"] == e for b in d["benchmarks"]):
            fallos.append(f"E1 · el eje «{e}» no tiene ningún benchmark")
    for b in d["benchmarks"]:
        for k in ("id", "nombre", "eje", "mide", "url", "revisado"):
            if not b.get(k):
                fallos.append(f"E2 · {b.get('id', '?')} sin «{k}»")
        if b.get("eje") not in d["ejes"]:
            fallos.append(f"E2 · {b.get('id')} usa un eje que no existe: {b.get('eje')}")
        if not str(b.get("url", "")).startswith("https://"):
            fallos.append(f"E2 · {b.get('id')} no tiene una URL https")
        try:
            dias = (hoy - date.fromisoformat(b["revisado"])).days
        except (KeyError, ValueError):
            fallos.append(f"E3 · {b.get('id')}: «revisado» no es una fecha")
            continue
        if dias > max_dias:
            fallos.append(f"E3 · {b.get('id')} se revisó hace {dias} días (> {max_dias}): verificar que la URL "
                          "exista y que lo citado siga vigente, y actualizar «revisado»")
    return fallos


def html_que_mide(a: dict) -> str:
    """El mismo bloque que `sitio/src/components/QueMide.astro`, para las páginas de Python."""
    from html import escape as e

    def nombre(t):
        return '<span data-nombre>' + e(t) + '</span>'

    def enl(url, txt):
        return f'<a href="{e(url)}" target="_blank" rel="noopener">{txt}</a>'

    out = ['  <section id="que-mide" class="que-mide">', "    <h2>Qué mide esta página y qué no</h2>"]
    if a.get("no_responde"):
        bs = [enl(b["url"], nombre(b["nombre"])) for b in a["no_responde"]]
        lista = ", ".join(bs[:-1]) + " y " + bs[-1] if len(bs) > 1 else bs[0]
        out.append('    <p class="aviso" data-no-responde>Si lo vas a usar para <strong>programar con un agente</strong> '
                   "(Claude Code, Cursor), <strong>esta página no responde esa pregunta</strong>: no medimos sesiones "
                   f"largas de un agente en un repositorio. Para eso mira {lista}.</p>")
    out.append("    <h3>Lo que sostiene el veredicto</h3>")
    if a["n_suites"]:
        sat = (f' <strong><span data-cifra>{a["n_saturadas"]}</span> '
               f'{"está saturada" if a["n_saturadas"] == 1 else "están saturadas"}</strong> para los modelos de esta '
               "página: todos quedan dentro del margen de error del mejor modelo en esa suite, así que no los "
               "distingue." if a["n_saturadas"] else "")
        out.append(f'    <p class="meta"><span data-cifra>{a["n_suites"]}</span> suites, cada una con sus pruebas '
                   f"publicadas.{sat}</p>")
        out.append('    <ul class="lista-suites">')
        for s in a["suites"]:
            marca = '<strong class="saturada"> · saturada, no los distingue</strong>' if s["saturada"] else ""
            out.append(f'      <li>{enl(s["url"], e(s["nombre"]))} — {e(s["decide"])}{marca}</li>')
        out.append("    </ul>")
    if a["n_tareas"]:
        out.append(f'    <p class="meta"><span data-cifra>{a["n_tareas"]}</span> tareas agénticas, que el modelo '
                   "ejecuta en un entorno real y verifica un test, no un juez:</p>")
        out.append('    <ul class="lista-suites">')
        for t in a["tareas"]:
            out.append("      <li>" + enl(t["url"], nombre(t["id"])) + "</li>")
        out.append("    </ul>")
    out.append("    <h3>Lo que no medimos</h3>")
    out.append('    <p class="meta">Para estas preguntas, este benchmark no tiene dato. Te dejamos dónde mirar '
               "(revisado el <span data-cifra>" + "-".join(reversed(a["revisado"].split("-"))) + "</span>):</p>")
    out.append('    <ul class="lista-suites">')
    for x in a["no_medimos"]:
        bs = " · ".join(enl(b["url"], nombre(b["nombre"])) + " (" + e(b["mide"])
                        + ("; " + e(b["vigencia"]) if b.get("vigencia") else "") + ")" for b in x["benchmarks"])
        out.append(f'      <li><strong>{e(x["que"])}</strong>: {bs}</li>')
    out.append("    </ul>")
    out.append("  </section>")
    return "\n".join(out) + "\n"
