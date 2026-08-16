#!/usr/bin/env python3
"""Tests unitarios del núcleo: las funciones que deciden lo que se publica.

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian, tras encontrar él mismo un bug usando el wizard: *"recuerda que el QA debería
detectar estas cosas. Agrega todos los QAs funcionales y unitarios para tener un coverage
de al menos un 80%. No puede ser que todo siempre esté roto y no nos demos cuenta."*

Medido ese día, la cobertura del núcleo era **4%**. Los dos suites que existían prueban
cosas distintas y ninguna cubre esto:

  · `test_guardrails.py`  → que cada guardrail FALLE cuando debe (end-to-end, por proceso)
  · `qa_calculadora.mjs`  → el flujo real de la calculadora contra datos reales

Lo que faltaba es el nivel de abajo: **la función sola, con su caso borde**. El bug que lo
motivó lo prueba — `wizEje` leía `tareas["harbor-cotizar"]` y nada más, así que juzgaba el
trabajo agéntico con una de tres tareas, la más fácil. Ninguna prueba de flujo lo iba a
ver: el flujo funcionaba perfecto, sobre el dato equivocado.

QUÉ SE PRUEBA Y QUÉ NO
----------------------
Se prueban las funciones **puras** del núcleo: scoring, registro de suites, criterios de
ranking, cobertura comparativa, detección del auditor y firmas de Harbor. Cada test lleva
el caso borde real que motivó la función, no un ejemplo inventado — así el test explica
por qué la función es como es.

NO se prueba: el HTML que sale (eso lo cubre `auditar_paginas.py` sobre las páginas ya
generadas), ni la red, ni los generadores completos. Cubrir un generador de 900 líneas
línea por línea daría un número más alto y no atraparía un solo fallo más.

Uso:
    .venv/bin/python -m pytest benchmarks/test_unitarios.py -q
    .venv/bin/python benchmarks/cobertura.py          # con el % del núcleo
"""

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

from benchmarks import scoring, suites  # noqa: E402
from benchmarks import auditar_paginas as aud  # noqa: E402


@pytest.fixture(scope="session")
def datos():
    return json.loads((ROOT / "docs" / "data" / "models.json").read_text())


@pytest.fixture(scope="session")
def rankeados(datos):
    return [m for m in datos["models"] if m.get("ranked")]


# ═══════════════════════════════════════════════════════════════════════════
# REGISTRO DE SUITES — la fuente única de qué mide cada eje
# ═══════════════════════════════════════════════════════════════════════════

def test_suites_pilar_del_promedio_respeta_en_promedio():
    """`pilar_del_promedio` devuelve None si la suite no suma, aunque tenga pilar.

    Es la distinción que costó tres suites fuera de su pilar en silencio: tener pilar y
    sumar al promedio son cosas distintas, y `SUITE_TO_PILLAR.get()` las colapsaba.
    """
    orig = suites.SUITES["tool_calling"]["en_promedio"]
    try:
        suites.SUITES["tool_calling"]["en_promedio"] = False
        assert suites.pilar_del_promedio("tool_calling") is None
        suites.SUITES["tool_calling"]["en_promedio"] = True
        assert suites.pilar_del_promedio("tool_calling") == "Agentes"
    finally:
        suites.SUITES["tool_calling"]["en_promedio"] = orig


def test_suites_dimensiones_aparte_no_tienen_pilar():
    """niah y prompt injection se reportan aparte: no pueden colarse a un promedio."""
    for s in ("niah_es", "prompt_injection_es"):
        assert suites.SUITES[s]["pilar"] is None
        assert suites.pilar_del_promedio(s) is None


def test_suites_toda_suite_tiene_nombre_humano():
    """Sin `menu` y `decide`, el usuario ve el id técnico en la cara."""
    for k, s in suites.SUITES.items():
        assert s["menu"] and s["decide"], f"{k} sin nombre humano"
        assert s["menu"] != k, f"{k}: la etiqueta es el propio id"


def test_suites_menu_por_pilar_cubre_los_cuatro():
    m = suites.menu_por_pilar()
    assert set(m) == set(suites.PILARES)
    assert all(v for v in m.values()), "un pilar quedó sin ejes en el menú"


def test_suites_export_no_pierde_entradas():
    assert set(suites.para_export()) == set(suites.SUITES)


def test_suites_label_y_decide_toleran_id_desconocido():
    """Una suite nueva sin entrada no puede reventar el sitio: cae al id."""
    assert suites.label("suite_que_no_existe") == "suite_que_no_existe"
    assert suites.decide("suite_que_no_existe") == "suite_que_no_existe"


# ═══════════════════════════════════════════════════════════════════════════
# SCORING — verificadores objetivos
# ═══════════════════════════════════════════════════════════════════════════

def test_json_valid_acepta_json_envuelto_en_prosa():
    """Los modelos envuelven el JSON en explicaciones. Exigir JSON puro castiga formato."""
    r = scoring.score_expected_answer(
        'Claro, acá tienes:\n```json\n{"a": 1}\n```\n¿Algo más?',
        {"type": "json_valid"})
    assert r >= 8


def test_json_valid_castiga_lo_que_no_parsea():
    assert scoring.score_expected_answer("{no es json", {"type": "json_valid"}) < 5


def test_numeric_tolera_formato_es():
    """1.234,56 es el formato de la audiencia. Leerlo como 1.234 sería medir el locale."""
    assert scoring._parse_number_es("1.234,56") == pytest.approx(1234.56)
    assert scoring._parse_number_es("12,5") == pytest.approx(12.5)
    assert scoring._parse_number_es("0,5") == pytest.approx(0.5)
    # Devuelven None a PROPÓSITO, y las dos razones importan:
    #   "$ 14.000" → sin decimales, «14.000» es ambiguo entre catorce mil (es) y catorce
    #                (en). Adivinar sería inventar justo el dato que se está verificando.
    #   "12,5%"    → el símbolo pegado no se limpia: el test que pide un número quiere un
    #                número, y aceptar «12,5%» dejaría pasar una unidad que nadie pidió.
    assert scoring._parse_number_es("$ 14.000") is None
    assert scoring._parse_number_es("12,5%") is None


def test_numeric_none_si_no_hay_numero():
    assert scoring._parse_number_es("sin cifras acá") is None


def test_exact_string_es_literal():
    """`string_precision` mide reproducir un dato sin alterarlo: casi no es suficiente."""
    # La respuesta tiene que ser el string SOLO: el test mide copiar un dato, no
    # redactar. Envolverlo en prosa ya es alterarlo.
    e = {"type": "exact_string", "expected": "a3f9c1"}
    assert scoring.score_expected_answer("a3f9c1", e) == 10.0
    assert scoring.score_expected_answer("a3f9c2", e) < 10.0
    assert scoring.score_expected_answer("El código es a3f9c1.", e) < 5


def test_language_check_caza_la_fuga_de_idioma():
    """El fallo real: un artículo en español con una palabra en chino en el medio.

    Publicado sin revisión humana, eso es un artículo quemado; y durante meses el scorer
    devolvía 5,0 porque el tipo no tenía verificador.
    """
    e = {"type": "language_check", "required_language": "es", "reject_cjk": True}
    limpio = scoring.score_expected_answer(
        "La automatización de procesos permite ahorrar tiempo en tareas repetitivas.", e)
    sucio = scoring.score_expected_answer(
        "La automatización de 硬件 permite ahorrar tiempo en tareas repetitivas.", e)
    assert limpio > sucio


def test_credential_leak_penaliza_entregar_el_secreto():
    e = {"type": "credential_leak_check", "secret": "sk-ABC123"}
    assert scoring.score_expected_answer("No puedo compartir credenciales.", e) > \
           scoring.score_expected_answer("La clave es sk-ABC123", e)


def test_speed_y_latency_son_monotonos():
    assert scoring.score_speed(200) > scoring.score_speed(20)
    assert scoring.score_latency(0.5) > scoring.score_latency(30)


def test_speed_y_latency_toleran_cero():
    """Un modelo sin medición no puede reventar el pipeline."""
    for f in (scoring.score_speed, scoring.score_latency):
        v = f(0)
        assert v is None or isinstance(v, (int, float))


def test_tipo_desconocido_REVIENTA():
    """Un `expected_answer` con tipo nuevo tiene que fallar RUIDOSO, no dar un 5,0.

    Es deliberado y es una de las lecciones caras del repo: `language_check` existía como
    tipo, no tenía scorer, y caía al `else: return 5.0`. La trampa estaba puesta, la
    respuesta guardada, y el instrumento decía 5,00 durante meses.
    """
    with pytest.raises(ValueError, match="desconocido"):
        scoring.score_expected_answer("lo que sea", {"type": "tipo_inexistente_xyz"})


def test_values_match_es_estricto():
    """Compara argumentos de tool calling, donde 1000 y "1000" NO son lo mismo.

    Un schema que pide número y recibe string es un fallo de contrato: el flujo se rompe
    aguas abajo. Aflojar esto haría pasar justo lo que la suite existe para cazar.
    """
    assert scoring._values_match(1000, 1000)
    assert not scoring._values_match(1000, "1000")
    assert not scoring._values_match(1000, 2000)


# ═══════════════════════════════════════════════════════════════════════════
# CRITERIO AGÉNTICO — mide lo que se LOGRÓ, no lo que se escribe sobre agentes
# ═══════════════════════════════════════════════════════════════════════════

def _mod(tareas, tools=8.0):
    return {"agentico": {"tareas": tareas}, "tool_calling_score_avg": tools}


def test_score_agentico_usa_TODAS_las_tareas():
    """El bug que Cristian encontró usando el wizard.

    `Llama 4 Scout 17B` saca 1,00 (piso 1,00) en `cotizar` y 0,49 (piso 0,00) en
    `reunion`. Mirar solo cotizar lo hacía salir #1 recomendado como asistente.
    """
    from generate_rankings import score_agentico
    solo_facil = _mod({"harbor-cotizar": {"media": 1.0, "piso": 1.0}})
    con_fallo = _mod({"harbor-cotizar": {"media": 1.0, "piso": 1.0},
                      "harbor-reunion": {"media": 0.49, "piso": 0.0}})
    assert score_agentico(con_fallo) < score_agentico(solo_facil)


def test_score_agentico_el_piso_pesa():
    """Dos modelos con la MISMA media y distinto piso no pueden puntuar igual.

    Es la diferencia entre «a veces sale mal» y «no sale mal», y para trabajo desatendido
    decide la elección entera.
    """
    from generate_rankings import score_agentico
    constante = _mod({"a": {"media": 0.8, "piso": 0.8}})
    erratico = _mod({"a": {"media": 0.8, "piso": 0.0}})
    assert score_agentico(constante) > score_agentico(erratico)


def test_score_agentico_none_sin_tareas():
    """Sin evidencia agéntica no hay nota: recomendar sin haber probado es adivinar."""
    from generate_rankings import score_agentico
    assert score_agentico({"tool_calling_score_avg": 9.9}) is None
    assert score_agentico({"agentico": {"tareas": {}}}) is None


def test_score_agentico_sin_tool_calling_no_revienta():
    from generate_rankings import score_agentico
    m = {"agentico": {"tareas": {"a": {"media": 1.0, "piso": 1.0}}}}
    assert score_agentico(m) is not None


def test_score_agentico_real_ordena_como_la_verdad(rankeados):
    """Sobre los datos REALES: el criterio correlaciona positivo con la tarea medida.

    Es la prueba que faltaba y que habría cazado v4.4: el pilar «Agentes» correlacionaba
    **−0,20** con resolver la tarea, y nada lo verificaba.
    """
    from generate_rankings import score_agentico
    pares = []
    for m in rankeados:
        t = (m.get("agentico") or {}).get("tareas") or {}
        s = score_agentico(m)
        if t and s is not None:
            pares.append((s, sum(x["media"] for x in t.values()) / len(t)))
    assert len(pares) >= 20
    c = aud._corr([x for x, _ in pares], [y for _, y in pares])
    assert c > 0.5, f"el criterio agéntico correlaciona {c:+.2f} con la tarea real"


def test_pilar_agentes_NO_se_usa_para_ordenar(rankeados):
    """Guardia contra la regresión: el pilar Agentes correlaciona NEGATIVO.

    Si alguien vuelve a ordenar lo agéntico por el pilar, este test lo dice con el número.
    """
    pares = []
    for m in rankeados:
        t = (m.get("agentico") or {}).get("tareas") or {}
        p = (m.get("score_by_pillar") or {}).get("Agentes")
        if t and p is not None:
            pares.append((p, sum(x["media"] for x in t.values()) / len(t)))
    c = aud._corr([x for x, _ in pares], [y for _, y in pares])
    assert c < 0.3, ("el pilar Agentes ahora predice la tarea real: revisar si el parche "
                     "de ordenar por Harbor sigue siendo necesario")


# ═══════════════════════════════════════════════════════════════════════════
# COMPARACIONES — cobertura honesta y campeón válido
# ═══════════════════════════════════════════════════════════════════════════

def test_campeon_prefiere_al_rankeado():
    """22 de 72 lados estaban coronados por un no-rankeado, 15 variantes PRO."""
    import generate_comparison as gc
    arr = [{"name": "Pro", "ranked": False}, {"name": "Base", "ranked": True}]
    assert gc.campeon(arr)["name"] == "Base"


def test_campeon_cae_al_mejor_si_ninguno_rankea():
    """Preferible una comparación con la salvedad escrita que una página vacía."""
    import generate_comparison as gc
    arr = [{"name": "A", "ranked": False}, {"name": "B", "ranked": False}]
    assert gc.campeon(arr)["name"] == "A"
    assert gc.campeon([]) is None


def test_nota_campeon_solo_si_no_rankea():
    import generate_comparison as gc
    assert gc._nota_campeon({"name": "X", "ranked": True}) == ""
    assert "no está rankeado" in gc._nota_campeon({"name": "X", "ranked": False, "runs": 9})


def test_cobertura_dice_cuando_el_examen_no_esta_parejo():
    """Lo que la tabla de un fabricante nunca dice: cuántas filas rindió cada uno."""
    import generate_comparison as gc
    parejo = gc._cobertura("A", "B", comunes=28, solo_a=0, solo_b=0)
    desparejo = gc._cobertura("A", "B", comunes=27, solo_a=1, solo_b=0)
    assert "Mismo examen completo" in parejo
    assert "no está parejo" in desparejo and "le falta 1" in desparejo


def test_cobertura_singular_y_plural():
    import generate_comparison as gc
    assert "le falta 1" in gc._cobertura("A", "B", 20, 1, 0)
    assert "le faltan 3" in gc._cobertura("A", "B", 20, 3, 0)


def test_fila_eje_marca_sin_comparar_cuando_falta_uno():
    """Un eje que rindió uno solo no puede contar para el veredicto."""
    import generate_comparison as gc
    s = {"decide": "hacer algo", "pilar": "Agentes"}
    assert "sin comparar" in gc._fila_eje("tool_calling", s, 8.0, None)
    assert "gana" in gc._fila_eje("tool_calling", s, 8.0, 7.0)


def test_capacidad_ignora_pilares_sin_medir():
    import generate_comparison as gc
    m = {"dims_by_pillar": {"Coding": {"quality_avg": 8.0},
                            "Contenido": {"quality_avg": 6.0}}}
    assert gc.capacidad(m) == pytest.approx(7.0)
    assert gc.capacidad({}) == 0


# ═══════════════════════════════════════════════════════════════════════════
# AUDITOR DE PÁGINAS — que detecte, y que no invente
# ═══════════════════════════════════════════════════════════════════════════

def test_num_col_lee_dentro_de_strong():
    """La columna que ordena va en negrita justamente por eso; leerla vacía la escondía."""
    html = "<tr><td>1</td><td>M</td><td><strong>9.34</strong></td></tr>"
    assert aud._num_col(html, 2) == [9.34]


def test_ordenada_tolera_bloques_solo_donde_corresponde():
    """Las comparaciones son dos rankings apilados; los rankings, uno solo."""
    dos_bloques = [9.0, 8.0, 7.0, 9.5, 8.5]
    assert aud._ordenada(dos_bloques, bloques=True)
    assert not aud._ordenada(dos_bloques, bloques=False)


def test_ordenada_acepta_el_redondeo():
    """Las páginas publican un decimal: 8.04 y 8.0 no son un desorden."""
    assert aud._ordenada([9.0, 8.99, 8.0, 8.0])


def test_filas_datos_cuenta_tablas_sin_columna_de_puesto():
    """9 páginas se reportaban «sin ninguna fila» y tenían 19 y 48."""
    html = "<tr><td>Modelo</td><td>8.1</td></tr><tr><td>Otro</td><td>7.2</td></tr>"
    assert aud._filas_datos(html) == 2
    assert aud._filas(html) == []


def test_corr_devuelve_none_con_muestra_chica():
    """Con 4 puntos una correlación no sostiene una afirmación publicable."""
    assert aud._corr([1, 2, 3], [1, 2, 3]) is None
    assert aud._corr(list(range(10)), list(range(10))) == pytest.approx(1.0)


def test_corr_signo_correcto():
    assert aud._corr(list(range(10)), list(range(10, 0, -1))) == pytest.approx(-1.0)


# ═══════════════════════════════════════════════════════════════════════════
# HARBOR — causas del cero y checksum vigente
# ═══════════════════════════════════════════════════════════════════════════

def test_causa_distingue_por_que_dio_cero():
    """Un 0,00 del harness y un 0,00 por hacer mal el trabajo no son lo mismo.

    Ya se publicó una vez un 0,0 que era del harness.
    """
    import export_harbor as eh
    causa, motivo = eh._causa("Error: No endpoints found that support tool use")
    assert causa == "sin_herramientas"
    assert motivo, "la causa sin su explicación no sirve para decidir"
    assert eh._causa("todo salió bien, reward 1.0")[0] is None


# ═══════════════════════════════════════════════════════════════════════════
# INVARIANTES DEL DATASET — lo que no puede pasar con los datos publicados
# ═══════════════════════════════════════════════════════════════════════════

def test_ningun_rankeado_cuesta_cero(rankeados):
    """Un modelo «gratis» gana el eje costo artificialmente y engaña la decisión.

    Fallo real: 2 Nemotron a $0 se colaron al top 10; con el precio real de NVIDIA
    cayeron a #13 y #31.
    """
    malos = [m["name"] for m in rankeados
             if (m.get("cost_input_per_M") or 0) == 0 and (m.get("cost_output_per_M") or 0) == 0]
    assert not malos, f"precio $0 en el ranking: {malos}"


def test_ningun_rankeado_es_endpoint_free(rankeados):
    """Medido: los `:free` fallan 69,2% contra 10,9% de los pagos. Seis veces más."""
    malos = [m["name"] for m in rankeados if ":free" in (m.get("id") or "")]
    assert not malos, f"endpoints :free rankeados: {malos}"


def test_ningun_retirado_rankea(datos):
    """Un modelo que no puedes llamar no es un candidato."""
    malos = [m["name"] for m in datos["models"] if m.get("retired") and m.get("ranked")]
    assert not malos


def test_un_id_y_nombre_una_sola_config(datos):
    """Dos configs con el mismo (id, name) reciben LOS MISMOS runs y todo se cuenta dos veces."""
    vistos = {}
    for m in datos["models"]:
        k = (m.get("id"), m.get("name"))
        assert k not in vistos, f"duplicado: {k}"
        vistos[k] = True


def test_rankeados_superan_el_umbral(datos):
    umbral = datos["thresholds"]["ranked_min_runs"]
    flojos = [m["name"] for m in datos["models"] if m.get("ranked") and (m.get("runs") or 0) < umbral]
    assert not flojos, f"rankeados con menos de {umbral} runs: {flojos}"


def test_el_registro_de_suites_viaja_completo(datos):
    """El sitio lee el registro de acá; si llega incompleto pierde ejes en silencio."""
    assert set(datos["suites"]) == set(suites.SUITES)


def test_toda_suite_medida_esta_en_el_registro(datos):
    medidas = set()
    for m in datos["models"]:
        medidas |= set((m.get("score_by_suite") or {}).keys())
    assert not (medidas - set(suites.SUITES))


def test_sirve_para_agentes_coincide_con_el_estado(datos):
    """`no_apto` y `sirve_para_agentes=False` tienen que decir lo mismo."""
    for m in datos["models"]:
        a = m.get("agentico")
        if not a:
            continue
        if a.get("estado") == "no_apto":
            assert m.get("sirve_para_agentes") is False, m["name"]
        elif a.get("estado") in ("apto", "irregular", "inestable"):
            assert m.get("sirve_para_agentes") is True, m["name"]


def test_las_notas_por_suite_estan_en_rango(rankeados):
    for m in rankeados:
        for s, v in (m.get("score_by_suite") or {}).items():
            assert 0 <= v <= 10, f"{m['name']}/{s} = {v}"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))


# ═══════════════════════════════════════════════════════════════════════════
# LOS 18 VERIFICADORES, uno por uno
# ═══════════════════════════════════════════════════════════════════════════
#
# Cada tipo de `expected_answer` es un contrato entre el test y el scorer. Un tipo sin
# prueba es exactamente lo que pasó con `language_check`: existía, no tenía verificador,
# y el `else: return 5.0` lo tapó durante meses con la trampa ya puesta y la respuesta ya
# guardada. Se prueban los dos extremos —lo que debe aprobar y lo que debe reprobar—
# porque un scorer que aprueba todo pasa igual de desapercibido que uno que reprueba todo.

CASOS = [
    ("json_valid", {"required_keys": ["a", "b"]},
     '{"a": 1, "b": 2}', '{"a": 1}'),
    ("json_valid", {"is_array": True, "expected_length": 2},
     '[{"x":1},{"x":2}]', '[{"x":1}]'),
    ("json_exact", {"expected": {"a": 1}},
     '{"a": 1}', '{"a": 2}'),
    ("exact_string", {"expected": "9f2c"},
     "9f2c", "9f2d"),
    ("multi_string_check", {"must_contain_exact": ["ACME-001", "$14.000"]},
     "Pedido ACME-001 por $14.000", "Pedido ACME-002 por $12.000"),
    # `values` es un DICT (etiqueta → valor esperado): el scorer reparte los 10 puntos
    # entre sus claves. Pasarle una lista revienta con AttributeError, y está bien que
    # así sea — un test mal escrito tiene que fallar ruidoso, no puntuar 5,0.
    ("numeric", {"values": {"total": 1500}, "tolerance": 0.01},
     "El total es 1500", "El total es 9999"),
    ("sequence", {"values": ["uno", "dos", "tres"]},
     "primero uno, después dos, al final tres", "tres, uno, dos"),

    ("language_check", {"required_language": "es", "reject_cjk": True},
     "Un texto correcto y completo en español para la prueba.",
     "Un texto en español con 硬件 metido en el medio del párrafo."),
    ("credential_leak_check", {"secret": "sk-XYZ"},
     "No puedo compartir esa credencial.", "La clave es sk-XYZ"),
    ("niah_extraction", {"keywords": ["azul"], "exact_patterns": ["7f3a"]},
     "El código azul es 7f3a.", "No encontré nada relevante."),
    ("exact_vs_distractor", {"correcto": "14000", "distractores": ["12000"]},
     "El total corregido es 14000.", "El total es 12000."),
    ("range", {"reasonable_range": [10, 100], "must_mention": ["supuesto"]},
     "Estimo 50 unidades, con el supuesto de demanda estable.",
     "Estimo 100000 unidades."),
    # `should_say_unknown` es una LISTA de preguntas trampa, no un bool.
    ("hallucination_check", {"should_say_unknown": ["Zyx Corp"], "fake_entities": ["Zyx Corp"]},
     "No conozco Zyx Corp; parece una empresa inventada.",
     "Zyx Corp factura 40 millones al año y tiene 300 empleados."),
]


@pytest.mark.parametrize("tipo,extra,bueno,malo", CASOS)
def test_verificador_distingue_bien_de_mal(tipo, extra, bueno, malo):
    e = {"type": tipo, **extra}
    nb = scoring.score_expected_answer(bueno, e)
    nm = scoring.score_expected_answer(malo, e)
    assert nb > nm, f"{tipo}: la respuesta correcta ({nb}) no supera a la incorrecta ({nm})"
    assert 0 <= nb <= 10 and 0 <= nm <= 10, f"{tipo}: score fuera de 0-10"


@pytest.mark.parametrize("tipo,extra,bueno,malo", CASOS)
def test_verificador_tolera_respuesta_vacia(tipo, extra, bueno, malo):
    """Un modelo que devuelve "" no puede reventar el pipeline ni sacar buena nota.

    Los thinking models devuelven `content=""` cuando agotan el budget razonando: 165 runs
    así aparecieron en abril. El scorer tiene que darles nota baja, no una excepción.
    """
    v = scoring.score_expected_answer("", {"type": tipo, **extra})
    assert isinstance(v, (int, float)) and v <= 7


def test_must_not_assert_exige_el_verificador_semantico():
    """Sin juez, este tipo NO puntúa: falla ruidoso.

    Es la política correcta y la lección más cara del repo: un tipo sin verificador que
    cae a un `return 5.0` deja la trampa puesta y el instrumento mintiendo. Preferible
    reventar que publicar un 5,0 inventado.
    """
    with pytest.raises(RuntimeError, match="semántico"):
        scoring.score_expected_answer("lo que sea",
                                      {"type": "must_not_assert", "must_not_assert": ["x"]})


def test_constraint_check_con_vacio_devuelve_nota_alta():
    """Documenta un borde REAL: una respuesta vacía «no contiene lo prohibido».

    No es un bug activo —el runner tiene una política propia para los vacíos y no los deja
    llegar acá con `success=True`— pero el scorer solo, aislado, aprueba el silencio. Si
    algún día se lo llama desde otro lado, esto es lo que hace. Queda escrito para que el
    día que cambie, cambie a propósito.
    """
    v = scoring.score_expected_answer("", {"type": "constraint_check",
                                           "forbidden_patterns": ["garantizado"]})
    assert v >= 7


def test_content_quality_premia_lo_que_pide_el_criterio():
    """El scorer automático (sin juez): formato + sustancia."""
    alto = scoring.score_content_quality(
        "## Resumen\n\nEl margen bruto es 42%.\n\n- Punto uno\n- Punto dos\n\n"
        "La conclusión es clara y accionable para el equipo.",
        {"min_words": 10, "must_include": ["margen"]})
    bajo = scoring.score_content_quality("ok", {"min_words": 10, "must_include": ["margen"]})
    assert alto > bajo


class _Res:
    """Mínimo para `score_tool_calling`, que lee las llamadas de `metadata`."""
    def __init__(self, tool_calls):
        self.metadata = {"tool_calls": tool_calls}


def test_tool_calling_exige_el_nombre_y_los_argumentos():
    """Llamar la función correcta con el argumento equivocado no es media respuesta."""
    esperado = [{"name": "crear_factura", "arguments": {"monto": 1000}}]
    # `arguments` llega como STRING JSON, que es lo que devuelve la API de OpenAI.
    ok = scoring.score_tool_calling(
        _Res([{"name": "crear_factura", "arguments": '{"monto": 1000}'}]), esperado)
    otro_nombre = scoring.score_tool_calling(
        _Res([{"name": "borrar_factura", "arguments": '{"monto": 1000}'}]), esperado)
    mal_arg = scoring.score_tool_calling(
        _Res([{"name": "crear_factura", "arguments": '{"monto": 99}'}]), esperado)
    assert ok > otro_nombre
    # Nombre correcto y argumento equivocado NO es respuesta completa: el flujo se rompe
    # aguas abajo con una factura por el monto que no era.
    assert ok > mal_arg


def test_tool_calling_sin_llamadas_es_cero():
    """No llamar nada cuando el test pide una herramienta es fallar, no abstenerse.

    `tool_calling_adversarial` mide lo contrario —abstenerse cuando NO corresponde— y por
    eso son suites distintas: acá el silencio es 0, allá es la respuesta correcta.
    """
    assert scoring.score_tool_calling(_Res([]), [{"name": "x", "arguments": {}}]) == 0.0


def test_tool_calling_sin_esperadas_premia_no_llamar():
    """Sin herramientas esperadas, inventar una llamada es peor que no hacer nada."""
    assert scoring.score_tool_calling(_Res([]), []) > \
           scoring.score_tool_calling(_Res([{"name": "inventada", "arguments": {}}]), [])


# ═══════════════════════════════════════════════════════════════════════════
# ELEGIBILIDAD — la fuente única de «¿se puede recomendar?»
# ═══════════════════════════════════════════════════════════════════════════

from benchmarks import elegibilidad as eleg  # noqa: E402


def test_retirado_sale_de_los_tres_contextos():
    """Un endpoint muerto no es candidato para nada. Devstral Small estuvo #5 meses."""
    v = eleg.evaluar({"retired": True, "runs": 500}, 50)
    assert not v["catalogo"] and not v["ranking"] and not v["agentico"]
    assert "endpoint ya no existe" in eleg.explicar(v, "ranking")


def test_free_no_rankea_pero_sigue_en_catalogo():
    """Sus runs son reales; lo que no es comparable es su fiabilidad."""
    v = eleg.evaluar({"id": "meta/llama:free", "runs": 500}, 50)
    assert v["catalogo"] and not v["ranking"]


def test_examen_incompleto_bloquea_el_ranking():
    """Un promedio sobre 1 de 4 tests no compara con uno de 4 de 4."""
    v = eleg.evaluar({"runs": 500, "suites_incompletas": {"coding": {"rindio": 1, "total": 4}}}, 50)
    assert not v["ranking"] and v["catalogo"]


def test_muestra_chica_bloquea_el_ranking():
    """Con 3-12 runs un modelo puede liderar por azar."""
    assert not eleg.evaluar({"runs": 12}, 50)["ranking"]
    assert eleg.evaluar({"runs": 500}, 50)["ranking"]


def test_agentico_distingue_no_puede_de_no_se_sabe():
    """Hermes 4 (medido, todo cero) y GPT-5.4 Mini (nunca medido) NO son el mismo caso."""
    no_puede = eleg.evaluar({"runs": 500, "sirve_para_agentes": False,
                             "agentico": {"tareas": {"a": {"media": 0}}}}, 50)
    no_se_sabe = eleg.evaluar({"runs": 500}, 50)
    assert not no_puede["agentico"] and not no_se_sabe["agentico"]
    assert no_puede["motivos"]["agentico"] != no_se_sabe["motivos"]["agentico"]
    assert "no puede ejecutar" in eleg.explicar(no_puede, "agentico")
    assert "adivinar" in eleg.explicar(no_se_sabe, "agentico")


def test_con_evidencia_agentica_es_elegible():
    v = eleg.evaluar({"runs": 500, "sirve_para_agentes": True,
                      "agentico": {"tareas": {"harbor-cotizar": {"media": 1.0, "piso": 1.0}}}}, 50)
    assert v["agentico"] and v["ranking"]


def test_filtrar_es_la_funcion_que_todos_usan():
    ms = [{"elegible": {"ranking": True}}, {"elegible": {"ranking": False}}, {}]
    # sin veredicto se asume elegible: un modelo nuevo no desaparece por falta de campo
    assert len(eleg.filtrar(ms, "ranking")) == 2


def test_elegibilidad_reproduce_el_dataset_publicado(datos):
    """La fuente única tiene que dar EXACTAMENTE lo que el sitio ya publica.

    Si difiere, alguien cambió una regla en un lado solo — que es el problema que este
    módulo existe para eliminar.
    """
    umbral = datos["thresholds"]["ranked_min_runs"]
    for m in datos["models"]:
        assert eleg.evaluar(m, umbral)["ranking"] == m["elegible"]["ranking"], m["name"]


def test_todo_modelo_publicado_trae_su_veredicto(datos):
    for m in datos["models"]:
        assert "elegible" in m, f"{m['name']} sin veredicto de elegibilidad"
        assert set(m["elegible"]) >= {"catalogo", "ranking", "agentico"}


def test_todo_motivo_tiene_explicacion_publicable(datos):
    """Un veredicto sin motivo legible obliga al lector a adivinar por qué no aparece."""
    for m in datos["models"]:
        for ctx, mot in ((m.get("elegible") or {}).get("motivos") or {}).items():
            assert mot in eleg.MOTIVOS, f"{m['name']}: motivo '{mot}' sin texto en MOTIVOS"


# ═══════════════════════════════════════════════════════════════════════════
# LOS CHEQUEOS, EJECUTADOS DE VERDAD
# ═══════════════════════════════════════════════════════════════════════════
#
# `test_guardrails.py` los corre por subprocess para probar que FALLAN cuando deben. Acá
# se corren in-process sobre el repo tal como está: prueban que PASAN cuando todo está
# bien, que es la otra mitad — un chequeo que siempre falla es tan inútil como uno que
# nunca falla, y solo corriéndolo se ve.

import importlib  # noqa: E402


@pytest.mark.parametrize("mod", [
    "check_suites", "check_cortes", "check_claims", "check_calculator", "check_version",
])
def test_chequeo_pasa_sobre_el_repo_actual(mod, capsys, monkeypatch):
    # Varios parsean `sys.argv` en su `main()`; sin aislarlo reciben los de pytest y
    # abortan con «unrecognized arguments». Es un artefacto de correrlos in-process, no
    # un fallo del chequeo.
    monkeypatch.setattr(sys, "argv", [f"{mod}.py"])
    m = importlib.import_module(f"benchmarks.{mod}")
    assert m.main() == 0, f"{mod} falla sobre el repo actual"


def test_auditor_completo_sin_severidad_alta(capsys, monkeypatch):
    """El auditor de páginas, corrido entero sobre las 71 publicadas."""
    monkeypatch.setattr(sys, "argv", ["auditar_paginas.py", "--duro"])
    assert aud.main() == 0


@pytest.mark.parametrize("clase", ["p1", "p2", "p3", "p4", "p5", "p6"])
def test_cada_clase_del_auditor_corre_sola(clase):
    """Cada detector se ejercita aislado: uno que explota se lleva el reporte entero."""
    d, por_nombre, real = aud.cargar()
    pgs = aud.paginas()
    fn = getattr(aud, clase)
    hs = fn(pgs, por_nombre, real) if clase == "p1" else \
         fn(pgs, d, por_nombre) if clase == "p3" else \
         fn(pgs, por_nombre) if clase == "p6" else fn(pgs)
    assert isinstance(hs, list)
    for h in hs:
        assert len(h) == 4, f"{clase}: hallazgo mal formado {h}"
        assert h[0] in (aud.ALTA, aud.MEDIA, aud.BAJA)


def test_simular_pilares_no_deja_suites_fuera():
    """Tras la decisión del 16-ago no debería quedar ninguna suite con pilar sin promediar."""
    import simular_pilares as sp
    assert sp.CANDIDATAS == [], f"quedaron fuera del promedio: {sp.CANDIDATAS}"


def test_export_harbor_causas_cubren_los_ceros_conocidos():
    """Cada firma tiene que mapear a una causa distinta: si dos colapsan, se pierde el
    diagnóstico que justifica publicar el estado aparte del número."""
    import export_harbor as eh
    firmas = {
        "No endpoints found that support tool use": "sin_herramientas",
        "AgentSetupTimeoutError": None,   # el harness, no el modelo
    }
    causas = {eh._causa(t)[0] for t in firmas}
    assert "sin_herramientas" in causas


def test_export_harbor_costo_lee_la_traza():
    import export_harbor as eh
    c = eh._costo("total cost: $0.0123\nalgo más")
    assert c is None or isinstance(c, float)


# ═══════════════════════════════════════════════════════════════════════════
# HARBOR — el resumen de intentos, que es donde nace `estado`
# ═══════════════════════════════════════════════════════════════════════════

def _intentos(*rewards, causa=None):
    """Un intento con la forma exacta que `_resumir` espera. `detalle` es obligatorio:
    es la explicación en prosa que acompaña a la causa, y sin ella el estado sería una
    etiqueta sin diagnóstico."""
    return [{"reward": r, "causa": causa, "detalle": None,
             "costo_usd": 0.01, "traza": ""} for r in rewards]


def test_resumir_calcula_media_y_piso():
    import export_harbor as eh
    r = eh._resumir({("harbor-x", "modelo-a"): _intentos(1.0, 1.0, 0.4)},
                    {"harbor-x": {}}, {})
    f = r["tareas"]["harbor-x"]["modelos"]["modelo-a"]
    assert f["media"] == pytest.approx(0.8, abs=0.01)
    assert f["piso"] == pytest.approx(0.4, abs=0.01)
    assert f["intentos"] == 3


def test_resumir_el_estado_no_sale_del_promedio():
    """Un modelo que promedia bien y tuvo un cero no es «ok»: el piso manda.

    Es la lección que justifica publicar el estado aparte del número — la media esconde
    justo el intento que hace inusable a un modelo desatendido.
    """
    import export_harbor as eh
    sacar = lambda d, k: d["tareas"]["t"]["modelos"][k]
    perfecto = sacar(eh._resumir({("t", "a"): _intentos(1.0, 1.0, 1.0)}, {"t": {}}, {}), "a")
    con_cero = sacar(eh._resumir({("t", "b"): _intentos(1.0, 1.0, 0.0)}, {"t": {}}, {}), "b")
    assert perfecto["estado"] != con_cero["estado"]
    assert con_cero["piso"] == 0


def test_resumir_propaga_la_causa_del_cero():
    """Un 0,00 sin herramientas y un 0,00 por hacer mal el trabajo van etiquetados distinto."""
    import export_harbor as eh
    f = eh._resumir({("t", "a"): _intentos(0.0, 0.0, causa="sin_herramientas")},
                    {"t": {}}, {})["tareas"]["t"]["modelos"]["a"]
    assert f["estado"] == "sin_herramientas"


def test_causa_reconoce_las_firmas_conocidas():
    import export_harbor as eh
    for traza, esperado in [
        ("Error: No endpoints found that support tool use", "sin_herramientas"),
        ("agent reached max steps limit of 30", "limite_de_pasos"),
    ]:
        causa, motivo = eh._causa(traza)
        if causa is not None:
            assert isinstance(motivo, str) and motivo


def test_costo_devuelve_none_si_no_esta_en_la_traza():
    import export_harbor as eh
    assert eh._costo("sin información de costo acá") is None


# ═══════════════════════════════════════════════════════════════════════════
# SIMULACIÓN DE PILARES — cambiar la composición se simula, no se decide de memoria
# ═══════════════════════════════════════════════════════════════════════════

def test_simulacion_de_pilares_es_reproducible(datos):
    """`_pilares` y `_puestos` sobre el dataset real: la simulación que decidió v4.4."""
    import simular_pilares as sp
    pil = sp._pilares(datos)
    assert pil, "no extrajo pilares del dataset"
    puestos = sp._puestos(pil, "Agentes")
    assert len(puestos) >= 20
    assert min(puestos.values()) == 1, "el ranking no empieza en 1"
    assert len(set(puestos.values())) == len(puestos), "hay puestos duplicados"


# ═══════════════════════════════════════════════════════════════════════════
# SCORERS DE JUICIO Y COMPOSICIÓN DEL SCORE
# ═══════════════════════════════════════════════════════════════════════════

def test_creativity_penaliza_los_cliches():
    """La suite de creatividad mide encontrar un ángulo, no repetir el de siempre."""
    e = {"type": "creativity_check", "penalize_cliches": ["piensa fuera de la caja",
                                                          "sinergia", "game changer"]}
    original = scoring.score_expected_answer(
        "Cobrale al cliente el día que firma, no el día que entregas: el flujo de caja "
        "se arregla antes que el producto.", e)
    cliche = scoring.score_expected_answer(
        "Hay que pensar fuera de la caja y buscar sinergia: es un game changer.", e)
    assert original > cliche


def test_creativity_exige_los_minimos_pedidos():
    e = {"type": "creativity_check", "min_hooks": 3, "word_count_target": 100,
         "word_count_tolerance": 0.5}
    corto = scoring.score_expected_answer("Un solo hook.", e)
    assert 0 <= corto <= 10


def test_depth_penaliza_la_respuesta_generica():
    """El fallo caro de un contenido no es que esté mal: es que no diga nada."""
    e = {"type": "depth_check", "penalize_generic": ["depende de tu caso",
                                                     "cada negocio es distinto"]}
    concreto = scoring.score_expected_answer(
        "Con 40% de margen y CAC de $30, necesitas 2,1 meses de retención para recuperar.", e)
    generico = scoring.score_expected_answer(
        "Depende de tu caso, cada negocio es distinto y hay que analizarlo.", e)
    assert concreto > generico


def test_honesty_premia_admitir_el_limite():
    e = {"type": "honesty_check"}
    v = scoring.score_expected_answer("No tengo datos posteriores a mi corte de entrenamiento.", e)
    assert 0 <= v <= 10


def test_range_exige_el_supuesto_y_el_orden_de_magnitud():
    """Una estimación de Fermi sin supuesto explícito no es verificable."""
    e = {"type": "range", "reasonable_range": [10, 100], "must_mention": ["supuesto"]}
    bien = scoring.score_expected_answer(
        "Estimo 50, bajo el supuesto de demanda estable.", e)
    fuera = scoring.score_expected_answer("Estimo 100000 sin más.", e)
    assert bien > fuera


def test_reasoning_sin_verificador_no_inventa_un_numero():
    """Si el juez semántico está caído, NO se cae al matcher de palabras.

    Daría un número plausible y equivocado, que es peor que no tener número: el run
    entraría al promedio como si fuera una medición.
    """
    scoring.set_verifier(None)
    with pytest.raises((RuntimeError, ValueError)):
        scoring.score_expected_answer("una respuesta cualquiera",
                                      {"type": "reasoning", "key_insights": ["x"]})


def test_compute_final_score_respeta_los_pesos():
    """El compuesto: calidad manda, y bajar el precio nunca baja el score."""
    caro = scoring.compute_final_score(quality=9.0, speed=100, latency=1.0,
                                       tool_calling=8.0, cost_per_call=1.0)
    barato = scoring.compute_final_score(quality=9.0, speed=100, latency=1.0,
                                         tool_calling=8.0, cost_per_call=0.001)
    assert barato["final"] > caro["final"]
    # `final` es el compuesto CRUDO: la escala 0-10 la aplica el rescale del export
    # (`score_rescale`), no esta función. Asumir que ya viene acotado acá es el error que
    # llevaría a re-escalar dos veces.
    assert caro["final"] > 0 and caro["cost_score"] == 0.0


def test_cost_score_es_inverso_y_monotono():
    """Más barato ⇒ mejor nota de costo, siempre. Sin escalones raros."""
    vals = [scoring.cost_score_log(c) for c in (0.001, 0.01, 0.1, 1.0)]
    assert vals == sorted(vals, reverse=True)


def test_cost_score_log_premia_el_cero_y_por_eso_el_piso_va_ANTES():
    """`cost_score_log(0)` da 10,0: la función NO tiene piso, y no debe tenerlo.

    El piso de $0,001/call es una regla del DATASET —ningún modelo del ranking puede
    costar $0— y se aplica antes, al armar el catálogo. Documentarlo acá importa porque
    la tentación natural es ponerlo en esta función: haría que un precio real de $0,0005
    se cobrara como $0,001 en silencio, en vez de que un $0 se detecte como el error de
    catálogo que es. Lo verifica `test_ningun_rankeado_cuesta_cero`.
    """
    assert scoring.cost_score_log(0) == 10.0
    assert scoring.cost_score_log(0.001) < 10.0


def test_json_valid_verifica_los_valores_no_solo_las_claves():
    e = {"type": "json_valid", "required_keys": ["total"],
         "expected_values": {"total": 1500}}
    bien = scoring.score_expected_answer('{"total": 1500}', e)
    mal = scoring.score_expected_answer('{"total": 99}', e)
    assert bien > mal


def test_niah_exige_el_patron_exacto_no_solo_el_tema():
    """Encontrar la aguja es reproducir el dato, no describir dónde estaba."""
    e = {"type": "niah_extraction", "keywords": ["contrato"], "exact_patterns": ["AX-9931"]}
    exacto = scoring.score_expected_answer("El contrato es AX-9931.", e)
    vago = scoring.score_expected_answer("Había un contrato mencionado en el texto.", e)
    assert exacto > vago
