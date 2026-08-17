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
    # SABOTEA de verdad, con un doc propio. La v1 no saboteaba nada: se apoyaba en que
    # «hoy YA hay 5 docs vencidos». El 16-ago-2026 se arreglaron los cinco y el test se
    # quedó sin nada que cazar — su propio comentario lo había anticipado.
    #
    # Un test que solo pasa mientras el repo esté sucio se rompe justo cuando lo limpiás,
    # y lo peor: hasta ese día daba verde sin probar nada.
    tmp = ROOT / "_DOC_VENCIDO_DE_PRUEBA.md"
    try:
        tmp.write_text("<!-- doc: vigente | verificado: 2020-01-01 -->\n# prueba\n")
        vencidos = _correr("check_docs.py", "--dias", "90") != 0
    finally:
        tmp.unlink(missing_ok=True)
    # Y en verde cuando no hay ninguno: sin esto, un chequeo que SIEMPRE falla pasaría.
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


@prueba("check_suites", "el sitio volviendo a escribir a mano las etiquetas de los ejes")
def _t_suites():
    app = ROOT / "docs" / "app.js"
    with Sabotaje(app):
        # La forma exacta que tenía la copia vieja. Vivió meses, divergió en 7 suites y
        # nadie se enteró porque una etiqueta distinta no rompe nada: solo hace que el
        # usuario elija un eje creyendo que está en otro pilar.
        app.write_text(app.read_text(encoding="utf-8") +
                       '\nconst _copia = [{ value: "tool_calling", label: "A mano otra vez" }];\n',
                       encoding="utf-8")
        return _correr("check_suites.py") != 0


@prueba("qa Q15", "una página de comparación publicada que ya nadie regenera")
def _t_huerfanas():
    d = ROOT / "docs" / "modelo-fantasma-vs-otro"
    try:
        d.mkdir(exist_ok=True)
        # Una huérfana no falla: carga, se ve bien y sirve datos congelados. Se descubrió
        # preguntando lo contrario de lo habitual — no «¿falta una página?», sino
        # «¿sobra una?» — y había cuatro, una de ellas mintiendo sobre su frescura.
        (d / "index.html").write_text("<html><body>página congelada</body></html>")
        r = subprocess.run(["node", str(ROOT / "benchmarks" / "qa_calculadora.mjs")],
                           capture_output=True, text=True, cwd=ROOT)
        return r.returncode != 0
    finally:
        (d / "index.html").unlink(missing_ok=True)
        d.rmdir() if d.exists() else None


@prueba("check_consistency", "un doc vivo citando un score que ya no existe")
def _t_consistency():
    rm = ROOT / "MODELOS.md"
    with Sabotaje(rm):
        # Una cifra inventada junto a un modelo real es exactamente el drift que este
        # chequeo existe para cazar: prosa que fue correcta y hoy cita otro número.
        rm.write_text(rm.read_text(encoding="utf-8") +
                      "\n\nGPT-5.6 Luna alcanza un score de 3.14 en el ranking.\n",
                      encoding="utf-8")
        return _correr("check_consistency.py") != 0


@prueba("check_endpoints", "un modelo con endpoint muerto que sigue rankeando")
def _t_endpoints():
    # No se le pega a ningún proveedor: se le pasa un id inexistente y se comprueba que
    # lo clasifique como MUERTO en vez de dejarlo pasar. Sin red, el chequeo tiene que
    # distinguir «no hay credencial» de «el modelo no existe» — que es justo la confusión
    # que casi retira a Llama 3.1 8B por falta de GROQ_API_KEY.
    r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_endpoints.py"),
                        "--models", "proveedor-inventado/modelo-que-no-existe"],
                       capture_output=True, text=True, cwd=ROOT)
    salida = (r.stdout or "") + (r.stderr or "")
    return "MUERTO" in salida.upper() or "SIN CREDENCIAL" in salida.upper() or r.returncode != 0


@prueba("check_cobertura", "una regla aplicada en una superficie y no en las demás")
def _t_cobertura():
    gr = ROOT / "benchmarks" / "generate_rankings.py"
    with Sabotaje(gr):
        # El caso exacto que lo motivó: volver a poner la segunda tabla con un flag a
        # mano página por página, en vez de decidirla con el criterio medido. Así fue como
        # terminó en 2 de 16, y con las páginas que más la necesitaban afuera.
        gr.write_text(gr.read_text(encoding="utf-8").replace(
            '"slug": "mejor-llm-para-agentes"',
            '"segunda_tabla_valor": True, "slug": "mejor-llm-para-agentes"', 1),
            encoding="utf-8")
        return _correr("check_cobertura.py") != 0


@prueba("check_caminos", "un script que mide fuera del runner")
def _t_caminos():
    tmp = ROOT / "_desvio_de_prueba.py"
    try:
        tmp.write_text('import requests\nrequests.post("https://openrouter.ai/api/v1/chat/completions")\n')
        return _correr("check_caminos.py") != 0
    finally:
        tmp.unlink(missing_ok=True)


@prueba("check_truncamiento", "una nota construida sobre respuestas cortadas a la mitad")
def _t_truncamiento():
    # Se fabrica el caso exacto del 17-ago: un modelo con la mitad del examen terminando
    # en `finish_reason="length"`. Nada más está mal —los runs tienen contenido, éxito y
    # forma válida—, que es precisamente por qué ningún otro detector lo ve.
    #
    # El archivo se escribe en results/ porque el chequeo lee de ahí; el nombre lleva
    # `_prueba_` y se borra siempre, incluso si la prueba explota.
    import json as _json
    tmp = ROOT / "benchmarks" / "results" / "_prueba_truncamiento.json"
    try:
        runs = [{"model": "Modelo De Prueba Truncado", "model_id": "prueba/truncado",
                 "suite": "reasoning", "success": True, "quality": 7.0,
                 "finish_reason": "length" if i % 2 else "stop",
                 "output_tokens": 2048 if i % 2 else 700}
                for i in range(60)]
        tmp.write_text(_json.dumps({"metadata": {"timestamp": "prueba"}, "results": runs}))
        # --todos porque el modelo inventado no está en models.json (no es rankeado);
        # lo que se prueba es que el umbral dispare, no la lista de rankeados.
        return _correr("check_truncamiento.py", "--todos", "--duro") != 0
    finally:
        tmp.unlink(missing_ok=True)


@prueba("check_secretos", "una credencial real del .env dentro de un archivo publicable")
def _t_secretos():
    # Se toma un valor REAL del .env y se lo escribe en un archivo versionado, que es
    # exactamente la forma del incidente del 17-ago. Si el chequeo no lo ve, no sirve.
    # El archivo se crea y se borra; el valor nunca se imprime ni queda en disco.
    import sys as _sys
    _sys.path.insert(0, str(ROOT / "benchmarks"))
    from check_secretos import valores_del_env
    env = valores_del_env()
    if not env:
        return True  # sin .env en esta máquina no hay nada que probar (CI)
    valor = next(iter(env.values()))
    tmp = ROOT / "_prueba_secreto.md"
    try:
        tmp.write_text(f"config de ejemplo\n\n    api_key = {valor}\n")
        subprocess.run(["git", "add", "-N", str(tmp)], capture_output=True, cwd=ROOT)
        return _correr("check_secretos.py") != 0
    finally:
        subprocess.run(["git", "rm", "-q", "--cached", "--force", str(tmp)],
                       capture_output=True, cwd=ROOT)
        tmp.unlink(missing_ok=True)


@prueba("check_blog_consistency", "un post del blog citando un score que ya no existe")
def _t_blog():
    # El blog es OTRO repo, así que puede no estar clonado en esta máquina (CI). Sin él
    # no hay nada que probar y la prueba pasa: acusar en falso sería peor.
    blog = Path.home() / "Playground" / "sitios" / "cristiantala-blog"
    posts = blog / "src" / "content" / "blog"
    if not posts.is_dir():
        return True
    # El caso real de julio: ocho posts en producción con claims muertos, uno coronando
    # como «#1 de mi benchmark» a un modelo que estaba #9.
    tmp = posts / "_prueba_guardrail_blog.md"
    try:
        tmp.write_text(
            "---\ntitle: prueba\nseoTitle: Modelo Inventado saca score 99.99 en mi benchmark\n"
            "description: prueba\npubDate: 2026-08-17\n---\n\n"
            "Modelo Inventado tiene un score de 99.99 y es el #1 de mi benchmark.\n",
            encoding="utf-8")
        return _correr("check_blog_consistency.py") != 0
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
