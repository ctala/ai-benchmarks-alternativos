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
# Lo que corre el QA o el pipeline y NO puede tener sabotaje, con el motivo escrito. Una
# exención sin motivo, una que ya no corre en ningún lado o una que ya tiene prueba ponen R5
# en rojo: la lista solo puede achicarse con razón, nunca crecer en silencio.
EXENTOS_R5 = {
    "test_guardrails.py":
        "es la prueba de los demás; la cuidan la trampa de argparse de `_correr` y el "
        "control verde antes de cada sabotaje",
}


def _scripts_de_qa() -> set[str]:
    """El archivo que corre cada entrada de `qa.CHEQUEOS` (`check_x.py`, `qa_calculadora.mjs`…).

    Se lee el módulo, no el texto: el docstring de qa.py nombra scripts que no corre.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("_qa_r5", ROOT / "benchmarks" / "qa.py")
    qa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qa)
    out = set()
    for c in qa.CHEQUEOS:
        for arg in c[2]:
            m = re.search(r"benchmarks/(\w+\.(?:py|mjs))$", str(arg))
            if m:
                out.add(m.group(1))
                break
        else:
            raise ValueError(f"entrada de qa.py sin script reconocible: {c[1]!r}")
    return out


def r5_guardrails_probados():
    """Un chequeo que nunca falla no es un chequeo. Todo lo que corre `qa.py` —y los
    `check_*` del pipeline— tiene su prueba de sabotaje en `test_guardrails.py`, o una
    exención con motivo en `EXENTOS_R5`.

    3-nov-2026. Hasta hoy R5 solo miraba `regenerate_all.py`, y 8 de los 21 chequeos del QA
    no están ahí: los 3 sin prueba convivían con este verde (AUDITORIA-GUARDRAILS-2026-11,
    H2). Y «tiene prueba» era que el nombre apareciera en cualquier lugar del archivo, un
    comentario incluido. Ahora la prueba tiene que INVOCARLO: el nombre del archivo entre
    comillas, que es como lo llaman `_correr(...)` y `ROOT / "benchmarks" / ...`.
    """
    tg = (ROOT / "benchmarks" / "test_guardrails.py").read_text()
    pipe = (ROOT / "benchmarks" / "regenerate_all.py").read_text()
    universo = _scripts_de_qa()
    universo |= {p.name for p in (ROOT / "benchmarks").glob("check_*.py") if p.name in pipe}

    def invocado(archivo: str) -> bool:
        return re.search(rf"[\"']{re.escape(archivo)}[\"']", tg) is not None

    faltan = []
    for archivo, motivo in sorted(EXENTOS_R5.items()):
        if not motivo.strip():
            faltan.append(f"{archivo} está exento SIN motivo: una exención se justifica o se borra")
        if archivo not in universo:
            faltan.append(f"{archivo} está exento y ya no corre en qa.py ni en el pipeline: "
                          f"borrar la exención")
        elif invocado(archivo):
            faltan.append(f"{archivo} está exento y YA tiene prueba en test_guardrails.py: "
                          f"borrar la exención")
    for archivo in sorted(universo - EXENTOS_R5.keys()):
        if not invocado(archivo):
            faltan.append(f"{archivo} corre en qa.py o en el pipeline y NO tiene prueba de "
                          f"que falle cuando debe (test_guardrails.py)")
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
    import paginas_leidas as pl
    sin, leidas = [], set()
    for pg in sorted(DOCS.rglob("index.html")):
        if pg.parent == DOCS:
            continue
        leidas.add(pl.url_de(DOCS, pg))
        if leer(pg.read_text(errors="replace")) is None:
            sin.append(pg.parent.name)
    # Regla de páginas leídas (motor-sitio 2.3): todas las del registro salvo la home.
    return [f"docs/{s}/ no declara su contrato: el auditor tiene que adivinar su "
            f"estructura, y ahí es donde nacen los puntos ciegos" for s in sin] \
        + pl.exigir("R7", leidas, pl.esperadas() - {"/"})


# ── R8 · ningún guardrail se debilita desde el último tag ─────────────────────
def _texto_en_tag(rel: str) -> str | None:
    """El archivo tal como estaba en el último tag (la base de `check_changelog` C1)."""
    import subprocess
    tag = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], capture_output=True,
                         text=True, cwd=ROOT).stdout.strip()
    if not tag:
        return None
    r = subprocess.run(["git", "show", f"{tag}:{rel}"], capture_output=True, text=True, cwd=ROOT)
    return r.stdout if r.returncode == 0 else None


def _maximo_de_pruebas() -> tuple[int, str]:
    """El MÁXIMO de `@prueba` en el tag y en cada commit posterior que tocó el archivo.

    Contra el tag solo no alcanza: el tag tenía 35 y el corte ya va en 51, así que se podían
    borrar 16 de las nuevas sin que nada se pusiera rojo. Lo cazó la prueba de sabotaje al
    nacer. «Nunca baja» quiere decir nunca, no «no baja del tag».
    """
    import subprocess
    rel = "benchmarks/test_guardrails.py"
    tag = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], capture_output=True,
                         text=True, cwd=ROOT).stdout.strip()
    commits = subprocess.run(["git", "log", "--format=%H", f"{tag}..HEAD", "--", rel],
                             capture_output=True, text=True, cwd=ROOT).stdout.split()
    mejor, donde = -1, tag
    for ref in [tag, *commits]:
        r = subprocess.run(["git", "show", f"{ref}:{rel}"], capture_output=True, text=True, cwd=ROOT)
        n = _n_pruebas(r.stdout) if r.returncode == 0 else -1
        if n > mejor:
            mejor, donde = n, ref[:9]
    return mejor, donde


def _n_pruebas(s: str) -> int:
    return len(re.findall(r"^@prueba\(", s, re.M))


def _texto_actual(rel: str) -> str:
    """El árbol de trabajo: R8 tiene que ver lo que todavía no se commiteó."""
    return (ROOT / rel).read_text(encoding="utf-8")


def _chequeos_de(fuente: str) -> dict[str, tuple[list[str], bool]]:
    """script → (argumentos, bloqueante) de un `qa.py` dado como TEXTO.

    Se ejecuta el texto como si fuera el archivo real: así el `qa.py` del tag se lee con
    las mismas reglas que el de hoy, sin depender de cómo se formatee la lista.
    """
    import types
    mod = types.ModuleType("_qa_r8")
    mod.__file__ = str(ROOT / "benchmarks" / "qa.py")
    exec(compile(fuente, mod.__file__, "exec"), mod.__dict__)
    out = {}
    for c in mod.CHEQUEOS:
        args = [str(a) for a in c[2]]
        script = next((m.group(1) for a in args
                       if (m := re.search(r"benchmarks/(\w+\.(?:py|mjs))$", a))), None)
        if script:
            out[script] = (args, bool(c[3]))
    return out


def r8_ningun_guardrail_se_debilita():
    """El instrumento de la fila del 3-nov «durante un corte mayor ningún guardrail se
    debilita para que pase» (corte-v5 1.4). Contra el último tag, rojo si:

      · `test_guardrails.py` tiene MENOS `@prueba` que el máximo que tuvo desde el tag, en
        cualquier commit (el conteo nunca baja);
      · un chequeo que era bloqueante pasó a informativo o salió de `qa.py`, y desde el tag
        no entró a `DECISIONES.md` ninguna línea que nombre su script;
      · un chequeo que en el tag corría con `--duro` ya no lo lleva: sin el flag sale con 0
        siempre y es un bloqueante de mentira (pasó con `check_truncamiento` y `check_ci`).

    Sin tag no hay base: no se puede afirmar nada, y lo dice en vez de dar verde.
    """
    tg_tag = _texto_en_tag("benchmarks/test_guardrails.py")
    qa_tag = _texto_en_tag("benchmarks/qa.py")
    if tg_tag is None or qa_tag is None:
        return ["no hay un tag con test_guardrails.py y qa.py contra el cual comparar"]
    faltan = []

    antes, donde = _maximo_de_pruebas()
    ahora = _n_pruebas(_texto_actual("benchmarks/test_guardrails.py"))
    if ahora < antes:
        faltan.append(f"test_guardrails.py tiene {ahora} pruebas de sabotaje y llegó a tener "
                      f"{antes} ({donde}): el conteo no baja")

    dec_tag = set((_texto_en_tag("DECISIONES.md") or "").splitlines())
    nuevas = [ln for ln in _texto_actual("DECISIONES.md").splitlines() if ln not in dec_tag]
    viejo = _chequeos_de(qa_tag)
    nuevo = _chequeos_de(_texto_actual("benchmarks/qa.py"))
    for script, (args, bloq) in sorted(viejo.items()):
        hoy = nuevo.get(script)
        if bloq and (hoy is None or not hoy[1]):
            if not any(script in ln for ln in nuevas):
                que = "salió de qa.py" if hoy is None else "pasó de bloqueante a informativo"
                faltan.append(f"{script} {que} sin una fila nueva en DECISIONES.md que lo nombre")
        if "--duro" in args and hoy is not None and "--duro" not in hoy[0]:
            faltan.append(f"{script} corría con --duro en el tag y ya no: sin el flag sale con "
                          f"0 siempre")
    return faltan


# ── R9 · ningún chequeo de qa.py depende de un --duro que no recibe ────────────
# script → por qué puede correr sin `--duro` y seguir siendo un control de verdad.
EXENTOS_R9 = {
    "check_secretos.py": "sin el flag igual sale con 1 ante un valor real del .env; --duro "
                         "solo suma las sospechas de forma, que en el QA cubre gitleaks",
}


def r9_duro_que_no_llega(fuente_qa: str | None = None) -> list[str]:
    """Un script con `--duro` sale con 0 sin el flag. Si `qa.py` no se lo pasa, el QA lo
    pinta ✅ aunque el script imprima ❌. R8 caza el flag QUITADO desde el tag; esto caza el
    que NUNCA se pasó. Pasó con `check_agentico_publicado` (6-nov-2026): tres Claude 5.5
    rankeados sin Harbor y el QA en verde."""
    chequeos = _chequeos_de(fuente_qa if fuente_qa is not None
                            else _texto_actual("benchmarks/qa.py"))
    faltan = []
    for script, (args, _) in sorted(chequeos.items()):
        f = ROOT / "benchmarks" / script
        if not f.exists() or "--duro" in args:
            continue
        if re.search(r"""add_argument\(\s*["']--duro["']""", f.read_text()):
            if not str(EXENTOS_R9.get(script) or "").strip():
                faltan.append(f"{script} define --duro y qa.py lo corre sin él: sale con 0 y "
                              f"el QA lo muestra ✅ aunque falle")
    for script in EXENTOS_R9:
        if script not in chequeos:
            faltan.append(f"EXENTOS_R9 nombra a {script}, que ya no corre en qa.py")
    return faltan


REGLAS = [
    ("R1", "el filtro de no-aptos está en TODA superficie agéntica", r1_filtro_agentico),
    ("R2", "cada tarea del wizard tiene quien verifique su promesa", r2_promesas_del_wizard),
    ("R3", "la elegibilidad se LEE del dato, no se recalcula", r3_elegibilidad_unica),
    ("R4", "toda suite medida está declarada, y el chequeo corre", r4_suites_registradas),
    ("R5", "todo lo que corre el QA está probado contra su fallo, o exento con motivo", r5_guardrails_probados),
    ("R6", "la segunda tabla se decide midiendo, no con un flag", r6_segunda_tabla),
    ("R7", "toda página publicada declara lo que publica", r7_contrato_de_pagina),
    ("R8", "ningún guardrail se debilita desde el último tag", r8_ningun_guardrail_se_debilita),
    ("R9", "ningún chequeo del QA depende de un --duro que no recibe", r9_duro_que_no_llega),
]


def main() -> int:
    global DOCS
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=None,
                    help="revisar lo que compila Astro (sitio/dist); los datos, de docs/")
    a = ap.parse_args()
    if a.dist:
        DOCS = a.dist
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
