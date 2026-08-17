#!/usr/bin/env python3
"""LA FUENTE ÚNICA de «¿este modelo se puede recomendar, y para qué?».

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian, después de encontrar él mismo tres fallos distintos en un día usando el sitio:
*"define bien cómo haremos el QA, tenemos solo una fuente de la verdad, la idea es que
todos usen la misma. No puede recomendar algo que no cumpla lo que estamos haciendo."*

El diagnóstico era exacto. Medido ese día: **76 condicionales de filtrado en 25 archivos**
deciden a mano si un modelo entra —`retired`, `ranked`, `sirve_para_agentes`,
`provider_variant`, `:free`, mínimos de runs— y cada superficie se armó la suya.

Y se puede fechar por qué se multiplicaron: cada campo **nació de un fallo distinto, en un
momento distinto**, y se aplicó donde dolía ese día. `score_by_pillar` el 25-abr con la
calculadora original; `retired` y `provider_variant` el 13-jul, el día que se descubrió
que Devstral Small llevaba meses **#5 del ranking con el endpoint apagado**;
`sirve_para_agentes` el 14-ago por Hermes 4. Lo escrito antes no los tenía, lo escrito
después los copiaba del vecino que los tuviera a mano, y nada verificaba que estuvieran
todos.

Los tres fallos de ese día son el mismo bug con distinta ropa:

  · el wizard juzgaba lo agéntico con UNA de tres tareas (`harbor-cotizar`) y recomendaba
    Llama 4 Scout 17B, que en `reunion` saca 0,00 en al menos un intento;
  · la calculadora ponía #3 del pilar Agentes a Hermes 4 405B, que no tiene endpoint con
    herramientas — la página de ese mismo eje ya lo filtraba;
  · el QA verificaba el wizard contra una COPIA de su lista de candidatos, así que probaba
    su propia réplica y no lo que la app hace.

EL PRINCIPIO
------------
**La regla se decide una vez, en el export, y se GRABA en el dato.** Ninguna superficie
—ni Python, ni el JS del sitio, ni el QA— vuelve a calcularla: leen `m["elegible"]`.

No es elegancia: es la única forma de que una regla nueva llegue a las once superficies
el mismo día. Cuando la regla vive en código, cada consumidor tiene su versión y divergen
en silencio; cuando vive en el dato, hay una sola y viaja con él.

    ANTES                             AHORA
    app.js      decide               app.js      lee m.elegible.agentico
    rankings    decide (distinto)    rankings    lee m.elegible.agentico
    landings    decide (distinto)    landings    lee m.elegible.agentico
    QA          re-decide            QA          lee m.elegible.agentico

LOS TRES CONTEXTOS
------------------
No es un flag: dónde puede aparecer un modelo depende de para qué se lo mira.

  `catalogo`  aparece en listados y datos. Casi todo entra: sus mediciones son reales.
  `ranking`   compite por un puesto. Exige muestra suficiente y examen completo.
  `agentico`  se puede recomendar para operar un agente. Exige EVIDENCIA de haberlo hecho.

Un modelo puede estar en el catálogo y no rankear (examen a medias), o rankear y no ser
apto para un agente (Gemini 3.6 Flash es lo contrario: #3 agéntico y #76 general).
"""

# Motivos, en el idioma del lector. Un veredicto sin motivo obliga a adivinar por qué un
# modelo no aparece, y eso ya costó una sesión entera de arqueología.
MOTIVOS = {
    "retirado": "su endpoint ya no existe: quien lo integre se estrella",
    "variante_proveedor": "es el mismo modelo servido por otra infra; su fila canónica ya está",
    "free": "medido en un endpoint `:free`, que falla 6× más y puede servirse con otra cuantización",
    "sin_muestra": "no llega al mínimo de corridas para que su promedio sea comparable",
    "examen_incompleto": "rindió algunas suites a medias: su promedio no compara con uno completo",
    "sin_herramientas": "no existe endpoint que le dé herramientas: no puede ejecutar nada en un agente",
    "sin_evidencia_agentica": "nunca se lo probó dentro de un agente; recomendarlo sería adivinar",
    "esfuerzo": "es la misma base razonando más, al mismo precio: no es otro producto",
    "self_hosted": "corre en hardware propio: su velocidad y costo no comparan con una API",
    "ruta_suscripcion": ("es el mismo modelo por una suscripción personal: el precio y el "
                         "cupo no son los que vas a pagar tú"),
}


def evaluar(m: dict, umbral_ranking: int) -> dict:
    """El veredicto de un modelo en los tres contextos, con su motivo.

    Recibe el modelo YA armado por el export (con `runs`, `agentico`, `suites_incompletas`)
    y no toca disco ni red: es una función pura, y por eso se puede probar sola.
    """
    v = {"catalogo": True, "ranking": True, "agentico": True, "motivos": {}}

    def no(ctx, motivo):
        v[ctx] = False
        v["motivos"].setdefault(ctx, motivo)

    # ── Fuera de todo: no se puede usar ────────────────────────────────────
    if m.get("retired"):
        for c in ("catalogo", "ranking", "agentico"):
            no(c, "retirado")
    if m.get("provider_variant"):
        no("ranking", "variante_proveedor")

    # ── Las `-sub` salen del catálogo público (17-ago-2026) ────────────────
    # Cristian: *"saca los modelos de suscripción de la lista para no seguir
    # mareándonos"*. Cada Claude aparecía dos veces —`claude-opus-5` por API y
    # `claude-opus-5-sub` por la suscripción de Claude Code— con nombres casi
    # iguales y números distintos, y el lector no tiene cómo saber cuál le aplica.
    # El que le aplica es SIEMPRE el de la API: la suscripción tiene un cupo
    # personal y un precio que no puede reproducir.
    #
    # Sus runs NO se borran: siguen en los datos y son los que destaparon el
    # truncamiento de la ruta API (0,81 de brecha en Opus 5). Esa comparación se
    # sigue pudiendo hacer desde el JSON; lo que se saca es la fila duplicada de
    # las páginas.
    if m.get("provider") == "claude_code":
        no("catalogo", "ruta_suscripcion")
    if m.get("self_hosted"):
        no("ranking", "self_hosted")

    # ── Ranking: el MISMO examen, entero ───────────────────────────────────
    #
    # 17-ago-2026 — Cristian: *"no seguiría poniendo el filtro de 50 runs. Todos
    # deben de tener todos y punto, si no no son comparables."*
    #
    # El umbral de 50 era un PROXY de comparabilidad, y como proxy fallaba en las
    # dos direcciones: dos modelos con 50 runs pueden haber rendido tests
    # distintos (no comparables, y pasaban), y uno con 40 runs de un examen que en
    # ese momento fuera más corto quedaba fuera sin razón.
    #
    # El criterio real es rendir el examen entero: las 29 suites que puntúan, con
    # todos sus tests. Son 143 tests, así que **cualquiera que lo complete tiene
    # ≥143 runs** y el viejo umbral de 50 queda subsumido: no filtraba nada que
    # éste no filtre mejor. Un umbral arbitrario menos.
    #
    # Simulado antes de aplicarlo, como manda PLAN-ESTABILIDAD R1 para un cambio
    # de presentación: 78 de los 83 rankeados ya rendían el examen completo. A los
    # 5 restantes les faltaban 51 tests EN TOTAL — se completan, no se pierden.
    if ":free" in (m.get("id") or ""):
        no("ranking", "free")
    # Las suites de fuera del índice (long-context, seguridad, idioma) se reportan
    # incompletas si lo están, pero NO bloquean: su score va aparte a propósito, y
    # exigirlas obligaría a medir 800K de contexto para rankear en Coding.
    # Booleano POSITIVO, no ausencia de incompletas: ese dict está vacío tanto
    # cuando el modelo rindió todo como cuando no rindió NADA, y leer la segunda
    # como la primera metió 29 modelos con cero runs al ranking en la primera
    # versión de este cambio (lo cazó la simulación, no un usuario).
    if m.get("examen_completo") is not True:
        no("ranking", "examen_incompleto")
        # Y tampoco al catálogo — o sea: fuera de la calculadora y de los listados.
        # Cristian: *"Solo los medidos completos aparecen en el benchmark /
        # calculadora. Si no, no aparecen."*
        #
        # Es más duro que lo anterior y es correcto: la calculadora existe para
        # DECIDIR, y ofrecer un modelo cuyo promedio sale de un examen más corto es
        # ofrecer una comparación que no se sostiene. «En evaluación» sonaba a
        # prudente y en la práctica publicaba lo mismo con una etiqueta.
        #
        # Sus runs NO se pierden ni se borran: siguen en models.json con su motivo,
        # y la entrada/salida de cada uno sigue guardada en results/responses/. Lo
        # que se saca es la recomendación, no la evidencia — para eso está la
        # auditoría. El camino de vuelta es medir lo que falta, no bajar el listón.
        no("catalogo", "examen_incompleto")
    if m.get("notes") and "no rankea por política" in (m.get("notes") or "").lower():
        no("ranking", "esfuerzo")

    # ── Agéntico: exige EVIDENCIA, no capacidad declarada ──────────────────
    #
    # Las dos condiciones nacieron de fallos distintos y ninguna sustituye a la otra:
    # Hermes 4 405B tiene tareas medidas y todas en cero (no puede); GPT-5.4 Mini no tiene
    # ninguna (no se sabe). Publicar los dos como candidatos es afirmar de más en los dos
    # sentidos.
    if m.get("sirve_para_agentes") is False:
        no("agentico", "sin_herramientas")
    elif not ((m.get("agentico") or {}).get("tareas")):
        no("agentico", "sin_evidencia_agentica")

    return v


def explicar(v: dict, ctx: str) -> str:
    """Frase publicable de por qué un modelo no entra en ese contexto."""
    mot = (v.get("motivos") or {}).get(ctx)
    return MOTIVOS.get(mot, mot or "")


def filtrar(models, ctx: str):
    """Los modelos elegibles en ese contexto. ESTA es la función que se usa, siempre.

    Si estás por escribir `[m for m in models if not m["retired"] and ...]`, esto es lo
    que buscabas. `check_elegibilidad.py` verifica que nadie vuelva a escribirlo a mano.
    """
    return [m for m in models if (m.get("elegible") or {}).get(ctx, True)]
