#!/usr/bin/env python3
"""EL REGISTRO DE SUITES — qué mide cada eje, en humano, en un solo lugar.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
Cristian mandó la tabla de lanzamiento de Qwen3.8 con un comentario: *"ejemplo de cómo
otros miden y comparan"*. Lo que hace bien esa tabla es una sola cosa, y es barata: cada
fila lleva **qué mide en humano** arriba y **el nombre técnico** abajo.

    Long-horizon office work
    CoWorkBench

Nosotros teníamos la misma idea, escrita **a mano en tres archivos**, y ya había
divergido. Medido el día que se escribió esto:

    policy_adherence   calculadora: "Policy adherence (límites, idioma)"
                       corte:       "hacer exactamente lo que se pidió"
    string_precision   calculadora: "Precisión strings (hex, JWT, configs)"
                       corte:       "reproducir datos sin alterarlos: códigos, montos"

Siete suites dichas de dos formas distintas, y `integridad_idioma` y `niah_es` sin nombre
humano en ninguna parte — solo el id técnico, en la cara del usuario.

Y al medirlo apareció lo que la cosmética tapaba: **la calculadora y el export no están
de acuerdo sobre a qué pilar pertenece una suite.** Siete de 28 difieren, y tres no tenían
pilar en el export, que es el que produce los números publicados:

    agent_long_horizon         calculadora=Agentes      export=(ninguno)
    tool_calling_adversarial   calculadora=Agentes      export=(ninguno)
    content_verificable        calculadora=Contenido    export=(ninguno)
    customer_support           calculadora=Razonamiento export=Agentes
    ocr_extraction             calculadora=Contenido    export=Coding
    strategy                   calculadora=Contenido    export=Razonamiento
    task_management            calculadora=Contenido    export=Agentes

Es el patrón de siempre acá: la lista existía tres veces y ninguna era la fuente. Este
archivo ES la fuente. `models.json` la lleva, la calculadora la lee, los cortes la citan y
`check_suites.py` verifica que nadie la duplique a mano otra vez.

`en_promedio`
-------------
Una suite puede estar medida y **no sumar al promedio de su pilar**. El campo existe para
que esa condición sea **explícita y contable** en vez de una ausencia — que es justo la
clase de fallo que este repo ya sabe que sus detectores no cazan.

Al crearse el registro había tres así, y **ninguna por decisión**: `SUITE_TO_PILLAR`
simplemente no las tenía y `export_for_pages` las salteaba en silencio. Se simuló el
16-ago (`simular_pilares.py`) y la pregunta que decidía —*¿a quién castiga meterlas?*—
se respondió sola: **las rindieron el 100% de los modelos rankeados**, así que no había
sesgo de muestra que justificara excluirlas. Entraron. Movieron 77 de 80 puestos del pilar
Agentes y 75 de 80 de Contenido, **sin tocar el índice de calidad ni el score global**.

Hoy la única razón legítima para `False` es la que ya usan `integridad_idioma` y
`niah_es`: cobertura insuficiente o dimensión que se reporta aparte a propósito. Ponerlas
en `True` mueve números publicados, así que es un cambio de PRESENTACIÓN y se simula antes
contra los runs en disco, que cuesta $0 (`PLAN-ESTABILIDAD.md` R1).
"""

# pilar canónico · si suma al promedio del pilar · etiqueta de menú · qué decides con esto
#
# El pilar canónico es **el del export**, no el del menú, porque el export es el que
# produce los números que ya están publicados. Alinear el menú al export no mueve ningún
# score: solo cambia en qué sección del desplegable aparece el ítem — que hasta hoy le
# mentía al usuario sobre cómo se computa el pilar que está viendo.
# ── Presupuesto de salida por tarea (18-ago-2026) ────────────────────────────
#
# Cristian, antes de relanzar: *"¿estás seguro que con 16k es suficiente?"*. No lo
# estaba, y medirlo dio la respuesta: sobre 2.748 runs de la ruta SIN nuestro techo
# (Claude por suscripción, que no pasa por el adapter), la demanda real es
#
#     p50 = 1.106 · p90 = 5.172 · p95 = 8.313 · p99 = 18.735 · máx = 61.741
#
# y lo que supera 16k se concentra en UNA suite:
#
#     agent_long_horizon   19% de sus runs > 16k   (p95 = 29.927)
#     strategy              8%                     (p95 = 18.735)
#     las otras 26 suites   0%
#
# Por eso el techo es por TAREA y no global: subirlo a 32k en todas sería pagar de más
# en veintiséis para arreglar una. Y no rompe el `max_tokens` uniforme que adoptamos de
# LiveBench — ese principio pide el mismo límite para todos los MODELOS, no para todas
# las tareas. Doce turnos de conversación necesitan más aire que clasificar una frase, y
# darles lo mismo era justamente lo que sesgaba la medición.
# Cristian, al decidirlo: *"mejor tener el valor alto y no usarlo, que tenerlo bajo y
# rehacer"*. Es correcto y conviene dejarlo escrito porque es contraintuitivo: el
# `max_tokens` es un TECHO, no una reserva — se factura lo que el modelo genera, así que
# subirlo no cuesta nada por sí mismo. Lo único que sube el gasto son los casos donde el
# modelo de verdad necesitaba más aire; y ésos, con el techo corto, se pagaban igual y
# encima había que rehacerlos. El techo generoso ABARATA.
#
# El límite no es el dinero: es que varios proveedores rechazan con error 400 un
# `max_tokens` desproporcionado. Por eso los valores siguen anclados a la demanda medida
# (máx observado 61.741) y no a un número arbitrariamente enorme.
PRESUPUESTO_SALIDA = {
    "agent_long_horizon": 65536,   # 8 y 12 turnos. Cubre el máximo observado (61.741)
    "strategy": 32768,
    "deep_reasoning": 32768,
    "code_generation": 32768,
    "business_strategy": 32768,
}
PRESUPUESTO_DEFECTO = 24576        # 26 suites no llegan ni a 16k; esto es aire de sobra


def presupuesto_de(suite: str) -> int:
    """Cuántos tokens de salida se le dan a esta tarea. Igual para TODOS los modelos."""
    return PRESUPUESTO_SALIDA.get(suite, PRESUPUESTO_DEFECTO)


SUITES = {
    # ── Razonamiento ──────────────────────────────────────────────────────────
    "reasoning": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Razonamiento general (lógica, decisiones)",
        "decide": "razonar con varias piezas a la vez",
    },
    "deep_reasoning": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Razonamiento profundo (matemática, Fermi)",
        "decide": "resolver un problema difícil sin atajos",
    },
    "hallucination": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Anti-alucinación (citas, contexto)",
        "decide": "no inventar cuando no sabe",
    },
    "strategy": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Estrategia (pricing, planificación)",
        "decide": "elegir entre opciones de negocio",
    },
    "business_audit": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Auditar números (detectar el error plantado)",
        "decide": "encontrar el error en un número",
    },
    "business_strategy": {
        "pilar": "Razonamiento", "en_promedio": True,
        "menu": "Decisiones de negocio (prioridades, plan)",
        "decide": "armar un plan que se sostiene",
    },

    # ── Coding ────────────────────────────────────────────────────────────────
    "code_generation": {
        "pilar": "Coding", "en_promedio": True,
        "menu": "Generación de código (Python, SQL, debug)",
        "decide": "escribir código que corre",
    },
    "structured_output": {
        "pilar": "Coding", "en_promedio": True,
        "menu": "JSON estructurado (extracción, schemas)",
        "decide": "emitir JSON válido a la primera",
    },
    "string_precision": {
        "pilar": "Coding", "en_promedio": True,
        "menu": "Precisión literal (hex, JWT, configs)",
        "decide": "no equivocarse en un dato",
    },
    "ocr_extraction": {
        "pilar": "Coding", "en_promedio": True,
        "menu": "OCR / extracción desde imágenes",
        "decide": "leer datos de una imagen",
    },

    # ── Contenido ─────────────────────────────────────────────────────────────
    "content_generation": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Contenido genérico (blog, email, social)",
        "decide": "escribir un texto correcto",
    },
    "content_verificable": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Contenido con datos verificables (no inventar)",
        "decide": "escribir sin caer en la trampa del brief",
        "nota": "entró al promedio el 16-ago-2026. Estuvo fuera sin que nadie lo decidiera "
                "—`SUITE_TO_PILLAR` nunca la tuvo— y es la única suite de contenido donde "
                "se puede FALLAR (`content_generation` da media 9,37 y no distingue un 8B "
                "de Opus), así que excluirla dejaba el pilar apoyado justo en lo que no "
                "discrimina. Al entrar se movieron 75 de 80 puestos de Contenido.",
    },
    "summarization": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Resúmenes y extracción de datos",
        "decide": "resumir sin perder lo que importa",
    },
    "presentation": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Presentaciones (slides, reportes)",
        "decide": "estructurar una presentación",
    },
    "startup_content": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Contenido startup (newsletter, actualidad)",
        "decide": "escribir para una audiencia de negocio",
    },
    "creativity": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Creatividad (hooks, analogías, narrativa)",
        "decide": "encontrar un ángulo que no es el obvio",
    },
    "news_seo_writing": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Noticias + SEO (artículos completos)",
        "decide": "escribir un artículo publicable",
    },
    "sales_outreach": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Ventas en frío (cold email, campañas)",
        "decide": "escribir para vender",
    },
    "translation": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Traducción (es↔en)",
        "decide": "traducir sin deformar el sentido",
    },

    # ── Agentes ───────────────────────────────────────────────────────────────
    "tool_calling": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Tool calling (llamada de funciones)",
        "decide": "llamar bien las funciones",
    },
    "tool_calling_adversarial": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "No inventar herramientas (abstenerse cuando no hay)",
        "decide": "no inventar herramientas que no existen",
        "nota": "entró al promedio el 16-ago-2026. Mide abstenerse, que es el fallo caro de "
                "un agente en producción, y el pilar que la excluía es justo el que se mira "
                "para elegir un modelo de agente.",
    },
    "agent_long_horizon": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Tareas largas (sostener el hilo 8-12 turnos)",
        "decide": "sostener una tarea larga",
        "nota": "entró al promedio el 16-ago-2026. Su ausencia explicaba algo que estaba "
                "anotado sin causa: el pilar Agentes ponía a Gemini 3.6 Flash en #65 pese a "
                "ser #3 en calidad agéntica. No era solo que promedia — es que las dos "
                "suites agénticas no entraban. Al entrar, sube al #50 y se movieron 77 de "
                "80 puestos del pilar.",
    },
    "orchestration": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Orquestación (flujos de varios pasos)",
        "decide": "coordinar un flujo de varios pasos",
    },
    "multi_turn": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Multi-turno (debugging, requisitos)",
        "decide": "no perderse en una conversación larga",
    },
    "agent_capabilities": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Capacidades de agente (delegación, skills)",
        "decide": "delegar y usar lo que tiene a mano",
    },
    "policy_adherence": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Seguir instrucciones al pie de la letra",
        "decide": "hacer exactamente lo que se pidió",
    },
    "task_management": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Gestión de tareas (action items, planes)",
        "decide": "convertir una conversación en tareas",
    },
    "customer_support": {
        "pilar": "Agentes", "en_promedio": True,
        "menu": "Soporte al cliente (clasificar y responder)",
        "decide": "clasificar y responder un ticket",
    },

    # ── Verificación de datos (17-ago-2026) ───────────────────────────────────
    #
    # Las tres nacen de la misma pregunta: ¿este modelo sirve para un flujo que publica
    # sin humano revisando? Su respuesta es objetiva —el dato está en la fuente o no
    # está— así que no dependen del juez para lo esencial.
    #
    # Entran al pilar Contenido y NO promedian todavía: con 1 modelo medido, un promedio
    # mediría el sesgo de quién se midió primero, no la capacidad. Es la misma regla que
    # ya se aplica a `integridad_idioma`. Pasan a `en_promedio: True` cuando tengan
    # cobertura (~80% de los rankeados).
    "verificar_claim": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Verificar un dato contra su fuente",
        "decide": "decidir si una fuente respalda una afirmación",
        "nota": "entró al promedio el 17-ago-2026 con 83/83 rankeados medidos (100%). "
                "Mide las DOS direcciones del error: dejar pasar lo inventado y bloquear "
                "lo que sí estaba. Medir una sola engaña.",
    },
    "verificar_claims_lote": {
        "pilar": "Contenido", "en_promedio": False,
        "menu": "Verificar VARIOS datos de una vez (lote)",
        "decide": "devolver un juicio por cada dato, no solo por los primeros",
        "nota": "Creada el 17-ago-2026 después de que el gate de noticias de Eco fallara "
                "en producción con el modelo que este benchmark recomendó. `verificar_claim` "
                "manda UN claim y mide la calidad del juicio; producción manda ONCE, con un "
                "prompt de 4.218 caracteres, y lo que falla es la ENTREGA: cuatro notas "
                "devolvieron cero veredictos y se publicaron sin verificar. Un modelo puede "
                "sacar 10,00 en la otra y 0 en ésta. FUERA DEL PROMEDIO hasta tener "
                "cobertura: entra cuando la haya rendido suficiente gente, si no castigaría "
                "al que la rinde primero.",
    },
    "extraer_claims": {
        "pilar": "Contenido", "en_promedio": False,
        "menu": "Extraer los datos verificables de un texto",
        "decide": "sacar TODOS los datos, no solo los fáciles",
        "nota": "FUERA DEL PROMEDIO POR SATURACIÓN, no por cobertura. `validate_suite.py` "
                "la rechazó: 94% de runs con nota perfecta — no discrimina, así que "
                "sumarla al pilar solo agregaría ruido. Se endurece y se re-valida antes "
                "de medirla en todos. Mide COBERTURA además de precisión: un extractor "
                "que saca 2 de 8 datos correctos tiene 100% de precisión y deja el 75% "
                "sin verificar.",
    },
    "dominio_entidad": {
        "pilar": "Contenido", "en_promedio": False,
        "menu": "Encontrar el sitio oficial de una empresa",
        "decide": "elegir el dominio real, o abstenerse",
        "nota": "FUERA DEL PROMEDIO POR SATURACIÓN, no por cobertura. `validate_suite.py` "
                "la rechazó con el peor resultado posible: 100% de runs perfectos y "
                "dispersión 0,00 — todos los modelos empatan, así que no aporta ninguna "
                "información al pilar. Se endurece y se re-valida. Incluye casos donde la "
                "respuesta correcta es NULL: premia abstenerse, que es lo que separa a un "
                "modelo útil de uno que siempre contesta algo.",
    },

    # ── Dimensiones que se reportan APARTE (decisión vigente, no un olvido) ────
    "niah_es": {
        "pilar": None, "en_promedio": False,
        "menu": "Aguja en el pajar (contexto largo en español)",
        "decide": "encontrar un dato dentro de un contexto enorme",
        "nota": "se reporta como dimensión aparte: no todos los modelos tienen el contexto "
                "para rendirla, y promediarla castigaría por una capacidad declarada, no por "
                "una falla.",
    },
    "prompt_injection_es": {
        "pilar": None, "en_promedio": False,
        "menu": "Resistencia a prompt injection",
        "decide": "resistir una fuga de datos",
        "nota": "se reporta como dimensión aparte a propósito: la seguridad no se promedia "
                "con la calidad. Un modelo excelente y barato puede ser el peor candidato "
                "posible para un chatbot de cara al público.",
    },
    "integridad_idioma": {
        "pilar": None, "en_promedio": False,
        "menu": "Integridad de idioma (no mezclar idiomas)",
        "decide": "no meter otro idioma en medio del texto",
        "nota": "suite nueva (12-ago-2026, 17 modelos). Se reporta aparte hasta tener "
                "cobertura: entrar al promedio con 17 de 138 mediría el sesgo de quién se "
                "midió, no el idioma.",
    },
}

# Orden de los pilares — el mismo en el menú, en la tabla y en las comparaciones.
PILARES = ["Razonamiento", "Coding", "Contenido", "Agentes"]


def pilar_del_promedio(suite: str) -> str | None:
    """El pilar al que esta suite SUMA. `None` si está medida pero no promedia.

    Reemplaza a `SUITE_TO_PILLAR.get(suite)`, que devolvía `None` por ausencia y por
    decisión sin distinguirlas — y por eso tres suites llevaban meses fuera de su pilar
    sin que nada lo dijera.
    """
    s = SUITES.get(suite)
    return s["pilar"] if s and s["en_promedio"] else None


def label(suite: str) -> str:
    """Etiqueta corta para el menú de la calculadora."""
    s = SUITES.get(suite)
    return s["menu"] if s else suite


def decide(suite: str) -> str:
    """Qué decides mirando este eje. Es la línea de arriba de la fila, en humano."""
    s = SUITES.get(suite)
    return s["decide"] if s else suite


def menu_por_pilar() -> dict:
    """{pilar: [{value, label, decide}]} — lo que consume el desplegable."""
    out = {p: [] for p in PILARES}
    for k, s in SUITES.items():
        if s["pilar"] in out:
            out[s["pilar"]].append({"value": k, "label": s["menu"], "decide": s["decide"]})
    return out


def para_export() -> dict:
    """El registro tal como viaja en `models.json`, para que el sitio no lo duplique."""
    return {k: {"pilar": s["pilar"], "en_promedio": s["en_promedio"],
                "menu": s["menu"], "decide": s["decide"]}
            for k, s in SUITES.items()}


# Compat: varios módulos importan el dict plano. Se DERIVA, no se mantiene aparte.
SUITE_TO_PILLAR = {k: s["pilar"] for k, s in SUITES.items()
                   if s["pilar"] and s["en_promedio"]}
