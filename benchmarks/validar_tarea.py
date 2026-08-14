#!/usr/bin/env python3
"""Verifica que una tarea de Harbor cumpla el ESTÁNDAR antes de gastar en medirla.

El estándar es la rúbrica de Terminal-Bench Science adaptada a negocio — ver
`tareas-agente/ESTANDAR-TAREAS.md`. Los criterios se citan por su número (C2, C7…).

POR QUÉ EXISTE (14-ago-2026)
----------------------------
Cristian: *"deberíamos generar el estándar para cómo generamos los tests, o agentes que
los hagan."*

El estándar es `tareas-agente/ESTANDAR-TAREAS.md`. Esto es lo que lo hace cumplir — y
existe por la regla de oro del repo: **una regla sin instrumento que la haga cumplir es
una regla que ya se rompió.** Un estándar de 18 reglas que nadie verifica es una lista de
buenas intenciones, y este repo ya pagó cinco veces por exactamente eso en un solo día.

QUÉ CHEQUEA, Y QUÉ NO PUEDE CHEQUEAR
------------------------------------
Chequea lo VERIFICABLE: que exista el artefacto, que los tests tengan un criterio por
función, que la solución derive en vez de venir precomputada, que haya canario, que los
chequeos negativos no pasen con una respuesta vacía.

**No puede chequear si la tarea vale la pena medirse.** Que sea representativa del
trabajo de un emprendedor (R1) sigue siendo criterio humano. El instrumento evita que una
tarea mal CONSTRUIDA llegue a un lote; no evita que midamos algo que a nadie le importa.

Uso:
    python benchmarks/validar_tarea.py tareas-agente/harbor-cotizar
    python benchmarks/validar_tarea.py --todas
"""

import argparse
import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAREAS = ROOT / "tareas-agente"


class Resultado:
    def __init__(self, tarea: str):
        self.tarea, self.fallos, self.avisos, self.ok = tarea, [], [], []

    def falla(self, regla, msg): self.fallos.append(f"{regla} · {msg}")
    def avisa(self, regla, msg): self.avisos.append(f"{regla} · {msg}")
    def pasa(self, regla): self.ok.append(regla)


def _tests_py(d: Path) -> Path | None:
    for p in (d / "tests").glob("*.py"):
        return p
    return None


def validar(d: Path) -> Resultado:
    r = Resultado(d.name)

    # ── Estructura mínima de Harbor ──────────────────────────────────────────
    for f in ("task.toml", "instruction.md"):
        (r.pasa if (d / f).exists() else lambda _: r.falla("estructura", f"falta {f}"))("estructura")
    if not (d / "environment").is_dir():
        r.falla("R4", "no hay `environment/` — sin datos, las trampas sólo pueden estar "
                      "en la consigna, y una trampa señalizada mide lectura, no criterio")

    tp = _tests_py(d)
    if not tp:
        r.falla("R5", "no hay tests/*.py — no hay verificador")
        return r
    src = tp.read_text(encoding="utf-8")
    arbol = ast.parse(src)
    funcs = [n for n in arbol.body if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]

    # ── R5 · verifica un ARTEFACTO, no prosa ────────────────────────────────
    lee_archivo = bool(re.search(r"Path\(|read_text|json\.load|open\(", src))
    if not lee_archivo:
        r.falla("R5", "los tests no leen ningún archivo: ¿está verificando prosa? "
                      "Parsear texto libre costó SEIS falsos negativos en la v1 de cotizar")
    else:
        r.pasa("R5")

    # ── R6 · un test por criterio, con nombre que lo diga ───────────────────
    if len(funcs) < 3:
        r.falla("R6", f"solo {len(funcs)} tests: con reward parcial, pocos tests dan un "
                      f"número sin diagnóstico")
    else:
        r.pasa("R6")
    genericos = [f.name for f in funcs
                 if re.fullmatch(r"test_(correcto|ok|valido|resultado|salida|todo)", f.name)]
    if genericos:
        r.falla("R6", f"nombres que no dicen qué criterio miden: {', '.join(genericos)}")

    # ── R2 · cada test declara su consecuencia ──────────────────────────────
    # Se busca plata, incumplimiento o una decisión: un test que sólo dice "verifica el
    # formato" es prolijidad, y la prolijidad no decide qué modelo usar.
    # R2 pide que la consecuencia esté DECLARADA — "plata o una decisión", no plata
    # obligatoriamente. La primera versión de este chequeo solo reconocía dinero y jerga
    # legal, y marcó como incompletos 9 tests de `harbor-reunion` que sí explicaban su
    # consecuencia, en términos operativos ("nadie la hace, y el tablero dice que sí
    # tiene dueño"). El instrumento estaba más angosto que la regla que hace cumplir.
    sin_consecuencia = []
    for f in funcs:
        doc = ast.get_docstring(f) or ""
        if not doc:
            sin_consecuencia.append(f.name); continue
        declara = re.search(r"consecuencia", doc, re.I)
        cuantifica = re.search(r"US\$|\bUSD\b|\$\s?\d|de más|de menos|incumpl|vencid|"
                               r"duplicad|cobra|factura|human[oa]|decisión|riesgo", doc, re.I)
        if not (declara or cuantifica):
            sin_consecuencia.append(f.name)
    if sin_consecuencia:
        r.avisa("R2", f"sin consecuencia explícita en el docstring: {', '.join(sin_consecuencia)}")
    else:
        r.pasa("R2")

    # ── R7 · los negativos tienen que caer con una respuesta vacía ──────────
    # Un test "no cobró X" pasa con silencio. Tiene que existir un test de forma.
    tiene_forma = any(re.search(r"exист|existe|is_file|\.exists\(\)|assert isinstance|"
                                r"falta|no está|valido|valid", ast.get_docstring(f) or f.name, re.I)
                      or re.search(r"\.exists\(\)|isinstance", ast.unparse(f))
                      for f in funcs)
    if not tiene_forma:
        r.falla("R7", "ningún test valida que el artefacto EXISTA y tenga forma: "
                      "una respuesta vacía pasaría los chequeos negativos")
    else:
        r.pasa("R7")

    # ── R8 · la solución DERIVA ─────────────────────────────────────────────
    sol = d / "solution"
    if not sol.is_dir():
        r.falla("R8", "no hay `solution/`")
    else:
        py = list(sol.glob("*.py"))
        if not py:
            r.falla("R8", "la solución no tiene script: un artefacto final no demuestra "
                          "cómo se llegó, y queda mudo si cambian los datos del entorno")
        else:
            s = py[0].read_text(encoding="utf-8")
            if not re.search(r"open\(|read_text|csv\.|json\.load", s):
                r.falla("R8", f"{py[0].name} no lee el entorno: parece precomputada")
            else:
                r.pasa("R8")

    # ── R10 · canario anti-contaminación ────────────────────────────────────
    if "canary" not in src.lower():
        r.falla("R10", "falta el canario GUID anti-contaminación de corpus")
    else:
        r.pasa("R10")

    inst = (d / "instruction.md").read_text(encoding="utf-8") if (d / "instruction.md").exists() else ""

    # ── C2 · well_specified + C15 · test_instruction_alignment ──────────────
    # De la rúbrica de Terminal-Bench Science: la consigna debe describir COMPLETAMENTE
    # lo que los tests verifican, con mapeo 1:1. Un examen con preguntas ocultas no mide
    # criterio, mide adivinación.
    #
    # La forma de cumplirlo sin regalar las trampas la da τ-bench: un documento de
    # POLÍTICA que el agente SÍ recibe. Oculto ≠ no especificado — las REGLAS van
    # escritas, las SITUACIONES van escondidas en los datos.
    # ¿El entorno ENUNCIA las reglas que los tests verifican?
    #
    # Cuatro intentos me llevó aceptar que esto no se automatiza bien. Primero busqué
    # archivos llamados `politica*` — y `harbor-facturacion` tiene sus reglas en
    # `README-negocio.md`. Después busqué verbos normativos — y «se factura» no matchea
    # «se facturan». Cada parche del regex deja otra forma afuera.
    #
    # Así que el chequeo hace lo que SÍ puede: cuenta líneas con forma de norma y
    # **falla solo cuando no hay ninguna**. Entre 1 y 2 avisa y lo decide un humano.
    # Es la misma honestidad que el estándar declara para el criterio 5: hay cosas que
    # un script no puede juzgar, y fingir que sí da confianza falsa.
    entorno = list((d / "environment").glob("*")) if (d / "environment").is_dir() else []
    NORMATIVO = re.compile(
        r"\b(se factur\w*|se cobra\w*|no se cobra\w*|se asigna\w*|no se asigna\w*|"
        r"debe\w*|se puede\w*|no se puede|s[oó]lo se|siempre|nunca|correspond\w*|"
        r"es un tope|se escala|se aplica\w*|se elige|se respeta|requiere|exige)\b", re.I)
    normas = 0
    for f in entorno:
        if f.suffix.lower() not in (".md", ".txt") or not f.is_file():
            continue
        normas = max(normas, sum(1 for l in f.read_text(errors="replace").splitlines()
                                 if NORMATIVO.search(l)))
    tiene_politica = normas >= 3

    if len(funcs) > 6 and normas == 0:
        r.falla("C2", f"{len(funcs)} tests y ningún documento del entorno enuncia REGLAS "
                      f"(≥3 normas). La consigna sola ({len(inst.split())} palabras) no puede "
                      f"especificar lo que verifican {len(funcs)} tests: se están testeando "
                      f"reglas que nadie escribió. τ-bench lo resuelve con un documento de "
                      f"política que el agente SÍ recibe")
    elif len(funcs) > 6 and normas < 3:
        r.avisa("C2", f"el entorno enuncia solo {normas} regla(s) para {len(funcs)} tests. "
                      f"Puede estar bien —una regla puede cubrir varios tests— pero "
                      f"revisalo: la consigna debe especificar QUÉ se verifica")
    else:
        r.pasa("C2")

    # ── C7 · essential_difficulty ───────────────────────────────────────────
    # La dificultad tiene que venir del razonamiento del negocio, no del formato. No se
    # puede medir estáticamente, pero SÍ se puede avisar del olor: si toda la salida es
    # un JSON armado a mano, el fallo probable es de sintaxis y no de criterio.
    # Medido en `harbor-ruteo`: los 4 modelos que entregaron sacaron 11/11 en las
    # decisiones; los 2 que fallaron lo hicieron por comillas mal cerradas.
    # La señal no es «menciona json» sino «muestra un ESQUEMA para copiar a mano»: un
    # bloque cercado que contiene llaves y comillas. Si el bloque tiene comandos, el
    # artefacto lo produce una herramienta y el formato deja de ser la dificultad.
    esquema_a_mano = any("{" in b and '"' in b
                         for b in re.findall(r"```[a-z]*\n(.*?)```", inst, re.S))
    if esquema_a_mano:
        r.avisa("C7", "la consigna muestra un esquema JSON para escribir a mano: verificá "
                      "que la dificultad esté en la DECISIÓN y no en la sintaxis. Medido en "
                      "`harbor-ruteo` v1: los que entregaron sacaron 11/11 en las decisiones "
                      "y los que fallaron fue por comillas mal cerradas. La salida: que una "
                      "HERRAMIENTA del entorno produzca el artefacto (patrón τ-bench)")

    # ── C21 · environment_hygiene ───────────────────────────────────────────
    dock = d / "environment" / "Dockerfile"
    if dock.exists():
        t = dock.read_text()
        if "tests" in t or "solution" in t:
            r.falla("C21", "el Dockerfile copia tests/ o solution/ a la imagen: el agente "
                           "puede leer la respuesta")
        else:
            r.pasa("C21")

    # ── C25 · expert_time_estimate ──────────────────────────────────────────
    toml = (d / "task.toml").read_text() if (d / "task.toml").exists() else ""
    m = re.search(r"expert_time_estimate_min\s*=\s*([\d.]+)", toml)
    if not m or float(m.group(1)) <= 0:
        r.falla("C25", "falta `expert_time_estimate_min` o es 0: calibra la dificultad y "
                       "los timeouts del agente")
    else:
        r.pasa("C25")

    if len(inst.split()) > 250:
        r.avisa("C16", f"la consigna tiene {len(inst.split())} palabras: `instruction_clarity` "
                       f"pide prosa mínima orientada al resultado, sin pistas de la solución")
    return r


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tarea", nargs="?", help="ruta a la tarea")
    ap.add_argument("--todas", action="store_true")
    a = ap.parse_args()

    if a.todas:
        dirs = [d for d in sorted(TAREAS.iterdir())
                if d.is_dir() and (d / "task.toml").exists()]
    elif a.tarea:
        dirs = [Path(a.tarea)]
    else:
        ap.error("pasá una tarea o --todas")

    print("\nValidación contra ESTANDAR-TAREAS.md\n")
    total_fallos = 0
    for d in dirs:
        r = validar(d)
        estado = "❌" if r.fallos else ("⚠️ " if r.avisos else "✅")
        print(f"  {estado} {r.tarea}  ({len(r.ok)} reglas en verde)")
        for f in r.fallos:
            print(f"       ❌ {f}")
        for w in r.avisos:
            print(f"       ⚠️  {w}")
        total_fallos += len(r.fallos)

    print()
    if total_fallos:
        print(f"  ❌ {total_fallos} violación(es) del estándar. No lanzar el lote.")
        print("     El estándar está en tareas-agente/ESTANDAR-TAREAS.md — cada regla")
        print("     existe porque su ausencia costó algo concreto.")
        return 1
    print("  ✅ todas las tareas cumplen el estándar verificable.")
    print("     Ojo: que sea REPRESENTATIVA (R1) no lo puede chequear un script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
