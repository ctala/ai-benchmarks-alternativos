#!/usr/bin/env python3
"""
Prueba que cada guardrail CACE lo que dice cazar. Sin dependencias, sin pytest.

POR QUÉ EXISTE (13-ago-2026)
----------------------------
Cristian: *"¿entonces nunca más perderemos info? ¿o tendremos problemas de
desincronización o duplicidad?"*

La respuesta honesta era **no**, y el agujero más grande era éste: el repo tenía
**ocho guardrails y CERO pruebas**. Ni un archivo de test. Si `check_calculator` se
rompe mañana, pasa en verde y nadie se entera — que es exactamente el modo de falla
que los guardrails vinieron a resolver, un nivel más arriba.

Es la pregunta vieja: *quis custodiet ipsos custodes*. Un guardrail sin prueba es una
promesa, no un control.

CÓMO PRUEBA
-----------
No verifica que el guardrail pase en verde — eso no prueba nada, un `return 0` fijo
también pasa. Verifica que **falle cuando debe**: se le presenta una versión rota del
mundo y se exige exit ≠ 0. Es el mismo criterio que el RUNBOOK ya pedía para el
canario (*"validalo contra un caso que SABÉS que está roto"*), ahora aplicado a todos.

Cada prueba deja el repo como lo encontró, incluso si falla.

Uso:
    python benchmarks/test_guardrails.py          # exit 1 si algún guardrail no caza
    python benchmarks/test_guardrails.py -v
"""

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = str(ROOT / ".venv" / "bin" / "python")
if not Path(PY).exists():
    PY = sys.executable

VERBOSE = "-v" in sys.argv
resultados: list[tuple[str, bool, str]] = []


def _correr(script: str, *args) -> int:
    return subprocess.run([PY, str(ROOT / "benchmarks" / script), *args],
                          cwd=ROOT, capture_output=True, text=True).returncode


class Sabotaje:
    """Rompe un archivo, corre la prueba, y lo restaura pase lo que pase."""

    def __init__(self, ruta: Path):
        self.ruta = ruta
        self.backup = None

    def __enter__(self):
        if self.ruta.exists():
            self.backup = Path(tempfile.mkdtemp()) / self.ruta.name
            shutil.copy2(self.ruta, self.backup)
        return self

    def __exit__(self, *exc):
        if self.backup and self.backup.exists():
            shutil.copy2(self.backup, self.ruta)
        elif self.backup is None and self.ruta.exists():
            self.ruta.unlink()
        return False


def prueba(nombre: str, detalle: str):
    def deco(fn):
        try:
            ok = fn()
        except Exception as e:  # una prueba que revienta es una prueba que falla
            ok, detalle_final = False, f"{detalle} — excepción: {e}"
        else:
            detalle_final = detalle
        resultados.append((nombre, bool(ok), detalle_final))
        return fn
    return deco


# ── check_calculator: un umbral fuera del rango real no filtra a nadie ─────────
@prueba("check_calculator", "un umbral de calidad bajo el mínimo real")
def _t_calculadora():
    app = ROOT / "docs" / "app.js"
    with Sabotaje(app):
        s = app.read_text(encoding="utf-8")
        # 0.1 está muy por debajo de cualquier score real: no filtraría a nadie
        app.write_text(s.replace("quality: 8.0,", "quality: 0.1,", 1), encoding="utf-8")
        return _correr("check_calculator.py") != 0


# ── check_version: superficies que declaran versiones distintas ────────────────
@prueba("check_version", "dos superficies declarando versiones distintas")
def _t_version():
    ref = ROOT / "scoring_reference.json"
    with Sabotaje(ref):
        d = json.loads(ref.read_text())
        d["version"] = "v9.9"
        ref.write_text(json.dumps(d, indent=2))
        return _correr("check_version.py") != 0


# ── check_docs: un doc vigente sin verificar hace demasiado ───────────────────
@prueba("check_docs", "un doc vigente con verificación vencida")
def _t_docs():
    # No sabotea nada: hoy YA hay 5 docs vencidos, así que debe salir distinto de 0.
    # Si algún día no hay ninguno, la prueba se vuelve vacía — por eso también se
    # comprueba que con una ventana absurda (100 años) salga en verde.
    vencidos = _correr("check_docs.py", "--dias", "90") != 0
    sin_vencidos = _correr("check_docs.py", "--dias", "36500") == 0
    return vencidos and sin_vencidos


# ── el gate del canario: un lote grande sin recibo no arranca ─────────────────
@prueba("gate del canario", "lote de >3 modelos sin recibo fresco")
def _t_canario_gate():
    recibo = ROOT / "benchmarks" / "results" / "_canario_ultimo.json"
    with Sabotaje(recibo):
        if recibo.exists():
            recibo.unlink()
        rc = subprocess.run(
            [PY, str(ROOT / "benchmarks" / "runner.py"), "--quick",
             "--models", "tencent-hy3", "gpt-5.6-luna", "qwen3.7-flash", "gemma-4-26b",
             "--tests", "retrieval_distractores"],
            cwd=ROOT, capture_output=True, text=True).returncode
        return rc != 0


# ── scoring: un tipo desconocido tiene que EXPLOTAR, no devolver 5.0 ─────────
@prueba("scoring", "un expected_answer con tipo inexistente")
def _t_scoring_raise():
    sys.path.insert(0, str(ROOT))
    from benchmarks.scoring import score_expected_answer  # noqa: E402
    try:
        score_expected_answer("cualquier cosa", {"type": "tipo_que_no_existe"})
    except ValueError:
        return True
    return False


@prueba("generate_superficies", "el mapa de superficies desactualizado respecto del registro")
def _t_superficies():
    doc = ROOT / "SUPERFICIES.md"
    with Sabotaje(doc):
        # Se le quita una superficie al doc: el --check tiene que notar que ya no
        # coincide con `check_version.SUPERFICIES`, que es de donde se genera.
        doc.write_text(doc.read_text(encoding="utf-8").replace(
            "| `README.md` |", "| `ARCHIVO-QUE-NO-VA` |", 1), encoding="utf-8")
        return _correr("generate_superficies.py", "--check") != 0


@prueba("check_calculator C5", "un eje medido que la calculadora dejó de exponer")
def _t_calc_c5():
    app = ROOT / "docs" / "app.js"
    with Sabotaje(app):
        # C1-C4 preguntan si la calculadora se ROMPIÓ; C5 si quedó INCOMPLETA. Sin este
        # test, el día que alguien saque un eje del JS todo sigue en verde.
        app.write_text(app.read_text(encoding="utf-8").replace("agentic_quality", "_x_"),
                       encoding="utf-8")
        return _correr("check_calculator.py") != 0


@prueba("check_cortes", "un corte por eje desincronizado de models.json")
def _t_cortes():
    pg = ROOT / "docs" / "mejor-llm-para-json" / "index.html"
    if not pg.exists():
        return False
    with Sabotaje(pg):
        import re as _re
        pg.write_text(_re.sub(r"(<tr><td>1</td><td>(?:<strong>)?)[^<]+",
                              r"\1Modelo Inventado", pg.read_text(encoding="utf-8"), count=1),
                      encoding="utf-8")
        return _correr("check_cortes.py") != 0


@prueba("check_claims", "un doc vivo afirmando lo que una decisión vigente reemplazó")
def _t_claims():
    rm = ROOT / "README.md"
    with Sabotaje(rm):
        rm.write_text(rm.read_text(encoding="utf-8") +
                      "\n## Score = combinación ponderada (NO solo calidad)\n",
                      encoding="utf-8")
        return _correr("check_claims.py") != 0


@prueba("check_caminos", "un script que mide fuera del runner")
def _t_caminos():
    tmp = ROOT / "_desvio_de_prueba.py"
    try:
        tmp.write_text('import requests\nrequests.post("https://openrouter.ai/api/v1/chat/completions")\n')
        return _correr("check_caminos.py") != 0
    finally:
        tmp.unlink(missing_ok=True)


def main() -> int:
    print("Probando que cada guardrail CACE su propio fallo:\n")
    for nombre, ok, detalle in resultados:
        marca = "✅" if ok else "❌"
        print(f"  {marca} {nombre:<22} {detalle}")
    fallan = [n for n, ok, _ in resultados if not ok]
    print()
    if fallan:
        print(f"  ❌ {len(fallan)} guardrail(s) NO cazan lo que dicen cazar: {', '.join(fallan)}")
        print("     Un guardrail que no falla ante su propio fallo es una promesa, no un control.")
        return 1
    print(f"  ✅ los {len(resultados)} guardrails fallan cuando deben.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
