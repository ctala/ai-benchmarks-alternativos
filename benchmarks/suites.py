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
Una suite puede estar medida y **no sumar al promedio de su pilar**. Hoy eso le pasa a
tres, y no por decisión: `SUITE_TO_PILLAR` simplemente no las tenía, así que
`export_for_pages` las salteaba en silencio. El campo existe para que esa condición sea
**explícita y contable** en vez de una ausencia — que es justo la clase de fallo que este
repo ya sabe que sus detectores no cazan.

Ponerlas en `True` mueve números publicados: es un cambio de PRESENTACIÓN, y esos se
simulan antes contra los runs en disco (`PLAN-ESTABILIDAD.md`). Hasta que esa simulación
se corra y se decida, quedan en `False` con el motivo escrito.
"""

# pilar canónico · si suma al promedio del pilar · etiqueta de menú · qué decides con esto
#
# El pilar canónico es **el del export**, no el del menú, porque el export es el que
# produce los números que ya están publicados. Alinear el menú al export no mueve ningún
# score: solo cambia en qué sección del desplegable aparece el ítem — que hasta hoy le
# mentía al usuario sobre cómo se computa el pilar que está viendo.
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
        "pilar": "Contenido", "en_promedio": False,
        "menu": "Contenido con datos verificables (no inventar)",
        "decide": "escribir sin caer en la trampa del brief",
        "nota": "medida en 92 modelos y fuera del promedio de Contenido: `SUITE_TO_PILLAR` "
                "nunca la tuvo. Es la única suite de contenido donde se puede FALLAR "
                "(`content_generation` da media 9,37 y no distingue un 8B de Opus), así que "
                "excluirla deja el pilar apoyado justo en lo que no discrimina.",
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
        "pilar": "Agentes", "en_promedio": False,
        "menu": "No inventar herramientas (abstenerse cuando no hay)",
        "decide": "no inventar herramientas que no existen",
        "nota": "medida en 82 modelos y fuera del promedio de Agentes. Mide abstenerse, que "
                "es el fallo caro de un agente en producción — y el pilar que lo excluye es "
                "justo el que la gente mira para elegir un modelo de agente.",
    },
    "agent_long_horizon": {
        "pilar": "Agentes", "en_promedio": False,
        "menu": "Tareas largas (sostener el hilo 8-12 turnos)",
        "decide": "sostener una tarea larga",
        "nota": "medida en 91 modelos y fuera del promedio de Agentes. Explica algo que ya "
                "estaba anotado sin causa: el pilar Agentes ponía a Gemini 3.6 Flash en #65 "
                "pese a ser #3 en calidad agéntica. No era solo que promedia — es que las "
                "dos suites agénticas nuevas no entraban.",
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
