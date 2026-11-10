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
    "agent_long_horizon": 98304,   # 8 y 12 turnos. Máximo observado: 61.741
    "strategy": 49152,
    "deep_reasoning": 49152,
    "code_generation": 49152,
    "business_strategy": 49152,
}
PRESUPUESTO_DEFECTO = 32768        # 26 suites no llegan ni a 16k; esto es aire de sobra

# EL JUEZ CANÓNICO (14-sep-2026). El juez pone el 70% de la nota en las suites juzgadas,
# así que dos lotes con jueces distintos no rindieron el mismo examen. Los rankeados con
# procedencia registrada (desde el 14-ago) los puntuó Phi-4 vía OpenRouter; el Phi-4
# cuantizado del Ollama local puntuó 9 runs en toda la historia. El 14-sep los dos
# lanzadores del lote salieron con `phi4` (local) porque el CLAUDE.md lo mostraba como
# default, y lo cazó una auditoría antes de gastar. `runner.py` rechaza otro juez salvo
# `--juez-no-canonico`.
JUEZ_CANONICO = "phi4-or"

# 2-sep-2026 — POR QUÉ SE SUBIÓ (de 24.576/32.768/65.536).
# Cristian: *"igual podemos crecer el max tokens de todo, ya que no quiere decir que lo
# vayan a ocupar todo"*. Es correcto y ya estaba escrito en `adapters.py`: **se factura
# lo que el modelo genera, no el límite.** Subir el techo no encarece por sí mismo.
#
# El motivo para subirlo ahora: ese día se empezó a mandar `reasoning: {effort: medium}`
# a los thinking models (revertido el 14-sep: el examen volvió a ser el default, ver
# `effort.py`), y el effort **no agrega presupuesto, reparte el que hay** (~50% en
# medium, ~80% en high). Con los techos viejos, medium dejaba 12.288 tokens de respuesta
# en la mayoría de las suites; con éstos deja 16.384, y `high` —si algún día se declara
# en un test— pasa de dejar 4.915 a 6.553.
#
# El límite NO es el precio, es qué acepta el proveedor: el comentario viejo de
# `presupuesto_efectivo` avisa que 131.072 «varios proveedores lo rechazan de plano».
# Probado el 2-sep contra 7 modelos repartidos por el catálogo (GLM 5.3, Qwen 3.8 Flash,
# Luna, DeepSeek V4 Flash, Gemma 4 31B, Llama 3.3 70B, Kimi K2.7 Code) en 32k/48k/64k/96k:
# **los 7 aceptan los cuatro techos.** Por eso 98.304 y no 131.072.


# ── Peldaño de cada suite (corte-v5 3.1.a · DECISIONES, 4-nov-2026) ──────────
#
# Del post «Modo thinking: cuándo usarlo» (cristiantala.com/modo-thinking-ia-cuando-usarlo/):
# el razonamiento paga cuando la tarea sube la escalera, y en los dos primeros peldaños
# solo agrega costo y latencia.
#
#     1 buscar un dato · 2 ordenar la data · 3 concluir · 4 decidir
#
# Decide el MODO del examen de v5 (`effort.modo_examen`): en los peldaños 1 y 2 un modelo
# con interruptor se mide con el thinking APAGADO; en el 3 y el 4, a su default. La
# escritura va en el 2 (decisión de Cristian). Toda suite del índice tiene peldaño y
# ninguna otra lo tiene: lo exige `check_suites.py` S7. Una suite fuera del índice se mide
# al default (no es parte del examen que se compara).
PELDANO = {
    "string_precision": 1, "hallucination": 1, "ocr_extraction": 1,
    "summarization": 2, "translation": 2, "structured_output": 2, "task_management": 2,
    "customer_support": 2, "integridad_idioma": 2, "policy_adherence": 2,
    "content_generation": 2, "presentation": 2, "startup_content": 2,
    "news_seo_writing": 2, "sales_outreach": 2,
    "business_audit": 3, "verificar_claim": 3, "reasoning": 3, "content_verificable": 3,
    "creativity": 3, "tool_calling_adversarial": 3, "multi_turn": 3, "orchestration": 3,
    "agent_capabilities": 3, "code_generation": 3,
    "business_strategy": 4, "strategy": 4, "deep_reasoning": 4, "agent_long_horizon": 4,
    # 10-nov-2026: entra al examen (sin promediar). Peldaño 3 = al default, que es como se
    # midieron TODOS sus runs vigentes (sin peldaño, el runner no pide nada). Un 1-2 la
    # mediría apagada y sería otra versión del examen que la huella no ve.
    "prompt_injection_es": 3,
}


def peldano_de(suite: str | None) -> int | None:
    """El peldaño de la escalera (1-4) de una suite del índice; `None` fuera de él."""
    return PELDANO.get(suite) if suite else None


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
        "pilar": "Coding", "en_promedio": False, "en_examen": True,
        "fuera_por": "rasgo",
        "menu": "Precisión literal (hex, JWT, configs)",
        "decide": "no equivocarse en un dato",
        "nota": "FUERA DEL ÍNDICE desde 5.0.0 y DENTRO DEL EXAMEN (Cristian, 7-nov-2026, "
                "variante B). Saturada: 65 de 78 modelos copian todo y hubo un solo error de "
                "copia real; lo que separa a los modelos es su POLÍTICA ante algo que parece "
                "un secreto (Claude Fable 5.1 se niega a los 6), no su precisión. Se publica "
                "aparte como el rasgo «¿maneja credenciales?» (sí / a veces / se niega, con "
                "la cuenta). Se sigue rindiendo para que todo modelo tenga el rasgo; en 5.1 "
                "la precisión se rediseña con cadenas difíciles que no parezcan secretos.",
    },
    "precision_datos": {
        "pilar": "Coding", "en_promedio": False,
        # "por_decidir" (9-nov-2026): reemplazo propuesto de la precisión de
        # `string_precision`. Si entra al índice se decide con la simulación de la parada D.
        "fuera_por": "por_decidir",
        "menu": "Precisión con datos de negocio (RUT, montos, SKU)",
        "decide": "no cambiar un carácter de un dato que cuesta plata",
        "nota": "NUEVA el 9-nov-2026 (ventana v6.1, tarea 5.5). Mide lo que `string_precision` "
                "dejó de medir cuando su política ante cadenas que parecen secretos tapó la "
                "precisión: 14 tests y 81 ítems con identificadores fiscales y bancarios "
                "ficticios con dígito verificador válido, montos que cambian de formato sin "
                "cambiar de valor y caracteres confundibles. Nada parece una credencial. "
                "Verdad exacta por ítem, sin juez. Fuera del índice hasta decidir en la "
                "parada D, con la simulación, si reemplaza a la precisión del examen.",
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
        "pilar": "Agentes", "en_promedio": False,
        # `fuera_por`: por qué no promedia. "cobertura" (el default) CADUCA cuando la
        # rinde suficiente gente; "medicion" y "saturacion" no caducan nunca. Sin este
        # campo, el test de motivos veía el 97% de cobertura y pedía re-decidir algo ya
        # decidido.
        "fuera_por": "medicion",
        "menu": "Tool calling (llamada de funciones)",
        "decide": "llamar bien las funciones",
        "nota": "FUERA del promedio desde el 17-sep-2026 — y de hecho lo estuvo siempre: "
                "`export_for_pages.general` lo excluía POR CÓDIGO mientras el registro "
                "declaraba lo contrario, así que nunca contó en el titular dijera lo que "
                "dijera esta tabla. El motivo de la exclusión es bueno y está medido: el "
                "juez sólo lee TEXTO, y en esta suite la respuesta correcta ES la llamada a "
                "la herramienta, así que al modelo que la hace limpia le pone 1/5 ('no "
                "proporciona detalles') y al que la ignora y escribe un párrafo, 7.5. "
                "Contaminaba `quality` entre -0,14 y -0,22 justo a los que hacen bien tool "
                "calling. Se sigue publicando como badge: `tool_calling_score_avg`.",
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
        "fuera_por": "saturacion",   # no caduca con la cobertura: su nota ya lo dice
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
        "fuera_por": "saturacion",   # 100% de runs perfectos, dispersión 0,00
        "menu": "Encontrar el sitio oficial de una empresa",
        "decide": "elegir el dominio real, o abstenerse",
        "nota": "FUERA DEL PROMEDIO POR SATURACIÓN, no por cobertura. `validate_suite.py` "
                "la rechazó con el peor resultado posible: 100% de runs perfectos y "
                "dispersión 0,00 — todos los modelos empatan, así que no aporta ninguna "
                "información al pilar. Se endurece y se re-valida. Incluye casos donde la "
                "respuesta correcta es NULL: premia abstenerse, que es lo que separa a un "
                "modelo útil de uno que siempre contesta algo.",
    },

    # ── Suite de noticias (Ecosistema Startup corpus) ──────────────────────────
    # LICENCIA PENDIENTE: textos de Eco requieren aprobación CC BY 4.0 antes de medición
    # Diseño aprobado: benchmark-pack-noticias_e470.md
    "noticias_relevancia": {
        "pilar": "Contenido", "en_promedio": False,
        # "regresion" (9-nov-2026): SALE DEL BENCHMARK. En sus casos casi todos aciertan, así
        # que sirve el más barato disponible (DECISIONES, 9-nov). No se mide en lotes ni se
        # publica como ocasión; sus casos se corren con `--fuera-del-examen` como prueba de
        # regresión del filtro de Eco. Sigue en el registro porque tiene runs medidos (S1).
        "fuera_por": "regresion",
        "menu": "Filtrar notas por criterio editorial",
        "decide": "distinguir si una nota es para tu medio",
        "nota": "REESCRITA el 9-nov-2026 (ventana v6.1). 58 notas, una por test (29 pasan): ~20 que "
                "cumplen, ~20 que violan un veto y ~20 trampas (el mismo hecho ya publicado "
                "por otro medio, comunicado promocional sin hecho contra comunicado con una "
                "ronda, titular de gadget con cuerpo de negocio). Verdad POR CONSTRUCCIÓN: "
                "cada caso cae de un lado de una regla escrita del criterio A-Filtro, sin "
                "etiqueta a ojo. Las notas se reescribieron desde hechos públicos; ningún "
                "texto de Eco. Absorbe la detección de duplicados a escala chica. Es una "
                "OCASIÓN (etapa del pipeline de noticias), no entra al índice en esta ventana. "
                "SALE DEL BENCHMARK el 9-nov-2026: validate_suite con 8 modelos, 99 % de runs "
                "perfectos sin contar 19 errores 429; queda como prueba de regresión del filtro "
                "de Eco (sirve el más barato disponible que no deje pasar una nota vetada).",
    },
    "noticias_repetidas": {
        "pilar": "Agentes", "en_promedio": False,
        "fuera_por": "cobertura",
        "menu": "Detectar duplicados en flujo de noticias",
        "decide": "evitar publicar el mismo hecho dos veces",
        "nota": "FUERA DEL PROMEDIO hasta tener cobertura (80%). Suite creada 10-oct-2026. "
                "6 lotes de ~43 notas (259 totales). F1 sobre pares contra ground truth de "
                "23 grupos etiquetados manualmente el 10-oct. Referencia sin modelo: embeddings "
                "alcanzan 88.9%. Un modelo solo vale la pena si supera la regla gratis.",
    },
    "noticias_pauta": {
        "pilar": "Contenido", "en_promedio": False,
        "fuera_por": "cobertura",
        "menu": "Redactar nota siguiendo pauta editorial",
        "decide": "escribir publicable con la pauta, sin revisar",
        "nota": "FUERA DEL PROMEDIO hasta tener cobertura (80%). Suite creada 10-oct-2026. "
                "12 tests (3 rondas LATAM + 3 producto IA + 3 regionales + 3 comunicados). "
                "REDACTA una nota de 600-900 palabras desde ficha de hechos. 40% forma "
                "automática (sin voseo, título ≤60 chars), 30% fidelidad a cifras, 30% utilidad "
                "(3 preguntas Y/N al verificador). BLOQUEANTE: requiere crear 12 fichas (~1h).",
    },
    "noticias_extraccion": {
        "pilar": "Contenido", "en_promedio": False,
        # "regresion" (9-nov-2026): sale del benchmark; ver noticias_relevancia.
        "fuera_por": "regresion",
        "menu": "Extraer las afirmaciones verificables de una noticia",
        "decide": "sacar todos los datos, también el del último párrafo",
        "nota": "NUEVA el 9-nov-2026 (ventana v6.1). Etapa de extracción del pipeline de "
                "noticias, como OCASIÓN (no promedia). 25 fuentes reescritas desde hechos "
                "públicos (13 en inglés, 12 en español) con 259 afirmaciones plantadas, una "
                "siempre en el párrafo final. Sin juez: 8,5 × recall + 1,5 × acierto de núcleo "
                "× recall − 1 por afirmación con una cifra que no está en la fuente (tope 3). "
                "SALE DEL BENCHMARK el 9-nov-2026: sd 0,26 y rango 9,16-9,87; cada modelo "
                "omite 0 a 8 afirmaciones y casi siempre distintas. Queda como prueba de "
                "regresión de la extracción de Eco (258 afirmaciones: se corrigieron las anclas "
                "de una verdad discutible y se sacó otra).",
    },
    "noticias_verificacion": {
        "pilar": "Agentes", "en_promedio": False,
        # "regresion" (9-nov-2026): sale del benchmark; ver noticias_relevancia.
        "fuera_por": "regresion",
        "menu": "Verificar afirmaciones contra fuente",
        "decide": "encontrar qué requiere fuente antes de publicar",
        "nota": "REESCRITA el 9-nov-2026 (ventana v6.1). Etapa de verificación del pipeline "
                "de noticias, como OCASIÓN (no promedia). 30 casos (5 deben pasar, 25 "
                "bloquear, 10 de ellos con un solo problema escondido) con 171 afirmaciones: RESPALDADO, NO_RESPALDADO o CONTRADICE, con "
                "cifras alteradas, magnitud, atribución, datos ausentes y fuente cortada por "
                "muro de pago. Nota = media geométrica entre el acierto en lo respaldado y el "
                "acierto exacto en lo que no (confundir CONTRADICE con NO_RESPALDADO es "
                "error): respaldar todo saca 1,7 y bloquear todo, 0. SALE DEL BENCHMARK el "
                "9-nov-2026: 98 % de runs perfectos y 0 de 240 decisiones del gate distintas; "
                "queda como prueba de regresión del gate de Eco.",
    },
    "noticias_redaccion": {
        "pilar": "Contenido", "en_promedio": False,
        "fuera_por": "ocasion",
        "menu": "Redactar una noticia desde una fuente",
        "decide": "escribir la nota sin inventar cifras",
        "nota": "NUEVA el 9-nov-2026 (ventana v6.1). Etapa de redacción del pipeline de "
                "noticias, como OCASIÓN (no promedia). 25 fuentes (12 en inglés, 13 en "
                "español) reescritas desde hechos públicos; cada una OMITE un dato que el "
                "modelo probablemente conoce (año, valuación). Sin juez: 35 % ninguna cifra "
                "ajena a la fuente (normalizada: US$100M = «100 millones de dólares»), 25 % el "
                "dato clave cerca de su entidad, 15 % sin CJK, 15 % largo, 10 % sin voseo. "
                "Los defectos de estilo se cuentan aparte y no entran a la nota.",
    },
    "noticias_traduccion": {
        "pilar": "Contenido", "en_promedio": False,
        # "regresion" (9-nov-2026): sale del benchmark; ver noticias_relevancia.
        "fuera_por": "regresion",
        "menu": "Corregir fragmentos en otro alfabeto",
        "decide": "traducir el fragmento sin tocar el resto",
        "nota": "NUEVA el 9-nov-2026 (ventana v6.1). Etapa de corrección del pipeline de "
                "noticias, como OCASIÓN (no promedia). 15 textos en español con 26 fragmentos "
                "en chino, japonés o coreano (4 con cifra: 10億円 = 1.000 millones de yenes). "
                "Sin juez: 35 % sin CJK, 30 % el resto intacto, 25 % el término aceptado en su "
                "lugar, 10 % la cifra bien convertida. SALE DEL BENCHMARK el 9-nov-2026: 94 % "
                "de runs perfectos, sd 0,15. Queda como prueba de regresión de Eco: ninguna "
                "cifra ni unidad alterada.",
    },
    "noticias_seo_discover": {
        "pilar": "Contenido", "en_promedio": False,
        "fuera_por": "cobertura",
        "menu": "Título y metadatos para Google Discover",
        "decide": "estructurar para que Google recomiende la nota",
        "nota": "FUERA DEL PROMEDIO hasta tener cobertura (80%). Suite creada 10-oct-2026. "
                "15 tests. Genera titulo, meta_titulo, meta_descripcion, slug, keyword, alt_imagen. "
                "70% automático (largos, formato, clickbait, cifras), 30% verificador (2 preguntas). "
                "Mide guidelines de Google Discover, NO tráfico real. BLOQUEANTE: requiere seleccionar "
                "15 notas y anotar protagonista (~15 min).",
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
        # 10-nov-2026 (Cristian): se rinde en el examen sin promediar. Cuentan los runs de la
        # ventana y los anteriores con la suite idéntica (huella_suite). Activada tras medir a
        # los 53 rankeados de otra versión y simular: 74 → 74, ningún score se mueve.
        "en_examen": True,
        "menu": "Resistencia a prompt injection",
        "decide": "resistir una fuga de datos",
        "nota": "se reporta como dimensión aparte a propósito: la seguridad no se promedia "
                "con la calidad. Un modelo excelente y barato puede ser el peor candidato "
                "posible para un chatbot de cara al público.",
    },
    "integridad_idioma": {
        "pilar": "Contenido", "en_promedio": True,
        "menu": "Integridad de idioma (no mezclar idiomas)",
        "decide": "no meter otro idioma en medio del texto",
        "nota": "entró al promedio el 17-sep-2026 con 107/107 rankeados medidos (100%). "
                "Estuvo fuera por cobertura —17 de 138 en agosto, y con esa muestra habría "
                "medido el sesgo de quién se midió primero—, pero esa razón caducó y el "
                "export la promediaba igual desde que pasó el umbral: el registro decía una "
                "cosa y el titular hacía otra (lo vigila `check_suites` S6). Entra DECLARADA "
                "porque medir decisiones de negocio EN ESPAÑOL es el diferencial de este "
                "benchmark —Cristian, 17-sep: *«lo nuestro es negocios en español, tiene que "
                "estar»*—: un modelo que mete inglés o chino en medio de un texto no sirve "
                "para publicar. Completar los 8 que faltaban costó 32 runs.",
    },
}

# Orden de los pilares — el mismo en el menú, en la tabla y en las comparaciones.
PILARES = ["Razonamiento", "Coding", "Contenido", "Agentes"]


def del_indice() -> set[str]:
    """Las suites que CUENTAN para el examen completo y para el índice de calidad.

    ES LA ÚNICA DEFINICIÓN. Todo lo demás —`niah_es`, `prompt_injection_es`,
    `integridad_idioma`, `dominio_entidad`, `extraer_claims`, `verificar_claims_lote`—
    se reporta como dimensión aparte y no bloquea a nadie.

    POR QUÉ EXISTE (20-ago-2026)
    ----------------------------
    Esto estaba resuelto por PREFIJO de nombre en cinco archivos:

        APARTE = ("niah", "prompt_injection")

    y esa tupla cubre 2 de las 6 suites que están fuera del índice. Las otras cuatro no
    empiezan con esos prefijos, así que cada consumidor que usaba la heurística creía
    que `integridad_idioma` contaba. Consecuencias reales del mismo día:

      · `completar_examen.py` mandó a medir tres modelos por tests de una suite que no
        cuenta para nada — Gemini 3.7 Flash, Step 3.5 Flash y Nemotron 3 Super.
      · `export_for_pages.py` publicó las dos respuestas a la vez para Nemotron 3 Super:
        `examen_completo: true` y `ranked: false`, sin ningún otro motivo, porque adentro
        del MISMO archivo convivían las dos definiciones.

    El criterio no era ambiguo ni estaba sin escribir: `SUITES[s]["en_promedio"]` ya lo
    decía. Lo que faltaba era una función a la que llamar, así que cada quien se
    escribió la suya. `check_suites.py` S5 impide que vuelva a haber una segunda.

    Desde el 7-nov-2026 se separa RENDIR de PROMEDIAR: esta función es lo que promedia
    (el índice de calidad); lo que hay que rendir para el examen completo es `del_examen()`.
    """
    return {s for s, v in SUITES.items() if v.get("en_promedio")}


def del_examen() -> set[str]:
    """Las suites que hay que RENDIR enteras para el examen completo (y que el runner exige).

    Es `del_indice()` más las que se rinden sin promediar (`en_examen: True`). Hoy, solo
    `string_precision`: salió del índice en 5.0.0 (7-nov-2026, variante B) pero se sigue
    rindiendo porque de ella sale el rasgo «¿maneja credenciales?». Sacarla también del
    examen habría bajado el examen de 143 a 137 pruebas —un cambio de MEDICIÓN, no de
    presentación— y los modelos nuevos se quedarían sin el rasgo.
    """
    return del_indice() | {s for s, v in SUITES.items() if v.get("en_examen")}


def de_regresion() -> set[str]:
    """Las suites que salieron del benchmark y quedan como prueba de regresión de Eco.

    Sus runs se guardan en `results/` (son la evidencia de la decisión), pero el export no
    los publica: ni `score_by_suite`, ni conteos, ni presupuesto (DECISIONES, 9-nov-2026,
    «Una etapa donde casi todos aciertan»)."""
    return {s for s, v in SUITES.items() if v.get("fuera_por") == "regresion"}


def fuera_del_indice(suite: str) -> bool:
    """¿Esta suite se reporta aparte y NO bloquea el ranking?"""
    return suite not in del_indice()


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
