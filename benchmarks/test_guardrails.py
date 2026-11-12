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

import contextlib
import html
import json
import os
import re
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
        app.write_text(app.read_text(encoding="utf-8").replace("multiturno_quality", "_x_"),
                       encoding="utf-8")
        return _correr("check_calculator.py") != 0


@prueba("check_calculator C6", "la tabla histórico vuelve a decir «antes del examen v5» de un reemplazado")
def _t_calc_c6():
    idx = ROOT / "docs" / "index.html"
    with Sabotaje(idx):
        # 7-nov-2026: el fallo real. Los 7 reemplazados rindieron el examen v5 entero y la
        # tabla decía que se midieron antes y no nombraba a su sucesor.
        html = idx.read_text(encoding="utf-8")
        i = html.index('data-motivo="reemplazo"')
        j = html.index("</tr>", i)
        fila = re.sub(r"<td>Lo reemplazó .*?</td>", "<td>Medido antes del examen v5</td>",
                      html[i:j], count=1, flags=re.DOTALL)
        idx.write_text(html[:i] + fila + html[j:], encoding="utf-8")
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
        pg.write_text(_re.sub(r"(<tr><td>(?:1|≈)</td><td>(?:<a[^>]*>)?(?:<strong>)?)[^<]+",
                              r"\1Modelo Inventado", pg.read_text(encoding="utf-8"), count=1),
                      encoding="utf-8")
        return _correr("check_cortes.py") != 0


# corte-v5 1.10: las otras cuatro reglas de check_cortes, cada una con su sabotaje. Hasta
# acá solo C2 tenía prueba (AUDITORIA-GUARDRAILS-2026-11, H6).
def _cortes_cfg():
    sys.path.insert(0, str(ROOT))
    from benchmarks.generate_rankings import RANKINGS
    return RANKINGS


@prueba("check_cortes --dist", "filas con la forma de Astro y un #1 cambiado, y un lector que no reconoce las filas (C3 y C4 leen cero)")
def _t_cortes_dist():
    # 11-nov-2026 (motor-sitio 2.3). Frente a `dist`, FILA_1 no leía nada. Sin Node en el CI, el
    # árbol es una copia de docs/ y las filas se reescriben con la forma que compila Astro.
    import re as _re
    base = Path(tempfile.mkdtemp()) / "dist"
    for f in (ROOT / "docs").glob("*/index.html"):
        d = base / f.parent.name / "index.html"
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, d)

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_cortes.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    def a_astro(t):
        return _re.sub(r"<tr><td>(\d+|≈)</td><td>",
                       lambda m: '<tr>\n  <td class="num">' + (m.group(1) if m.group(1) == "≈" else
                                 f'<span data-cifra>{m.group(1)}</span>') + "</td>\n  <td>", t)

    for f in base.glob("*/index.html"):
        f.write_text(a_astro(f.read_text(encoding="utf-8")), encoding="utf-8")
    ok = correr()[0] == 0                                     # control con la forma de Astro
    pg = base / "mejor-llm-para-json" / "index.html"
    t = pg.read_text(encoding="utf-8")
    m = _re.search(r'<td class="num">(?:<span data-cifra>1</span>|≈)</td>\s*<td>(?:<a[^>]*>)?(?:<strong>)?([^<]+)', t)
    if not m:
        raise AssertionError("mejor-llm-para-json no tiene #1 con la forma de Astro: el sabotaje no tocaría nada")
    pg.write_text(t[:m.start(1)] + "Un modelo que no encabeza" + t[m.end(1):], encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "`structured_output`" in out and "desincronizada" in out
    pg.write_text(t, encoding="utf-8")
    guardadas = {f: f.read_text(encoding="utf-8") for f in base.glob("*/index.html")}
    for f, x in guardadas.items():
        f.write_text(x.replace("<tr>", '<tr class="otra">'), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "C3 leyó 0 de" in out and "C4 leyó 0 de" in out
    for f, x in guardadas.items():
        f.write_text(x, encoding="utf-8")
    ok = ok and correr()[0] == 0
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


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
        import re as _re  # la primera fila es «1» o «≈» (grupo de cabeza, v6.0.0)
        roto = _re.sub(r"<tr><td>(1|≈)</td>", lambda x: f"<tr><td>99</td><td>{no_apto}</td></tr>{x[0]}", t, count=1)
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
    # 6-nov-2026: la página era grok-4-1-vs-4-5, que pasó al histórico y ya no tiene
    # escalera. Se busca cualquier página con un empate en la cima: si no hay, la prueba no
    # tiene qué romper y lo dice, en vez de dar verde sin sabotear nada.
    import re as _re
    pg = next((p for p in sorted((ROOT / "docs").glob("*/index.html"))
               if "Empatan arriba" in p.read_text(encoding="utf-8", errors="ignore")), None)
    if pg is None:
        raise AssertionError("ninguna página tiene una fila «Empatan arriba»: el sabotaje no tocaría nada")
    with Sabotaje(pg):
        html = pg.read_text(encoding="utf-8")
        roto = _re.sub(r"Empatan arriba \d+ de \d+", "Gana X", html, count=1)
        pg.write_text(roto, encoding="utf-8")
        return roto != html and _correr("check_ganadores.py") != 0


@prueba("check_ganadores", "un grupo de cabeza viejo, una página que corona dentro del grupo o un veredicto con un modelo no rankeado")
def _t_ganadores_grupo():
    # 6-nov-2026: dos landings coronaban a Claude Fable 5 (histórico) como «la mejor
    # calidad medida» de v5, y los textos nombraban a un #1 con el top 20 en 0,19 puntos.
    import re as _re
    if _correr("check_ganadores.py") != 0:
        raise AssertionError("check_ganadores ya está en rojo: el sabotaje no probaría nada")
    grupo = ROOT / "docs" / "mejor-llm-para-razonamiento" / "index.html"
    veredicto = ROOT / "docs" / "mejor-llm-para-agentes" / "index.html"
    h = grupo.read_text(encoding="utf-8")
    m = _re.search(r'data-grupo-cabeza="([^"]*)"', h)
    if not m or len(m.group(1).split(",")) < 2:
        raise AssertionError("razonamiento ya no tiene un grupo de más de uno: el sabotaje no tocaría nada")
    with Sabotaje(grupo):
        # G3: el grupo publicado no es el de models.json (se le quita uno)
        corto = ",".join(m.group(1).split(",")[:-1])
        grupo.write_text(h.replace(m.group(0), f'data-grupo-cabeza="{corto}"', 1), encoding="utf-8")
        if _correr("check_ganadores.py") == 0:
            return False
        # G3: con grupo, el texto corona a uno
        grupo.write_text(h.replace("<h2>Quiénes encabezan</h2>",
                                   "<h2>Por qué Inkling Small lidera</h2>", 1), encoding="utf-8")
        if "lidera" not in grupo.read_text(encoding="utf-8") or _correr("check_ganadores.py") == 0:
            return False
        # G3: la página no publica su grupo
        grupo.write_text(h.replace(m.group(0), "", 1), encoding="utf-8")
        if _correr("check_ganadores.py") == 0:
            return False
    hv = veredicto.read_text(encoding="utf-8")
    card = _re.search(r'(<span class="verdict-tag">[^<]*</span>\s*<strong>)([^<]*)(</strong>)', hv)
    if not card:
        raise AssertionError("agentes ya no tiene veredicto con tarjetas: el sabotaje no tocaría nada")
    with Sabotaje(veredicto):
        # G4: el veredicto nombra a un modelo del histórico (el caso real), en una tarjeta
        # que no recomienda —«Lo que te ahorras»— para que solo G4 lo pueda cazar.
        veredicto.write_text(hv.replace(
            card.group(0), '<span class="verdict-tag">Lo que te ahorras</span>\n        <strong>Claude Fable 5</strong>', 1),
            encoding="utf-8")
        if _correr("check_ganadores.py") == 0:
            return False
        # G1: recomienda a un rankeado que no está en el grupo
        d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
        g = _re.search(r'data-grupo-cabeza="([^"]*)"', hv).group(1).split(",")
        fuera = next(x["name"] for x in d["models"] if x.get("ranked") and x["key"] not in g)
        veredicto.write_text(hv.replace(card.group(0), card.group(1) + fuera + card.group(3), 1),
                             encoding="utf-8")
        return _correr("check_ganadores.py") != 0


@prueba("check_ganadores --dist", "un lector que no reconoce el HTML (G2, G3 y G5 leen cero páginas), "
                                  "y una corona o una carta con la forma de Astro que nombra a un modelo del histórico")
def _t_ganadores_dist():
    # 11-nov-2026 (motor-sitio 2.3). Frente al HTML de Astro, check_ganadores leyó cero filas y
    # reportó contradicciones falsas sin saber que no leía. Ahora cuenta páginas contra el
    # registro. Sin Node en el CI, el árbol es una copia de docs/ (el control) y las formas de
    # Astro se inyectan: `data-corona` en Modelo, `veredicto-tag` + enlace, el grupo sin valor.
    import re as _re
    base = Path(tempfile.mkdtemp()) / "dist"
    for f in (ROOT / "docs").glob("*/index.html"):
        d = base / f.parent.name / "index.html"
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, d)

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_ganadores.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0                                     # control
    # Cada lector, roto en todas sus páginas a la vez: tiene que decir que leyó cero.
    for regla, de, a in (("G3", "data-grupo-cabeza", "data-otro-grupo"),
                         ("G5", "gana <strong>", "gana <b>"),
                         ("G2", "Empatan", "Igualan")):
        guardadas = {}
        for f in base.glob("*/index.html"):
            t = f.read_text(encoding="utf-8")
            if de in t:
                guardadas[f] = t
                t2 = t.replace(de, a)
                if regla == "G5":   # las otras formas de coronar también se rompen
                    t2 = t2.replace("Empate técnico en calidad:", "Parejos:").replace("Resumen: quién gana", "Resumen")
                if regla == "G2":
                    t2 = _re.sub(r"(<td class=\"lad-verdict\">)Gana ", r"\1Sale ", t2)
                f.write_text(t2, encoding="utf-8")
        rc, out = correr()
        ok = ok and bool(guardadas) and rc != 0 and f"{regla} leyó 0 de" in out
        for f, t in guardadas.items():
            f.write_text(t, encoding="utf-8")
    ok = ok and correr()[0] == 0                              # restaurado

    # Las formas de Astro: el grupo vacío sin valor se lee (sigue verde) y quitarlo es rojo.
    rk = base / "mejor-llm-barato" / "index.html"
    t = rk.read_text(encoding="utf-8")
    if 'data-grupo-cabeza=""' not in t:
        raise AssertionError("mejor-llm-barato ya no tiene grupo vacío: el control de Astro no probaría nada")
    rk.write_text(t.replace('data-grupo-cabeza=""', "data-grupo-cabeza", 1), encoding="utf-8")
    ok = ok and correr()[0] == 0
    rk.write_text(t.replace('data-grupo-cabeza=""', "", 1), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "mejor-llm-barato: no publica su grupo" in out
    rk.write_text(t, encoding="utf-8")

    # Una corona de Astro (`data-corona`) y una carta de Astro que nombran al histórico.
    comp = next(base / e for e in ("claude-vs-chatgpt",) if (base / e / "index.html").exists()) / "index.html"
    tc = comp.read_text(encoding="utf-8")
    comp.write_text(tc.replace("</body>", '<p>En calidad gana <a class="a-ficha" data-modelo="claude-fable-5" '
                                          'data-corona href="#"><strong>Claude Fable 5</strong></a>.</p></body>', 1),
                    encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "corona a «Claude Fable 5»" in out
    comp.write_text(tc, encoding="utf-8")
    ag = base / "mejor-llm-para-agentes" / "index.html"
    ta = ag.read_text(encoding="utf-8")
    ag.write_text(ta.replace("</body>", '<div><span class="veredicto-tag">Lo que te ahorras</span>\n'
                                        '<a class="a-ficha" data-modelo="claude-fable-5" href="#"><strong>Claude Fable 5</strong></a></div></body>', 1),
                  encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "nombra a «Claude Fable 5», que no está rankeado" in out
    ag.write_text(ta, encoding="utf-8")
    ok = ok and correr()[0] == 0
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


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


@prueba("check_registro R5", "un modelo fuera del ranking sin motivo registrado")
def _t_registro_motivo():
    # 11-nov-2026 (Cristian): «el que no rankea sin motivo registrado es un error de datos».
    # Pasaba con Qwen 3-Next 80B Thinking (`effort_variant` no viajaba en el dato). Se borra
    # el motivo de UN modelo en una copia de models.json y R5 tiene que nombrarlo.
    real = ROOT / "docs" / "data" / "models.json"
    r = lambda f: subprocess.run([PY, str(ROOT / "benchmarks" / "check_registro.py"), "--models", str(f)],
                                 cwd=ROOT, capture_output=True, text=True)
    if r(real).returncode != 0:
        return False  # control
    d = json.loads(real.read_text(encoding="utf-8"))
    m = next(x for x in d["models"] if not x.get("ranked"))
    m["elegible"]["motivos"].pop("ranking", None)
    copia = Path(tempfile.mkdtemp()) / "models.json"
    copia.write_text(json.dumps(d), encoding="utf-8")
    out = r(copia)
    shutil.rmtree(copia.parent, ignore_errors=True)
    return out.returncode != 0 and f"R5 · {m['key']}" in out.stdout


@prueba("check_registro R6", "un redirect en el sitemap, un destino que falta en el sitemap y un redirect en llms.txt")
def _t_registro_indices():
    # 11-nov-2026 (motor-sitio 2.3). El sitemap listaba 19 redirects que la página misma marca
    # `noindex`: Google los rastreaba para descartarlos. Hoy el sitemap y llms.txt salen del
    # registro; R6 exige que digan exactamente sus destinos. Se rompe una copia de docs/.
    import registro_paginas as _rp
    regs = _rp.paginas()
    redirect = next(e["url"] for e in regs if e["redirect_a"])
    destino = next(e["url"] for e in regs if not e["redirect_a"] and e["url"] != "/")
    site = "https://benchmarks.cristiantala.com"
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "docs"
    shutil.copytree(ROOT / "docs", base)
    r = lambda: subprocess.run([PY, str(ROOT / "benchmarks" / "check_registro.py"), "--docs", str(base)],
                               cwd=ROOT, capture_output=True, text=True)
    ok = r().returncode == 0                                       # control
    sm, ll = base / "sitemap.xml", base / "llms.txt"
    tsm, tll = sm.read_text(encoding="utf-8"), ll.read_text(encoding="utf-8")
    loc = f"<loc>{site}{destino}</loc>"
    for f, roto, marca in (
            (sm, tsm.replace("</urlset>", f"<url><loc>{site}{redirect}</loc></url></urlset>"),
             f"R6 · sitemap.xml lista {redirect}, que el registro declara redirect"),
            (sm, tsm.replace(loc, ""), f"R6 · sitemap.xml no lista {destino}"),
            (ll, tll + f"\n- [Redirect]({site}{redirect})\n",
             f"R6 · llms.txt lista {redirect}, que el registro declara redirect")):
        original = f.read_text(encoding="utf-8")
        if roto == original:
            raise AssertionError(f"el sabotaje «{marca}» no cambió el archivo")
        f.write_text(roto, encoding="utf-8")
        out = r()
        ok = ok and out.returncode != 0 and marca in out.stdout
        f.write_text(original, encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("paridad_sitio", "una fila que sale sin declarar, una URL perdida, una congelada que cambia, "
                         "una afirmación que cambia sin motivo y una frase retirada que vuelve")
def _t_paridad_sitio():
    # 11-nov-2026 (motor-sitio 1.7). El corte reemplaza docs/ por lo que compila Astro: una
    # diferencia sin declarar se publicaría en silencio. Sin Node en el CI (llega en la 2.5),
    # el `dist` se arma desde los contratos de docs/ tal como Astro debe publicarlos —sin los
    # modelos de `fuera` y con los redirects del registro—, se exige verde y se rompe.
    import contrato_pagina, registro_paginas as rp
    if _correr("exportar_sitio.py") != 0:
        return False
    datos = ROOT / "sitio" / "src" / "datos" / "comparaciones"
    base = Path(tempfile.mkdtemp()) / "dist"
    regs = [e for e in rp.paginas() if e["motor"] == "astro"]

    def escribir(e, contrato):
        f = base / e["url"].strip("/") / "index.html"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"<html><body>{contrato}</body></html>", encoding="utf-8")
        return f

    def marcas(tipo, d):
        """Las marcas `data-afirmacion` con la forma que emiten Ranking.astro y Variantes.astro (2.3)."""
        if not d:
            return ""
        a = d.get("afirmaciones") or {}
        mod = lambda k, n: f'<a data-modelo="{k}" href="#"><strong>{html.escape(n)}</strong></a>'
        if tipo == "ranking":
            h = f'<section class="results" data-grupo-cabeza="{",".join(a.get("grupo_cabeza") or [])}"></section><section>'
            if a.get("mejor_compra"):
                h += f'<div data-afirmacion="mejor_compra">{mod("x", a["mejor_compra"])}</div>'
            h += "".join(f'<h3 data-afirmacion="top3">#1 {mod("x", n)}</h3>' for n in a.get("top3") or [])
            h += "".join(f'<li data-afirmacion="frontera">{mod("x", n)}</li>' for n in a.get("frontera") or [])
            return h + "</section>"
        v = d.get("veredicto")
        if not v:
            return ""
        texto = {"empatan_todos": "Empatan: el precio no compra nada", "empatan_arriba": "Empatan A y B",
                 "compra": "El precio compra algo", "al_reves": "Va al revés: gana el barato", "gana": "Gana A"}
        h = (f'<section><p class="lead" data-afirmacion="veredicto">{"Los tiers empatan en calidad" if v["empatan_todos"] else "Gana uno"}</p>'
             f'<div data-afirmacion="empiece">{mod(v["empiece"]["key"], v["empiece"]["name"])}</div>')
        if v["caro"]["key"] != v["empiece"]["key"]:
            h += f'<div data-afirmacion="caro">{mod(v["caro"]["key"], v["caro"]["name"])}</div>'
        h += "".join(f'<tr data-afirmacion="escalera"><td><strong>{html.escape(lab)}</strong></td>'
                     f'<td><span data-nombre>{texto[t]}</span></td></tr>' for lab, t in (a.get("escalera") or {}).items())
        return h + "</section>"

    paginas = {}
    for e in regs:
        if e["redirect_a"]:
            paginas[e["slug"]] = escribir(e, contrato_pagina.emitir("redirect", "x", []))
            continue
        c = contrato_pagina.leer((ROOT / "docs" / e["slug"] / "index.html").read_text(encoding="utf-8"))
        if e["tipo"] != "comparacion":   # rankings y variantes: el contrato no cambia (sesión 2)
            sub = "rankings" if e["tipo"] == "ranking" else "variantes"
            jf = ROOT / "sitio" / "src" / "datos" / sub / f"{e['slug']}.json"
            d = json.loads(jf.read_text(encoding="utf-8")) if jf.exists() else None
            paginas[e["slug"]] = escribir(e, contrato_pagina.emitir(c["tipo"], "x", c["recomienda"],
                                                                    c.get("ordena_por"), c.get("tablas"))
                                          + ("" if e["congelada"] else marcas(e["tipo"], d)))
            continue
        fuera = {m["name"] for m in json.loads((datos / f"{e['slug']}.json").read_text(encoding="utf-8"))["fuera"]}
        rec = [n for n in c["recomienda"] if n not in fuera]
        tablas = [dict(t, filas=len(rec)) for t in c.get("tablas") or []] if fuera & set(c["recomienda"]) else c.get("tablas")
        paginas[e["slug"]] = escribir(e, contrato_pagina.emitir(c["tipo"], "x", rec, c.get("ordena_por"), tablas))

    # Los datos van en una copia: el sabotaje de una afirmación edita un JSON exportado.
    copia_datos = base.parent / "datos"
    shutil.copytree(ROOT / "sitio" / "src" / "datos", copia_datos)

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "paridad_sitio.py"), "--dist", str(base),
                            "--datos", str(copia_datos)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0  # control
    viva = next(e for e in regs if not e["redirect_a"] and not e["congelada"])
    cong = next(e for e in regs if e["congelada"])
    for e, cambio, marca in (
            (viva, lambda c: c.update(recomienda=c["recomienda"][1:]), "sin estar declarado"),
            (cong, lambda c: c.update(ordena_por="Precio"), "ordena_por cambió"),
            (viva, None, "se perdió")):
        f = paginas[e["slug"]]
        antes = f.read_text(encoding="utf-8")
        if cambio is None:
            f.unlink()
        else:
            c = contrato_pagina.leer(antes)
            cambio(c)
            f.write_text(f"<html><body>{contrato_pagina.emitir(c['tipo'], 'x', c['recomienda'], c.get('ordena_por'), c.get('tablas'))}</body></html>",
                         encoding="utf-8")
        rc, out = correr()
        ok = ok and rc != 0 and f"{e['url']}" in out and marca in out
        f.write_text(antes, encoding="utf-8")

    # Sesión 2: una afirmación de un ranking que cambia sin motivo declarado (la mejor compra sale
    # de la misma función en los dos motores: si difiere, es un error) y una frase retirada que
    # vuelve a aparecer en lo compilado.
    rk = next(e for e in regs if e["tipo"] == "ranking" and not e["redirect_a"])
    jr = copia_datos / "rankings" / f"{rk['slug']}.json"
    orig = jr.read_text(encoding="utf-8")
    d = json.loads(orig)
    d["afirmaciones"]["mejor_compra"] = "Un modelo que nadie recomendó"
    jr.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and rk["url"] in out and "«mejor_compra» cambia sin motivo declarado" in out
    jr.write_text(orig, encoding="utf-8")

    # Sesión 4 (2.3): las afirmaciones se leen del HTML de dist. Una página que publica otra
    # mejor compra que su JSON falla, y un dist que no trae las marcas no se da por leído.
    f = paginas[rk["slug"]]
    antes = f.read_text(encoding="utf-8")
    mc = json.loads(orig)["afirmaciones"]["mejor_compra"] or json.loads(orig)["afirmaciones"]["top3"][0]
    clave = "mejor_compra" if json.loads(orig)["afirmaciones"]["mejor_compra"] else "top3"
    f.write_text(antes.replace(f"<strong>{html.escape(mc)}</strong>", "<strong>Otro modelo</strong>", 1), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and f"dist publica «{clave}»" in out and rk["url"] in out
    f.write_text(antes, encoding="utf-8")
    sin_marcas = {}
    for e in regs:
        if e["tipo"] in ("ranking", "variantes") and not e["redirect_a"] and not e["congelada"]:
            g = paginas[e["slug"]]
            sin_marcas[g] = g.read_text(encoding="utf-8")
            g.write_text(sin_marcas[g].replace("data-afirmacion=", "data-otra="), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "paridad de afirmaciones en dist leyó 0 de" in out
    for g, t in sin_marcas.items():
        g.write_text(t, encoding="utf-8")

    # Una sección vacía en el dato Y en la página: la paridad entre los dos no ve nada, y la
    # plantilla oculta la sección. Pasó con la frontera de /mejor-llm-open-source/ (2.3).
    d = json.loads(orig)
    d["afirmaciones"]["frontera"] = []
    jr.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    f.write_text(re.sub(r'<li data-afirmacion="frontera">.*?</li>', "", antes), encoding="utf-8")
    if f.read_text(encoding="utf-8") == antes:
        raise AssertionError("el sabotaje de la frontera vacía no cambió la página")
    rc, out = correr()
    ok = ok and rc != 0 and "la sección «frontera» sale vacía" in out and rk["url"] in out
    jr.write_text(orig, encoding="utf-8")
    f.write_text(antes, encoding="utf-8")

    # 11-nov (2.4): «Entrar es gratis» salió también de docs/ y la prohíbe check_cta C4; la
    # prueba usa otra frase que sigue retirada.
    f.write_text(antes.replace("<body>", "<body><p>Filtra con score global ≥ 6,8.</p>"), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "«con score global ≥ 6,8»: sigue en dist" in out and rk["url"] in out
    f.write_text(antes, encoding="utf-8")
    ok = ok and correr()[0] == 0   # y vuelve a verde: los sabotajes se deshicieron
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


@prueba("check_espanol_neutro", "voseo en una ficha (dos niveles abajo), un árbol que no se lee y uno al que le faltan páginas")
def _t_espanol_neutro():
    # 11-nov-2026 (motor-sitio 2.3). Buscaba en `docs/*/index.html`, un nivel: las 132 fichas de
    # `docs/modelo/` nunca se revisaron, y el «mirá» de /glm-5.2-explicado/ estuvo publicado sin
    # que el QA lo corriera. Ahora lee todo el árbol y falla si lee menos páginas que el registro.
    base = Path(tempfile.mkdtemp()) / "docs"
    for f in (ROOT / "docs").rglob("index.html"):
        d = base / f.relative_to(ROOT / "docs")
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, d)

    def correr(raiz):
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_espanol_neutro.py"), "--dist", str(raiz)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr(base)[0] == 0                                  # control: las páginas de hoy
    ficha = next((base / "modelo").rglob("index.html"))
    antes = ficha.read_text(encoding="utf-8")
    ficha.write_text(antes.replace("</body>", "<p>Si querés probarlo, pedile una cotización.</p></body>"),
                     encoding="utf-8")
    rc, out = correr(base)
    ok = ok and rc != 0 and "querés" in out and "modelo/" in out
    ficha.write_text(antes, encoding="utf-8")
    vacio = base.parent / "vacio"
    vacio.mkdir()
    rc, out = correr(vacio)                                    # lee cero páginas → rojo
    ok = ok and rc != 0 and "leyó 0 de" in out
    shutil.rmtree(base / "modelo")                             # le faltan las fichas → rojo
    rc, out = correr(base)
    ok = ok and rc != 0 and "no revisó" in out and "/modelo/" in out
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


@prueba("check_paleta P5", "un color inventado en lo compilado, también escrito corto por el minificador")
def _t_paleta_dist():
    # 11-nov-2026 (motor-sitio 2.2). `dist` lleva lo de Astro y el legado copiado de docs/: lo que
    # se publica es lo compilado, no la fuente. El minificador escribe `#fff`; un color inventado
    # escrito corto (`#fa0`) tiene que caer igual que uno largo. Un color citado en un comentario
    # (cómo murió un color) no cuenta.
    # 2.3: P5 exige leer todas las páginas del registro, así que el árbol es una copia de docs/
    # (verde por sí sola) con los archivos de la prueba agregados.
    base = Path(tempfile.mkdtemp()) / "dist"
    shutil.copytree(ROOT / "docs", base)
    (base / "a").mkdir()
    (base / "a" / "index.html").write_text(
        '<style>.x{color:#fff;background:#7A00DF}</style><!-- antes era #ffd700 --><a href="#top">.</a>',
        encoding="utf-8")
    (base / "s.css").write_text(":root{--c:#006080}/* #b478ff murió el 19-ago */", encoding="utf-8")

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_paleta.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0   # control: colores del manual y de brand.json, y uno citado en comentario
    for archivo, color, esperado in (("a/index.html", "#ffd700", "#ffd700"), ("s.css", "#fa0", "#ffaa00")):
        f = base / archivo
        antes = f.read_text(encoding="utf-8")
        f.write_text(antes + f"<i style='color:{color}'></i>" if f.suffix == ".html"
                     else antes + f".y{{color:{color}}}", encoding="utf-8")
        rc, out = correr()
        ok = ok and rc != 0 and "P5" in out and esperado in out
        f.write_text(antes, encoding="utf-8")
    ok = ok and correr()[0] == 0
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


@prueba("check_paleta P3/P4", "un color literal en el motor nuevo y un token editado a mano, también en el :root del legado")
def _t_paleta_sitio():
    # 11-nov-2026 (motor-sitio 1.2). En `sitio/` ningún color se escribe: sale de tokens.css,
    # y tokens.css sale de brand.json. P3 caza el literal aunque sea un color DEL manual
    # (el verde neón escrito a mano se desvía igual cuando el manual cambia); P4 caza el
    # token retocado en el archivo generado en vez de en brand.json.
    tokens = ROOT / "sitio" / "src" / "styles" / "tokens.css"
    if not tokens.exists():   # es generado y está en .gitignore: en el CI no viene
        _correr("tokens_sitio.py")
    if not tokens.exists() or _correr("check_paleta.py") != 0:
        return False  # control: el estado actual tiene que pasar
    nuevo = ROOT / "sitio" / "src" / "styles" / "_sabotaje.css"
    with Sabotaje(nuevo):
        nuevo.write_text(".cta { color: #39ff14; }\n", encoding="utf-8")
        p3 = _correr("check_paleta.py") != 0
    with Sabotaje(tokens):
        t = tokens.read_text(encoding="utf-8")
        linea = next(l for l in t.splitlines() if l.strip().startswith("--color-primary:"))
        tokens.write_text(t.replace(linea, "  --color-primary: #7a00e0;"), encoding="utf-8")
        p4 = _correr("check_paleta.py") != 0
    # 2.2: el :root del legado (docs/style.css) también sale de brand.json; retocarlo a mano cae.
    css = ROOT / "docs" / "style.css"
    with Sabotaje(css):
        t = css.read_text(encoding="utf-8")
        linea = next(l for l in t.splitlines() if l.strip().startswith("--green:"))
        # un color DE la marca en el rol equivocado: P1 no lo ve, solo P4 (sale de brand.json o no)
        css.write_text(t.replace(linea, "  --green: #006080;   /* primary */"), encoding="utf-8")
        p4_legado = _correr("check_paleta.py") != 0
    return p3 and p4 and p4_legado and not nuevo.exists() and _correr("check_paleta.py") == 0


@prueba("check_movil", "una página que desborda a 390 px, una sin viewport de móvil y un dist sin nada que medir")
def _t_movil():
    # 11-nov-2026 (motor-sitio). La revisión a 390 px era a mano y mintió: Chrome sin interfaz
    # dibuja a ~500 px. Se emula un teléfono de verdad sobre un `dist` sintético: control verde
    # (una tabla ancha DENTRO de su caja con desplazamiento, y un redirect ancho que no se
    # mide), y después un rojo por regla, cada uno con su etiqueta.
    base = Path(tempfile.mkdtemp()) / "dist"
    vp = '<meta name="viewport" content="width=device-width, initial-scale=1">'

    def escribir(url, cuerpo, head=vp):
        f = base / url.strip("/") / "index.html" if url != "/" else base / "index.html"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"<!doctype html><html><head>{head}<title>x</title></head>"
                     f"<body style=\"margin:0\">{cuerpo}</body></html>", encoding="utf-8")

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_movil.py"), "--dist", str(base),
                            "--sin-compilar"], cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    try:
        escribir("/", '<p>inicio</p><div style="overflow-x:auto"><table><tr>'
                 + "".join(f"<td>columna-larga-{i}</td>" for i in range(30)) + "</tr></table></div>")
        escribir("/se-movio/", '<div style="width:2000px">ancho</div>',
                 head=vp + '<meta http-equiv="refresh" content="0; url=/">')
        codigo, salida = correr()
        if codigo != 0 or "2 páginas" in salida:
            raise AssertionError(f"control en rojo o midió el redirect: {salida[-400:]}")
        escribir("/ancha/", '<div style="width:600px">empuja la página</div>')
        codigo, salida = correr()
        if codigo == 0 or "M2" not in salida or "/ancha/" not in salida:
            return False
        escribir("/ancha/", "<p>ya no empuja</p>", head="")  # sin viewport de móvil: 980 px
        codigo, salida = correr()
        if codigo == 0 or "M1" not in salida:
            return False
        shutil.rmtree(base)
        escribir("/se-movio/", "<p>solo un redirect</p>", head=vp + '<meta http-equiv="refresh" content="0; url=/">')
        codigo, salida = correr()
        return codigo != 0 and "no se pudo medir" in salida
    finally:
        shutil.rmtree(base.parent, ignore_errors=True)


@prueba("check_registro R1-R4", "un modelo fuera del ranking, una cifra a mano, una URL perdida y una página sin registro")
def _t_registro():
    # 11-nov-2026 (motor-sitio 1.4). Al 11-nov, 24 de 27 comparaciones de versión exacta
    # mostraban modelos que ya no rankeaban y nada lo veía. Se arma un `dist` sintético con
    # las páginas Astro del registro tal como deben salir de las plantillas, se exige verde
    # y después se rompe UNA regla por vez: cada rojo tiene que venir de SU regla.
    import registro_paginas as rp
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    dentro = next(m["key"] for m in d["models"] if m.get("ranked"))
    fuera = next(m["key"] for m in d["models"] if not m.get("ranked"))
    regs = [e for e in rp.paginas() if e["motor"] == "astro"]
    sitio = "https://benchmarks.cristiantala.com"
    base = Path(tempfile.mkdtemp()) / "dist"

    def pagina(e, modelo=dentro, extra=""):
        if e["redirect_a"]:
            u = f"{sitio}/{e['redirect_a']}/"
            return (f'<html><head><link rel="canonical" href="{u}"><meta name="robots" '
                    f'content="noindex, follow"><meta http-equiv="refresh" content="0; url={u}">'
                    f'</head><body><p>Se movió a <a href="{u}">la comparación</a>.</p></body></html>')
        aviso = '<div data-congelada>Foto del 11-nov-2026</div>' if e["congelada"] else ""
        return (f'<html><head><title>X vs Y en 2026</title></head><body>{aviso}<table><tr>'
                f'<td data-modelo="{modelo}">Modelo 4.5</td><td data-cifra>7,21</td></tr></table>'
                f'<p>Medido el 11-nov-2026 con <span data-nombre>Phi-4</span>.</p>'
                f'<a data-anterior="{fuera}" href="#">Versión 4.1</a>{extra}</body></html>')

    def escribir(e, html):
        f = base / e["url"].strip("/") / "index.html"
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_registro.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    for e in regs:
        escribir(e, pagina(e))
    # 2.2: `dist` lleva también el legado (fichas, landings, home), copiado de docs/ como en el build.
    copia = [PY, str(ROOT / "benchmarks" / "copiar_legado.py"), "--dist", str(base)]
    if subprocess.run(copia, cwd=ROOT, capture_output=True, text=True).returncode != 0:
        return False
    if correr()[0] != 0:
        return False  # control: el dist bien hecho tiene que pasar
    # Copiar dos veces es un choque: dos motores escriben la misma ruta y tiene que fallar.
    r = subprocess.run(copia, cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0 or "chocan" not in r.stdout:
        return False
    ficha = next(e for e in rp.paginas() if e["tipo"] == "ficha")
    viva = next(e for e in regs if not e["redirect_a"] and not e["congelada"])
    cong = next(e for e in regs if e["congelada"])
    redi = next(e for e in regs if e["redirect_a"])
    casos = [
        ("R1", viva, pagina(viva, modelo=fuera)),
        ("R1", cong, pagina(cong).replace("<div data-congelada>", "<div>")),
        ("R1", viva, pagina(viva, extra=f'<a data-anterior="{dentro}" href="#">Anterior</a>')),
        ("R2", viva, pagina(viva, extra="<p>Gana por 0,45 puntos.</p>")),
        ("R3", redi, pagina(redi).replace(redi["redirect_a"], "otra-parte")),
        ("R3", viva, None),
        ("R3", ficha, None),   # una página del legado que no llega a dist: el corte la borraría
        ("R4", {"url": "/inventada-vs-otra/", "redirect_a": None, "congelada": None}, pagina(viva)),
    ]
    ok = True
    for regla, e, html in casos:
        f = base / e["url"].strip("/") / "index.html"
        antes = f.read_text(encoding="utf-8") if f.exists() else None
        if html is None:
            f.unlink()
        else:
            escribir(e, html)
        rc, out = correr()
        ok = ok and rc != 0 and f"{regla} · {e['url']}" in out
        if antes is None:
            f.unlink(missing_ok=True)
        else:
            f.write_text(antes, encoding="utf-8")
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


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


@prueba("check_suites S6", "el titular promedia con otro criterio que `del_indice()`")
def _t_suites_declarado_vs_real():
    """S6 es un AVISO, no un fallo: el exit code no cambia, así que se lee el texto.

    9-nov-2026 · reescrito junto con S6. El aviso viejo nacía siempre en rojo (leía
    funciones del export que ya no deciden), así que el control era por suite. Ahora S6
    nace verde, y el control es global: sin aviso S6 antes de romper; con aviso después de
    cambiar el filtro de `general` por un prefijo, que es exactamente la segunda definición
    del índice que vivió en el export hasta el 17-sep.
    """
    exp = ROOT / "benchmarks" / "export_for_pages.py"

    def s6_avisa() -> bool:
        salida = subprocess.run([PY, str(ROOT / "benchmarks" / "check_suites.py")],
                                capture_output=True, text=True, cwd=ROOT).stdout
        return any("S6 ·" in ln and "⚠️" in ln for ln in salida.splitlines())

    if s6_avisa():
        return False  # control sucio: ya avisa antes de romper nada, no prueba nada
    with Sabotaje(exp):
        original = exp.read_text(encoding="utf-8")
        roto = original.replace(
            'if str(r.get("suite", "")) in _INDICE and not _is_low_coverage(r)]',
            'if not _is_niah(r) and not _is_low_coverage(r)]', 1)
        if roto == original:
            raise AssertionError("el sabotaje no cambió nada: `general` ya no se arma así")
        exp.write_text(roto, encoding="utf-8")
        return s6_avisa()


@prueba("check_suites S7", "una suite del índice sin peldaño (se mediría al default en silencio)")
def _t_suites_peldano():
    reg = ROOT / "benchmarks" / "suites.py"
    if _correr("check_suites.py") != 0:
        return False  # control sucio: ya falla antes de romper nada
    with Sabotaje(reg):
        original = reg.read_text(encoding="utf-8")
        roto = original.replace('"hallucination": 1, ', "", 1)
        if roto == original:
            raise AssertionError("el sabotaje no cambió nada: `hallucination` ya no está así en PELDANO")
        reg.write_text(roto, encoding="utf-8")
        return _correr("check_suites.py") != 0


@prueba("check_mezcla", "un modelo abierto con su examen repartido entre dos proveedores")
def _t_mezcla():
    """Bloqueante desde 5.2.a: la función que decide y el exit code que sale de ella."""
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from collections import Counter as _C
    from benchmarks.check_mezcla import veredicto, codigo_salida
    # Un mezclado sale con 1; un cerrado sin proveedor registrado, no (M2).
    if codigo_salida(_C(limpio=69, mezclado=1)) != 1 or codigo_salida(_C(limpio=69, no_registrado=1)) != 0:
        return False
    # Y el script de verdad lee runs: un informativo ciego también da 0.
    salida = subprocess.run([PY, str(ROOT / "benchmarks" / "check_mezcla.py")],
                            capture_output=True, text=True, cwd=ROOT).stdout
    if " 0 runs del índice leídos" in salida or "mezclados:" not in salida:
        return False
    limpio = [{"upstream_provider": "Z.AI", "cuantizacion": "fp8"}] * 3
    if veredicto(limpio, abierto=True)[0] != "limpio":
        return False  # control sucio
    mezcla = limpio + [{"upstream_provider": "DeepInfra", "cuantizacion": "fp4"}]
    sin_reg = limpio + [{"upstream_provider": None}]
    # El mismo proveedor escrito distinto (API directa «openai», OpenRouter «OpenAI») NO
    # es una mezcla; dos proveedores de verdad distintos sí (6-nov-2026).
    mismo = [{"upstream_provider": "openai"}] * 3 + [{"upstream_provider": "OpenAI "}] * 2
    if veredicto(mismo, abierto=False)[0] != "limpio":
        return False
    otro = [{"upstream_provider": "Google"}] * 3 + [{"upstream_provider": "Google AI Studio"}]
    return (veredicto(otro, abierto=False)[0] == "mezclado"
            and veredicto(mezcla, abierto=True)[0] == "mezclado"
            and veredicto(sin_reg, abierto=True)[0] == "mezclado"
            and veredicto(sin_reg, abierto=False)[0] == "no_registrado"
            and veredicto(limpio, abierto=True, harbor=["Z.AI", "Novita"])[0] == "mezclado")


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


@prueba("qa Q16", "un modelo sin `sin_dato_comunitario`, o una ficha que dice «sin dato» teniendo banda")
def _t_dato_comunitario():
    # corte-v5 2.4. Control verde y dos mundos rotos: el export que pierde el campo en un
    # modelo, y una ficha que dice «sin dato comunitario» a todos aunque tengan banda.
    qa = lambda: subprocess.run(["node", str(ROOT / "benchmarks" / "qa_calculadora.mjs")],  # noqa: E731
                                capture_output=True, text=True, cwd=ROOT)
    def q16_falla(r):
        return r.returncode != 0 and any("❌ Q16" in ln for ln in r.stdout.splitlines())
    r = qa()
    if r.returncode != 0 or "✅ Q16" not in r.stdout:
        return False  # control verde
    mj = ROOT / "docs" / "data" / "models.json"
    with Sabotaje(mj):
        d = json.loads(mj.read_text(encoding="utf-8"))
        d["models"][0].pop("sin_dato_comunitario", None)
        mj.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        if not q16_falla(qa()):
            return False
    app = ROOT / "docs" / "app.js"
    with Sabotaje(app):
        original = app.read_text(encoding="utf-8")
        roto = original.replace("if (m.sin_dato_comunitario || !m.externos) {", "if (true) {", 1)
        if roto == original:
            raise AssertionError("el sabotaje no cambió nada: datoComunitario ya no se escribe así")
        app.write_text(roto, encoding="utf-8")
        return q16_falla(qa())


@prueba("sync_cachebust", "un ?v= de app.js que no corresponde a su contenido")
def _t_cachebust():
    # corte-v5 2.5. Control verde con el index.html real; después un `?v=` viejo, que es
    # exactamente lo que pasó tras 2.4 sin que nada fallara.
    if _correr("sync_cachebust.py", "--check") != 0:
        return False  # control verde
    idx = ROOT / "docs" / "index.html"
    with Sabotaje(idx):
        original = idx.read_text(encoding="utf-8")
        roto, n = re.subn(r"app\.js\?v=[A-Za-z0-9._-]+", "app.js?v=00000000", original, count=1)
        if n == 0 or roto == original:
            raise AssertionError("el sabotaje no cambió nada: index.html ya no carga app.js?v=")
        idx.write_text(roto, encoding="utf-8")
        return _correr("sync_cachebust.py", "--check") != 0


@prueba("solo_fechas", "un cambio real de datos escondido entre las fechas de corrida")
def _t_solo_fechas():
    # corte-v5 2.7. En un repo desechable con el models.json real: el control es el commit
    # diario del Action (solo cambia `generated_at`) y tiene que dar 0 y restaurarse. Los dos
    # sabotajes son lo que NO puede descartarse: un dato real junto a la fecha de corrida, y
    # una fecha que es dato (`retired_at`), que no lleva marcador de fecha de corrida.
    #
    # El entorno va sin variables GIT_*: dentro del pre-push heredan el GIT_DIR del repo real
    # y un `git init` acá lo reconfiguraría (pasó, ver la memoria del 2026).
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    tmp = Path(tempfile.mkdtemp())
    try:
        def git(*a):
            subprocess.run(["git", *a], cwd=tmp, env=env, check=True, capture_output=True)

        def correr(*a):
            r = subprocess.run([PY, str(ROOT / "benchmarks" / "solo_fechas.py"), *a],
                               cwd=tmp, env=env, capture_output=True, text=True)
            if r.returncode not in (0, 1):
                raise AssertionError(f"solo_fechas salió con {r.returncode}: {r.stderr[-200:]}")
            return r.returncode

        git("init", "-q")
        git("config", "user.email", "prueba@local")
        git("config", "user.name", "prueba")
        original = (ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8")
        mj = tmp / "models.json"
        mj.write_text(original, encoding="utf-8")
        git("add", "models.json")
        git("commit", "-q", "-m", "base")

        def con(*cambios):
            texto = original
            for patron, reemplazo in cambios:
                texto, n = re.subn(patron, reemplazo, texto, count=1)
                if n == 0:
                    raise AssertionError(f"el sabotaje no encontró {patron!r} en models.json")
            mj.write_text(texto, encoding="utf-8")

        fecha = (r'"generated_at": "[^"]+"', '"generated_at": "2099-01-01T00:00:00"')
        con(fecha)
        git("add", "models.json")
        if correr("--cached", "--restaurar") != 0:
            return False  # control verde: solo la fecha de corrida
        if mj.read_text(encoding="utf-8") != original:
            raise AssertionError("--restaurar no devolvió models.json al commit")
        con(fecha, (r'"retired_at": "\d{4}-\d{2}-\d{2}"', '"retired_at": "1999-01-01"'))
        dato_fecha = correr()
        con(fecha, (r'"score_global": [0-9.]+', '"score_global": 1.23'))
        dato_real = correr()
        return dato_fecha == 1 and dato_real == 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@prueba("validate B4", "un rankeado con runs de antes de v5, o un histórico rankeado o sin era")
def _t_b4_ranking_v5():
    # 5-nov-2026. Control verde con el models.json real; después tres mundos rotos: un
    # rankeado que pierde `examen_v5`, un histórico que además rankea, y uno sin era.
    if _correr("validate.py") != 0:
        return False  # control verde
    mj = ROOT / "docs" / "data" / "models.json"
    resultados = []
    for romper in ("sin_v5", "en_los_dos", "sin_era"):
        with Sabotaje(mj):
            d = json.loads(mj.read_text(encoding="utf-8"))
            rk = next(m for m in d["models"] if m.get("ranked"))
            hi = next((m for m in d["models"] if m.get("historico")), None)
            if romper == "sin_v5":
                rk["examen_v5"] = False
            else:
                if hi is None:
                    raise AssertionError("el sabotaje necesita un modelo en el histórico")
                if romper == "en_los_dos":
                    hi["ranked"] = True
                else:
                    hi["era"] = None
            mj.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
            resultados.append(_correr("validate.py") != 0)
    return all(resultados)


@prueba("validate C4", "la ficha de un histórico que no lo dice, o una nota pública que no se imprime")
def _t_c4_fichas_v5():
    if _correr("validate.py") != 0:
        return False  # control verde
    from benchmarks.generate_model_cards import slug
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    hi = next(m for m in d["models"] if m.get("historico")
              and (ROOT / "docs" / "modelo" / slug(m) / "index.html").exists())
    nt = next(m for m in d["models"] if m.get("nota_publica"))
    resultados = []
    for m, quitar in ((hi, r'<p class="meta fechada historico"[^>]*>.*?</p>'),
                      (nt, r'<p class="meta nota-publica">.*?</p>')):
        f = ROOT / "docs" / "modelo" / slug(m) / "index.html"
        with Sabotaje(f):
            html = f.read_text(encoding="utf-8")
            roto = re.sub(quitar, "", html, count=1, flags=re.S)
            if roto == html:
                raise AssertionError(f"el sabotaje no encontró qué quitar en {f}")
            f.write_text(roto, encoding="utf-8")
            resultados.append(_correr("validate.py") != 0)
    return all(resultados)


@prueba("validate C1", "una página que nombra a un retirado sin declararlo en su línea fechada")
def _t_c1_foto_fechada():
    # 4-nov-2026. C1 deja pasar a un retirado solo si la página es una foto fechada que lo
    # declara (`data-retirados`). Control verde con el sitio real; después: la ficha de un
    # retirado sin su línea, una página de alternativas que lo nombra, y una línea fechada
    # que declara a otro modelo (no excusa al que no nombra).
    if _correr("validate.py") != 0:
        return False  # control verde
    ficha = ROOT / "docs" / "modelo" / "qwen-3.6-max" / "index.html"
    alt = ROOT / "docs" / "alternativas-claude" / "index.html"
    resultados = []
    with Sabotaje(ficha):
        html = ficha.read_text(encoding="utf-8")
        roto = re.sub(r'<p class="meta fechada"[^>]*>.*?</p>', "", html, count=1)
        if roto == html:
            raise AssertionError("el sabotaje no encontró la línea fechada en la ficha")
        ficha.write_text(roto, encoding="utf-8")
        resultados.append(_correr("validate.py") != 0)
    with Sabotaje(alt):
        alt.write_text(alt.read_text(encoding="utf-8").replace(
            "</main>", "<p>Qwen 3.6 Max</p></main>", 1), encoding="utf-8")
        resultados.append(_correr("validate.py") != 0)
    with Sabotaje(ficha):
        html = ficha.read_text(encoding="utf-8")
        ficha.write_text(html.replace('data-retirados="Qwen 3.6 Max"', 'data-retirados="Hermes 4 70B"', 1),
                         encoding="utf-8")
        resultados.append(_correr("validate.py") != 0)
    return all(resultados)


@prueba("generate_comparison", "una comparación con un lado sin modelos que se salta en silencio")
def _t_comparacion_sin_modelos():
    # 4-nov-2026. Saltarse la página dejaba publicada la versión vieja: /fable-5-vs-deepseek-r1/
    # siguió recomendando a R1 retirado. Control: una comparación real genera; sabotaje: un
    # lado que no matchea nada tiene que ser error, no aviso.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import generate_comparison as gc
    real = gc.COMPARISONS[0]
    pagina = ROOT / "docs" / real["slug"] / "index.html"
    antes = list(gc.COMPARISONS)
    argv = sys.argv
    try:
        with Sabotaje(pagina):
            gc.COMPARISONS[:] = [real]
            sys.argv = ["generate_comparison.py", "--slug", real["slug"]]
            gc.main()  # control verde: no levanta
        roto = {**real, "slug": "prueba-lado-vacio",
                "b": {"name": "Nadie", "familia": "no-existe-ninguna-familia-asi"}}
        gc.COMPARISONS[:] = [roto]
        sys.argv = ["generate_comparison.py", "--slug", "prueba-lado-vacio"]
        try:
            gc.main()
        except SystemExit:
            return not (ROOT / "docs" / "prueba-lado-vacio").exists()
        return False
    finally:
        gc.COMPARISONS[:] = antes
        sys.argv = argv
        shutil.rmtree(ROOT / "docs" / "prueba-lado-vacio", ignore_errors=True)


@prueba("generate_manual_landings", "una landing que recomienda un muerto por su nombre a secas")
def _t_landings_sin_muertos():
    # 4-nov-2026. El guardia buscaba el nombre CON sufijo («DeepSeek R1 (reasoning)») y el
    # HTML lo escribe a secas: R1 y las Laguna pasaban sin verse. Y las reviews son fotos
    # fechadas (DECISIONES, 4-nov-2026): citan a un retirado solo si la línea visible lo
    # declara y se retiró DESPUÉS de la medición.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import generate_manual_landings as g
    data = g.load_data()
    paginas = {}
    for slug, fn in g.LANDINGS:
        html = fn(data)
        if slug in g.FECHADAS:
            html = g._con_linea_fechada(html, slug, data["models"])
        paginas[slug] = html

    def rojo(html, slug):
        try:
            g._no_recomendar_muertos(html, slug)
        except SystemExit:
            return True
        return False

    if any(rojo(h, s) for s, h in paginas.items()):
        return False  # control verde: las páginas reales pasan
    alt = paginas["alternativas-claude"]
    if rojo(alt.replace("</main>", "<p>Llama 3.3 70B</p></main>", 1), "alternativas-claude"):
        return False  # retirado en Groq y vivo en OpenRouter: no es un muerto
    review = paginas["fable-5-review"]
    sin_linea = re.sub(r'<p class="meta fechada"[^>]*>.*?</p>', "", review, count=1)
    if sin_linea == review:
        raise AssertionError("el sabotaje no encontró la línea fechada en fable-5-review")
    return all([
        # el bug: el nombre a secas, sin el sufijo de models.json
        rojo(alt.replace("</main>", "<p><strong>Hermes 4 70B</strong></p></main>", 1),
             "alternativas-claude"),
        # una review sin su línea de fecha
        rojo(sin_linea, "fable-5-review"),
        # un retirado ANTES de la medición (Devstral Small, 13-jul) no entra en la foto
        rojo(review.replace("</main>", "<p>Devstral Small</p></main>", 1), "fable-5-review"),
        # el retirado que la review sí declara, en una página de alternativas, es rojo
        rojo(alt.replace("</main>", "<p>DeepSeek R1</p></main>", 1), "alternativas-claude"),
    ])


def _dist_lee_cero(script: str, marca: str, args: tuple = ()) -> bool:
    """Regla de páginas leídas (motor-sitio 2.3) para un guardrail con `--dist`: sobre una copia
    de docs/ da verde (el control: `--dist` lee de verdad), y sobre un árbol vacío da rojo
    diciendo que leyó cero. Sin el conteo, un árbol que no se lee no tiene nada que objetar."""
    tmp = Path(tempfile.mkdtemp())
    copia, vacio = tmp / "copia", tmp / "vacio"
    shutil.copytree(ROOT / "docs", copia)
    vacio.mkdir()

    def correr(base):
        r = subprocess.run([PY, str(ROOT / "benchmarks" / script), *args, "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    rc0, out0 = correr(copia)
    rc1, out1 = correr(vacio)
    shutil.rmtree(tmp, ignore_errors=True)
    if rc0 != 0:
        raise AssertionError(f"{script} --dist sobre una copia de docs/ ya está en rojo: {out0[-300:]}")
    return rc1 != 0 and marca in out1


@prueba("auditar_paginas --dist", "un árbol que no se lee (cero páginas)")
def _t_auditar_dist():
    return _dist_lee_cero("auditar_paginas.py", "auditar_paginas leyó 0 de", ("--duro",))


@prueba("check_fichas_alcanzables --dist", "las fichas intactas y los listados que F2 no lee (cero páginas)")
def _t_fichas_dist():
    # En un árbol vacío F1 ya falla (no hay fichas): ese rojo no probaría F2. Acá las fichas
    # están y cada listado se salta (lleva `http-equiv="refresh"`): solo el conteo de F2 lo caza.
    import fnmatch
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "dist"
    shutil.copytree(ROOT / "docs", base)

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_fichas_alcanzables.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0                                   # control
    for f in base.glob("*/index.html"):
        if any(fnmatch.fnmatch(f.parent.name, x) for x in ("mejor-llm-*", "*-vs-*", "alternativas-*")):
            f.write_text(f.read_text(encoding="utf-8").replace("<head>", '<head><meta http-equiv="refresh" content="0">', 1),
                         encoding="utf-8")
    rc, out = correr()
    shutil.rmtree(tmp, ignore_errors=True)
    return ok and rc != 0 and "F2 leyó 0 de" in out


@prueba("check_indice_calidad --dist", "un árbol que no se lee (ni la home, ni las páginas, ni las fichas)")
def _t_indice_dist():
    return _dist_lee_cero("check_indice_calidad.py", "check_indice_calidad leyó 0 de")


@prueba("check_calculator --dist", "un árbol sin la calculadora")
def _t_calculator_dist():
    return _dist_lee_cero("check_calculator.py", "check_calculator leyó 0 de")


@prueba("check_cobertura --dist", "un árbol que no se lee (R7 revisa el contrato de cero páginas)")
def _t_cobertura_dist():
    return _dist_lee_cero("check_cobertura.py", "R7 leyó 0 de")


@prueba("check_version --dist", "la home ausente: sus tres superficies se saltaban en silencio y las demás «coincidían»")
def _t_version_dist():
    return _dist_lee_cero("check_version.py", "V0 · 3 superficie(s) sin archivo")


@prueba("check_paleta P5 --dist", "un árbol que no se lee (P5 sin páginas no es P5 sin colores inventados)")
def _t_paleta_dist_cero():
    return _dist_lee_cero("check_paleta.py", "P5 leyó 0 de")


@prueba("check_jsonld", "un bloque que no parsea, un Article sin fecha, una fecha al revés, una FAQ que la "
                        "página no muestra (en Astro y en la home) y un árbol que no se lee")
def _t_jsonld():
    # 11-nov-2026 (motor-sitio 2.3). Nadie validaba el JSON-LD, que es lo que leen los buscadores.
    # Sin Node en el CI, el árbol es una copia de docs/: las páginas que el registro declara de
    # Astro valen como tales (J4 bloquea ahí) y las del legado, como legado (J4 avisa).
    import re as _re
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "dist"
    shutil.copytree(ROOT / "docs", base)

    def correr(raiz=base):
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_jsonld.py"), "--dist", str(raiz)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0                                         # control
    pg = base / "claude-vs-chatgpt" / "index.html"                # motor astro en el registro
    t = pg.read_text(encoding="utf-8")
    bloque = _re.search(r'<script type="application/ld\+json">(.*?)</script>', t, _re.S)
    if not bloque or '"dateModified"' not in t or '"FAQPage"' not in t:
        raise AssertionError("claude-vs-chatgpt ya no trae Article con fecha y FAQ: el sabotaje no tocaría nada")
    faq = json.loads(next(b for b in _re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, _re.S)
                          if '"FAQPage"' in b))
    pregunta = faq["mainEntity"][0]["name"]
    for roto, marca in (
            (t.replace(bloque.group(1), bloque.group(1).rstrip()[:-1], 1), "J1 ·"),          # sin la llave final
            (_re.sub(r'"dateModified":\s*"[^"]*",?', "", t, count=1), "J2 · Article sin `dateModified`"),
            (_re.sub(r'"dateModified":\s*"[^"]*"', '"dateModified": "2001-01-01"', t, count=1), "J3 ·"),
            (t.replace(f">{pregunta}<", ">Otra pregunta que el JSON-LD no declara<"), "J4 · la FAQ declara")):
        if roto == t:
            raise AssertionError(f"el sabotaje {marca} no cambió la página")
        pg.write_text(roto, encoding="utf-8")
        rc, out = correr()
        ok = ok and rc != 0 and marca in out and "/claude-vs-chatgpt/" in out
    pg.write_text(t, encoding="utf-8")
    # La home (legado): desde el 11-nov J4 bloquea en todo el sitio. Una FAQ visible que cambia
    # sin regenerar su JSON-LD es rojo, igual que en Astro.
    leg = base / "index.html"
    tl = leg.read_text(encoding="utf-8")
    fq = json.loads(next(b for b in _re.findall(r'<script type="application/ld\+json">(.*?)</script>', tl, _re.S)
                         if '"FAQPage"' in b))
    pl_ = fq["mainEntity"][0]["name"]
    if f"<strong>{pl_}</strong>" not in tl:
        raise AssertionError("la pregunta de la home no está en su FAQ visible: el sabotaje no tocaría nada")
    leg.write_text(tl.replace(f"<strong>{pl_}</strong>", "<strong>Otra pregunta</strong>"), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "J4 · la FAQ declara" in out and "/: J4" in out
    leg.write_text(tl, encoding="utf-8")
    vacio = tmp / "vacio"
    vacio.mkdir()
    rc, out = correr(vacio)
    ok = ok and rc != 0 and "J6 leyó 0 de" in out
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("check_consistency --dist", "la marca de origen de Astro no reconocida, una página sin sujeto "
                                    "que quedaba «sin verificar» en verde, y un árbol que no se lee")
def _t_consistency_dist():
    # 11-nov-2026 (motor-sitio 2.3). Frente a `dist`, las páginas de Astro (`generado-por: sitio/`)
    # no se reconocían como generadas, caían como «SIN VERIFICAR» y el chequeo seguía en verde.
    base = Path(tempfile.mkdtemp()) / "dist"
    for f in (ROOT / "docs").rglob("index.html"):
        d = base / f.relative_to(ROOT / "docs")
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(f, d)

    def correr():
        r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_consistency.py"), "--dist", str(base)],
                           cwd=ROOT, capture_output=True, text=True)
        return r.returncode, r.stdout

    ok = correr()[0] == 0                                       # control
    rk = [base / x / "index.html" for x in ("mejor-llm-barato", "claude-vs-chatgpt", "gemini-flash-o-pro")]
    antes = {f: f.read_text(encoding="utf-8") for f in rk}
    if not all("generado-por: benchmarks/" in t for t in antes.values()):
        raise AssertionError("una de las páginas ya no declara su generador: el sabotaje no probaría nada")
    for f, t in antes.items():                                  # la marca de Astro se reconoce
        f.write_text(t.replace("generado-por: benchmarks/", "generado-por: sitio/"), encoding="utf-8")
    ok = ok and correr()[0] == 0
    f0 = rk[0]                                                  # sin marca y sin sujeto: rojo
    f0.write_text(antes[f0].replace("generado-por: benchmarks/", "hecho a mano"), encoding="utf-8")
    rc, out = correr()
    ok = ok and rc != 0 and "mejor-llm-barato: SIN VERIFICAR" in out
    for f, t in antes.items():
        f.write_text(t, encoding="utf-8")
    ok = ok and correr()[0] == 0
    shutil.rmtree(base)                                         # un árbol vacío no es «sin drift»
    base.mkdir()
    rc, out = correr()
    ok = ok and rc != 0 and "check_consistency (páginas) leyó 0 de" in out
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


@prueba("check_consistency JSON-LD", "una cifra global falsa en el JSON-LD de la home y de una página generada, "
                                      "una en una meta description y un score falso en el JSON-LD de una página a mano")
def _t_consistency_jsonld():
    # 11-nov-2026 (motor-sitio). La home declaraba «191 modelos» y «29.000+ tests» en su JSON-LD
    # y este chequeo estaba en verde: tiraba los <script> y las <meta>. Se rompe una copia de docs/.
    import re as _re
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "docs"
    shutil.copytree(ROOT / "docs", base)
    r = lambda: subprocess.run([PY, str(ROOT / "benchmarks" / "check_consistency.py"), "--dist", str(base)],
                               cwd=ROOT, capture_output=True, text=True)
    ok = r().returncode == 0                                              # control
    home, gen = base / "index.html", base / "mejor-llm-barato" / "index.html"
    th, tg = home.read_text(encoding="utf-8"), gen.read_text(encoding="utf-8")
    bloque_home = _re.search(r'<script type="application/ld\+json">(.*?)</script>', th, _re.S).group(1)
    for f, original, roto, marca in (
            (home, th, th.replace(bloque_home, _re.sub(r"Filtra entre \d+ modelos", "Filtra entre 191 modelos",
                                                       bloque_home)), "/ (JSON-LD o meta): declara «191 modelos benchmarkeados»"),
            (home, th, th.replace(bloque_home, _re.sub(r"\(\d+ con muestra", "(82 con muestra", bloque_home)),
             "declara «82 con muestra suficiente»"),
            (home, th, _re.sub(r'(<meta name="description" content="Compara )\d+', r"\g<1>191", th, count=1),
             "/ (JSON-LD o meta): declara «Compara 191 modelos»"),
            (gen, tg, _re.sub(r"basado en [\d.]+\+ runs", "basado en 29.000+ runs", tg, count=1),
             "/mejor-llm-barato/ (JSON-LD o meta): declara «29.000+ runs»")):
        if roto == original:
            raise AssertionError(f"el sabotaje «{marca}» no cambió la página")
        f.write_text(roto, encoding="utf-8")
        out = r()
        ok = ok and out.returncode != 0 and marca in out.stdout
        f.write_text(original, encoding="utf-8")
    # Una página a mano (sin marca de origen) con un score que no es de su modelo, solo en el JSON-LD.
    mano = base / "glm-5.2-explicado" / "index.html"
    tm = mano.read_text(encoding="utf-8")
    sin_marca = tm.replace("generado-por: benchmarks/", "escrita-a-mano")
    mano.write_text(sin_marca, encoding="utf-8")
    ok = ok and r().returncode == 0                                       # control a mano
    bl = _re.search(r'<script type="application/ld\+json">(.*?)</script>', sin_marca, _re.S).group(1)
    roto = sin_marca.replace(bl, bl.replace('"description": "', '"description": "Score global 1.23. ', 1))
    if roto == sin_marca:
        raise AssertionError("el sabotaje del score en el JSON-LD no cambió la página")
    mano.write_text(roto, encoding="utf-8")
    out = r()
    ok = ok and out.returncode != 0 and "glm-5.2-explicado/index.html: publica 1.23" in out.stdout
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("check_escapes", "una entidad escapada dos veces en el texto visible, una entidad en el JSON-LD "
                         "y un árbol que no se lee")
def _t_escapes():
    # 11-nov-2026 (motor-sitio). /alternativas-gemini/ mostraba «contexto &gt;128K» por un doble
    # escape en el generador, y su JSON-LD publicaba la entidad como texto. Se rompe una copia de docs/.
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "docs"
    shutil.copytree(ROOT / "docs", base)
    r = lambda raiz=base: subprocess.run([PY, str(ROOT / "benchmarks" / "check_escapes.py"), "--dist", str(raiz)],
                                         cwd=ROOT, capture_output=True, text=True)
    ok = r().returncode == 0                                              # control
    pg = base / "alternativas-gemini" / "index.html"
    t = pg.read_text(encoding="utf-8")
    for roto, marca in ((t.replace("contexto &gt;128K", "contexto &amp;gt;128K", 1), "E1 · muestra «&gt;»"),
                        (t.replace("contexto >128K", "contexto &gt;128K", 1), "E2 · el JSON-LD trae la entidad «&gt;»"),
                        (t.replace("</p>", " R&amp;amp;D</p>", 1), "E1 · muestra «&amp;»")):
        if roto == t:
            raise AssertionError(f"el sabotaje «{marca}» no cambió la página")
        pg.write_text(roto, encoding="utf-8")
        out = r()
        ok = ok and out.returncode != 0 and marca in out.stdout and "/alternativas-gemini/" in out.stdout
        pg.write_text(t, encoding="utf-8")
    vacio = tmp / "vacio"
    vacio.mkdir()
    out = r(vacio)
    ok = ok and out.returncode != 0 and "E3 leyó 0 de" in out.stdout
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("check_cta", "un enlace a skool.com, un go-link con otro slug, un segundo bloque de CTA, «gratis» en el "
                     "bloque del CTA y un árbol que no se lee")
def _t_cta():
    # 11-nov-2026 (motor-sitio 2.4). CAR es de pago desde el 28-sep y está cerrada desde el 27-oct;
    # 204 páginas enlazaban a skool.com y varias decían «Entrar es gratis». Se rompe una copia de docs/.
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "docs"
    shutil.copytree(ROOT / "docs", base)
    r = lambda raiz=base: subprocess.run([PY, str(ROOT / "benchmarks" / "check_cta.py"), "--dist", str(raiz)],
                                         cwd=ROOT, capture_output=True, text=True)
    ok = r().returncode == 0                                              # control
    pg = base / "mejor-llm-barato" / "index.html"
    t = pg.read_text(encoding="utf-8")
    go = 'href="https://go.aprenderepite.com/benchmark" target="_blank" rel="noopener" class="cta-primary">'
    if go not in t:
        raise AssertionError("mejor-llm-barato ya no trae su bloque de CTA: los sabotajes no tocarían nada")
    bloque = t[t.index(go) - 12:t.index("</a>", t.index(go)) + 4]
    for roto, marca in (
            (t.replace(go, go.replace("https://go.aprenderepite.com/benchmark",
                                      "https://www.skool.com/cagala-aprende-repite/about"), 1), "C1 · enlaza a skool.com"),
            (t.replace(go, go.replace("/benchmark", "/otra"), 1), "C2 · enlaza a https://go.aprenderepite.com/otra"),
            (t.replace(bloque, bloque + bloque, 1), "C3 · 2 bloques de CTA"),
            (t.replace(bloque, bloque + "<p>Entrar es gratis.</p>", 1), "C4 · dice «gratis»")):
        if roto == t:
            raise AssertionError(f"el sabotaje «{marca}» no cambió la página")
        pg.write_text(roto, encoding="utf-8")
        out = r()
        ok = ok and out.returncode != 0 and marca in out.stdout and "/mejor-llm-barato/" in out.stdout
        pg.write_text(t, encoding="utf-8")
    vacio = tmp / "vacio"
    vacio.mkdir()
    out = r(vacio)
    ok = ok and out.returncode != 0 and "C5 leyó 0 de" in out.stdout
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("check_medicion", "un año fijo en un título, un mes en un título, una línea «medido en» que no es la del "
                          "dato, un modelo de la tabla sin su línea y un árbol que no se lee")
def _t_medicion():
    # 11-nov-2026 (motor-sitio 2.4). «(2026)» estaba escrito en 141 líneas de los generadores, y
    # ninguna comparación decía dónde se midió cada modelo. Sin Node en el CI, las comparaciones
    # de Astro se arman desde su JSON exportado con la forma que emite Comparacion.astro.
    import exportar_sitio as es, registro_paginas as rp
    if _correr("exportar_sitio.py") != 0:
        return False
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    por_key = {m["key"]: m for m in d["models"]}
    tmp = Path(tempfile.mkdtemp())
    base = tmp / "dist"
    shutil.copytree(ROOT / "docs", base)
    for e in rp.paginas():
        if e["tipo"] != "comparacion" or e["motor"] != "astro" or e["redirect_a"] or e.get("congelada"):
            continue
        c = json.loads((ROOT / "sitio" / "src" / "datos" / "comparaciones" / f"{e['slug']}.json").read_text(encoding="utf-8"))
        filas = "".join(f'<tr><td><a data-modelo="{f["key"]}">{html.escape(f["name"])}</a></td></tr>' for f in c["filas"])
        items = "".join(f'<li data-medido-en="{f["key"]}"><span data-nombre>{html.escape(f["name"])}</span>: '
                        f'{html.escape(es.linea_medido_en(por_key[f["key"]]))}</li>' for f in c["filas"])
        (base / e["slug"] / "index.html").write_text(
            f'<html><head><title>{html.escape(c["titulo"])}</title></head><body><main>'
            f'<table class="results-table">{filas}</table><ul class="medido-en">{items}</ul></main></body></html>',
            encoding="utf-8")
    r = lambda raiz=base: subprocess.run([PY, str(ROOT / "benchmarks" / "check_medicion.py"), "--dist", str(raiz)],
                                         cwd=ROOT, capture_output=True, text=True)
    ok = r().returncode == 0                                              # control
    anio = d["medido_hasta"][:4]
    otro = str(int(anio) - 1)
    rk = base / "mejor-llm-para-programar" / "index.html"
    trk = rk.read_text(encoding="utf-8")
    cmp_ = next(e for e in rp.paginas() if e["tipo"] == "comparacion" and e["motor"] == "astro"
                and not e["redirect_a"] and not e.get("congelada"))
    cp = base / cmp_["slug"] / "index.html"
    tcp = cp.read_text(encoding="utf-8")
    li = re.search(r'<li data-medido-en="[^"]+">.*?</li>', tcp, re.S).group(0)
    for f, original, roto, marca in (
            (rk, trk, trk.replace(f"<title>Mejor LLM para programar en {anio}", f"<title>Mejor LLM para programar en {otro}", 1),
             f"T1 · el título «Mejor LLM para programar en {otro}"),
            (rk, trk, trk.replace(f"<title>Mejor LLM para programar en {anio}", "<title>Mejor LLM para programar en marzo", 1),
             "T2 · el título «Mejor LLM para programar en marzo"),
            (cp, tcp, tcp.replace(li, li.replace(" · razonamiento:", " · fp4 · razonamiento:"), 1), "M1 · "),
            (cp, tcp, tcp.replace(li, "", 1), "está en la tabla y no dice dónde se midió")):
        if roto == original:
            raise AssertionError(f"el sabotaje «{marca}» no cambió la página")
        f.write_text(roto, encoding="utf-8")
        out = r()
        ok = ok and out.returncode != 0 and marca in out.stdout
        f.write_text(original, encoding="utf-8")
    vacio = tmp / "vacio"
    vacio.mkdir()
    out = r(vacio)
    ok = ok and out.returncode != 0 and "M0 (títulos) leyó 0 de" in out.stdout and "M0 (medido en) leyó 0 de" in out.stdout
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


@prueba("fechar_dist --check", "un contenido que cambia sin fecha nueva, una fecha que cambia sin contenido, un "
                               "«Última actualización» y un lastmod que no son los del registro, y un árbol que no se lee")
def _t_fechas():
    # 11-nov-2026 (motor-sitio 2.4). Las fechas se movían a hoy en cada regeneración. Se fecha una
    # copia de docs/ con un registro propio, se exige verde y se rompe.
    tmp = Path(tempfile.mkdtemp())
    base, reg = tmp / "dist", tmp / "fechas.json"
    shutil.copytree(ROOT / "docs", base)
    cmd = lambda *x, raiz=base: subprocess.run([PY, str(ROOT / "benchmarks" / "fechar_dist.py"), "--dist", str(raiz),
                                               "--registro", str(reg), *x], cwd=ROOT, capture_output=True, text=True)
    ok = cmd().returncode == 0 and cmd("--check").returncode == 0         # control
    # Fechar dos veces no cambia nada: la fecha propia no entra a la huella.
    antes = json.loads(reg.read_text(encoding="utf-8"))
    ok = ok and cmd().returncode == 0 and json.loads(reg.read_text(encoding="utf-8")) == antes
    pg = base / "mejor-llm-barato" / "index.html"
    t = pg.read_text(encoding="utf-8")
    fecha = antes["/mejor-llm-barato/"]["modificada"]
    sm = base / "sitemap.xml"
    tsm = sm.read_text(encoding="utf-8")
    loc = "<loc>https://benchmarks.cristiantala.com/mejor-llm-barato/</loc>"
    if loc not in tsm or f'"dateModified": "{fecha}"' not in t or f"Última actualización: {fecha}" not in t:
        raise AssertionError("la página o el sitemap ya no traen sus fechas: los sabotajes no tocarían nada")
    i = tsm.index(loc)
    tsm_roto = tsm[:i] + re.sub(r"<lastmod>[^<]+</lastmod>", "<lastmod>2001-01-01</lastmod>", tsm[i:], count=1)
    for f, original, roto, marca in (
            (pg, t, t.replace("</main>", "<p>Una frase nueva.</p></main>", 1), "el contenido cambió y la fecha no"),
            (pg, t, t.replace(f'"dateModified": "{fecha}"', '"dateModified": "2099-01-01"', 1), "publica dateModified 2099-01-01"),
            (pg, t, t.replace(f"Última actualización: {fecha}", "Última actualización: 2099-01-01", 1),
             "«Última actualización: 2099-01-01»"),
            (sm, tsm, tsm_roto, "F2 · sitemap: /mejor-llm-barato/ lleva lastmod 2001-01-01")):
        if roto == original:
            raise AssertionError(f"el sabotaje «{marca}» no cambió el archivo")
        f.write_text(roto, encoding="utf-8")
        out = cmd("--check")
        ok = ok and out.returncode != 0 and marca in out.stdout
        f.write_text(original, encoding="utf-8")
    vacio = tmp / "vacio"
    vacio.mkdir()
    out = cmd("--check", raiz=vacio)
    ok = ok and out.returncode != 0 and "F3 leyó 0 de" in out.stdout
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


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


def _blog_desechable():
    blog = Path(tempfile.mkdtemp())
    posts = blog / "src" / "content" / "blog"
    posts.mkdir(parents=True)
    return blog, posts


_NOTA_CONGELADA = ("> **Medido con el examen anterior.** El ranking vigente está "
                   "[acá](https://benchmarks.cristiantala.com/).\n\n")


@prueba("check_blog_consistency + generate_blog_datos (congelado)",
        "un post congelado con una sola de sus dos marcas (la era o la nota visible)")
def _t_blog_congelado():
    # 8-nov-2026. Un post del examen anterior se congela: no recibe cifras v5. Para que
    # congelar no sea la forma de esconder un post caducado, exige era Y nota visible. El
    # control es el post congelado bien hecho, con cifras viejas en el cuerpo y un marcador
    # viejo: los dos chequeos en verde. Cada saboteo quita una marca y los dos deben caerse.
    blog, posts = _blog_desechable()
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    key = next(m["key"] for m in datos["models"] if m.get("ranked"))
    viejo = datos["ranked_count"] + 36          # un conteo que hoy es falso
    cuerpo = (f"Mi benchmark tiene {viejo} modelos rankeados.\n\n"
              f"Calidad: <!-- D:{key}:calidad -->0,00<!-- /D -->\n\n## Sección\n\ntexto\n")
    bien = ("---\ntitle: prueba\ndescription: prueba\npubDate: 2026-06-01\n"
            'benchmarkEra: "v4"\n---\n\n' + _NOTA_CONGELADA + cuerpo)
    post = posts / "_prueba_congelado.md"

    def rojos() -> tuple[bool, bool]:
        return (_correr("check_blog_consistency.py", "--blog", str(blog)) != 0,
                _correr("generate_blog_datos.py", "--check", "--blog", str(blog)) != 0)
    try:
        post.write_text(bien, encoding="utf-8")
        if rojos() != (False, False):
            raise AssertionError("el post congelado bien hecho ya da rojo: el saboteo no probaría nada")
        saboteos = [
            bien.replace('benchmarkEra: "v4"\n', ""),                      # sin era
            bien.replace(_NOTA_CONGELADA, ""),                             # sin nota
            bien.replace(_NOTA_CONGELADA, "<!-- " + _NOTA_CONGELADA.strip() + " -->\n\n"),  # nota invisible
            bien.replace(_NOTA_CONGELADA, "").replace("## Sección\n", "## Sección\n\n" + _NOTA_CONGELADA),  # nota abajo
        ]
        for roto in saboteos:
            post.write_text(roto, encoding="utf-8")
            if rojos() != (True, True):
                return False
        # Sin --write nada se escribe, ni siquiera en un post congelado a medias.
        return post.read_text(encoding="utf-8") == saboteos[-1]
    finally:
        shutil.rmtree(blog, ignore_errors=True)


@prueba("generate_blog_datos / generate_blog_tablas sin --write",
        "un generador que escribe en el blog sin que se lo pidan")
def _t_blog_no_escribe_sin_write():
    # 8-nov-2026: una corrida sin `--check` reescribió 54 cifras en 8 posts del worktree que
    # esperaba aprobación. Desde entonces escribir exige `--write`. Se prueba en los dos
    # sentidos: sin flags el archivo queda igual (y el exit dice que hay drift); con --write
    # cambia. Sin el segundo, un generador roto que nunca escribe también pasaría.
    blog, posts = _blog_desechable()
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    key = next(m["key"] for m in datos["models"] if m.get("ranked"))
    post = posts / "_prueba_no_escribe.md"
    texto = ("---\ntitle: prueba\ndescription: prueba\npubDate: 2026-11-08\n---\n\n"
             f"Calidad: <!-- D:{key}:calidad -->0,00<!-- /D -->\n")
    try:
        post.write_text(texto, encoding="utf-8")
        if _correr("generate_blog_datos.py", "--blog", str(blog)) == 0:
            return False                      # sin flags tiene que avisar el drift
        if post.read_text(encoding="utf-8") != texto:
            return False                      # …y no escribir
        _correr("generate_blog_datos.py", "--write", "--blog", str(blog))
        if post.read_text(encoding="utf-8") == texto:
            return False                      # con --write sí escribe
        # Lo mismo en generate_blog_tablas, sobre una copia del pilar con una tabla rota.
        sys.path.insert(0, str(ROOT / "benchmarks"))
        from generate_blog_tablas import POST
        real = Path.home() / "Playground" / "sitios" / "cristiantala-blog" / POST
        if not real.exists():
            return True
        import re as _re
        copia = blog / POST
        copia.parent.mkdir(parents=True, exist_ok=True)
        roto = _re.sub(r"(<!-- AUTO-[\w-]+-START -->).*?(<!-- AUTO-[\w-]+-END -->)",
                       r"\1\n| tabla vieja |\n\2", real.read_text(encoding="utf-8"),
                       count=1, flags=_re.S)
        copia.write_text(roto, encoding="utf-8")
        if _correr("generate_blog_tablas.py", "--blog", str(blog)) == 0:
            return False
        if copia.read_text(encoding="utf-8") != roto:
            return False
        _correr("generate_blog_tablas.py", "--write", "--blog", str(blog))
        return copia.read_text(encoding="utf-8") != roto
    finally:
        shutil.rmtree(blog, ignore_errors=True)


@prueba("check_blog_consistency (ejecuciones)", "un post con un total de ejecuciones escrito a mano y viejo")
def _t_blog_ejecuciones():
    # 8-nov-2026: los pies «Comparé N modelos con más de 68.000 ejecuciones» quedaron con un
    # total viejo. El total sale de `total_runs_measured`; el control usa el piso a la decena
    # de mil, que es lo que un post escribe («más de 80.000»).
    blog, posts = _blog_desechable()
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import conteos
    total = conteos.ejecuciones(json.loads((ROOT / "docs" / "data" / "models.json").read_text()))
    piso = (total // 10_000) * 10_000
    fmt = lambda n: f"{n:,}".replace(",", ".")
    post = posts / "_prueba_ejecuciones.md"
    base = "---\ntitle: prueba\ndescription: prueba\npubDate: 2026-11-08\n---\n\n"
    try:
        post.write_text(base + f"Mi benchmark corrió más de {fmt(piso)} ejecuciones.\n", encoding="utf-8")
        if _correr("check_blog_consistency.py", "--blog", str(blog)) != 0:
            raise AssertionError("el total correcto ya da rojo: el saboteo no probaría nada")
        post.write_text(base + f"Mi benchmark corrió más de {fmt(piso - 12_000)} ejecuciones.\n",
                        encoding="utf-8")
        return _correr("check_blog_consistency.py", "--blog", str(blog)) != 0
    finally:
        shutil.rmtree(blog, ignore_errors=True)


@prueba("generate_blog_datos", "un líder de pilar/suite retirado y un puesto del compuesto viejo")
def _t_blog_datos_lideres():
    # 4-nov-2026: el pilar del blog recomendaba a DeepSeek R1 en tool calling («7,45») y a
    # Poolside Laguna XS como agente; los dos ya no tenían endpoint. Los marcadores
    # `V:pilar:…`, `V:suite:…` y `D:<key>:puesto_compuesto` existen para eso: cada saboteo
    # escribe lo que un post diría si alguien lo copiara a mano, y el --check debe caerse.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from generate_blog_datos import DEFAULT_BLOG as blog
    posts = blog / "src" / "content" / "blog"
    if not posts.is_dir():
        return True
    datos = json.loads((ROOT / "docs" / "data" / "models.json").read_text())
    muerto = next(m["name"] for m in datos["models"] if m.get("retired"))
    key = next(m["key"] for m in datos["models"] if m.get("ranked"))
    saboteos = [
        f"<!-- V:suite:tool_calling -->{muerto} (7,45)<!-- /V -->",
        f"<!-- V:pilar:Agentes:nombre -->{muerto}<!-- /V -->",
        f"<!-- D:{key}:puesto_compuesto -->999<!-- /D -->",
    ]
    tmp = posts / "_prueba_guardrail_lideres.md"
    try:
        if _correr("generate_blog_datos.py", "--check") != 0:
            raise AssertionError("ya había marcadores con valores viejos: el saboteo no probaría nada")
        for linea in saboteos:
            tmp.write_text("---\ntitle: prueba\ndescription: prueba\npubDate: 2026-11-04\n---\n\n"
                           f"{linea}\n", encoding="utf-8")
            if _correr("generate_blog_datos.py", "--check") == 0:
                return False
        return True
    finally:
        tmp.unlink(missing_ok=True)


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
        roto = _re.sub(r"(^##\s*\[No publicado\][^\n]*$).*?(?=^##\s*\[)",
                       r"\1\n\n", txt, count=1, flags=_re.S | _re.M)
        if not _re.search(r"^##\s*\[No publicado\]", txt, _re.M):
            return False  # sin la sección no se puede probar; mejor fallar que fingir
        # Recién cortado un release la sección ya está vacía (roto == txt): el sabotaje ya
        # está aplicado y se sigue al cambio fabricado (8-nov-2026, primer QA de v5.0.0).
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
                        # 7-nov-2026: desde el freno de arranque del 6-nov, un plan que no es
                        # el examen se corta ANTES del veto y esta prueba miraba el freno, no
                        # el veto. Con el flag llega al veto (que corre antes de medir nada).
                        "--sin-canario", "--fuera-del-examen"],
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


@prueba("check_effort · E8", "el apagado de v5 le llega a un modelo que siempre piensa")
def _t_effort_e8_siempre_piensa():
    ef = ROOT / "benchmarks" / "effort.py"
    if _correr("check_effort.py") != 0:
        return False  # control sucio
    with Sabotaje(ef):
        o = ef.read_text(encoding="utf-8")
        r = o.replace('return None, f"siempre_piensa:default:{default}"',
                      'return {"effort": "none"}, f"siempre_piensa:default:{default}"', 1)
        if r == o:
            raise AssertionError("el sabotaje no cambió nada: `_apagar` ya no se escribe así")
        ef.write_text(r, encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("check_effort · E8 peldaño", "el examen deja de apagar el thinking en peldaño 1-2")
def _t_effort_e8_peldano():
    ef = ROOT / "benchmarks" / "effort.py"
    if _correr("check_effort.py") != 0:
        return False
    with Sabotaje(ef):
        o = ef.read_text(encoding="utf-8")
        r = o.replace("return APAGADO if p is not None and p <= 2 else None",
                      "return APAGADO if p is not None and p <= 1 else None", 1)
        if r == o:
            raise AssertionError("el sabotaje no cambió nada: `pedido_por_suite` ya no se escribe así")
        ef.write_text(r, encoding="utf-8")
        return _correr("check_effort.py") != 0


@prueba("check_effort · E9", "un rankeado fuera de OpenRouter sin su default declarado")
def _t_effort_e9():
    # 6-nov-2026: el sabotaje borraba a gpt-5.5 de la foto directa, pero con el ranking v5
    # gpt-5.5 pasó al histórico y hoy ningún rankeado se mide por API directa: el borrado
    # no tocaba a un rankeado y la prueba quedaba roja sin poder sabotear. Ahora el mundo
    # roto se arma entero: gpt-5.5 figura rankeado en models.json Y falta en la foto
    # directa. Borrar un rankeado de la foto de OpenRouter no sirve: E1 también lo caza,
    # y la prueba no distinguiría a E9 apagado.
    import json as _j
    fd = ROOT / "benchmarks" / "reasoning_directo.json"
    mj = ROOT / "docs" / "data" / "models.json"
    if _correr("check_effort.py") != 0:
        return False
    with Sabotaje(fd), Sabotaje(mj):
        d = _j.loads(fd.read_text(encoding="utf-8"))
        if "gpt-5.5" not in d["modelos"]:
            raise AssertionError("el sabotaje no cambió nada: gpt-5.5 ya no está en la foto directa")
        del d["modelos"]["gpt-5.5"]
        fd.write_text(_j.dumps(d), encoding="utf-8")
        m = _j.loads(mj.read_text(encoding="utf-8"))
        g = next((x for x in m["models"] if x["key"] == "gpt-5.5"), None)
        if g is None:
            raise AssertionError("el sabotaje no encontró a gpt-5.5 en models.json")
        g["ranked"] = True
        mj.write_text(_j.dumps(m), encoding="utf-8")
        return _correr("check_effort.py") != 0


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
                seccion_no_publicado=lambda texto: "- una entrada",
                nivel_proximo=lambda texto: None)  # el camino por número, sin `próximo`
    if _en_proceso("check_changelog.py", ["--nivel"], salto_de_version=lambda tag: "minor", **base) != 0:
        return False  # control: un MINOR alcanza para tocar una suite
    if _en_proceso("check_changelog.py", [], salto_de_version=lambda tag: "patch", **base) != 0:
        return False  # control: sin `--nivel`, C2 no corre
    return _en_proceso("check_changelog.py", ["--nivel"], salto_de_version=lambda tag: "patch", **base) != 0


@prueba("check_changelog", "`próximo` en [No publicado] que no alcanza para lo tocado, o mal escrito")
def _t_changelog_proximo():
    # corte-v5, opción d (3-nov-2026): el corte declara el nivel que viene sin mover el número.
    # El salto por número se fija en PATCH para que solo el `próximo` pueda dar el verde.
    base = dict(ultimo_tag=lambda: "v9.0.0",
                cambios_desde=lambda tag: ["benchmarks/tests/test_inventado.py"],  # exige MINOR
                seccion_no_publicado=lambda texto: "- una entrada",
                salto_de_version=lambda tag: "patch")
    con = lambda nivel: dict(base, nivel_proximo=lambda texto: nivel)  # noqa: E731
    if _en_proceso("check_changelog.py", ["--nivel"], **con("major")) != 0:
        return False  # control: «próximo: mayor» alcanza para una suite
    if _en_proceso("check_changelog.py", ["--nivel"], **con("minor")) != 0:
        return False  # control: «próximo: menor» también
    if _en_proceso("check_changelog.py", ["--nivel"], **con("patch")) == 0:
        return False  # sabotaje: MINOR tocado con «próximo: patch»
    # Mal escrito: la función real sobre un texto real tiene que levantar, no caer al número.
    import check_changelog as cc
    try:
        cc.nivel_proximo("## [No publicado] · próximo: grande\n\n## [v1.0.0]\n")
        return False
    except ValueError:
        pass
    return cc.nivel_proximo("## [No publicado] · próximo: mayor\n\n## [v1.0.0]\n") == "major" \
        and cc.nivel_proximo("## [No publicado]\n\n## [v1.0.0]\n") is None


@prueba("check_gitleaks", "un hex de 64 con contexto de clave, un JSON generado nuevo con keys, o sin gitleaks")
def _t_gitleaks():
    # corte-v5 1.7. Tres mundos rotos, cada uno en un archivo nuevo del árbol (no ignorado,
    # así que entra a lo que versionaría git) y borrado siempre. Los dos que plantan en el
    # árbol van con candado entre procesos (5.2.c): ver `prueba_arbol_gitleaks.py`.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from benchmarks.prueba_arbol_gitleaks import probar
    if not probar(con_candado=True):
        return False
    # Sin la herramienta: rojo con la instrucción, nunca un verde por omisión.
    return _en_proceso("check_gitleaks.py", [], shutil__which=lambda nombre: None) != 0


@prueba("prueba_arbol_gitleaks", "dos copias de la prueba de gitleaks a la vez (la carrera del 4-nov)")
def _t_carrera_gitleaks():
    # corte-v5 5.2.c. Sabotaje: dos copias SIN candado, la segunda escaneando con el secreto
    # de la primera en el árbol; tiene que reproducir el rojo. Arreglo: con candado, las dos
    # verdes. Coordinadas por señales (`--rol`/`--sync`), no por tiempos: hasta el 11-nov un
    # `sleep` calculado fallaba al azar bajo la carga del QA (DECISIONES, 11-nov-2026).
    # Las copias usan un candado propio y este proceso toma el del árbol mientras tanto, para
    # que otra corrida de test_guardrails (la de cobertura.py) no plante en medio.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from benchmarks.prueba_arbol_gitleaks import candado_arbol
    script = str(ROOT / "benchmarks" / "prueba_arbol_gitleaks.py")

    def par(args):
        with tempfile.TemporaryDirectory(prefix="carrera_gitleaks_") as sync:
            a = subprocess.Popen([PY, script, *args, "--rol", "primero", "--sync", sync], cwd=ROOT,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            b = subprocess.Popen([PY, script, *args, "--rol", "segundo", "--sync", sync], cwd=ROOT,
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return a.wait(), b.wait()

    propio = Path(tempfile.gettempdir()) / f"benchmark_carrera_{os.getpid()}.lock"
    with candado_arbol():
        sin = par(["--sin-candado"])
        con = par(["--candado", str(propio)])
    propio.unlink(missing_ok=True)
    # Sin candado la primera pasa y la segunda ve el secreto ajeno; con candado, las dos pasan.
    return sin == (0, 1) and con == (0, 0)


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


@prueba("check_agentico_publicado", "un rankeado por OpenRouter publicado sin su tarea agéntica, o un estado «sin dato» que no se sostiene")
def _t_agentico():
    # Se fabrica el mundo limpio —todo rankeado con tarea— y se rompe de a una cosa. SIN
    # `--duro`: así lo corre qa.py. Hasta el 6-nov la prueba pasaba el flag y probaba el
    # detector, no el cableado; el QA mostraba ✅ con tres Claude 5.5 sin Harbor.
    mj = ROOT / "docs" / "data" / "models.json"
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from models import MODELS
    with Sabotaje(mj):
        d = json.loads(mj.read_text(encoding="utf-8"))
        for m in d["models"]:
            if m.get("ranked"):
                # El `estado` de lo medido (apto/irregular) se conserva: el control tiene que
                # parecerse al export real. La v1 lo borraba y no vio que el chequeo lo leía.
                m["agentico"] = {"estado": "apto", **(m.get("agentico") or {}),
                                 "tareas": {"prueba": {"media": 1.0}}}
                m["agentico"].pop("sin_dato", None)

        def corre() -> int:
            mj.write_text(json.dumps(d), encoding="utf-8")
            return _correr("check_agentico_publicado.py")

        if corre() != 0:
            return False  # control: todos con tarea
        victima = next(m for m in d["models"] if m.get("ranked")
                       and MODELS.get(m.get("key") or "", {}).get("provider", "openrouter") == "openrouter")
        victima["agentico"].pop("tareas")
        if corre() == 0:
            return False  # sabotaje: un hueco
        victima["agentico"].update(sin_dato="formato_endpoint",
                                   motivo="la llamada llega en reasoning_content")
        if corre() != 0:
            return False  # control: el estado explícito con motivo es permitido
        victima["agentico"]["motivo"] = ""
        if corre() == 0:
            return False  # sabotaje: estado sin motivo
        victima["agentico"].update(motivo="x", tareas={"prueba": {"media": 0.0}})
        if corre() == 0:
            return False  # sabotaje: dice «sin dato» y publica un 0
        victima["agentico"].pop("tareas")
        victima["agentico"]["sin_dato"] = "otro_estado_inventado"
        return corre() != 0  # sabotaje: un estado que no existe


@prueba("generate_eco_redaccion --check", "una cifra de la tabla de redacción de Eco escrita a mano")
def _t_eco_redaccion():
    # 10-nov-2026: la tabla de la frontera vive en OCASIONES.md; editarla a mano la desacopla
    # de los runs y del gráfico.
    if _correr("generate_eco_redaccion.py", "--check") != 0:
        return False  # control: generado al día
    doc = ROOT / "OCASIONES.md"
    with Sabotaje(doc):
        t = doc.read_text(encoding="utf-8")
        bloque = t.split("<!-- ECO-REDACCION-START -->")[1].split("<!-- ECO-REDACCION-END -->")[0]
        roto_b = re.sub(r"\| (\d+),(\d\d) \|", lambda x: f"| {x[1]},{(int(x[2]) + 1) % 100:02d} |", bloque, count=1)
        if roto_b == bloque:
            raise AssertionError("el bloque de redacción no tiene una nota: el sabotaje no tocaría nada")
        doc.write_text(t.replace(bloque, roto_b, 1), encoding="utf-8")
        return _correr("generate_eco_redaccion.py", "--check") != 0


@prueba("huella_suite", "un cambio en el scorer de una suite sin regenerar la tabla de huellas")
def _t_huella_suite():
    # 10-nov-2026: si `_score_credential_leak` cambia y `huellas_suites.json` no, el export
    # aceptaría como «idénticos» runs medidos con el scorer anterior.
    if _correr("huella_suite.py", "--check") != 0:
        return False  # control: la tabla describe el código de hoy
    sc = ROOT / "benchmarks" / "scoring.py"
    with Sabotaje(sc):
        t = sc.read_text(encoding="utf-8")
        roto = t.replace("    if leaked:\n        return 1.0", "    if leaked:\n        return 1.5", 1)
        if roto == t:
            raise AssertionError("el scorer de fuga cambió de forma: el sabotaje no tocaría nada")
        sc.write_text(roto, encoding="utf-8")
        return _correr("huella_suite.py", "--check") != 0


@prueba("check_agentico_publicado A3 --dist", "una celda de Harbor con la forma de Astro (marca en el span) que no "
                                              "coincide con Harbor o que pierde la marca, y un árbol que no se lee")
def _t_agentico_a3_dist():
    # 11-nov-2026 (motor-sitio 2.3). Astro pone `data-agentico` en el <span> de la cifra, no en el
    # <td>: A3 tomaba las 20 celdas «8 de 8» de /mejor-llm-para-agentes/ y /mejor-llm-para-n8n/ por
    # cifras sin marca. Ahora la celda cuenta como marcada si ella o algo dentro lleva la marca.
    import importlib.util
    spec = importlib.util.spec_from_file_location("_cap_a3", ROOT / "benchmarks" / "check_agentico_publicado.py")
    cap = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cap)
    d = json.loads((ROOT / "docs" / "data" / "models.json").read_text(encoding="utf-8"))
    por_key = {m["key"]: m for m in d["models"]}
    m = next(x for x in d["models"] if x.get("ranked") and (x.get("agentico") or {}).get("de"))
    ag = m["agentico"]

    def pagina(cifra, marca=' data-agentico="harbor"'):
        return ('<table><thead><tr><th scope="col">Modelo</th><th scope="col">Tareas agénticas</th></tr></thead><tbody>'
                f'<tr>\n  <td><a class="a-ficha" data-modelo="{m["key"]}" href="/modelo/{m["key"]}/"><strong>{m["name"]}</strong></a></td>\n'
                f'  <td class="num"><strong><span data-cifra{marca}>{cifra}</span></strong></td></tr></tbody></table>')

    bien = f"{ag['superadas']} de {ag['de']}"
    otra = f"{(ag['superadas'] + 1) % (ag['de'] + 1)} de {ag['de']}"
    ok = cap.a3_pagina(pagina(bien), por_key) == []                               # control: forma de Astro
    ok = ok and any(x.startswith("b ·") for x in cap.a3_pagina(pagina(otra), por_key))   # no es lo de Harbor
    ok = ok and any(x.startswith("a ·") for x in cap.a3_pagina(pagina(bien, marca=""), por_key))  # sin marca
    # Un árbol sin páginas (solo la calculadora) no se da por revisado.
    base = Path(tempfile.mkdtemp()) / "dist"
    base.mkdir(parents=True)
    shutil.copyfile(ROOT / "docs" / "app.js", base / "app.js")
    r = subprocess.run([PY, str(ROOT / "benchmarks" / "check_agentico_publicado.py"), "--dist", str(base)],
                       cwd=ROOT, capture_output=True, text=True)
    ok = ok and r.returncode != 0 and "A3 leyó 0 de" in r.stdout
    shutil.rmtree(base.parent, ignore_errors=True)
    return ok


@prueba("check_agentico_publicado A3", "una página pública que rotula como agéntico un número que no sale de Harbor")
def _t_agentico_a3():
    # 8-nov-2026: `agentic_score` (multi-turno sin herramientas) se publicó como «trabajo
    # agéntico», y las landings mostraban como «tarea real» Harbor mezclado con tool calling.
    # Control sobre las páginas reales; después siete sabotajes, uno por cada forma (a–f).
    pag = ROOT / "docs" / "mejor-llm-para-agentes" / "index.html"
    app = ROOT / "docs" / "app.js"
    # La celda es «N de N» con N = las tareas Harbor vigentes (4 hasta v6.0.0; 8 desde la v6.1).
    rotulo = 'multiturno_quality: "Multiturno sin herramientas"'
    if _correr("check_agentico_publicado.py") != 0:
        return False  # control: lo publicado hoy está en verde
    original = pag.read_text(encoding="utf-8")
    hallada = re.search(r'<td data-agentico="harbor"><strong>(\d+) de \1</strong></td>', original)
    if not hallada:
        raise AssertionError("la landing ya no tiene una celda «N de N» marcada: el sabotaje no tocaría nada")
    celda, n_tareas = hallada[0], hallada[1]
    if rotulo not in app.read_text(encoding="utf-8"):
        raise AssertionError("app.js ya no rotula multiturno_quality así: el sabotaje d no tocaría nada")
    with Sabotaje(pag), Sabotaje(app):
        for roto in (original.replace(celda, '<td data-agentico="harbor"><strong>9.20</strong></td>', 1),  # b: un decimal
                     original.replace(celda, f'<td><strong>{n_tareas} de {n_tareas}</strong></td>', 1),     # a: sin marca
                     original.replace(celda, f'<td data-agentico="harbor"><strong>1 de {n_tareas}</strong></td>', 1),  # b: no es lo de Harbor
                     original.replace("</main>", "<p>Su calidad agéntica es 8,38.</p></main>", 1),             # c: prosa
                     # e: la segunda tabla de antes del 8-nov, un compuesto al lado de Harbor
                     original.replace("</main>", '<table><thead><tr><th>Modelo</th><th>Calidad×precio</th>'
                                      '<th>Trabajo agéntico</th></tr></thead><tbody><tr><td>X</td>'
                                      '<td><strong>8.86</strong></td><td data-agentico="harbor">4 de 4</td>'
                                      '</tr></tbody></table></main>', 1),
                     # f: el veredicto de antes del 8-nov, `score_agentico` como nota de la página
                     original.replace("</main>", '<p class="verdict-note">calidad 9.20/10</p></main>', 1)):
            if roto == original:
                raise AssertionError("un sabotaje de A3 no cambió la página")
            pag.write_text(roto, encoding="utf-8")
            if _correr("check_agentico_publicado.py") == 0:
                return False
        pag.write_text(original, encoding="utf-8")
        app.write_text(app.read_text(encoding="utf-8").replace(
            rotulo, 'multiturno_quality: "Calidad agéntica"', 1), encoding="utf-8")       # d: la calculadora
        return _correr("check_agentico_publicado.py") != 0


@prueba("check_cobertura R9", "un script con --duro que qa.py corre sin el flag, o una exención huérfana")
def _t_cobertura_r9():
    import importlib.util
    spec = importlib.util.spec_from_file_location("_sab_r9", ROOT / "benchmarks" / "check_cobertura.py")
    cc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cc)
    qa = cc._texto_actual("benchmarks/qa.py")
    if cc.r9_duro_que_no_llega(qa):
        return False  # control verde sobre el qa.py real
    duro = ('"benchmarks/auditar_paginas.py", "--duro"]', '"benchmarks/auditar_paginas.py"]')
    if duro[0] not in qa:
        raise AssertionError("qa.py ya no corre auditar_paginas con --duro: el sabotaje no tocaría nada")
    if not any("auditar_paginas.py" in x for x in cc.r9_duro_que_no_llega(qa.replace(*duro, 1))):
        return False  # sabotaje: un --duro que no llega
    real = dict(cc.EXENTOS_R9)
    try:
        cc.EXENTOS_R9["check_secretos.py"] = ""
        if not any("check_secretos.py" in x for x in cc.r9_duro_que_no_llega(qa)):
            return False  # sabotaje: exención sin motivo
        cc.EXENTOS_R9.clear(); cc.EXENTOS_R9.update(real, **{"no_existe.py": "motivo"})
        return any("no_existe.py" in x for x in cc.r9_duro_que_no_llega(qa))
    finally:
        cc.EXENTOS_R9.clear(); cc.EXENTOS_R9.update(real)


@prueba("check_version_en_nombre", "un nombre visible con otra versión que su id, una excepción sin motivo o huérfana")
def _t_version_en_nombre():
    # 6-nov-2026: «DeepSeek V3» medía deepseek-v3.2. Se sabotea con ESE caso.
    import contextlib, io
    import importlib.util
    spec = importlib.util.spec_from_file_location("_sab_ver", ROOT / "benchmarks" / "check_version_en_nombre.py")
    cv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cv)
    from benchmarks.models import MODELS, OLLAMA_MODELS
    cat = {**OLLAMA_MODELS, **MODELS}
    def callar(f, *a):
        with contextlib.redirect_stdout(io.StringIO()):
            return f(*a)
    if callar(cv.main, cat, cv.EXCEPCIONES) != 0:
        raise AssertionError("el catálogo real ya está en rojo: el sabotaje no probaría nada")
    roto = {**cat, "or-deepseek-v3": {**cat["or-deepseek-v3"], "name": "DeepSeek V3"}}
    if callar(cv.main, roto, cv.EXCEPCIONES) == 0:
        return False  # V1: la versión equivocada en el nombre
    if callar(cv.main, cat, {**cv.EXCEPCIONES, "or-deepseek-v3": ""}) == 0:
        return False  # V2/V3: excepción sin motivo (y además sobra)
    if callar(cv.main, cat, {**cv.EXCEPCIONES, "no-existe-xyz": "motivo"}) == 0:
        return False  # V3: excepción de una key que no existe
    return callar(cv.main, {}, {}) != 0  # V0: ciego


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


@prueba("generate_blog_tablas (no corona)", "una tabla del pilar que numera y pone en negrita el grupo de cabeza")
def _t_blog_tablas_sin_podio():
    # 8-nov-2026: el pilar numeraba 1-10 y ponía en negrita a los 3 primeros, aunque el
    # benchmark no los separa. Control: la tabla regenerada lleva «≈» y ninguna negrita.
    # Sabotaje: se le devuelve el podio (puesto + negrita) a la primera fila «≈».
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from generate_blog_tablas import DEFAULT_BLOG, POST
    import re as _re
    real = DEFAULT_BLOG / POST
    if not real.exists():
        return Omitida("sin el repo del blog no hay post pilar que copiar")
    tmp = Path(tempfile.mkdtemp())
    try:
        copia = tmp / POST
        copia.parent.mkdir(parents=True)
        shutil.copy2(real, copia)
        _correr("generate_blog_tablas.py", "--write", "--blog", str(tmp))
        t = copia.read_text(encoding="utf-8")
        bloque = _re.search(r"<!-- AUTO-TOP10-START -->.*?<!-- AUTO-TOP10-END -->", t, _re.S).group()
        if "| ≈ |" not in bloque or "**" in bloque:
            raise AssertionError("control: la tabla regenerada corona (sin «≈» o con negritas)")
        if _correr("generate_blog_tablas.py", "--check", "--blog", str(tmp)) != 0:
            raise AssertionError("control: recién regenerada y el --check da rojo")
        fila = _re.search(r"^\| ≈ \| ([^|]+) \|", bloque, _re.M)
        podio = bloque.replace(fila.group(0), f"| 1 | **{fila.group(1).strip()}** |", 1)
        copia.write_text(t.replace(bloque, podio), encoding="utf-8")
        return _correr("generate_blog_tablas.py", "--check", "--blog", str(tmp)) != 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@prueba("check_ganadores G6", "una comparación con versión que corona a un modelo que su título no nombra")
def _t_ganadores_g6():
    # 8-nov-2026: /fable-5-vs-opus-4-8/ coronaba a Fable 5.1 porque el lado se elegía por
    # familia (`match: ["fable"]`). Saboteo 1: se regenera esa página con el lado por
    # familia, como era. Saboteo 2: a una foto histórica se le agrega un ganador de pilar.
    # Control en verde primero, y las páginas se restauran pase lo que pase.
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import generate_comparison as gc
    slug, foto = "fable-5-vs-opus-4-8", "gpt-5.6-terra-vs-sol"
    pagina, pagina_foto = ROOT / "docs" / slug / "index.html", ROOT / "docs" / foto / "index.html"
    original, original_foto = pagina.read_text(encoding="utf-8"), pagina_foto.read_text(encoding="utf-8")
    try:
        if _correr("check_ganadores.py") != 0:
            raise AssertionError("check_ganadores ya está en rojo: el saboteo no probaría nada")
        cfg = dict(next(c for c in gc.COMPARISONS if c["slug"] == slug))
        cfg["a"] = {"name": cfg["a"]["name"], "familia": "claude"}      # por familia, como era antes
        ms = gc.load_models()
        A, B = gc.family(ms, cfg["a"]), gc.family(ms, cfg["b"])
        if not any(m["name"] == "Claude Fable 5.1" for m in A):
            raise AssertionError("el lado por familia ya no trae a Fable 5.1: el saboteo no reproduce el bug")
        pagina.write_text(gc.render(cfg, A, B), encoding="utf-8")
        if _correr("check_ganadores.py") == 0:
            return False
        pagina.write_text(original, encoding="utf-8")
        roto = original_foto.replace(
            "<h2>Preguntas frecuentes</h2>",
            "<p>En calidad pura de este pilar gana <strong>GPT-5.6 Sol</strong> claramente.</p>"
            "\n  <h2>Preguntas frecuentes</h2>", 1)
        if roto == original_foto:
            raise AssertionError("la foto ya no tiene FAQ: el saboteo no tocaría nada")
        pagina_foto.write_text(roto, encoding="utf-8")
        return _correr("check_ganadores.py") != 0
    finally:
        pagina.write_text(original, encoding="utf-8")
        pagina_foto.write_text(original_foto, encoding="utf-8")


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
        # Vacía el motivo de `test_guardrails.py`: una exención sin porqué. (Hasta el 9-nov era
        # la de `test_unitarios.py`, que salió de la lista: `_t_error_del_proveedor` la prueba.)
        roto = _re.sub(r'("test_guardrails\.py":\s*)\n?\s*"[^"]*"\s*\n?\s*"[^"]*"', r'\1""', t, count=1)
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


@prueba("check_specs --empuje", "un push a main que lleva un change activo, aunque salga de otra rama, y un push sin refs (S1)")
def _t_specs_empuje_a_main():
    # 11-nov-2026. El release v6.1.0 se empujó con `HEAD:main` desde `ventana/v6-1` y llevó a
    # main un change activo: S1 miraba el nombre de la rama local. Repo DESECHABLE y variables
    # GIT_* fuera del entorno (memoria: dentro de un hook, git hereda GIT_DIR y la prueba
    # reconfiguraría el repo real).
    import tempfile as _tf
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t",
               GIT_COMMITTER_EMAIL="t@t")
    d = Path(_tf.mkdtemp())
    try:
        g = lambda *a: subprocess.run(["git", *a], cwd=d, env=env, capture_output=True,
                                      text=True, check=True).stdout.strip()
        g("init", "-q")
        (d / "openspec" / "changes" / "archive" / "2026-11-01-viejo").mkdir(parents=True)
        (d / "openspec" / "changes" / "archive" / "2026-11-01-viejo" / "tasks.md").write_text("- [x] 1\n")
        g("add", "-A"); g("commit", "-qm", "limpio")
        limpio = g("rev-parse", "HEAD")
        (d / "openspec" / "changes" / "corte-x").mkdir()
        (d / "openspec" / "changes" / "corte-x" / "tasks.md").write_text("- [ ] 1\n")
        g("add", "-A"); g("commit", "-qm", "activo")
        activo = g("rev-parse", "HEAD")

        def empuje(linea: str) -> int:
            return subprocess.run([PY, str(ROOT / "benchmarks" / "check_specs.py"), "--empuje",
                                   "--repo", str(d)], input=linea + "\n", cwd=ROOT, env=env,
                                  capture_output=True, text=True).returncode
        cero = "0" * 40
        # controles: main limpio pasa; el activo a otra rama pasa; un borrado no manda nada
        if empuje(f"refs/heads/v {limpio} refs/heads/main {cero}") != 0:
            return False
        if empuje(f"refs/heads/v {activo} refs/heads/corte/x {cero}") != 0:
            return False
        if empuje(f"(delete) {cero} refs/heads/main {limpio}") != 0:
            return False
        # el fallo: el commit con un change activo va a main desde otra rama
        if empuje(f"refs/heads/ventana {activo} refs/heads/main {limpio}") == 0:
            return False
        # 11-nov-2026: un push sin refs (o con líneas que no son refs) es un push que S1 no vio
        if empuje("") == 0 or empuje("   ") == 0:
            return False
    finally:
        shutil.rmtree(d, ignore_errors=True)
    # y el hook que se instala lo corre ANTES del QA (si alguien lo saca, esto cae)
    from benchmarks import instalar_hooks as ih
    h = ih.HOOK
    # y lee la entrada completa antes que nada, y se la pasa a S1
    return ("check_specs.py\" --empuje || exit 1" in h and h.index("--empuje") < h.index("qa.py")
            and 'REFS="$(cat)"' in h and h.index('REFS="$(cat)"') < h.index("--empuje")
            and 'printf \'%s\\n\' "$REFS" |' in h)


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


# ── check_indice_calidad: la nota v6 tiene una definición (9-nov-2026) ──────────────
@prueba("check_indice_calidad", "una nota recalculada con otro peso, una cifra del grupo a mano, "
        "un sin dato agéntico en un orden por la nota, un tier que es ruta")
def _t_indice_calidad():
    import copy
    sys.path.insert(0, str(ROOT))
    from benchmarks import check_indice_calidad as ci
    data, readme, html, fuentes, paginas = ci.leer_todo()
    # control: con el árbol real, verde (y leyendo datos de verdad)
    if ci.revisar(data, readme, html, fuentes, paginas):
        return False
    if not any(m.get("score_calidad") is not None for m in data["models"]):
        return False
    rk = [m for m in data["models"] if m.get("ranked")]
    sin = [m for m in data["models"] if (m.get("agentico") or {}).get("sin_dato")]
    if not rk:
        return False
    if not sin:
        # 10-nov-2026: desde la v6.1 ningún modelo tiene «sin dato agéntico» (GPT-OSS, los únicos,
        # se midieron por DekaLLM). I5 se sabotea sobre una copia con uno sintético, no real.
        data = copy.deepcopy(data)
        x = next(m for m in data["models"] if not m.get("ranked") and m.get("score_calidad") is None)
        x["agentico"] = {**(x.get("agentico") or {}), "sin_dato": "formato_endpoint"}
        if ci.i5_sin_dato(data, readme, {}):
            return False  # control del sintético: sin rankear ni nota, tiene que dar verde
        sin = [x]
    # De punta a punta, por el script real que corre qa.py: control verde y un README con el
    # N del grupo escrito a mano (el fallo más probable al editar texto) tiene que salir rojo.
    if _correr("check_indice_calidad.py") != 0:
        return False
    with Sabotaje(ROOT / "README.md"):
        r = ROOT / "README.md"
        t = r.read_text(encoding="utf-8")
        roto = re.sub(r"no separa a estos (\*{0,2})(\d+)",
                      lambda x: f"no separa a estos {x[1]}{int(x[2]) + 1}", t, count=1)
        if roto == t:
            raise AssertionError("el README no tiene la línea del grupo: el sabotaje no tocaría nada")
        r.write_text(roto, encoding="utf-8")
        if _correr("check_indice_calidad.py") == 0:
            return False
    casos = []
    # I1: una nota publicada que no sale de la fórmula (otro peso)
    d = copy.deepcopy(data); m = next(x for x in d["models"] if x.get("ranked"))
    m["score_calidad"] = round(0.5 * m["quality_avg"] + 0.5 * m["nota_harbor"], 2)
    casos.append(ci.i1_nota(d["models"]))
    # I2: app.js combina examen y Harbor por su cuenta, y un generador define el peso
    f = dict(fuentes); f["docs/app.js"] += "\nconst q = 0.8 * m.quality_avg + 0.2 * m.nota_harbor;\n"
    casos.append(ci.i2_peso_unico(f))
    f = dict(fuentes); f["benchmarks/generate_rankings.py"] += "\nPESO_HARBOR_EN_CALIDAD = 0.3\n"
    casos.append(ci.i2_peso_unico(f))
    # I3: el HTML estático con otro peso
    casos.append(ci.i3_html(data, html.replace('class="peso-harbor">25<', 'class="peso-harbor">30<')))
    # I4: el README con un N escrito a mano, y un más barato que no es el más barato
    casos.append(ci.i4_grupo(data, re.sub(r"no separa a estos (\d+) de",
                                          lambda x: f"no separa a estos {int(x[1]) + 1} de", readme)))
    d = copy.deepcopy(data); d["grupo_cabeza"]["mas_barato"] = {"key": d["grupo_cabeza"]["claves"][0], "name": "x"}
    casos.append(ci.i4_grupo(d, readme))
    # I5: un sin dato agéntico que rankea, y otro listado en una tabla «Calidad»
    d = copy.deepcopy(data); x = next(y for y in d["models"] if y["key"] == sin[0]["key"])
    x["ranked"], x["score_calidad"] = True, 8.0
    casos.append(ci.i5_sin_dato(d, readme, {}))
    pag = {"docs/x/index.html": ('<table><tr><th scope="col">Calidad</th></tr>'
                                 f'<tr><td><a href="/modelo/{sin[0]["key"]}/">x</a></td></tr></table>')}
    casos.append(ci.i5_sin_dato(data, readme, pag))
    # I6: un tier que es una ruta
    d = copy.deepcopy(data); d["models"][0]["tier"] = "cloud_nim"
    casos.append(ci.i6_tier(d))
    # I7: control verde con lo real; después, sobre una tarea sintética que ES la versión
    # de la regla, un check excluido con errata y un total distinto; resultados.json con otra
    # lista; y la versión publicada cambiada (la corregida ya se midió: la regla tiene que irse)
    from benchmarks import indice as ix
    tests, res, disco = ci.leer_harbor()
    if not ix.CHECKS_SIN_CONTAR or ci.i7_checks_sin_contar(ix.CHECKS_SIN_CONTAR, tests, res, disco):
        return False
    t0 = next(iter(ix.CHECKS_SIN_CONTAR)); r0 = ix.CHECKS_SIN_CONTAR[t0]
    otros = [f"test_otro_{i}" for i in range(r0["de"] - len(r0["checks"]))]
    src0 = "\n".join(f"def {c}():\n    pass\n" for c in [*r0["checks"], *otros])
    tests0, disco0 = {**tests, t0: src0}, {**disco, t0: r0["checksum"]}
    if ci.i7_checks_sin_contar(ix.CHECKS_SIN_CONTAR, tests0, res, disco0):
        return False                       # control de la tarea sintética: tiene que dar verde
    errata = {**ix.CHECKS_SIN_CONTAR, t0: {**r0, "checks": {**r0["checks"], "test_que_no_existe": "x"}}}
    casos.append(ci.i7_checks_sin_contar(errata, tests0, res, disco0))
    casos.append(ci.i7_checks_sin_contar({**ix.CHECKS_SIN_CONTAR, t0: {**r0, "de": r0["de"] + 1}},
                                         tests0, res, disco0))
    r2 = copy.deepcopy(res); r2["tareas"][t0]["checks_sin_contar"] = []
    casos.append(ci.i7_checks_sin_contar(ix.CHECKS_SIN_CONTAR, tests, r2, disco))
    r3 = copy.deepcopy(res); r3["tareas"][t0]["task_checksum"] = "0" * 64
    casos.append(ci.i7_checks_sin_contar(ix.CHECKS_SIN_CONTAR, tests, r3, disco))
    # I8: control verde; una ficha sin la línea, la calculadora sin su hueco, y la línea
    # publicada a mano (distinta de la que arma indice.py)
    fichas = ci.leer_fichas()
    if ci.i8_linea_checks(data, html, fuentes["docs/app.js"], fichas):
        return False
    k8 = next(m["key"] for m in data["models"] if m.get("nota_harbor") is not None and m["key"] in fichas)
    f8 = dict(fichas); f8[k8] = re.sub(r'<p class="ficha-fuente nota-checks">.*?</p>', "", f8[k8], flags=re.S)
    casos.append(ci.i8_linea_checks(data, html, fuentes["docs/app.js"], f8))
    casos.append(ci.i8_linea_checks(data, html.replace('id="nota-checks"', 'id="otra"'), fuentes["docs/app.js"], fichas))
    d = copy.deepcopy(data); d["indice_calidad"]["linea_checks"] = "Algunos checks no cuentan."
    casos.append(ci.i8_linea_checks(d, html, fuentes["docs/app.js"], fichas))
    # y de punta a punta: resultados.json sin la lista publicada tiene que dejar rojo el script
    with Sabotaje(ROOT / "tareas-agente" / "resultados.json"):
        rp = ROOT / "tareas-agente" / "resultados.json"
        rp.write_text(json.dumps(r2, ensure_ascii=False), encoding="utf-8")
        if _correr("check_indice_calidad.py") == 0:
            return False
    return all(bool(c) for c in casos)


def main() -> int:
    print("Probando que cada guardrail CACE su propio fallo:\n")
    lineas, code = resumen(resultados)
    print("\n".join(lineas))
    return code



@prueba("export_harbor · error_del_proveedor",
        "la firma lee los logs del entorno (el 429 de Postmark de incidente), una tarea sin dato "
        "entra como 0, los reintentos no tienen tope, o validate_suite cuenta un error como respuesta")
def _t_error_del_proveedor():
    # 9-nov-2026 (Cristian). Dos condiciones, dos sabotajes, con control verde antes de cada uno.
    pyc = tempfile.mkdtemp()   # bytecode aparte: un sabotaje del mismo tamaño no reusa el .pyc viejo

    def pytest_rc(filtro: str) -> int:
        return subprocess.run([PY, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                               str(ROOT / "benchmarks" / "test_unitarios.py"), "-k", filtro],
                              cwd=ROOT, capture_output=True, text=True,
                              env={**os.environ, "PYTHONPYCACHEPREFIX": pyc}).returncode

    k1, k2 = "error_del_proveedor_lee_solo", "sin_dato_del_proveedor_no_entra"
    if pytest_rc(k1) != 0 or pytest_rc(k2) != 0:
        return False   # control: las dos tienen que estar en verde antes de romper
    eh = ROOT / "benchmarks" / "export_harbor.py"
    with Sabotaje(eh):
        t = eh.read_text(encoding="utf-8")
        # La firma ingenua: busca el nombre de la excepción o el código en TODA la trayectoria,
        # que incluye la salida de los comandos del entorno.
        roto = t.replace(
            "    status, texto = salida_del_agente(trayectoria)\n    if status in TRANSITORIOS:",
            "    status, texto = salida_del_agente(trayectoria)\n"
            "    if any(x in trayectoria for x in TRANSITORIOS) or _CODIGO_PROVEEDOR.search(trayectoria):\n"
            "        return \"leído de la traza\"\n    if status in TRANSITORIOS:", 1)
        if roto == t:
            raise AssertionError("error_del_proveedor cambió de forma: el sabotaje no tocaría nada")
        eh.write_text(roto, encoding="utf-8")
        if pytest_rc(k1) == 0:
            return False
    ef = ROOT / "benchmarks" / "export_for_pages.py"
    with Sabotaje(ef):
        t = ef.read_text(encoding="utf-8")
        roto = t.replace('if fila.get("estado") == "sin_dato_proveedor":\n                        continue',
                         'if False:\n                        continue', 1)
        if roto == t:
            raise AssertionError("_cargar_agentico cambió de forma: el sabotaje no tocaría nada")
        ef.write_text(roto, encoding="utf-8")
        if pytest_rc(k2) == 0:
            return False
    k3 = "lote_harbor_repite"
    if pytest_rc(k3) != 0:
        return False
    lh = ROOT / "benchmarks" / "lote_harbor.py"
    with Sabotaje(lh):
        t = lh.read_text(encoding="utf-8")
        roto = t.replace("while validos < k and ultimos and ronda < tope:",
                         "while validos < k and ultimos:", 1)   # sin tope
        if roto == t:
            raise AssertionError("lote_harbor cambió de forma: el sabotaje no tocaría nada")
        lh.write_text(roto, encoding="utf-8")
        if pytest_rc(k3) == 0:
            return False
    # 10-nov-2026: lo que tumbó la infraestructura se repone; la clave no va en los argumentos.
    k5 = "lote_harbor_repone_lo_que_tumbo"
    k6 = "lote_harbor_no_pone_la_clave"
    if pytest_rc(k5) != 0 or pytest_rc(k6) != 0:
        return False
    for k, viejo, nuevo in (
            (k5, "repetidos, ronda, ultimos = 0, 0, cortados + infra",
             "repetidos, ronda, ultimos = 0, 0, cortados"),                  # no repone la infra
            (k6, '"-o", str(jobs), "--job-name", job, "-q"],',
             '"-o", str(jobs), "--job-name", job, "-q", "--agent-env", f"OPENROUTER_API_KEY={clave}"],')):
        with Sabotaje(lh):
            t = lh.read_text(encoding="utf-8")
            roto = t.replace(viejo, nuevo, 1)
            if roto == t:
                raise AssertionError("lote_harbor cambió de forma: el sabotaje no tocaría nada")
            lh.write_text(roto, encoding="utf-8")
            if pytest_rc(k) == 0:
                return False
    k4 = "validate_suite_no_cuenta_los_errores"
    if pytest_rc(k4) != 0:
        return False
    vs = ROOT / "benchmarks" / "validate_suite.py"
    with Sabotaje(vs):
        t = vs.read_text(encoding="utf-8")
        roto = t.replace('if r.get("success") and r.get("quality") is not None]',
                         'if r.get("quality") is not None]', 1)   # vuelve a contar los errores
        if roto == t:
            raise AssertionError("runs_validos cambió de forma: el sabotaje no tocaría nada")
        vs.write_text(roto, encoding="utf-8")
        if pytest_rc(k4) == 0:
            return False
    return all(pytest_rc(k) == 0 for k in (k1, k2, k3, k4))   # restaurado: verde otra vez

if __name__ == "__main__":
    sys.exit(main())
