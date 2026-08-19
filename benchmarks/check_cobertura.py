#!/usr/bin/env python3
"""¿Cada regla está aplicada en TODAS las superficies que califican, o solo donde me acordé?

POR QUÉ EXISTE (17-ago-2026)
----------------------------
Cristian, al descubrir que la segunda tabla estaba en 2 de 16 páginas: *"agregá estos QA
también para que no nos pase de nuevo que no lo hagamos para todo"*.

Es la clase de fallo que más veces se repitió en dos días, y siempre igual: se hace una
mejora, se aplica **donde uno la estaba mirando**, y las otras superficies quedan atrás sin
que nada avise. Ninguna rompe nada — simplemente no tienen lo bueno.

    la segunda tabla        en 2 de 16 páginas · las que MÁS la necesitaban no la tenían
    W6 (promesas del wizard) verificaba 2 de 8 tareas
    el filtro de no-aptos    en la página de agentes y NO en la calculadora
    `sirve_para_agentes`     donde dolió el día que nació, no en todas partes
    el criterio agéntico     en el ranking y no en el wizard
    `no_medir`               en models.py y sin exportar, así que nadie lo veía

Los guardrails que ya existen cazan que algo esté ROTO o DESINCRONIZADO. Ninguno preguntaba
lo otro: **¿esto que hicimos acá, debería estar también allá?**

CÓMO FUNCIONA
-------------
Cada regla transversal declara dos cosas: **qué superficies califican** y **cómo se ve
aplicada**. El chequeo compara los dos conjuntos. Si una superficie califica y no la tiene,
falla — con el nombre de la superficie, no con un «revisá todo».

Agregar una regla acá es el precio de hacer una mejora transversal, y es barato: dos
funciones. No agregarla es cómo se llega a 2 de 16.

Uso:  python benchmarks/check_cobertura.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"


# ── R1 · el filtro de no-aptos, en TODA superficie que recomiende para agentes ──
def r1_filtro_agentico():
    """Un modelo que no corre dentro de un agente no puede recomendarse en NINGUNA
    superficie agéntica. Estuvo en la página de cortes y no en la calculadora: con
    «Agentes» seleccionado, Hermes 4 405B salía #3 con tarea real 0,00."""
    faltan = []
    js = (DOCS / "app.js").read_text()
    if "sirve_para_agentes" not in js:
        faltan.append("docs/app.js no filtra por `sirve_para_agentes`")
    if "EJES_AGENTICOS" not in js:
        faltan.append("docs/app.js no distingue los ejes agénticos de los demás")
    gr = (ROOT / "benchmarks" / "generate_rankings.py").read_text()
    if "sirve_para_agentes" not in gr:
        faltan.append("generate_rankings.py no filtra no-aptos en los cortes agénticos")
    gl = (ROOT / "benchmarks" / "generate_manual_landings.py").read_text()
    if "sirve_para_agentes" not in gl:
        faltan.append("generate_manual_landings.py no filtra no-aptos (ej. /modelos-n8n/)")
    return faltan


# ── R2 · cada tarea del wizard con su verificador de promesa ───────────────────
def r2_promesas_del_wizard():
    """Cada opción del wizard afirma algo («rápida», «para agentes», «programar») y esa
    afirmación necesita un chequeo. W6 verificaba 2 de 8: el resto de las tareas podía
    recomendar cualquier cosa sin que nada avisara."""
    js = (DOCS / "app.js").read_text()
    qa = (ROOT / "benchmarks" / "qa_calculadora.mjs").read_text()
    m = re.search(r"tasks: \[(.*?)\n  \],", js, re.S)
    if not m:
        return ["no se pudo leer WIZ.tasks de app.js"]
    tareas = re.findall(r'id: "(\w+)"', m.group(1))
    # Una tarea está cubierta si algún chequeo la nombra o cubre su pilar/propiedad.
    cubiertas = set()
    for t in tareas:
        if re.search(rf'"{t}"|\b{t}\b', qa):
            cubiertas.add(t)
    # W9 cubre por pilar y W10 cubre «general»; se aceptan como cobertura genérica.
    if "W9 ·" in qa:
        cubiertas |= {"coding", "contenido", "razonamiento", "agentes"}
    if "W10 ·" in qa:
        cubiertas.add("general")
    if "t.latency" in qa:
        cubiertas.add("chat")
    faltan = [t for t in tareas if t not in cubiertas]
    return [f"la tarea «{t}» del wizard no tiene ningún chequeo que verifique su promesa"
            for t in faltan]


# ── R3 · la elegibilidad se lee, no se recalcula ──────────────────────────────
def r3_elegibilidad_unica():
    """`m["elegible"]` se decide una vez en el export. Una superficie que vuelve a
    combinar `retired` + `ranked` + `provider_variant` a mano es una copia que va a
    divergir — había 76 condicionales así en 25 archivos."""
    faltan = []
    d = json.loads(MODELS_JSON.read_text())
    if not d["models"] or "elegible" not in d["models"][0]:
        faltan.append("models.json no trae `elegible`: el veredicto no viaja con el dato")
    # Los generadores que RECOMIENDAN deberían poder leerlo.
    for f in ("generate_rankings.py", "generate_comparison.py", "generate_manual_landings.py"):
        src = (ROOT / "benchmarks" / f).read_text()
        # combinar tres flags a mano es la firma de la copia
        combos = len(re.findall(r"retired[^\n]{0,80}(ranked|provider_variant)", src))
        if combos >= 2:
            faltan.append(f"{f} recombina los flags de elegibilidad a mano ({combos} veces) "
                          f"en vez de leer `m['elegible']`")
    return faltan


# ── R4 · toda suite medida, en el registro y con nombre humano ────────────────
def r4_suites_registradas():
    """Una suite que se mide y no se declara muestra su id técnico al usuario y no
    aparece en ningún menú. Ya lo verifica `check_suites`; acá se comprueba que ese
    chequeo siga existiendo y corriendo en el pipeline."""
    faltan = []
    if not (ROOT / "benchmarks" / "check_suites.py").exists():
        faltan.append("check_suites.py no existe")
    pipe = (ROOT / "benchmarks" / "regenerate_all.py").read_text()
    if "check_suites.py" not in pipe:
        faltan.append("check_suites.py no corre en regenerate_all.py")
    qa = (ROOT / "benchmarks" / "qa.py").read_text()
    if "check_suites.py" not in qa:
        faltan.append("check_suites.py no está en el comando de QA")
    return faltan


# ── R5 · todo chequeo nuevo, probado contra su propio fallo ───────────────────
def r5_guardrails_probados():
    """Un chequeo que nunca falla no es un chequeo. Cada `check_*.py` del núcleo tiene
    que tener su prueba de sabotaje en `test_guardrails.py`."""
    tg = (ROOT / "benchmarks" / "test_guardrails.py").read_text()
    pipe = (ROOT / "benchmarks" / "regenerate_all.py").read_text()
    faltan = []
    for p in sorted((ROOT / "benchmarks").glob("check_*.py")):
        n = p.stem
        # solo los que el pipeline hace cumplir: los de uso manual no bloquean nada
        if f"{n}.py" not in pipe:
            continue
        if n not in tg:
            faltan.append(f"{n}.py corre en el pipeline y NO tiene prueba de que falle "
                          f"cuando debe (test_guardrails.py)")
    return faltan


# ── R6 · toda página de ranking, con el criterio de segunda tabla medido ─────
def r6_segunda_tabla():
    """El caso que originó este archivo: estaba en 2 de 16 páginas, activada a mano, y
    las que más la necesitaban no la tenían. Hoy la decide `_lleva_segunda_tabla`; esto
    verifica que nadie vuelva a ponerla con un flag."""
    gr = (ROOT / "benchmarks" / "generate_rankings.py").read_text()
    faltan = []
    if "_lleva_segunda_tabla" not in gr:
        faltan.append("generate_rankings.py no decide la segunda tabla con el criterio medido")
    if re.search(r'"segunda_tabla_valor":\s*True', gr):
        faltan.append("volvió el flag a mano `segunda_tabla_valor`: el criterio se mide, "
                      "no se declara página por página")
    return faltan


# ── R7 · toda página publicada DECLARA lo que publica ─────────────────────────
def r7_contrato_de_pagina():
    """Sin contrato, el auditor tiene que inferir la estructura con regex — y las 71
    páginas tienen ocho formas distintas. Cada regex cubre unas y deja otras ciegas: así
    aparecieron cinco falsos positivos y puntos ciegos en un día, todos el mismo bug.

    Una página nueva sin contrato entra en silencio y abre el siguiente punto ciego. Por
    eso falla acá: el contrato es el precio de publicar."""
    import sys as _s
    _s.path.insert(0, str(ROOT / "benchmarks"))
    from contrato_pagina import leer
    sin = []
    for pg in sorted(DOCS.rglob("index.html")):
        if pg.parent == DOCS:
            continue
        if leer(pg.read_text(errors="replace")) is None:
            sin.append(pg.parent.name)
    return [f"docs/{s}/ no declara su contrato: el auditor tiene que adivinar su "
            f"estructura, y ahí es donde nacen los puntos ciegos" for s in sin]


REGLAS = [
    ("R1", "el filtro de no-aptos está en TODA superficie agéntica", r1_filtro_agentico),
    ("R2", "cada tarea del wizard tiene quien verifique su promesa", r2_promesas_del_wizard),
    ("R3", "la elegibilidad se LEE del dato, no se recalcula", r3_elegibilidad_unica),
    ("R4", "toda suite medida está declarada, y el chequeo corre", r4_suites_registradas),
    ("R5", "todo guardrail del pipeline está probado contra su fallo", r5_guardrails_probados),
    ("R6", "la segunda tabla se decide midiendo, no con un flag", r6_segunda_tabla),
    ("R7", "toda página publicada declara lo que publica", r7_contrato_de_pagina),
]


def main() -> int:
    print("\nVerificando que cada regla esté aplicada DONDE CORRESPONDE, no solo donde se hizo…\n")
    total = 0
    for cid, titulo, fn in REGLAS:
        try:
            faltan = fn()
        except Exception as e:  # noqa: BLE001
            faltan = [f"el chequeo explotó: {type(e).__name__}: {e}"]
        if not faltan:
            print(f"  ✅ {cid} · {titulo}")
            continue
        total += len(faltan)
        print(f"  ❌ {cid} · {titulo}")
        for f in faltan:
            print(f"       · {f}")

    print()
    if total:
        print(f"  ❌ {total} superficie(s) quedaron atrás de una regla que ya existe.")
        print("     No están rotas: simplemente no tienen lo bueno, y nada lo decía.")
        return 1
    print(f"  ✅ las {len(REGLAS)} reglas transversales están aplicadas en todas sus superficies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
