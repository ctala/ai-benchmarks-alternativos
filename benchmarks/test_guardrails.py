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
resultados: list[tuple[str, str, str]] = []   # (nombre, "ok" | "falla" | "omitida", detalle)


class Omitida:
    """Lo que devuelve una prueba que NO pudo correr (sin `.env`, sin el blog).

    3-nov-2026 (corte-v5 1.9). Esas pruebas devolvían `True`: en el CI pasaban sin haber
    probado nada y el resumen las sumaba a «los N guardrails fallan cuando deben»
    (AUDITORIA-GUARDRAILS-2026-11, H5). Una omitida no falla, pero tampoco cuenta como
    verificada: se imprime con ⏭️ y el resumen dice cuántas fueron.
    """
    def __init__(self, motivo: str):
        self.motivo = motivo


def _correr(script: str, *args) -> int:
    """El exit code del guardrail — con el exit 2 de argparse tratado como FALLO del test.

    19-ago-2026. `_t_truncamiento` pasaba `--todos`, un flag que se había renombrado a
    `--solo-rankeados` el día anterior. argparse salía con 2, la prueba leía «≠ 0 → el
    guardrail cazó el caso» y daba VERDE. Nunca corrió el detector.

    Es el mismo falso verde que este archivo existe para evitar, una capa más arriba: el
    guardrail tenía quién lo probara, y la prueba no tenía quién la probara a ella. Un
    error de USO no es una detección, así que acá explota en vez de contar como éxito.
    """
    r = subprocess.run([PY, str(ROOT / "benchmarks" / script), *args],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 2 and "unrecognized arguments" in r.stderr:
        raise AssertionError(
            f"{script}: la prueba lo invoca con un flag que ya no existe "
            f"({' '.join(args)}). {r.stderr.strip().splitlines()[-1]}")
    return r.returncode


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
        if isinstance(ok, Omitida):
            resultados.append((nombre, "omitida", f"{detalle_final} — OMITIDA: {ok.motivo}"))
        else:
            resultados.append((nombre, "ok" if ok else "falla", detalle_final))
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


# ── check_version: el tag de la versión quedó fuera de la historia ─────────────
@prueba("check_version", "el tag de la versión quedó huérfano tras reescribir su commit")
def _t_version_tag_huerfano():
    # 15-sep-2026. v4.13.0 se taggeó y un rebase posterior reescribió su commit: el tag
    # apuntó fuera de main 11 días y nada falló, porque V2 sólo pedía que EXISTIERA. Se
    # reproduce en un repo DESECHABLE con copias de las superficies, nunca en el real: un
    # tag de prueba que sobreviviera a un fallo saldría publicado con el próximo push.
    import importlib.util
    import os
    spec = importlib.util.spec_from_file_location("cv", ROOT / "benchmarks" / "check_version.py")
    cv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cv)
    tmp = Path(tempfile.mkdtemp())
    # Sin NINGUNA variable GIT_* heredada. El hook de pre-push corre con GIT_DIR apuntando
    # al repo real: heredada, `git init/add/commit` en el desechable operan sobre el REAL.
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"GIT_AUTHOR_NAME": "prueba", "GIT_AUTHOR_EMAIL": "prueba@local",
                "GIT_COMMITTER_NAME": "prueba", "GIT_COMMITTER_EMAIL": "prueba@local"})
    try:
        for archivo in {s["archivo"] for s in cv.SUPERFICIES} | {"benchmarks/check_version.py"}:
            (tmp / archivo).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / archivo, tmp / archivo)

        def git(*a):
            return subprocess.run(["git", *a], cwd=tmp, env=env, capture_output=True,
                                  text=True, check=True).stdout.strip()

        git("init", "-q")
        # Y si igual el git-dir no quedó DENTRO del desechable, se aborta antes de tocar nada.
        if not Path(git("rev-parse", "--absolute-git-dir")).resolve().is_relative_to(tmp.resolve()):
            raise AssertionError("el repo desechable resolvió a otro repo: abortado sin tocarlo")
        git("add", "-A")
        git("commit", "-q", "-m", "release")
        chequeo = [PY, str(tmp / "benchmarks" / "check_version.py")]
        # Control: recién taggeado TIENE que pasar. Sin esto, un rojo por cualquier otro
        # motivo (una superficie que no se copió) contaría como detección.
        if subprocess.run([*chequeo, "--tag"], cwd=tmp, env=env,
                          capture_output=True).returncode != 0:
            raise AssertionError("el repo desechable no pasa ni recién taggeado")
        git("commit", "-q", "--amend", "-m", "release reescrito")  # lo que hace un rebase
        r = subprocess.run(chequeo, cwd=tmp, env=env, capture_output=True, text=True)
        return r.returncode != 0 and "V4" in r.stdout
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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
    if _correr("check_cortes.py") != 0:
        return False  # control verde (corte-v5 1.10: no lo tenía)
    with Sabotaje(pg):
        import re as _re
        pg.write_text(_re.sub(r"(<tr><td>1</td><td>(?:<a[^>]*>)?(?:<strong>)?)[^<]+",
                              r"\1Modelo Inventado", pg.read_text(encoding="utf-8"), count=1),
                      encoding="utf-8")
        return _correr("check_cortes.py") != 0


# corte-v5 1.10: las otras cuatro reglas de check_cortes, cada una con su sabotaje. Hasta
# acá solo C2 tenía prueba (AUDITORIA-GUARDRAILS-2026-11, H6).
def _cortes_cfg():
    sys.path.insert(0, str(ROOT))
    from benchmarks.generate_rankings import RANKINGS
    return RANKINGS


@prueba("check_cortes C3", "un corte agéntico que recomienda a un modelo que no corre en un agente")
def _t_cortes_c3():
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    no_apto = next((m["name"] for m in datos["models"] if m.get("sirve_para_agentes") is False), None)
    if not no_apto:
        raise AssertionError("ningún modelo marcado como no apto: no hay con qué sabotear")
    cfg = next(c for c in _cortes_cfg() if c.get("criterion") == "suite"
               and c["suite"] in {"tool_calling", "agent_long_horizon", "policy_adherence"})
    pg = ROOT / "docs" / cfg["slug"] / "index.html"
    if _correr("check_cortes.py") != 0:
        return False
    with Sabotaje(pg):
        t = pg.read_text(encoding="utf-8")
        roto = t.replace("<tr><td>1</td>", f"<tr><td>99</td><td>{no_apto}</td></tr><tr><td>1</td>", 1)
        if roto == t:
            raise AssertionError(f"{cfg['slug']} no tiene fila #1: el sabotaje no tocaría nada")
        pg.write_text(roto, encoding="utf-8")
        return _correr("check_cortes.py") != 0


@prueba("check_cortes C4", "una página con la segunda tabla puesta (o quitada) contra lo que dice el dato")
def _t_cortes_c4():
    pg = ROOT / "docs" / "mejor-llm-para-json" / "index.html"
    if _correr("check_cortes.py") != 0:
        return False
    marca = "La misma capacidad, por lo que cuesta"
    with Sabotaje(pg):
        t = pg.read_text(encoding="utf-8")
        roto = (t.replace(marca, "Otra tabla") if marca in t
                else t.replace("</body>", f"<h2>{marca}</h2></body>", 1))
        if roto == t:
            raise AssertionError("la página no cambió: el sabotaje no tocaría nada")
        pg.write_text(roto, encoding="utf-8")
        return _correr("check_cortes.py") != 0


@prueba("check_cortes C5", "un veredicto que corona a uno y una tabla que pone primero a otro")
def _t_cortes_c5():
    pg = ROOT / "docs" / "mejor-llm-para-agentes" / "index.html"
    if _correr("check_cortes.py") != 0:
        return False
    import re as _re
    with Sabotaje(pg):
        t = pg.read_text(encoding="utf-8")
        roto = _re.sub(r'(<p class="verdict-lead">).*?(</p>)',
                       r"\1Modelo Inventado encabeza la tabla en calidad.\2", t, count=1, flags=_re.S)
        if roto == t:
            raise AssertionError("la página ya no tiene `verdict-lead`: el sabotaje no tocaría nada")
        pg.write_text(roto, encoding="utf-8")
        return _correr("check_cortes.py") != 0


@prueba("check_ganadores", "una página que corona a quien su propia tabla no sostiene")
def _t_ganadores():
    # Los DOS casos reales del 19-ago: el veredicto que nombraba a un #73 como líder,
    # y el «Gana X» sobre tres celdas idénticas. Distinta causa, mismo efecto para
    # el lector — la tabla dice una cosa y el texto otra.
    pg = ROOT / "docs" / "grok-4-1-vs-4-5" / "index.html"
    if not pg.exists():
        return False
    with Sabotaje(pg):
        pg.write_text(pg.read_text(encoding="utf-8").replace(
            "Empatan arriba 3 de 4", "Gana 4.20", 1), encoding="utf-8")
        return _correr("check_ganadores.py") != 0


@prueba("check_release_mensual", "un reporte del mes que le atribuye a un modelo una cifra que no es suya")
def _t_release():
    # El caso real: cifras escritas a mano dentro de un generador data-driven. El PDF
    # publicaba «GPT-OSS 120B · 8.15» cuando el valor vivo era 8,03, y lo reimprimía
    # cada mes. Se prueba cambiando la nota de un modelo por otra: una cifra suelta
    # existe decenas de veces en el JSON, así que sólo lo caza quien verifica la PAREJA.
    #
    # 3-nov-2026. La v1 exigía que existiera el DATASHEET del mes en curso y buscaba una
    # pareja fija («Qwen 3.8 Flash | 9,85»). Entre el día 1 y el release de cada mes no
    # hay datasheet, y cuando lo hay la pareja ya no está: la prueba daba ROJO sin que
    # nada estuviera roto, y hasta entonces había dado verde sin probar nada. Ahora, si
    # no hay datasheet del mes, se fabrica uno mínimo y correcto desde models.json; en
    # los dos casos se exige control VERDE y recién entonces se sabotea la primera fila.
    from datetime import date
    import re as _re
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    R = sorted([m for m in d["models"] if m.get("ranked")],
               key=lambda x: -(x.get("quality_avg") or 0))
    ds = ROOT / f"DATASHEET_{date.today().strftime('%Y-%m')}.md"
    FILA = _re.compile(r"^(\| \*\*([^*|]+)\*\* \| \**)([5-9][.,]\d{2})\b", _re.M)
    with Sabotaje(ds):
        if not ds.exists():
            ds.write_text(f"# Datasheet de prueba: {len(R)} modelos rankeados\n\n"
                          f"| Modelo | Nota |\n|---|---|\n"
                          f"| **{R[0]['name']}** | {R[0]['quality_avg']:.2f} |\n", encoding="utf-8")
        if _correr("check_release_mensual.py") != 0:
            return False  # control: el datasheet íntegro tiene que pasar
        t = ds.read_text(encoding="utf-8")
        m = FILA.search(t)
        if not m:
            return False
        # una cifra que NO sea de ningún modelo cuyo nombre esté en esa celda
        fam = [x for x in d["models"] if x["name"] in m.group(2)]
        usadas = {f"{float(v):.2f}" for x in fam for v in _re.findall(r"-?\d+\.\d+", json.dumps(x))}
        otra = next(c for c in ("5.01", "5.02", "5.03", "5.04") if c not in usadas)
        ds.write_text(t[:m.start(3)] + otra + t[m.end(3):], encoding="utf-8")
        return _correr("check_release_mensual.py") != 0


@prueba("check_paleta", "un color inventado que el manual de marca no tiene")
def _t_paleta():
    # El caso real: alguien necesita «un amarillo para advertencia», lo escribe en una
    # regla y se queda. Así llegaron los 22 colores fuera de manual que había el 19-ago
    # — ninguno por decisión, todos por acumulación.
    css = ROOT / "docs" / "style.css"
    with Sabotaje(css):
        css.write_text(css.read_text(encoding="utf-8") +
                       "\n.inventado { color: #ffcc00; }\n", encoding="utf-8")
        return _correr("check_paleta.py") != 0


@prueba("check_fichas_alcanzables", "una página que lista modelos sin dejar llegar a su ficha")
def _t_fichas():
    # Se le quita el enlace a la ficha a UNA página de ranking, dejando el nombre pelado.
    # Es el estado exacto en que estaban las 16 páginas antes del 19-ago: publicaban al
    # modelo, y el lector que quería el detalle no tenía a dónde ir.
    pg = ROOT / "docs" / "mejor-llm-para-json" / "index.html"
    if not pg.exists():
        return False
    with Sabotaje(pg):
        import re as _re
        pg.write_text(_re.sub(r'<a class="a-ficha"[^>]*>(.*?)</a>', r"\1",
                              pg.read_text(encoding="utf-8")), encoding="utf-8")
        return _correr("check_fichas_alcanzables.py") != 0


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


@prueba("check_suites S6", "una suite que dice no promediar y sí promedia")
def _t_suites_declarado_vs_real():
    """S6 es un AVISO, no un fallo: el exit code no cambia, así que se lee el texto.

    Y como S6 NACE con dos avisos (`tool_calling`, `integridad_idioma`), un control
    global «verde antes de romper» es imposible — sería un sabotaje sobre un mundo ya
    sucio, que es el falso verde que este archivo existe para evitar. Así que el control
    es POR SUITE: `reasoning` no debe aparecer hoy, y debe aparecer tras el sabotaje.
    """
    reg = ROOT / "benchmarks" / "suites.py"

    def s6_menciona(texto: str) -> bool:
        salida = subprocess.run([PY, str(ROOT / "benchmarks" / "check_suites.py")],
                                capture_output=True, text=True, cwd=ROOT).stdout
        return any("S6" in ln and texto in ln for ln in salida.splitlines())

    if s6_menciona("reasoning"):
        return False  # control sucio: ya sale antes de romper nada, no prueba nada
    with Sabotaje(reg):
        original = reg.read_text(encoding="utf-8")
        roto = original.replace(
            '"reasoning": {\n        "pilar": "Razonamiento", "en_promedio": True,',
            '"reasoning": {\n        "pilar": "Razonamiento", "en_promedio": False,', 1)
        if roto == original:
            raise AssertionError(
                "el sabotaje no cambió nada: `reasoning` ya no se declara así en suites.py")
        reg.write_text(roto, encoding="utf-8")
        return s6_menciona("reasoning")


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
    # Control verde: desde el 3-nov es bloqueante, y un rojo previo haría pasar la prueba
    # sin que el modelo fabricado tuviera nada que ver.
    if _correr("check_truncamiento.py", "--duro") != 0:
        return False
    try:
        runs = [{"model": "Modelo De Prueba Truncado", "model_id": "prueba/truncado",
                 "suite": "reasoning", "success": True, "quality": 7.0,
                 "finish_reason": "length" if i % 2 else "stop",
                 "output_tokens": 2048 if i % 2 else 700}
                for i in range(60)]
        tmp.write_text(_json.dumps({"metadata": {"timestamp": "prueba"}, "results": runs}))
        # Sin `--solo-rankeados`: el modelo inventado no está en models.json, y desde el
        # 18-ago el default ya mira TODO lo que haya en disco. Lo que se prueba es que el
        # umbral dispare, no la lista de rankeados.
        return _correr("check_truncamiento.py", "--duro") != 0
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
        return Omitida("sin .env en esta máquina no hay un valor real que plantar")
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
    # 3-nov-2026 (corte-v5 1.9): sobre un blog DESECHABLE (`--blog`), no sobre el real. Antes,
    # sin el blog clonado (CI) devolvía True sin probar nada. El estado del blog real lo mira
    # el propio `check_blog_consistency` en el QA; esta prueba mira que el detector cace.
    blog = Path(tempfile.mkdtemp())
    posts = blog / "src" / "content" / "blog"
    posts.mkdir(parents=True)
    # El caso real de julio: ocho posts en producción con claims muertos, uno coronando
    # como «#1 de mi benchmark» a un modelo que estaba #9.
    #
    # 16-sep-2026 · esta prueba daba VERDE sin cazar nada. Saboteaba con «Modelo Inventado»,
    # que no está en el catálogo: el detector sólo mira modelos rankeados, así que ese texto
    # le era invisible. El exit≠0 que la prueba leía como «cazó» venía de OTRO lado — los 19
    # posts reales que publicaban cifras viejas. Pasaba gracias a la deuda, no a su saboteo,
    # y se descubrió al dejar el blog en cero. Por eso ahora: (1) control en verde primero,
    # porque sobre un blog sucio ningún saboteo prueba nada, y (2) el modelo sale de
    # models.json, para que la prueba no caduque cuando cambie el catálogo.
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    rankeados = sorted([m for m in datos["models"] if m.get("ranked")],
                       key=lambda m: -(m.get("score_calidad") or 0))
    modelo = rankeados[0]["name"]        # el primero por calidad
    posicion_falsa = len(rankeados)      # decir que es el último: siempre lejos del real
    tmp = posts / "_prueba_guardrail_blog.md"
    try:
        if _correr("check_blog_consistency.py", "--blog", str(blog)) != 0:
            raise AssertionError(
                "el blog vacío ya da rojo: el saboteo no probaría nada")
        tmp.write_text(
            f"---\ntitle: prueba\nseoTitle: {modelo} es el #{posicion_falsa} de mi benchmark\n"
            "description: prueba\npubDate: 2026-08-17\n---\n\n"
            f"En mi benchmark, {modelo} aparece hoy como el #{posicion_falsa}.\n",
            encoding="utf-8")
        return _correr("check_blog_consistency.py", "--blog", str(blog)) != 0
    finally:
        shutil.rmtree(blog, ignore_errors=True)


@prueba("generate_blog_datos", "un dato marcado en un post con el valor viejo")
def _t_blog_datos():
    # Sobre un blog DESECHABLE (`--blog`), como `_t_blog`: corre también en CI (corte-v5 1.9).
    blog = Path(tempfile.mkdtemp())
    posts = blog / "src" / "content" / "blog"
    posts.mkdir(parents=True)
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    key = next(m["key"] for m in datos["models"] if m.get("ranked"))
    tmp = posts / "_prueba_guardrail_datos.md"
    try:
        # Control en verde primero — la lección del 16-sep: sobre un mundo ya sucio, un
        # saboteo no prueba nada y la prueba pasa por el motivo equivocado.
        if _correr("generate_blog_datos.py", "--check", "--blog", str(blog)) != 0:
            raise AssertionError("el blog vacío ya da rojo: el saboteo no probaría nada")
        tmp.write_text(
            "---\ntitle: prueba\ndescription: prueba\npubDate: 2026-09-16\n---\n\n"
            f"Calidad de prueba: <!-- D:{key}:calidad -->0,00<!-- /D -->\n",
            encoding="utf-8")
        return _correr("generate_blog_datos.py", "--check", "--blog", str(blog)) != 0
    finally:
        shutil.rmtree(blog, ignore_errors=True)


@prueba("check_changelog", "cambios sin su entrada, y un bump que no alcanza")
def _t_changelog():
    # Dos fallos en uno, porque son las dos mitades del estándar (VERSIONADO.md):
    # que lo hecho esté ESCRITO, y que el número declarado alcance para lo que se tocó.
    ch = ROOT / "CHANGELOG.md"
    with Sabotaje(ch):
        txt = ch.read_text(encoding="utf-8")
        # Se vacía `## [No publicado]`: si hay cambios desde el último tag —y en un repo
        # vivo siempre los hay— tiene que protestar.
        import re as _re
        roto = _re.sub(r"(^##\s*\[No publicado\]\s*$).*?(?=^##\s*\[)",
                       r"\1\n\n", txt, count=1, flags=_re.S | _re.M)
        if roto == txt:
            return False  # sin la sección no se puede probar; mejor fallar que fingir
        ch.write_text(roto, encoding="utf-8")
        # Puede no haber cambios desde el tag (repo recién taggeado): se fabrica uno.
        tmp = ROOT / "benchmarks" / "_prueba_changelog.py"
        try:
            tmp.write_text("# archivo de prueba\n")
            subprocess.run(["git", "add", "-N", str(tmp)], capture_output=True, cwd=ROOT)
            return _correr("check_changelog.py") != 0
        finally:
            subprocess.run(["git", "rm", "-q", "--cached", "--force", str(tmp)],
                           capture_output=True, cwd=ROOT)
            tmp.unlink(missing_ok=True)


# ── qa.py: la tolerancia de lote deja de ser una lista cerrada ─────────────────
@prueba("qa · tolerancia de lote", "tolerar en main, o tolerar un rojo no declarado")
def _t_qa_tolerancia_lote():
    """26-sep-2026. La Regla 4 pushea un lote a medias, y eso pone en rojo por diseño dos
    chequeos (el export y el bump llegan al cerrar). Se degradan SÓLO en `lote/*` y SÓLO
    los nombrados; el riesgo del mecanismo no es que no tolere, es que tolere de más —
    y un QA que en una rama no bloquea nada es un QA que no existe.

    Se prueba en las tres direcciones con un chequeo de mentira que siempre falla, así
    la prueba no depende de si hoy el CHANGELOG está al día.
    """
    import contextlib
    import io
    import sys as _s
    _s.path.insert(0, str(ROOT / "benchmarks"))
    import qa as _qa

    # Una tolerancia cuyo nombre no existe entre los chequeos no tolera nada y nadie se
    # entera; y si el chequeo se renombra, queda viva apuntando a otro. Acá se cae.
    nombres = {c[1] for c in _qa.CHEQUEOS}
    if any(k not in nombres for k in (*_qa.TOLERADO_EN_LOTE, *_qa.DESELECT_EN_LOTE)):
        return False
    # Los secretos no se toleran en ninguna rama: es el único fallo del que no se vuelve.
    if "ninguna credencial real en los archivos versionados" in (
            {*_qa.TOLERADO_EN_LOTE, *_qa.DESELECT_EN_LOTE}):
        return False

    FALSO = "chequeo de mentira que siempre falla"
    originales, argv = list(_qa.CHEQUEOS), _s.argv
    try:
        _qa.CHEQUEOS[:] = [("datos", FALSO, [PY, "-c", "raise SystemExit(1)"], True, True)]

        def corrida(rama):
            _s.argv = ["qa.py", "--pre-merge", "--rama", rama]
            with contextlib.redirect_stdout(io.StringIO()):
                return _qa.main()

        # (a) control: en una rama de lote, un rojo que NO se declaró sigue frenando.
        if corrida("lote/prueba") == 0:
            return False
        # (b) en main no se tolera ni lo declarado: el gate de merge es el de siempre.
        _qa.TOLERADO_EN_LOTE[FALSO] = "motivo de prueba"
        if corrida("main") == 0:
            return False
        # (c) declarado + rama de lote: informativo, no frena.
        return corrida("lote/prueba") == 0
    finally:
        _s.argv = argv
        _qa.TOLERADO_EN_LOTE.pop(FALSO, None)
        _qa.CHEQUEOS[:] = originales


@prueba("runner · veto de catálogo", "medir un modelo marcado `no_medir`, pedido explícito")
def _t_veto():
    # El caso exacto del 18-ago: se pidió por nombre un modelo excluido por decisión y el
    # runner lo midió igual, porque el flag solo lo miraba la capa que publica. Se exige
    # que RECHACE — y que lo diga, no que lo descarte en silencio.
    r = subprocess.run([PY, str(ROOT / "benchmarks" / "runner.py"),
                        "--models", "gpt-5.6-luna-pro", "--tests", "reasoning",
                        "--sin-canario"],
                       capture_output=True, text=True, cwd=ROOT)
    salida = (r.stdout or "") + (r.stderr or "")
    return "RECHAZADOS" in salida and "gpt-5.6-luna-pro" in salida


@prueba("canario · truncamiento", "un modelo que razona sin estar declarado")
def _t_canario_trunca():
    # Se le pasan runs FABRICADOS con la firma del 18-ago: mitad cortados por el techo.
    # No se mide nada — `revisar()` es una función pura, y por eso se puede probar sola.
    import sys as _s
    _s.path.insert(0, str(ROOT / "benchmarks"))
    from canario import revisar
    runs = [{"success": True, "response_preview": "texto", "output_tokens": 2048,
             "finish_reason": "length", "suite": "business_audit", "tool_calls_made": 0}
            for _ in range(12)]
    runs += [{"success": True, "response_preview": "texto", "output_tokens": 400,
              "finish_reason": "stop", "suite": "business_audit", "tool_calls_made": 0}
             for _ in range(4)]
    return any("CORTADAS" in p for p in revisar("modelo-de-prueba", runs))


# ── check_effort: el effort vuelve a ser un string fijo ────────────────────────────
@prueba("check_effort", "el resolver vuelve a mandar `medium` a todos")
def _t_effort():
    mod = ROOT / "benchmarks" / "effort.py"
    with Sabotaje(mod):
        # La forma exacta del 2-sep: un string fijo, sin mirar qué soporta cada modelo.
        mod.write_text(mod.read_text(encoding="utf-8") +
                       '\n\ndef resolver(model_id, pedido=None, foto=None):\n'
                       '    return "medium", "sabotaje"\n', encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("check_effort · foto", "un modelo del catálogo que falta en la foto")
def _t_effort_foto():
    import json as _json
    foto = ROOT / "benchmarks" / "reasoning_openrouter.json"
    with Sabotaje(foto):
        datos = _json.loads(foto.read_text(encoding="utf-8"))
        datos["modelos"].pop("z-ai/glm-5.3", None)
        foto.write_text(_json.dumps(datos), encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("check_effort · E5", "un lote con effort pedido en la carpeta que lee el export")
def _t_effort_experimento():
    import json as _json
    # Nombre neutro a propósito: si lo cazara E6 por el nombre, no probaría E5.
    f = ROOT / "benchmarks" / "results" / "benchmark_zz_sabotaje_effort.json"
    with Sabotaje(f):
        f.write_text(_json.dumps({"metadata": {}, "results": [
            {"model": "X", "success": True, "reasoning_effort": "pedido:low"}]}),
            encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("check_effort · E6", "un experimento viejo, sin etiqueta, con nombre de experimento")
def _t_effort_nombre():
    # La forma exacta del 4-sep: `benchmark_exp_effort_low.json`, runs sin etiqueta.
    f = ROOT / "benchmarks" / "results" / "benchmark_exp_sabotaje.json"
    with Sabotaje(f):
        f.write_text('{"metadata": {}, "results": []}', encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("runner · juez canónico", "un lote lanzado con el Phi-4 local en vez de phi4-or")
def _t_juez_canonico():
    # El caso exacto del 14-sep: los dos lanzadores del lote salieron con `--judge-model
    # phi4`. Se pide `--list-models` a propósito: si la traba se rompe, el runner lista y
    # sale con 0, y la prueba falla sin haber medido ni gastado nada.
    r = subprocess.run([PY, str(ROOT / "benchmarks" / "runner.py"),
                        "--judge", "--judge-model", "phi4", "--list-models"],
                       capture_output=True, text=True, cwd=ROOT, timeout=120)
    salida = (r.stdout or "") + (r.stderr or "")
    return r.returncode != 0 and "juez canónico" in salida


@prueba("check_effort · E7", "una foto sin los parámetros que declara cada modelo")
def _t_effort_parametros():
    import json as _json
    foto = ROOT / "benchmarks" / "reasoning_openrouter.json"
    with Sabotaje(foto):
        datos = _json.loads(foto.read_text(encoding="utf-8"))
        # La forma de la foto antes del 14-sep: sin esto el adapter vuelve a mandarle
        # max_tokens a Sakana y sus tests con herramientas dan 404.
        datos.pop("parametros", None)
        foto.write_text(_json.dumps(datos), encoding="utf-8")
        return _correr("check_effort.py") != 0


# ── Tarea 1.1b/1.2 de corte-v5 (3-nov-2026): lo que corría en el QA sin prueba ──────
# R5 de `check_cobertura` pasó a leer `qa.py` entero y destapó seis entradas que nadie
# saboteaba (AUDITORIA-GUARDRAILS-2026-11). Cada prueba de abajo arranca con control VERDE
# sobre un mundo fabricado, y recién entonces lo rompe.

_salida_en_proceso = ""


def _en_proceso(archivo: str, argv: list[str], **reemplazos) -> int:
    """Corre el `main()` de un chequeo dentro de este proceso, con funciones reemplazadas.

    Para lo que no se puede fabricar en disco: la red (`check_presupuesto`) o una
    recursión (`cobertura.py` corre este mismo archivo para medir).
    """
    import contextlib
    import importlib.util
    import io
    spec = importlib.util.spec_from_file_location(f"_sab_{archivo}", ROOT / "benchmarks" / archivo)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Un reemplazo como `subprocess__run` toca el módulo `subprocess` de TODO el proceso,
    # no solo el del chequeo: sin restaurarlo, cada prueba posterior corría contra el falso.
    # Pasó al escribir esto: 7 pruebas de `check_specs` en rojo sin haber cambiado nada.
    originales = []
    argv_orig = sys.argv
    try:
        for ruta, valor in reemplazos.items():
            objetivo = mod
            *pre, ultimo = ruta.split("__")
            for p in pre:
                objetivo = getattr(objetivo, p)
            if not hasattr(objetivo, ultimo):
                raise AssertionError(f"{archivo}: ya no existe `{ruta}`, el sabotaje no tocaría nada")
            originales.append((objetivo, ultimo, getattr(objetivo, ultimo)))
            setattr(objetivo, ultimo, valor)
        sys.argv = [archivo, *argv]
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                return mod.main()
        finally:
            global _salida_en_proceso
            _salida_en_proceso = buf.getvalue()  # para las reglas que solo AVISAN (exit 0)
    finally:
        sys.argv = argv_orig
        for objetivo, nombre, valor in reversed(originales):
            setattr(objetivo, nombre, valor)


@prueba("check_presupuesto", "saldo de cuenta corto escondido detrás de una key con tope holgado")
def _t_presupuesto():
    # El falso verde del 17-ago tal cual: $720 libres en la key y $16,81 en la cuenta.
    # Sin red: se reemplaza `estado()`, que es lo único que consulta OpenRouter.
    holgado = ({"limit": 1000, "limit_remaining": 720.0}, {"total_credits": 500, "total_usage": 10})
    corto = ({"limit": 1000, "limit_remaining": 720.0}, {"total_credits": 100, "total_usage": 83.19})
    if _en_proceso("check_presupuesto.py", ["--necesito", "20"], estado=lambda: holgado) != 0:
        return False  # control: con saldo de sobra tiene que dejar pasar
    return _en_proceso("check_presupuesto.py", ["--necesito", "20"], estado=lambda: corto) != 0


@prueba("check_ci", "un fallo aislado de hace 10 días, o un cron declarado que no corre")
def _t_ci():
    # corte-v5 1.6. El caso de H1 tal cual: UNA corrida roja como último estado, días
    # atrás. Con la racha de 3 de antes esto daba verde. Sin red: se reemplazan las corridas
    # de `gh`, el YAML de main y el reloj.
    from datetime import datetime, timedelta, timezone
    ahora = datetime(2026, 11, 3, 12, 0, tzinfo=timezone.utc)

    def run(conclusion, hace_dias):
        t = (ahora - timedelta(days=hace_dias)).strftime("%Y-%m-%dT%H:%M:%SZ")
        return {"conclusion": conclusion, "createdAt": t, "status": "completed", "event": "push"}

    sin_cron = "on:\n  push:\n    branches: [main]\n"
    con_cron = sin_cron + "  schedule:\n    - cron: '0 9 * * *'\n"

    def ci(runs, yaml):
        return _en_proceso("check_ci.py", [], _runs=lambda: runs,
                           _yaml_de_main=lambda: yaml, _ahora=lambda: ahora)

    # Controles: un verde de ayer pasa; un rojo de hace 3 horas todavía tiene margen; y sin
    # cron en main, no correr hace 5 días es lo esperado (el Action solo corre en push).
    if ci([run("success", 1), run("failure", 3)], sin_cron) != 0:
        return False
    if ci([run("failure", 0.125), run("success", 1)], sin_cron) != 0:
        return False
    if ci([run("success", 5)], sin_cron) != 0:
        return False
    if ci([run("success", 1)], con_cron) != 0:
        return False
    # Sabotajes: el fallo aislado de hace 10 días, y con cron, 5 días sin ninguna corrida.
    if ci([run("failure", 10), run("success", 12), run("success", 13)], sin_cron) == 0:
        return False
    return ci([run("success", 5)], con_cron) != 0


@prueba("check_cortes C1", "un eje que decide, medido y sin su corte publicado (aviso)")
def _t_cortes_c1():
    # C1 AVISA y no frena (un corte que falta no rompe nada publicado): la prueba mira que el
    # aviso salga y nombre al eje, no el exit code. Necesita `_en_proceso`, por eso vive acá.
    eje = "tool_calling"
    if _en_proceso("check_cortes.py", []) != 0 or f"`{eje}` está medida" in _salida_en_proceso:
        return False  # control: con su corte, no hay aviso
    import importlib.util
    spec = importlib.util.spec_from_file_location("_cc_c1", ROOT / "benchmarks" / "check_cortes.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    def sin_el_corte():
        cortes = m._cortes_publicados()
        if eje not in cortes:
            raise AssertionError(f"`{eje}` ya no tiene corte: el sabotaje no quitaría nada")
        cortes.pop(eje)
        return cortes
    _en_proceso("check_cortes.py", [], _cortes_publicados=sin_el_corte)
    return f"`{eje}` está medida" in _salida_en_proceso


@prueba("check_changelog C2", "un cambio de medición publicado como patch")
def _t_changelog_bump():
    # corte-v5 1.10. La prueba de arriba corre SIN `--nivel`: C2 nunca se saboteaba aunque la
    # descripción lo nombrara (AUDITORIA-GUARDRAILS-2026-11, H6). Sin git ni CHANGELOG reales:
    # se fija lo tocado (una suite, que exige MINOR) y el salto declarado.
    tocado = lambda tag: ["benchmarks/tests/test_inventado.py"]  # noqa: E731
    base = dict(ultimo_tag=lambda: "v9.0.0", cambios_desde=tocado,
                seccion_no_publicado=lambda texto: "- una entrada")
    if _en_proceso("check_changelog.py", ["--nivel"], salto_de_version=lambda tag: "minor", **base) != 0:
        return False  # control: un MINOR alcanza para tocar una suite
    if _en_proceso("check_changelog.py", [], salto_de_version=lambda tag: "patch", **base) != 0:
        return False  # control: sin `--nivel`, C2 no corre
    return _en_proceso("check_changelog.py", ["--nivel"], salto_de_version=lambda tag: "patch", **base) != 0


@prueba("check_gitleaks", "un hex de 64 con contexto de clave, un JSON generado nuevo con keys, o sin gitleaks")
def _t_gitleaks():
    # corte-v5 1.7. Tres mundos rotos, cada uno en un archivo nuevo del árbol (no ignorado,
    # así que entra a lo que versionaría git) y borrado siempre.
    import secrets
    if _correr("check_gitleaks.py") != 0:
        return False  # control verde
    plantado = ROOT / "_prueba_gitleaks.md"
    try:
        plantado.write_text(f"config\n\nR2_SECRET_ACCESS_KEY={secrets.token_hex(32)}\n")
        if _correr("check_gitleaks.py") == 0:
            return False
    finally:
        plantado.unlink(missing_ok=True)
    # Un JSON generado NUEVO con keys de modelos no está en las exclusiones: tiene que verse.
    copia = ROOT / "docs" / "data" / "_prueba_gitleaks_models.json"
    try:
        shutil.copy2(ROOT / "docs" / "data" / "models.json", copia)
        if _correr("check_gitleaks.py") == 0:
            return False
    finally:
        copia.unlink(missing_ok=True)
    # Sin la herramienta: rojo con la instrucción, nunca un verde por omisión.
    return _en_proceso("check_gitleaks.py", [], shutil__which=lambda nombre: None) != 0


@prueba("cobertura.py", "el núcleo bajo el piso de cobertura")
def _t_cobertura_nucleo():
    # No se puede correr de verdad desde acá: mide corriendo test_guardrails, y eso es
    # recursivo. Se reemplaza `subprocess.run` por uno que devuelve el reporte de coverage;
    # lo que se prueba es lo que decide: leer la línea TOTAL y compararla con el piso.
    from types import SimpleNamespace

    def corrida(pct):
        def fake(cmd, **kw):
            out = f"Name  Stmts  Miss  Cover\nTOTAL  100  0  {pct}%\n" if "report" in cmd else "✅"
            return SimpleNamespace(stdout=out, returncode=0)
        return _en_proceso("cobertura.py", ["--duro"], subprocess__run=fake)

    if corrida(95) != 0:
        return False  # control: sobre el piso, pasa
    return corrida(60) != 0


@prueba("check_agentico_publicado", "un rankeado por OpenRouter publicado sin su tarea agéntica")
def _t_agentico():
    # Hoy el chequeo está en rojo informativo (8 sin tarea), así que sobre el dato real no
    # hay control posible. Se fabrica el mundo limpio —todo rankeado con tarea— y se le quita
    # la tarea a UNO servido por OpenRouter, que es el único caso que el chequeo reclama.
    mj = ROOT / "docs" / "data" / "models.json"
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from models import MODELS
    with Sabotaje(mj):
        d = json.loads(mj.read_text(encoding="utf-8"))
        for m in d["models"]:
            if m.get("ranked"):
                m["agentico"] = {**(m.get("agentico") or {}), "tareas": {"prueba": {"media": 1.0}}}
        mj.write_text(json.dumps(d), encoding="utf-8")
        if _correr("check_agentico_publicado.py", "--duro") != 0:
            return False  # control: todos con tarea
        victima = next(m for m in d["models"] if m.get("ranked")
                       and MODELS.get(m.get("key") or "", {}).get("provider", "openrouter") == "openrouter")
        victima["agentico"].pop("tareas")
        mj.write_text(json.dumps(d), encoding="utf-8")
        return _correr("check_agentico_publicado.py", "--duro") != 0


@prueba("auditar_paginas", "una página de ranking que no publica ninguna fila")
def _t_auditar_paginas():
    pg = ROOT / "docs" / "mejor-llm-para-json" / "index.html"
    if _correr("auditar_paginas.py", "--duro") != 0:
        raise AssertionError("ya hay hallazgos ALTA: el saboteo no probaría nada")
    with Sabotaje(pg):
        import re as _re
        html = pg.read_text(encoding="utf-8")
        roto = _re.sub(r"<tr[^>]*>\s*<td.*?</tr>", "", html, flags=_re.S)
        if roto == html:
            raise AssertionError("el sabotaje no cambió nada: la tabla ya no tiene esa forma")
        pg.write_text(roto, encoding="utf-8")
        return _correr("auditar_paginas.py", "--duro") != 0


@prueba("generate_censo_proveedores", "un censo de proveedores más viejo que su caducidad")
def _t_censo():
    # 3-nov-2026: `--check` devolvía 0 con 45 días encima y el QA imprimía ✅ (H7).
    from datetime import date, timedelta
    censo = ROOT / "docs" / "data" / "censo_proveedores.json"
    with Sabotaje(censo):
        d = json.loads(censo.read_text(encoding="utf-8"))
        d["consultado_at"] = date.today().isoformat()
        censo.write_text(json.dumps(d), encoding="utf-8")
        if _correr("generate_censo_proveedores.py", "--check") != 0:
            return False  # control: recién consultado
        d["consultado_at"] = (date.today() - timedelta(days=45)).isoformat()
        censo.write_text(json.dumps(d), encoding="utf-8")
        return _correr("generate_censo_proveedores.py", "--check") != 0


@prueba("generate_blog_tablas", "una tabla del pilar que quedó con el ranking viejo")
def _t_blog_tablas():
    # Sobre una COPIA del post en un blog desechable (`--blog`): no se toca el repo del
    # blog y la prueba corre igual donde no está clonado, con el post de este repo si no.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from generate_blog_tablas import DEFAULT_BLOG, POST
    real = DEFAULT_BLOG / POST
    if not real.exists():
        return Omitida("sin el repo del blog no hay post pilar que copiar")
    tmp = Path(tempfile.mkdtemp())
    try:
        copia = tmp / POST
        copia.parent.mkdir(parents=True)
        shutil.copy2(real, copia)
        if _correr("generate_blog_tablas.py", "--check", "--blog", str(tmp)) != 0:
            raise AssertionError("el pilar real ya está desfasado: el saboteo no probaría nada")
        import re as _re
        t = copia.read_text(encoding="utf-8")
        roto = _re.sub(r"(<!-- AUTO-[\w-]+-START -->).*?(<!-- AUTO-[\w-]+-END -->)",
                       r"\1\n| tabla vieja |\n\2", t, count=1, flags=_re.S)
        if roto == t:
            raise AssertionError("el post ya no tiene bloques AUTO: el sabotaje no tocaría nada")
        copia.write_text(roto, encoding="utf-8")
        return _correr("generate_blog_tablas.py", "--check", "--blog", str(tmp)) != 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@prueba("check_cobertura R5", "algo que corre en qa.py sin prueba ni exención, o una exención sin motivo")
def _t_cobertura_r5():
    def r5_rojo() -> bool:
        salida = subprocess.run([PY, str(ROOT / "benchmarks" / "check_cobertura.py")],
                                capture_output=True, text=True, cwd=ROOT).stdout
        return any(ln.strip().startswith("❌ R5") for ln in salida.splitlines())

    if r5_rojo():
        return False  # control: R5 tiene que estar en verde antes de romperlo
    qa_py = ROOT / "benchmarks" / "qa.py"
    with Sabotaje(qa_py):
        t = qa_py.read_text(encoding="utf-8")
        roto = t.replace("CHEQUEOS = [\n", 'CHEQUEOS = [\n    ("datos", "chequeo sin prueba", '
                         '[PY, "benchmarks/check_inventado.py"], True, True),\n', 1)
        if roto == t:
            raise AssertionError("qa.py ya no declara `CHEQUEOS = [`: el sabotaje no tocaría nada")
        qa_py.write_text(roto, encoding="utf-8")
        if not r5_rojo():
            return False
    cc = ROOT / "benchmarks" / "check_cobertura.py"
    with Sabotaje(cc):
        t = cc.read_text(encoding="utf-8")
        import re as _re
        # Vacía el motivo de `test_unitarios.py`: una exención sin porqué.
        roto = _re.sub(r'("test_unitarios\.py":\s*)"[^"]*"', r'\1""', t, count=1)
        if roto == t:
            raise AssertionError("EXENTOS_R5 ya no tiene la forma esperada")
        cc.write_text(roto, encoding="utf-8")
        return r5_rojo()


@prueba("check_cobertura R8", "una prueba borrada, un bloqueante bajado sin fila o un --duro quitado")
def _t_cobertura_r8():
    # corte-v5 1.4: el instrumento de «ningún guardrail se debilita». Se sabotea el árbol de
    # trabajo que R8 lee (`_texto_actual`) y se deja el tag real como base; nada toca disco.
    import importlib.util
    spec = importlib.util.spec_from_file_location("_sab_r8", ROOT / "benchmarks" / "check_cobertura.py")
    cc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cc)
    real = cc._texto_actual

    def r8(**cambios):
        def falso(rel):
            t = real(rel)
            for viejo, nuevo in cambios.get(rel, []):
                if viejo not in t:
                    raise AssertionError(f"{rel} ya no contiene {viejo!r}: el sabotaje no tocaría nada")
                t = t.replace(viejo, nuevo, 1)
            return t
        cc._texto_actual = falso
        try:
            return cc.r8_ningun_guardrail_se_debilita()
        finally:
            cc._texto_actual = real

    qa, tg, dec = "benchmarks/qa.py", "benchmarks/test_guardrails.py", "DECISIONES.md"
    cortes = ('[PY, "benchmarks/check_cortes.py"], True, True)',
              '[PY, "benchmarks/check_cortes.py"], False, True)')
    if r8():
        return False  # control verde
    # Exactamente una por debajo del máximo histórico desde el tag: el borde de la regla.
    maximo, _ = cc._maximo_de_pruebas()
    sobran = cc._n_pruebas(real(tg)) - maximo + 1
    if sobran < 1 or not r8(**{tg: [("\n@prueba(", "\n#prueba(")] * sobran}):
        return False  # una prueba menos que el máximo
    if not any("check_cortes.py" in x for x in r8(**{qa: [cortes]})):
        return False  # bloqueante → informativo sin fila
    fila = ("| 3-nov-2026 | **Vigente** | `check_cortes.py` pasa a informativo |",
            "| 3-nov-2026 | **Vigente** | `check_cortes.py` pasa a informativo |\n| x |")
    con_fila = r8(**{qa: [cortes], dec: [("\n| 3-nov-2026 |", "\n" + fila[0] + "\n| 3-nov-2026 |")]})
    if any("check_cortes.py" in x for x in con_fila):
        return False  # control: con su fila, bajar a informativo es una decisión, no un descuido
    duro = ('"benchmarks/auditar_paginas.py", "--duro"]', '"benchmarks/auditar_paginas.py"]')
    return any("auditar_paginas.py" in x for x in r8(**{qa: [duro]}))


@prueba("check_cobertura R5", "una exención huérfana (no corre en ningún lado) o ya probada (tiene sabotaje)")
def _t_cobertura_r5_exenciones():
    # corte-v5 1.12. La regla que impide que `EXENTOS_R5` crezca en silencio no tenía quien
    # la rompiera. Cada caso se inyecta por separado y se exige que el rojo NOMBRE al archivo
    # inyectado: un R5 rojo por otra causa no prueba esta regla.
    cc = ROOT / "benchmarks" / "check_cobertura.py"

    def r5_rojo_por(archivo: str) -> bool:
        salida = subprocess.run([PY, str(cc)], capture_output=True, text=True, cwd=ROOT).stdout
        rojo = any(ln.strip().startswith("❌ R5") for ln in salida.splitlines())
        return rojo and archivo in salida

    salida = subprocess.run([PY, str(cc)], capture_output=True, text=True, cwd=ROOT).stdout
    if any(ln.strip().startswith("❌ R5") for ln in salida.splitlines()):
        return False  # control verde
    # check_presupuesto.py corre en qa.py y tiene prueba: exentarlo es una exención ya probada.
    import re as _re
    if not _re.search(r"[\"']check_presupuesto\.py[\"']", Path(__file__).read_text()):
        raise AssertionError("check_presupuesto.py ya no se invoca acá: elegir otro ya probado")
    for archivo in ("check_fantasma.py", "check_presupuesto.py"):
        with Sabotaje(cc):
            t = cc.read_text(encoding="utf-8")
            roto = t.replace("EXENTOS_R5 = {\n",
                             f'EXENTOS_R5 = {{\n    "{archivo}": "motivo de sabotaje",\n', 1)
            if roto == t:
                raise AssertionError("check_cobertura.py ya no declara `EXENTOS_R5 = {`")
            cc.write_text(roto, encoding="utf-8")
            if not r5_rojo_por(archivo):
                return False
    return True



# ── check_specs: un change de OpenSpec que queda en el aire ───────────────────
def _raiz_specs(tmp: Path, *, activos=("corte-x",), archivados=(), tasks="- [x] 1.1 hecha\n",
                design=True, decisiones=True) -> Path:
    """Un `openspec/` DESECHABLE con la forma mínima correcta. Nunca el real: la prueba no
    debe depender de qué change esté abierto hoy (lección de `_t_release`, 3-nov-2026)."""
    raiz = tmp / "openspec"
    (raiz / "changes" / "archive").mkdir(parents=True)
    for n in activos:
        c = raiz / "changes" / n
        c.mkdir()
        (c / ".openspec.yaml").write_text("schema: spec-driven\ncreated: 2026-11-03\n")
        (c / "proposal.md").write_text("## Why\nx\n" + ("Ver DECISIONES.md.\n" if decisiones else ""))
        if design:
            (c / "design.md").write_text("## Context\nx\n")
        (c / "tasks.md").write_text(tasks)
    for n in archivados:
        c = raiz / "changes" / "archive" / n
        c.mkdir()
        (c / "tasks.md").write_text("- [x] 1.1 hecha\n- [ ] 1.2 quedó abierta\n")
    return raiz


def _specs(**kw) -> tuple[int, int]:
    """(exit del control limpio, exit del caso saboteado) sobre raíces desechables."""
    import tempfile as _tf
    rama = kw.pop("rama", "corte/x"); hoy = kw.pop("hoy", "2026-11-10")
    t1, t2 = Path(_tf.mkdtemp()), Path(_tf.mkdtemp())
    try:
        control = _correr("check_specs.py", "--raiz", str(_raiz_specs(t1)),
                          "--rama", "corte/x", "--hoy", "2026-11-10")
        roto = _correr("check_specs.py", "--raiz", str(_raiz_specs(t2, **kw)),
                       "--rama", rama, "--hoy", hoy)
        return control, roto
    finally:
        shutil.rmtree(t1, ignore_errors=True); shutil.rmtree(t2, ignore_errors=True)


@prueba("check_specs", "un change activo en main (S1)")
def _t_specs_en_main():
    control, roto = _specs(rama="main")
    return control == 0 and roto != 0


@prueba("check_specs", "dos changes activos a la vez (S2)")
def _t_specs_dos_activos():
    control, roto = _specs(activos=("a", "b"))
    return control == 0 and roto != 0


@prueba("check_specs", "un change sin tareas ni design (S3)")
def _t_specs_sin_artefactos():
    control, roto = _specs(tasks="## 1\n", design=False)
    return control == 0 and roto != 0


@prueba("check_specs", "un change que nadie toca en 28 días (S4)")
def _t_specs_en_el_aire():
    control, roto = _specs(hoy="2026-12-01")
    return control == 0 and roto != 0


@prueba("check_specs", "un change archivado con una tarea abierta (S5)")
def _t_specs_archivado_abierto():
    control, roto = _specs(archivados=("2026-11-30-viejo",))
    return control == 0 and roto != 0


@prueba("check_specs", "un change que no apunta a DECISIONES.md (S6)")
def _t_specs_sin_decisiones():
    control, roto = _specs(decisiones=False)
    return control == 0 and roto != 0


def resumen(res: list[tuple[str, str, str]]) -> tuple[list[str], int]:
    """Las líneas del reporte y el exit code. Aparte de `main` para que se pueda probar."""
    marcas = {"ok": "✅", "falla": "❌", "omitida": "⏭️ "}
    out = [f"  {marcas[e]} {n:<22} {d}" for n, e, d in res]
    fallan = [n for n, e, _ in res if e == "falla"]
    omitidas = [n for n, e, _ in res if e == "omitida"]
    verificadas = len(res) - len(omitidas)
    out.append("")
    if fallan:
        out.append(f"  ❌ {len(fallan)} guardrail(s) NO cazan lo que dicen cazar: {', '.join(fallan)}")
        out.append("     Un guardrail que no falla ante su propio fallo es una promesa, no un control.")
        code = 1
    else:
        out.append(f"  ✅ los {verificadas} guardrails verificados fallan cuando deben.")
        code = 0
    if omitidas:
        out.append(f"  ⏭️  {len(omitidas)} omitida(s) en esta máquina, NO verificadas: {', '.join(omitidas)}")
    return out, code


@prueba("test_guardrails · omitidas", "una prueba omitida que se cuenta como verificada")
def _t_omitidas():
    # corte-v5 1.9. El resumen es lo que lee quien mira el CI: si una omitida se suma a las
    # verificadas, el CI vuelve a decir «todo probado» sin `.env` ni blog.
    lineas, code = resumen([("a", "ok", "x"), ("b", "omitida", "x — OMITIDA: sin blog")])
    texto = "\n".join(lineas)
    if code != 0 or "los 1 guardrails verificados" not in texto or "1 omitida(s)" not in texto:
        return False
    _, code = resumen([("a", "falla", "x"), ("b", "omitida", "x")])
    return code != 0


def main() -> int:
    print("Probando que cada guardrail CACE su propio fallo:\n")
    lineas, code = resumen(resultados)
    print("\n".join(lineas))
    return code


if __name__ == "__main__":
    sys.exit(main())
