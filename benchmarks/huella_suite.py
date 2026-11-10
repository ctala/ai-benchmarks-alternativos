#!/usr/bin/env python3
"""La huella de una suite: prompts, scorer y juez, en un hash. (10-nov-2026)

POR QUÉ EXISTE
--------------
`prompt_injection_es` se rinde en el examen sin promediar. Cristian decidió (DECISIONES,
10-nov-2026) que el ranking acepte sus runs ANTERIORES a la ventana **solo si la suite es
idéntica a cuando se midió: prompts, scorer y juez, comprobado con un hash**. Un run de otra
versión no cuenta: el modelo se vuelve a medir en la ventana.

Comparar a mano «¿cambió algo desde junio?» es justo lo que este repo ya pagó caro (el
`prompt_sha` existe porque un prompt editado mezclaba runs viejos y nuevos en silencio). El
scorer de fuga cambió dos veces sin que el nombre de la suite cambiara: el 15-jul sumó los
bloqueos de plataforma en inglés y el 8-nov pasó a `negativas.py` con apóstrofos y tildes
normalizados. Las tres versiones puntúan distinto la misma respuesta.

QUÉ ENTRA EN LA HUELLA
----------------------
- **prompts**: el archivo de la suite (`benchmarks/tests/<suite>.py`) entero.
- **scorer**: el código de las funciones que puntúan, y por clausura todo lo que esas
  funciones nombran del mismo módulo (constantes y funciones auxiliares). No el archivo
  entero: un cambio en otra suite de `scoring.py` no invalida a esta.
- **juez**: el juez canónico si la suite se juzga; `None` si es verificable. Un run viejo cuya
  `quality` no es su `answer_score` se calificó con otra fórmula (con juez) y no coincide.

POR QUÉ UNA TABLA Y NO GIT EN VIVO
----------------------------------
El export corre también en el Action, con un clon superficial: sin historia, `git log`
fallaría y el ranking del CI saldría distinto del local. La historia se lee UNA vez con
`--actualizar` y queda en `huellas_suites.json` (versionado): para cada suite, la lista de
(desde, huella). `--check` (en el QA, bloqueante) falla si la huella del código de hoy no es la
última de la tabla: cambiar el scorer sin regenerarla deja el QA rojo.

Uso:
    python benchmarks/huella_suite.py --actualizar   # rehace la tabla desde git
    python benchmarks/huella_suite.py --check        # la tabla describe el código de hoy
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLA = ROOT / "benchmarks" / "huellas_suites.json"

# suite → de dónde salen sus prompts, qué funciones la puntúan y si la juzga un LLM.
REGISTRO = {
    "prompt_injection_es": {
        "tests": "benchmarks/tests/prompt_injection_es.py",
        "scorer": [("benchmarks/scoring.py", "_score_credential_leak"),
                   ("benchmarks/negativas.py", "es_negativa_fuga")],
        "juez": None,
    },
}


def _clausura(texto: str, nombre: str) -> str:
    """El código de `nombre` y de todo lo que nombra del mismo módulo, en orden estable.
    '' si el módulo o la función no existen (una versión sin ella es otra versión)."""
    try:
        arbol = ast.parse(texto)
    except SyntaxError:
        return ""
    defs = {}
    for n in arbol.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            defs[n.name] = n
        elif isinstance(n, (ast.Assign, ast.AnnAssign)):
            for t in (n.targets if isinstance(n, ast.Assign) else [n.target]):
                if isinstance(t, ast.Name):
                    defs[t.id] = n
    if nombre not in defs:
        return ""
    vistos, cola = [], [nombre]
    while cola:
        k = cola.pop()
        if k in vistos or k not in defs:
            continue
        vistos.append(k)
        cola += [x.id for x in ast.walk(defs[k]) if isinstance(x, ast.Name)]
    return "\n".join(ast.get_source_segment(texto, defs[k]) or "" for k in sorted(vistos))


def huella(suite: str, leer) -> str:
    """sha256 de prompts + scorer + juez. `leer(ruta)` devuelve el texto o '' si no existe."""
    reg = REGISTRO[suite]
    partes = {
        "prompts": leer(reg["tests"]),
        "scorer": [_clausura(leer(f), fn) for f, fn in reg["scorer"]],
        "juez": reg["juez"],
    }
    return hashlib.sha256(json.dumps(partes, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()


def _leer_disco(ruta: str) -> str:
    p = ROOT / ruta
    return p.read_text(encoding="utf-8") if p.exists() else ""


def huella_actual(suite: str) -> str:
    return huella(suite, _leer_disco)


def _historia(suite: str) -> list[dict]:
    """[(desde, huella)] desde git: una fila por commit que cambió la huella."""
    reg = REGISTRO[suite]
    archivos = [reg["tests"], *{f for f, _ in reg["scorer"]}]
    log = subprocess.run(["git", "log", "--reverse", "--format=%H %cI", "--", *archivos],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
    filas = []
    for ln in filter(None, log):
        sha, fecha = ln.split(" ", 1)

        def leer(ruta, sha=sha):
            r = subprocess.run(["git", "show", f"{sha}:{ruta}"], cwd=ROOT,
                               capture_output=True, text=True)
            return r.stdout if r.returncode == 0 else ""
        h = huella(suite, leer)
        if not filas or filas[-1]["huella"] != h:
            filas.append({"desde": fecha, "commit": sha[:9], "huella": h})
    return filas


def cargar_tabla() -> dict:
    return json.loads(TABLA.read_text(encoding="utf-8")) if TABLA.exists() else {}


def huella_en(tabla: dict, suite: str, fecha_iso: str) -> str | None:
    """La huella vigente en `fecha_iso` (AAAA-MM-DDTHH:MM:SS), o None si es anterior a todas."""
    vigente = None
    for f in tabla.get(suite) or []:
        if f["desde"][:19] <= fecha_iso[:19]:
            vigente = f["huella"]
    return vigente


def fecha_de_run(r: dict) -> str:
    """`timestamp` del runner (AAAAMMDD_HHMMSS…) en ISO; el de la recalificación si la hubo,
    porque la nota de un run recalificado la puso el scorer de ese día."""
    ts = str(r.get("timestamp") or "")
    if len(ts) < 8 or not ts[:8].isdigit():
        return ""
    # Hay timestamps sin hora (`20261109_v61c07`): se toma 00:00, lo conservador — un run del
    # mismo día que un cambio del scorer cae en la versión anterior y no cuenta.
    hora = ts[9:15] if len(ts) >= 15 and ts[9:15].isdigit() else "000000"
    iso = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}T{hora[:2]}:{hora[2:4]}:{hora[4:6]}"
    re_ = str(r.get("rescored_at") or "")
    return max(iso, re_[:19]) if re_ else iso


def run_coincide(r: dict, tabla: dict, actual: str) -> bool:
    """¿Este run se midió con la suite idéntica a la de hoy? Prompts y scorer por fecha; juez
    por la fórmula del propio run (verificable ⇒ quality == answer_score)."""
    suite = r.get("suite")
    if suite not in REGISTRO:
        return False
    if REGISTRO[suite]["juez"] is None and r.get("quality") != r.get("answer_score"):
        return False
    f = fecha_de_run(r)
    return bool(f) and huella_en(tabla, suite, f) == actual


def check() -> list[str]:
    tabla = cargar_tabla()
    fallos = []
    for s in REGISTRO:
        filas = tabla.get(s) or []
        if not filas:
            fallos.append(f"{s}: sin historia en {TABLA.name} — correr --actualizar")
        elif filas[-1]["huella"] != huella_actual(s):
            fallos.append(f"{s}: el código de hoy (prompts, scorer o juez) no es la última huella de "
                          f"{TABLA.name}: cambió y la tabla no — correr --actualizar")
    return fallos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--actualizar", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.actualizar:
        tabla = {s: _historia(s) for s in REGISTRO}
        for s in REGISTRO:
            if tabla[s][-1]["huella"] != huella_actual(s):
                # cambios sin commitear: la huella de hoy entra como última fila
                tabla[s].append({"desde": "9999-12-31T00:00:00", "commit": "sin-commit",
                                 "huella": huella_actual(s)})
        TABLA.write_text(json.dumps(tabla, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        for s, filas in tabla.items():
            print(f"{s}: {len(filas)} versión(es)")
            for f in filas:
                print(f"   desde {f['desde'][:10]}  {f['commit']}  {f['huella'][:12]}")
    fallos = check()
    for f in fallos:
        print(f"  ❌ {f}")
    if not fallos:
        print("✅ huellas de suite: la tabla describe el código de hoy")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
