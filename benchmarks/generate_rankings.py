#!/usr/bin/env python3
"""
Genera páginas pSEO de ranking "Mejor LLM para [caso]" en docs/<slug>/index.html
a partir de docs/data/models.json (data real del benchmark). Reusa el shell y los
helpers de generate_comparison.py (no duplica HTML ni lógica de datos).

Tipo de página distinto a las comparaciones: ranking filtrado por un criterio
(pilar, suite, costo o licencia), no un cara a cara [A] vs [B].

IMPORTANTE: cada vez que se agreguen modelos nuevos o cambien los scores,
volver a correr este script para mantener actualizados los rankings por
dimensión individual. También se puede usar el pipeline maestro
regenerate_all.py.

Uso:
    python benchmarks/generate_rankings.py             # todos
    python benchmarks/generate_rankings.py --slug mejor-llm-para-programar
"""
import argparse
import json
from datetime import date
from generate_comparison import (
    load_models, pillar, fmt_cost, esc, methodology, page_shell, SITE, DOCS, PILLARS,
    get_counts, fmt_k, get_meta, fmt_pct, existing_published,
)


# --- Helpers para rankings por suite específica --------------------------------
def suite(m, name: str) -> float:
    return (m.get("score_by_suite") or {}).get(name) or 0


# --- Rankings a generar -------------------------------------------------------
RANKINGS = [
    {
        "slug": "mejor-llm-para-programar",
        "title": "Mejor LLM para programar en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para programar (2026)",
        "intent_kw": "mejor llm para programar, mejor ia para programar, mejor modelo para coding, mejor ia para codigo, llm para programar",
        "criterion": "pillar", "pillar": "Coding",
        "case": "coding (generar código, JSON estructurado y debugging en tareas reales)",
        "what": "coding",
        "lead": "¿Qué modelo de IA conviene para programar en 2026? Lo medimos con tests de coding reales "
                "(plugins, scripts, templates de N8N), no con benchmarks de juguete. Ranking por calidad de código.",
        "use_cases": ["plugins WordPress", "scripts Python y Bash", "templates JSON para N8N", "debugging de errores reales", "refactor de código existente"],
        "why": "En producción el código tiene que compilar, integrarse con tu stack y mantenerse. Un modelo que genera código elegante pero con errores de sintaxis o que no respeta tu API te cuesta más tiempo del que ahorra.",
        "related": ["modelos-n8n", "mejor-llm-para-tool-calling", "alternativas-claude"],
    },
    {
        "slug": "mejor-llm-para-n8n",
        "title": "Mejor LLM para N8N y agentes en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para N8N y agentes (2026)",
        "intent_kw": "mejor llm para n8n, mejor modelo para agentes, llm para automatizacion, mejor ia para n8n, llm para hermes",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno largo, tool calling y flujos tipo N8N / Hermes)",
        "what": "agentes y operaciones",
        "lead": "Para agentes en N8N o Hermes lo que importa no es solo \"inteligencia\": es tool calling fiable, "
                "multi-turno y costo por call. Ranking por capacidad agéntica medida en multi-turno real.",
        "use_cases": ["workflows de N8N", "agentes Hermes", "chatbots de soporte", "orquestación multi-paso", "extracción de datos con herramientas"],
        "why": "Un agente que falla en el tercer turno o llama mal una función genera más trabajo manual que hacer la tarea a mano. Acá medimos estabilidad multi-turno y adherencia a schemas.",
        "related": ["mejor-llm-para-tool-calling", "modelos-n8n", "mejor-llm-para-agentes"],
    },
    {
        "slug": "mejor-llm-en-espanol",
        "title": "Mejor LLM para contenido en español en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido en español (2026)",
        "intent_kw": "mejor llm en español, mejor ia para escribir en español, modelo para contenido español, mejor ia para redactar",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing en español neutro (blogs, copy y textos largos, no traducción del inglés)",
        "what": "contenido en español",
        "lead": "La mayoría de los rankings miden contenido en inglés. Acá medimos español neutro real: blogs, "
                "copy y textos largos. Ranking por calidad de escritura en español.",
        "use_cases": ["blogs técnicos", "newsletters", "copy de landing pages", "posts para redes", "documentación en español"],
        "why": "Muchos modelos suenan bien en inglés pero traducen mal al español o usan modismos que no funcionan en toda Latinoamérica. Medimos español neutro, tecnicismos y estructura.",
        "related": ["mejor-llm-para-contenido", "alternativas-chatgpt", "modelos-baratos-emprendedores"],
    },
    {
        "slug": "mejor-llm-barato",
        "title": "LLM más baratos en 2026 (con buena calidad): ranking con benchmark real",
        "h1": "LLM más baratos con buena calidad (2026)",
        "intent_kw": "llm más barato, modelos de ia baratos, llm economico, mejor llm barato, ia barata para agentes",
        "criterion": "cost", "min_score": 6.8,
        "case": "presupuesto ajustado (mejor relación calidad/precio para volumen real)",
        "what": "relación calidad/precio",
        "lead": "El modelo más caro casi nunca es el que necesitas. Filtramos los que rinden bien (score global ≥ 6,8) "
                "y los ordenamos del más barato al más caro. Ideal para agentes con 1.000+ calls/mes.",
        "use_cases": ["agentes con alto volumen", "startups con presupuesto ajustado", "procesamiento batch", "prototipos que escalan", "calls diarios masivos"],
        "why": "Cuando pasas de cientos a miles de calls por mes, el costo por millón de tokens pasa a ser más importante que ganar 0.2 puntos de calidad. El ranking refleja eso.",
        "related": ["modelos-baratos-emprendedores", "mejor-llm-para-n8n", "mejor-llm-open-source"],
    },
    {
        "slug": "mejor-llm-open-source",
        "title": "Mejor LLM open source en 2026: ranking con benchmark real",
        "h1": "Mejor LLM open source (2026)",
        "intent_kw": "mejor llm open source, mejor modelo open source, llm codigo abierto, mejor ia open source, modelos open source local",
        "criterion": "open_source",
        "case": "open source (pesos abiertos — corres local o en cualquier provider, sin lock-in)",
        "what": "modelos open source",
        "lead": "Si quieres correr local o evitar lock-in, estos son los mejores modelos de pesos abiertos según el "
                "benchmark — ordenados por score global. Verificamos la licencia (cuidado con los \"Plus\" propietarios).",
        "use_cases": ["ejecución local", "privacidad de datos", "evitar vendor lock-in", "finetuning propio", "deploy en infraestructura propia"],
        "why": "Open source no es solo filosofía: es soberanía sobre tus datos, costos predecibles y la posibilidad de correr local cuando la privacidad lo exige.",
        "related": ["modelos-open-source-local", "qwen-vs-llama", "mejor-llm-barato"],
    },
    {
        "slug": "mejor-llm-para-razonamiento",
        "title": "Mejor LLM para razonamiento 2026: ranking con benchmark",
        "h1": "Mejor LLM para razonamiento (2026)",
        "intent_kw": "mejor llm para razonamiento, mejor ia para razonar, modelo razonamiento logico, llm razonamiento matematico",
        "criterion": "pillar", "pillar": "Razonamiento",
        "case": "razonamiento (math, lógica y planning)",
        "what": "razonamiento",
        "lead": "¿Qué modelo de IA razona mejor en 2026? Ranking por el pilar de razonamiento del benchmark: "
                "matemáticas, lógica formal, análisis causal y planificación multi-paso en español.",
        "use_cases": ["análisis de negocio", "matemáticas y lógica formal", "planificación con restricciones", "resúmenes ejecutivos con inferencias", "toma de decisiones estructurada"],
        "why": "Para tareas de razonamiento no sirve una respuesta que suena bien pero es incorrecta. Medimos precisión lógica, coherencia causal y capacidad de mantener el hilo en problemas complejos.",
        "related": ["mejor-llm-para-resumir-textos", "gpt-5.6-vs-claude-opus-4-8", "alternativas-chatgpt"],
    },
    {
        "slug": "mejor-llm-para-contenido",
        "title": "Mejor LLM para contenido y marketing en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para contenido y marketing (2026)",
        "intent_kw": "mejor llm para contenido, mejor ia para marketing, modelo para escribir blogs, mejor ia para copywriting, llm para contenido",
        "criterion": "pillar", "pillar": "Contenido",
        "case": "contenido y marketing (blogs, copy, newsletters y textos largos en español neutro)",
        "what": "contenido y marketing",
        "lead": "¿Qué modelo escribe mejor contenido en español en 2026? Ranking por el pilar de contenido del benchmark: "
                "blogs, copy, newsletters y textos largos con tono natural para hispanohablantes.",
        "use_cases": ["blogs SEO", "copy de marketing", "newsletters B2B", "posts para redes sociales", "guiones y presentaciones"],
        "why": "El contenido genérico no vende ni posiciona. Medimos estructura, tono natural, uso correcto de tecnicismos y capacidad de seguir instrucciones de estilo en español neutro.",
        "related": ["mejor-llm-en-espanol", "modelos-baratos-emprendedores", "alternativas-chatgpt"],
    },
    {
        "slug": "mejor-llm-para-agentes",
        "title": "Mejor LLM para agentes y automatizaciones en 2026: ranking con benchmark",
        "h1": "Mejor LLM para agentes y automatizaciones (2026)",
        "intent_kw": "mejor llm para agentes, mejor ia para automatizacion, modelo para n8n, llm para hermes, agentes ia 2026",
        "criterion": "pillar", "pillar": "Agentes",
        "case": "agentes y operaciones (multi-turno, tool calling y orquestación de flujos)",
        "what": "agentes y operaciones",
        "lead": "Para agentes y flujos automatizados no alcanza con 'inteligencia': importa multi-turno estable, "
                "tool calling confiable y costo por conversación. Ranking por el pilar Agentes.",
        "use_cases": ["agentes autónomos", "workflows multi-step", "soporte al cliente", "extracción con herramientas", "routing y clasificación"],
        "why": "Un agente es una cadena de decisiones. Si falla en el segundo o tercer paso, todo el flujo se rompe. Medimos estabilidad multi-turno, coherencia de estado y uso correcto de herramientas.",
        "related": ["mejor-llm-para-n8n", "mejor-llm-para-tool-calling", "alternativas-claude"],
    },
    # ── CORTES POR EJE INDIVIDUAL (15-ago-2026) ──────────────────────────────
    #
    # POR QUÉ. El sitio publicaba el índice global y los 4 pilares, y los dos son
    # PROMEDIOS. Medido: **Gemini 3.6 Flash es #3 de 80 en calidad agéntica y #76 de 80
    # en el índice global** — y el pilar Agentes tampoco lo mostraba (#65), porque
    # también promedia. Cristian lo detectó usándolo: *"lo estoy usando en Hermes y
    # funciona muy bien"*, contra un número que decía lo contrario.
    #
    # Un corte por eje NO es más granularidad del pilar: es dejar de promediar. Cada una
    # de estas páginas muestra además **el contraste con el índice global**, porque una
    # tabla que solo diga «#3» es tan parcial como una que solo diga «#76».
    {
        "slug": "mejor-llm-que-no-inventa-herramientas",
        "title": "Mejor LLM que no inventa herramientas en 2026: ranking adversarial",
        "h1": "Mejor LLM que NO inventa herramientas (2026)",
        "intent_kw": "llm no inventa funciones, modelo alucina herramientas, tool calling adversarial, agente llama funcion inexistente",
        "criterion": "suite", "suite": "tool_calling_adversarial",
        "case": "resistir la tentación de llamar una herramienta que no existe o que no corresponde",
        "what": "no inventar herramientas",
        "lead": "Un agente que inventa una función falla de la peor manera: con confianza. "
                "Este corte mide abstenerse cuando la herramienta correcta no está.",
        "use_cases": ["agentes con catálogo acotado de funciones", "workflows donde un error se ejecuta", "integraciones con APIs reales"],
        "why": "Medir «usa herramientas» premia al que siempre llama algo. Acá se mide lo contrario: reconocer cuándo NO hay herramienta que sirva y decirlo.",
        "related": ["mejor-llm-para-tool-calling", "mejor-llm-para-agentes"],
    },
    {
        "slug": "mejor-llm-para-json",
        "title": "Mejor LLM para JSON estructurado en 2026: ranking con benchmark",
        "h1": "Mejor LLM para emitir JSON válido (2026)",
        "intent_kw": "mejor llm json, modelo json estructurado, llm schema valido, ia extraccion estructurada",
        "criterion": "suite", "suite": "structured_output",
        "case": "emitir JSON que parsea a la primera y respeta el schema pedido",
        "what": "salida estructurada",
        "lead": "Si la salida va a otro sistema, un JSON roto es una tarea que no se hizo. "
                "Este corte ordena por salida estructurada, no por calidad de prosa.",
        "use_cases": ["integraciones entre sistemas", "extracción de datos", "agentes que escriben archivos", "pipelines automatizados"],
        "why": "Medido en nuestras tareas agénticas: modelos que entienden el trabajo perfectamente lo pierden todo por comillas mal cerradas. El JSON no es un detalle de formato, es el entregable.",
        "related": ["mejor-llm-para-programar", "mejor-llm-para-agentes"],
    },
    {
        "slug": "mejor-llm-seguro-datos-clientes",
        "title": "Mejor LLM para datos de clientes en 2026: resistencia a fuga",
        "h1": "Mejor LLM para manejar datos de clientes (2026)",
        "intent_kw": "llm seguro datos clientes, prompt injection espanol, modelo no filtra datos, ia segura chatbot",
        "criterion": "suite", "suite": "prompt_injection_es",
        "case": "resistir que un usuario le saque datos o instrucciones con prompt injection",
        "what": "resistencia a fuga de datos",
        "lead": "Si tu agente atiende gente de afuera y toca datos de clientes, este es el único eje que importa primero. "
                "El resto se arregla; una fuga no.",
        "use_cases": ["chatbots de cara al público", "agentes con datos personales", "soporte automatizado", "cualquier cosa con RUT, correo o compras"],
        "why": "La mayoría del catálogo puntúa MUY bajo acá, y el índice general no lo refleja porque la seguridad se reporta aparte. Un modelo excelente y barato puede ser el peor candidato posible para esto.",
        "related": ["mejor-llm-para-agentes", "mejor-llm-en-espanol"],
    },
    {
        "slug": "mejor-llm-para-tareas-largas",
        "title": "Mejor LLM para tareas multi-paso en 2026: ranking por horizonte largo",
        "h1": "Mejor LLM para tareas largas y multi-paso (2026)",
        "intent_kw": "mejor llm tareas largas, llm multi paso, agente horizonte largo, mantener contexto conversacion, llm que no se pierde",
        "criterion": "suite", "suite": "agent_long_horizon",
        "case": "tareas multi-paso donde el modelo tiene que sostener el hilo (8-12 turnos)",
        "what": "sostener una tarea larga",
        "lead": "Un asistente que se pierde en el turno 8 no sirve, por bien que responda el turno 1. "
                "Este corte ordena por la suite de horizonte largo, no por el promedio.",
        "use_cases": ["asistentes conversacionales", "agentes que iteran", "procesos de varios pasos", "soporte con historial"],
        "why": "El promedio general premia escribir bien y castiga poco perderse. Acá se mide lo contrario: recordar una restricción del turno 1 doce turnos después.",
        "related": ["mejor-llm-para-agentes", "mejor-llm-para-tool-calling"],
    },
    {
        "slug": "mejor-llm-para-seguir-instrucciones",
        "title": "Mejor LLM para seguir instrucciones en 2026: ranking de adherencia",
        "h1": "Mejor LLM para seguir instrucciones al pie de la letra (2026)",
        "intent_kw": "llm que sigue instrucciones, modelo obediente, llm adherencia politica, ia que hace lo que le pides",
        "criterion": "suite", "suite": "policy_adherence",
        "case": "hacer exactamente lo que se pidió, ni más ni menos",
        "what": "seguir instrucciones",
        "lead": "El fallo caro de un asistente no es no saber: es hacer otra cosa. "
                "Este corte ordena por adherencia a lo que se le pidió.",
        "use_cases": ["asistentes que operan tu negocio", "agentes con políticas escritas", "flujos con reglas duras"],
        "why": "Un modelo que 'mejora' tu instrucción por su cuenta es peligroso en producción: hace algo razonable que nadie pidió, y no avisa.",
        "related": ["mejor-llm-para-agentes", "mejor-llm-para-tareas-largas"],
    },
    {
        "slug": "mejor-llm-para-datos-exactos",
        "title": "Mejor LLM para datos exactos en 2026: ranking de precisión literal",
        "h1": "Mejor LLM para no equivocarse en un dato (2026)",
        "intent_kw": "llm preciso datos, modelo que no inventa numeros, ia precision literal, llm hex jwt configs",
        "criterion": "suite", "suite": "string_precision",
        "case": "reproducir datos sin alterarlos: códigos, montos, identificadores, configuraciones",
        "what": "precisión en datos literales",
        "lead": "Un dígito cambiado en un monto o en un token no se nota hasta que duele. "
                "Este corte ordena por precisión literal.",
        "use_cases": ["facturación y cotizaciones", "configuraciones", "extracción de identificadores", "traspaso de datos entre sistemas"],
        "why": "Es el eje que ningún promedio refleja y el que más rápido rompe una operación: los errores no se ven, se facturan.",
        "related": ["mejor-llm-para-programar", "mejor-llm-para-agentes"],
    },
    {
        "slug": "mejor-llm-para-tool-calling",
        "title": "Mejor LLM para tool calling en 2026: ranking con benchmark real",
        "h1": "Mejor LLM para tool calling (2026)",
        "intent_kw": "mejor llm para tool calling, mejor ia para funciones, modelo para llamar apis, llm function calling, agentes tool use",
        "criterion": "suite", "suite": "tool_calling",
        "case": "tool calling (llamada correcta de funciones y estructura JSON fiable)",
        "what": "tool calling",
        "lead": "El tool calling puede arruinar un agente: una función mal llamada es peor que una respuesta lenta. "
                "Ranking por la suite específica de tool calling del benchmark.",
        "use_cases": ["llamadas a APIs externas", "agentes con funciones definidas", "workflows N8N/Hermes", "validación de schemas JSON", "extracción estructurada"],
        "why": "El 80% de los errores de un agente viene de tool calling malformado: parámetros incorrectos, funciones inventadas o JSON roto. Medimos exactitud en la invocación, no solo si el modelo dice que soporta herramientas.",
        "related": ["mejor-llm-para-n8n", "mejor-llm-para-agentes", "modelos-n8n"],
    },
    {
        "slug": "mejor-llm-para-resumir-textos",
        "title": "Mejor LLM para resumir textos en 2026: ranking con benchmark",
        "h1": "Mejor LLM para resumir textos (2026)",
        "intent_kw": "mejor llm para resumir, mejor ia para resumir textos, modelo para summarization, resumen automatico ia, llm resumen",
        "criterion": "suite", "suite": "summarization",
        "case": "summarization (resumir textos largos sin perder información clave)",
        "what": "summarization",
        "lead": "Resumir no es solo acortar: es conservar lo importante y descartar el ruido. "
                "Ranking por la suite de summarization del benchmark.",
        "use_cases": ["resumen de documentos largos", "síntesis de reuniones", "abstracts", "digest de noticias", "resumen de soporte al cliente"],
        "why": "Un mal resumen pierde datos críticos o inventa conclusiones. Medimos fidelidad al original, compresión proporcional y coherencia del resumen en español.",
        "related": ["mejor-llm-para-razonamiento", "alternativas-claude", "mejor-llm-para-contenido"],
    },
]


# --- Modelos frontier que el usuario suele buscar -----------------------------
FRONTIER_PATTERNS = {
    "GPT-5.6 Luna": ["gpt-5.6-luna"],
    "GPT-5.6 Terra": ["gpt-5.6-terra"],
    "GPT-5.6 Sol": ["gpt-5.6-sol"],
    "Claude Opus 4.8": ["claude-opus-4.8"],
    "Claude Fable 5": ["claude-fable-5"],
    "Grok 4.5": ["grok-4.5"],
    "GPT-5.5": ["gpt-5.5"],
}


def has_pillars(m):
    return sum((m.get("score_by_pillar") or {}).get(p) or 0 for p in PILLARS) > 0


def rank_models(models, cfg):
    # ≥50 runs (estándar del benchmark) → un outlier con 3-12 runs no lidera por azar
    # ── SOLO EL PLANO COMÚN ─────────────────────────────────────────────────
    #
    # Antes el filtro era solo `runs >= 50`, así que entraban a TODAS las páginas
    # pSEO los modelos medidos fuera del plano común: self-hosted del Spark,
    # variantes de NIM/Ollama Cloud/Groq y los de suscripción. 49 de 117 candidatos.
    #
    # No son comparables: su velocidad y su latencia son de ESA infra, no del modelo
    # (Qwen 3.5 397B da **8,42 en NIM y 7,97 en Ollama Cloud** — 0,45 de diferencia sobre
    # una población que entera abarca 1,39, así que mueve muchas posiciones). `models.json` ya lo
    # resuelve con `ranked` —que exige plano común, muestra sólida y examen completo—
    # y las páginas lo estaban ignorando. Por eso **DiffusionGemma corriendo en el
    # Spark encabezaba /mejor-llm-para-agentes/**.
    #
    # EXCEPCIÓN, declarada en el config con `ruta_unica: True`: una variante entra si
    # es la ÚNICA forma de medir una capacidad. Caso real: Nemotron 3.5 Lightning no
    # tiene NINGÚN proveedor en OpenRouter que exponga `tools`, así que sus 4 suites
    # con herramientas solo se pueden medir por NIM. Excluirlo sería publicar que no
    # puede hacer tool calling cuando lo que no puede es esa ruta.
    base = [m for m in models
            if (m.get("score_global") or 0) > 0 and (m.get("runs") or 0) >= 50
            and has_pillars(m)
            and (m.get("ranked") or m.get("ruta_unica"))]
    crit = cfg["criterion"]

    # ── EN LAS PÁGINAS DE AGENTES, LO QUE NO CORRE EN UN AGENTE NO SE RECOMIENDA ──
    #
    # `/mejor-llm-para-agentes/` y `/mejor-llm-para-n8n/` responden literalmente "¿cuál
    # pongo en mi agente?". Medido el 14-ago dentro de un agente real: 5 modelos NO
    # PUEDEN ejecutar la tarea —dos porque no existe endpoint con tool use, tres porque
    # no sostienen el bucle— y varios de ellos puntúan alto en el pilar Agentes, que se
    # calcula con suites de texto y tool calling declarado. **Hermes 4 405B saca 8,20 de
    # calidad y 0,00 adentro de un agente.** Publicarlo en esa lista es exactamente el
    # fallo que el repo declara como el peor posible: recomendar algo que no se puede
    # usar. Es la misma regla que ya saca a los `retired` del ranking.
    #
    # Solo aplica al pilar Agentes: un modelo que no sostiene un bucle de herramientas
    # puede seguir siendo excelente escribiendo código cuando lo manejás vos.
    # Suites que describen trabajo DENTRO de un agente. Se listan explícitas porque no
    # todas las suites lo son: `summarization` no necesita herramientas, `tool_calling` sí.
    SUITES_AGENTICAS = {"agent_long_horizon", "tool_calling", "tool_calling_adversarial",
                        "policy_adherence", "agent_capabilities", "orchestration", "multi_turn"}
    es_agentica = (crit == "pillar" and cfg.get("pillar") == "Agentes") or \
                  (crit == "suite" and cfg.get("suite") in SUITES_AGENTICAS)
    if es_agentica:
        # Medido el 15-ago: `Llama 3.1 8B Instant` sale **#4 en agent_long_horizon** y NO
        # corre dentro de un agente (rompe el bucle de herramientas). La suite mide
        # sostener el hilo SIN herramientas, así que un modelo puede lucirse ahí y
        # romperse apenas tiene que llamar algo. Publicarlo cuarto en «mejor LLM para
        # tareas largas» es mandar a alguien a integrarlo — el mismo fallo que ya se
        # atajó en el pilar Agentes, un nivel más adentro.
        base = [m for m in base if m.get("sirve_para_agentes") is not False]

    if crit == "pillar":
        pil = cfg["pillar"]
        # Ordena por CAPACIDAD en la tarea, no por el compuesto con costo/velocidad.
        # Ver pillar_quality() para por qué.
        #
        # ⚠️ EL ORDEN Y LA CIFRA SALEN DE LA MISMA FUNCIÓN, y hasta el 16-ago-2026 no
        # era así: acá se ordenaba por `pillar_quality` y la columna imprimía
        # `score_for`, que para Agentes mezclaba tool calling. Resultado: la tabla se
        # veía desordenada respecto de su propia columna —el #4 con más nota que el #3—
        # y el criterio real era invisible. Pasaba en 16 páginas.
        base = [m for m in base if score_for(m, cfg) is not None and score_for(m, cfg) > 0]
        return sorted(base, key=lambda m: -score_for(m, cfg))
    if crit == "suite":
        sname = cfg["suite"]
        base = [m for m in base if suite(m, sname) > 0]
        return sorted(base, key=lambda m: -suite(m, sname))
    if crit == "cost":
        base = [m for m in base if (m.get("score_global") or 0) >= cfg.get("min_score", 6.8)]
        return sorted(base, key=lambda m: (m.get("cost_input_per_M") or 99) + (m.get("cost_output_per_M") or 99))
    if crit == "open_source":
        base = [m for m in base if m.get("open_source")]
        return sorted(base, key=lambda m: -(m.get("score_global") or 0))
    return sorted(base, key=lambda m: -(m.get("score_global") or 0))


def pillar_quality(m, name):
    """Capacidad PURA del modelo en ese pilar. Sin costo, sin velocidad, sin latencia.

    Alguien que busca "mejor LLM para contenido" pregunta quien ESCRIBE MEJOR, no
    quien tiene mejor relacion calidad/precio. Ordenar esa pagina por un compuesto
    que incluye costo y velocidad responde otra pregunta -- y respondia mal:

      "mejor llm para contenido" ordenado por el compuesto:  1. GPT-OSS 20B (Groq)
      ordenado por capacidad real de escribir:               1. MiniMax M3 (9.17)

    El compuesto coronaba a los modelos rapidos y baratos de Groq en una pagina que
    promete decir quien escribe mejor, y hundia al #6 a DeepSeek V4 Flash, que tenia
    la mejor calidad de contenido del lote. Mismo efecto en Agentes: Llama 3.1 8B
    aparecia sobre Opus 4.8 -- no por ser mejor agente, sino por ser barato y rapido.

    El costo NO desaparece: se muestra como columna, y el veredicto de bandas dice
    "de los que empatan en capacidad, el mas barato es X". Primero se mide el poder;
    despues se decide con el precio. En ese orden.
    """
    return ((m.get("dims_by_pillar") or {}).get(name) or {}).get("quality_avg") or 0


# Peso del tool calling REAL en las páginas de agentes. Interino: cuando v4.1
# rediseñe las suites agénticas (state-based + subset matching, diseño BFCL), el
# pilar va a medir capacidad agéntica de verdad y esto sobra.
PESO_TOOLS_AGENTES = 0.5

# Peso de la tarea REAL (Harbor) frente a `tool_calling` al ordenar lo agéntico. Tiene que
# coincidir con `PESO_TAREA_REAL` de `docs/app.js`: la calculadora y estas páginas ordenan
# el mismo eje y no pueden decir cosas distintas. Lo verifica `check_calculator`.
PESO_TAREA_REAL = 0.6


def score_agentico(m):
    """Lo que el modelo LOGRÓ dentro de un agente, no lo que escribe sobre agentes.

    Media y PISO de las tareas Harbor (0-1, llevado a 0-10). El piso pesa porque para
    trabajo desatendido «a veces falla» y «no falla» no son lo mismo, y promediar los
    intentos los vuelve indistinguibles.
    """
    t = (m.get("agentico") or {}).get("tareas") or {}
    vals = [x for x in t.values() if x.get("media") is not None]
    if not vals:
        return None
    media = sum(x["media"] for x in vals) / len(vals)
    piso = min((x.get("piso") if x.get("piso") is not None else 0) for x in vals)
    real = (0.6 * media + 0.4 * piso) * 10
    tools = m.get("tool_calling_score_avg")
    if tools is None:
        return real
    return PESO_TAREA_REAL * real + (1 - PESO_TAREA_REAL) * tools


def score_for(m, cfg):
    if cfg["criterion"] == "pillar":
        # ── AGENTES: el pilar solo no alcanza ───────────────────────────────
        #
        # Medido el 12-ago-2026: las 7 suites del pilar "Agentes" tienen su nota
        # dominada por la PROSA, no por el uso de herramientas. Correlación entre
        # `quality` y `tool_calling` en las 4 suites que dan tools: de −0,17 a
        # +0,13, y en tres de ellas manda el juez (hasta +0,99).
        #
        # Consecuencia publicada: **DiffusionGemma 26B encabezaba
        # /mejor-llm-para-agentes/ con "Agentes 8.8"** — un modelo de difusión local
        # cuyo score REAL de tool calling es 1,72. Estaba en el <meta description>,
        # o sea en el título que ve Google, y la página apunta a "llm para hermes".
        #
        # Hasta que v4.1 arregle las suites, el ranking de agentes incorpora la única
        # señal que sí mide capacidad agéntica y que ya teníamos medida. Con esto
        # DiffusionGemma pasa de #1 a #112 y el top queda con modelos de tool calling
        # 8,1–8,4.
        # ACTUALIZADO 16-ago-2026: el parche de arriba se midió contra verdad objetiva
        # (el reward de las tareas Harbor, verificado por pytest, no por un juez) y se
        # quedó corto. Sobre 75 modelos rankeados con tarea medida:
        #
        #     pilar Agentes solo                 −0,20   ← NEGATIVA
        #     65% pilar + 35% tool_calling       +0,44   ← el parche
        #     tool_calling solo                  +0,58
        #
        # O sea: el parche mejoraba, y el pilar que arrastraba adentro lo empeoraba. La
        # causa de fondo es que las nueve suites del pilar miden PROSA sobre agentes,
        # no ejecución — `agent_long_horizon` mide sostener el hilo SIN herramientas y
        # `tool_calling_adversarial` mide abstenerse.
        #
        # Ahora se ordena por lo que se midió HACIENDO el trabajo. `tool_calling`
        # desempata porque la tarea satura (muchos en 1,00).
        if cfg["pillar"] == "Agentes":
            ag = score_agentico(m)
            if ag is not None:
                return ag
            tool = m.get("tool_calling_score_avg")
            if tool is not None:
                # Sin tarea medida: el parche viejo, y topeado para que no supere a
                # quien sí la rindió y la aprobó.
                return min(5.9, (1 - PESO_TOOLS_AGENTES) * pillar_quality(m, cfg["pillar"])
                           + PESO_TOOLS_AGENTES * tool)
        return pillar_quality(m, cfg["pillar"])
    if cfg["criterion"] == "suite":
        return suite(m, cfg["suite"])
    return m.get("score_global") or 0


def score_label(cfg):
    if cfg["criterion"] == "pillar":
        return f"Calidad en {cfg['pillar']}"   # capacidad pura, sin costo ni velocidad
    if cfg["criterion"] == "suite":
        return cfg["suite"].replace("_", " ").title()
    return "Score global"


# Puesto de cada modelo en el ÍNDICE DE CALIDAD global. Se calcula una vez y se usa en
# la columna de contraste de los cortes por eje.
#
# POR QUÉ EXISTE ESA COLUMNA (15-ago-2026). Un corte por eje sin el global es tan parcial
# como el global sin el eje. Medido: **Gemini 3.6 Flash es #3 de 80 en calidad agéntica y
# #76 de 80 en el índice general** — quien lea solo una de las dos cifras se lleva una
# conclusión falsa en cualquiera de los dos sentidos. La página tiene que mostrar las dos
# juntas, que es exactamente el dato que ningún promedio da.
_PUESTO_GLOBAL: dict[str, int] = {}


def _cargar_puestos(models):
    if _PUESTO_GLOBAL:
        return
    r = sorted([m for m in models if m.get("ranked") and m.get("score_calidad") is not None],
               key=lambda m: -m["score_calidad"])
    for i, m in enumerate(r, 1):
        _PUESTO_GLOBAL[m["name"]] = i


def table_head(cfg):
    base_cols = '<th scope="col">#</th><th scope="col">Modelo</th>'
    if cfg["criterion"] == "suite":
        # Corte por eje: el eje + el CONTRASTE con el índice global. Los 4 pilares se
        # sacaron a propósito — son promedios, y el punto de esta página es dejar de
        # promediar.
        base_cols += (f'<th scope="col">{esc(score_label(cfg))}</th>'
                      '<th scope="col">Índice global</th>'
                      '<th scope="col">Puesto global</th>')
    elif cfg["criterion"] == "pillar":
        # Antes acá no se agregaba columna, con este argumento: «la columna del pilar
        # relevante ya está entre Coding/Contenido/Razon./Agentes». Era cierto mientras
        # el orden fuera `pillar_quality`. Dejó de serlo el 16-ago, cuando Agentes pasó a
        # ordenarse por la tarea Harbor: el número que decide el puesto no estaba en
        # NINGUNA columna, y la tabla se leía desordenada respecto de todo lo que mostraba.
        base_cols += f'<th scope="col">{esc(score_label(cfg))}</th>'
    else:
        base_cols += '<th scope="col">Global</th>'
    if cfg["criterion"] != "suite":
        base_cols += '<th scope="col">Coding</th><th scope="col">Contenido</th><th scope="col">Razon.</th><th scope="col">Agentes</th>'
    base_cols += '<th scope="col">$ in/out per M</th><th scope="col">Velocidad</th>'
    return f'<div class="table-scroll"><table class="results-table">\n      <thead>\n        <tr>{base_cols}</tr>\n      </thead>'


def row_ranking(rank, m, cfg, top=False, badges=None):
    """Fila de tabla que incluye la columna del score relevante para el ranking.

    `badges`: {nombre_modelo: etiqueta} -> marca en la tabla a los modelos que el
    veredicto cita. Sin esto la pagina se contradecia sola: el veredicto recomendaba
    un modelo y la tabla coronaba a otro, sin ninguna pista de por que. Ahora el
    recomendado es una fila VISIBLE y MARCADA de su propia evidencia.
    """
    badge = (badges or {}).get(m.get("name"))
    nm = f"<strong>{esc(m.get('name'))}</strong>" if top else esc(m.get("name"))
    if badge:
        nm += f' <span class="row-badge">{esc(badge)}</span>'
    relevant = score_for(m, cfg)
    if cfg["criterion"] == "suite":
        pg = _PUESTO_GLOBAL.get(m.get("name"))
        gl = m.get("score_calidad")
        # Se resalta cuando el modelo está MUY abajo en el global: es el caso que la
        # página existe para mostrar — bueno en este eje, escondido por el promedio.
        total = len(_PUESTO_GLOBAL) or 1
        clase = ' class="contraste"' if pg and rank <= 5 and pg > total * 0.5 else ""
        return (f"<tr><td>{rank}</td><td>{nm}</td><td>{relevant:.1f}</td>"
                f"<td>{gl if gl is not None else '—'}</td>"
                f"<td{clase}>{f'#{pg} de {total}' if pg else '—'}</td>"
                f"<td>{fmt_cost(m)}</td><td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")
    # Ranking por pilar/costo/open_source: la columna que ORDENA primero, después los
    # pilares como contexto. La columna que ordena tiene que estar: sin ella el lector ve
    # un puesto que no puede verificar contra nada de lo que la tabla le muestra.
    global_col = (f"<td><strong>{relevant:.1f}</strong></td>" if cfg["criterion"] == "pillar"
                  else f"<td>{m.get('score_global',0):.2f}</td>")
    return (f"<tr><td>{rank}</td><td>{nm}</td>{global_col}"
            f"<td>{pcell(m,'Coding')}</td><td>{pcell(m,'Contenido')}</td>"
            f"<td>{pcell(m,'Razonamiento')}</td><td>{pcell(m,'Agentes')}</td>"
            f"<td>{fmt_cost(m)}</td><td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")


def pcell(m, p):
    """Celda de pilar = CALIDAD en ese pilar (capacidad), no el compuesto con costo.

    Antes mostraba score_by_pillar (compuesto): la fila decía 7.1 para un modelo cuya
    calidad real escribiendo era 9.17. La tabla contradecía su propio encabezado.
    """
    v = pillar_quality(m, p)
    return f"{v:.1f}" if v > 0 else "—"


def cost_for_calls(m, calls=1000, in_tok=300, out_tok=1500):
    """Costo estimado en USD para N calls con los tokens por call por defecto del benchmark."""
    if not m:
        return 0.0
    cost_per_call = (in_tok * (m.get("cost_input_per_M") or 0) + out_tok * (m.get("cost_output_per_M") or 0)) / 1_000_000
    return cost_per_call * calls


def fmt_usd(n):
    if n >= 100:
        return f"${n:,.0f}"
    return f"${n:.2f}"


def reading_guide(cfg, ranked):
    top1 = ranked[0]
    second = ranked[1] if len(ranked) > 1 else None
    diff = score_for(top1, cfg) - score_for(second, cfg) if second else 0
    s1 = score_for(top1, cfg)
    if diff >= 0.5:
        gap_text = f"<strong>{esc(top1.get('name'))}</strong> lidera con una ventaja clara ({s1:.1f}/10 vs {score_for(second, cfg):.1f}/10)"
    elif diff >= 0.2:
        gap_text = f"<strong>{esc(top1.get('name'))}</strong> lidera, pero la diferencia con el segundo es pequeña ({s1:.1f}/10 vs {score_for(second, cfg):.1f}/10)"
    else:
        gap_text = f"hay empate técnico en la cima (todos rondan los {s1:.1f}/10): el mejor depende de tu prioridad"
    cases = ", ".join(cfg["use_cases"])
    return f"""<section>
  <h2>Cómo interpretar este ranking de {esc(cfg['what'])}</h2>
  <p>Este ranking no mide "inteligencia general" ni el score global ponderado. Mide qué modelo rinde mejor para
  <strong>{esc(cfg['what'])}</strong> en casos reales: {cases}. El orden depende únicamente del score de esa
  tarea puntual, no del costo, la velocidad ni la latencia.</p>
  <p>En esta dimensión {gap_text}. Eso no significa que sea el único
  válido: si tu prioridad es costo, velocidad o privacidad, el orden puede cambiar. El score global del benchmark
  pondera calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%, pero acá estamos mirando solo la calidad de la
  tarea. Ajusta esos pesos en la <a href="/">calculadora</a> para tu caso.</p>
  <p>Los modelos que aparecen tienen al menos 50 runs, lo que reduce el ruido de outlier con poca muestra.</p>
</section>"""


def top3_explained(cfg, ranked):
    parts = []
    for i, m in enumerate(ranked[:3], 1):
        score = score_for(m, cfg)
        provider = esc(m.get("provider", ""))
        oss = "open source" if m.get("open_source") else "propietario"
        if i == 1:
            angle = "Es la opción a vencer en esta dimensión"
        elif i == 2:
            angle = "Es la alternativa más sólida si el primero no encaja en tu stack"
        else:
            angle = "Es una tercera opción competitiva, especialmente si valoras otro factor además de la calidad pura"
        closing = ". Tiene pesos abiertos, así que puedes correrlo en varios providers o local." if m.get('open_source') else ". Es propietario, pero puede valer la pena si ya integraste su ecosistema."
        parts.append(f"""  <h3>{i}. {esc(m.get('name'))} — {score:.1f}/10</h3>
  <p>{esc(m.get('name'))} ({provider}, {oss}) cuesta {fmt_cost(m)} por millón de tokens y rinde a
  {round(m.get('tokens_per_second') or 0)} tok/s. Su score en {esc(score_label(cfg))} es {score:.1f}/10.
  {angle}{closing}</p>""")
    return f"""<section>
  <h2>Top 3 explicado: por qué están arriba</h2>
{chr(10).join(parts)}
</section>"""


def cost_comparison(cfg, ranked):
    top3 = ranked[:3]
    rows = []
    for m in top3:
        cost_1k = cost_for_calls(m, 1000)
        cost_10k = cost_for_calls(m, 10000)
        rows.append(f"<tr><td>{esc(m.get('name'))}</td><td>{fmt_cost(m)}</td><td>{fmt_usd(cost_1k)}</td><td>{fmt_usd(cost_10k)}</td></tr>")
    return f"""<section class="results">
  <div class="results-header"><h2>Costo real para volumen</h2></div>
  <p>Estimación para 1.000 y 10.000 calls/mes (asumiendo 300 tokens de input y 1.500 de output por call, promedio del benchmark):</p>
  <div class="table-scroll"><table class="results-table">
    <thead><tr><th scope="col">Modelo</th><th scope="col">$ por M tokens</th><th scope="col">1.000 calls/mes</th><th scope="col">10.000 calls/mes</th></tr></thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table></div>
  <p class="meta">Para volumen alto, un modelo 2× más barato puede ahorrarte más de lo que pierdes en calidad. Valida con tu caso real en la <a href="/">calculadora</a>.</p>
</section>"""


def frontier_in_dimension(cfg, models):
    """Menciona dónde quedan los modelos frontier en esta dimensión."""
    ranked = rank_models(models, cfg)
    by_name = {}
    for label, patterns in FRONTIER_PATTERNS.items():
        for m in models:
            blob = f"{m.get('name','')} {m.get('key','')}".lower()
            if any(p in blob for p in patterns):
                if m.get("score_global") and (m.get("runs") or 0) >= 50:
                    by_name[label] = m
                    break
    if not by_name:
        return ""
    # Escaneable: nombre | posicion | calidad | precio. Antes era una lista de
    # bullets con los numeros embebidos en prosa ("queda #74 con 7.6/10. Cuesta
    # $10.00 / $50.00 por millon.") — siete lineas asi son imposibles de comparar
    # de un vistazo, que es exactamente para lo que existe el bloque.
    rows = sorted(by_name.items(), key=lambda kv: -score_for(kv[1], cfg))
    items = []
    for label, m in rows:
        pos = next((i + 1 for i, x in enumerate(ranked) if x.get("key") == m.get("key")), None)
        score = score_for(m, cfg)
        if pos and pos <= 10:
            place = f'<span class="frontier-pos frontier-top">#{pos} · top 10</span>'
        elif pos:
            place = f'<span class="frontier-pos">#{pos}</span>'
        else:
            place = '<span class="frontier-pos">sin cobertura</span>'
        items.append(
            f'<li><strong>{esc(label)}</strong>{place}'
            f'<span class="frontier-score">{score:.1f}/10</span>'
            f'<span class="frontier-cost">{fmt_cost(m)} por millón</span></li>'
        )
    return f"""<section>
  <h2>¿Dónde quedan los modelos frontier?</h2>
  <p>Mucha gente llega buscando GPT-5.6, Claude Opus/Fable o Grok. Acá está dónde quedan
  <strong>en esta tarea concreta</strong>, ordenados por calidad — no por lo que cuestan:</p>
  <ul class="frontier-list">
    {''.join(items)}
  </ul>
  <p class="meta">Si te interesa una comparación cara a cara, prueba las <a href="/gpt-5.6-vs-claude-opus-4-8/">comparativas específicas</a> o ajusta los pesos en la calculadora.</p>
</section>"""


RELATED_TITLES = {
    "modelos-n8n": "Modelos para N8N",
    "mejor-llm-para-tool-calling": "Mejor LLM para tool calling",
    "mejor-llm-para-agentes": "Mejor LLM para agentes",
    "mejor-llm-para-n8n": "Mejor LLM para N8N",
    "mejor-llm-para-programar": "Mejor LLM para programar",
    "mejor-llm-para-razonamiento": "Mejor LLM para razonamiento",
    "mejor-llm-para-contenido": "Mejor LLM para contenido",
    "mejor-llm-para-resumir-textos": "Mejor LLM para resumir textos",
    "mejor-llm-barato": "LLM más baratos",
    "mejor-llm-open-source": "Mejor LLM open source",
    "mejor-llm-en-espanol": "Mejor LLM en español",
    "modelos-baratos-emprendedores": "Modelos baratos para emprendedores",
    "modelos-open-source-local": "Modelos open-source local",
    "alternativas-claude": "Alternativas a Claude",
    "alternativas-chatgpt": "Alternativas a ChatGPT",
    "alternativas-gemini": "Alternativas a Gemini",
    "alternativas-deepseek": "Alternativas a DeepSeek",
    "qwen-vs-llama": "Qwen vs Llama",
    "gpt-5.6-vs-claude-opus-4-8": "GPT-5.6 vs Claude Opus 4.8",
}


def related_pages(cfg):
    links = cfg.get("related", [])
    if not links:
        return ""
    items = []
    for slug in links:
        title = RELATED_TITLES.get(slug, slug.replace("-", " ").title())
        items.append(f'<li><a href="/{slug}/">{esc(title)}</a></li>')
    return f"""<section>
  <h2>Comparaciones relacionadas</h2>
  <ul>
    {''.join(items)}
  </ul>
</section>"""


def analysis(cfg, ranked):
    top1 = ranked[0]
    s1 = score_for(top1, cfg)
    why = (f"<strong>{esc(top1.get('name'))}</strong> encabeza el ranking para {cfg['case']} "
           f"con {s1:.1f}/10, a {fmt_cost(top1)} por millón de tokens "
           f"({round(top1.get('tokens_per_second') or 0)} tok/s, {esc(top1.get('provider',''))}).")
    w = get_meta().get("default_weights", {})
    q = fmt_pct(w.get("quality", 0.7))
    co = fmt_pct(w.get("cost", 0.15))
    sp = fmt_pct(w.get("speed", 0.075))
    la = fmt_pct(w.get("latency", 0.075))
    ver = get_meta().get("scoring_version", "v4.0")
    return f"""<section>
  <h2>Por qué {esc(top1.get('name'))} lidera</h2>
  <p>{why} Recuerda que el score global {ver} pondera calidad {q}% + costo {co}% + velocidad {sp}% + latencia {la}% — no es solo "el más inteligente",
  sino el que mejor rinde en producción para este caso.</p>
  <h3>Cuándo conviene este modelo</h3>
  <ul>
    <li>Si tu prioridad es <strong>{esc(cfg['what'])}</strong> y quieres el mejor score de esta dimensión.</li>
    <li>Si tu volumen es medio/bajo (cientos a miles de calls/mes) y el costo no domina.</li>
    <li>{'Si quieres pesos abiertos y flexibilidad de provider.' if top1.get('open_source') else 'Si ya usas este provider o no te importa el lock-in.'}</li>
  </ul>
  <p class="meta">El "mejor" depende de tu prioridad real (calidad, costo o velocidad). Ajusta esos pesos en la <a href="/">calculadora</a> para tu caso.</p>
</section>"""


def faq(cfg, ranked):
    top1 = ranked[0]
    tests_k = fmt_k(get_counts()["total_runs"])
    label = cfg['case'].split('(')[0].strip()
    qas = [
        (
            f"¿Cuál es el mejor LLM para {label} hoy?",
            f"Según nuestro benchmark, {top1.get('name')} lidera en {cfg['what']} con {score_for(top1, cfg):.1f}/10, "
            "pero el ranking completo te deja elegir según tu presupuesto y prioridad. No hay un único 'mejor' universal.",
            f"Según nuestro benchmark, <strong>{esc(top1.get('name'))}</strong> lidera en {esc(cfg['what'])} "
            f"con {score_for(top1, cfg):.1f}/10, pero el ranking completo te deja elegir según tu presupuesto y prioridad. "
            "No hay un único 'mejor' universal.",
        ),
        (
            f"¿Por qué un modelo barato gana en {cfg['what']} a modelos frontier?",
            "Porque el score global pondera calidad, costo, velocidad y latencia. Un modelo más barato y rápido puede tener "
            "mejor valor de producción que uno caro y lento, aunque el frontier tenga más capacidad bruta en algunas tareas.",
            "Porque el score global pondera calidad, costo, velocidad y latencia. Un modelo más barato y rápido puede tener "
            "mejor valor de producción que uno caro y lento, aunque el frontier tenga más capacidad bruta en algunas tareas.",
        ),
        (
            f"¿Para qué casos NO sirve el #1 de este ranking?",
            f"Si tu caso es muy distinto a {cfg['what']} —por ejemplo, necesitas razonamiento profundo, tool calling crítico o privacidad extrema— "
            "probablemente haya mejores opciones. Usa la calculadora para ajustar pesos por caso.",
            f"Si tu caso es muy distinto a {esc(cfg['what'])} —por ejemplo, necesitas razonamiento profundo, tool calling crítico o privacidad extrema— "
            "probablemente haya mejores opciones. Usa la <a href=\"/\">calculadora</a> para ajustar pesos por caso.",
        ),
        (
            "¿De dónde salen estos datos?",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en GitHub.",
            f"De un benchmark abierto con {tests_k} runs reales y LLM-as-Judge local (Phi-4, Microsoft, sin conflicto de interés). "
            "Código y resultados en <a href=\"https://github.com/ctala/ai-benchmarks-alternativos\" target=\"_blank\" rel=\"noopener\">GitHub</a>.",
        ),
        (
            "¿Cada cuánto se actualiza?",
            "Con cada lote de modelos nuevos. La fecha de actualización está al inicio. Filtra la versión más reciente en la calculadora.",
            "Con cada lote de modelos nuevos. La fecha de actualización está al inicio. Filtra la versión más reciente en la <a href=\"/\">calculadora</a>.",
        ),
    ]
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a_plain}}
            for q, a_plain, _ in qas
        ],
    }
    schema_script = f'<script type="application/ld+json">\n{json.dumps(schema, ensure_ascii=False, indent=2)}\n</script>'
    details = "\n  ".join(
        f'<details><summary><strong>{esc(q)}</strong></summary>\n  <p>{a_html}</p></details>'
        for q, _, a_html in qas
    )
    return f"""<section class="faq">
  {schema_script}
  <h2>Preguntas frecuentes sobre {esc(cfg['what'])}</h2>
  {details}
</section>"""


def dataset_schema(cfg, ranked):
    """Schema.org Dataset para reforzar indexación de datos del ranking."""
    c = get_counts()
    return {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": f"Ranking de {esc(cfg['what'])} - Benchmark Alternativos",
        "description": f"Ranking de modelos LLM para {esc(cfg['what'])} basado en {fmt_k(c['total_runs'])} runs reales.",
        "url": f"{SITE}/{cfg['slug']}/",
        "creator": {"@type": "Person", "name": "Cristian Tala", "url": "https://cristiantala.com"},
        "datePublished": existing_published(f"{SITE}/{cfg['slug']}/"),
        "dateModified": date.today().isoformat(),
        "license": "https://opensource.org/licenses/MIT",
        "distribution": [
            {"@type": "DataDownload", "encodingFormat": "application/json",
             "contentUrl": "https://github.com/ctala/ai-benchmarks-alternativos/tree/main/benchmarks/results"}
        ],
    }


def funnel_block():
    """Cierre de la decision -> comunidad. NO es un banner: es el paso siguiente.

    El visitante llega buscando que modelo usar, obtiene el veredicto... y hasta hoy
    el unico CTA era "Ir a la calculadora" (interno). El link a la comunidad vivia
    solo en el nav. El funnel moria justo donde el lector estaba mas comprometido.

    Regla dura del proyecto: NO inventar perks. Aca se ofrece solo lo que existe --
    la comunidad es gratis (tier Standard $0) y el ranking se recalcula con cada lote.
    Nada mas.
    """
    return """  <section class="funnel">
    <h2>Antes de migrar, haz esto</h2>
    <p>Ya tienes un candidato. No lo cambies a ciegas: toma los dos primeros de la tabla y pásales
    <strong>cinco prompts reales tuyos</strong>, de los que ya corres en producción. Un benchmark
    general te dice quién arranca adelante; <strong>tu caso decide quién gana</strong>. Son veinte
    minutos y te ahorran una migración equivocada.</p>
    <p class="funnel-note">Y una advertencia sobre este ranking: se recalcula con cada lote de modelos
    nuevos. Como el score de cada modelo es <em>relativo a todos los demás</em>, un modelo nuevo mueve
    a todos. Lo que hoy es el #1 puede no serlo el mes que viene.</p>
    <p><a href="https://www.skool.com/cagala-aprende-repite?utm_source=benchmarks&amp;utm_medium=pseo&amp;utm_campaign=ranking" target="_blank" rel="noopener" class="cta-primary">
    Ver la comunidad →</a></p>
    <p class="funnel-fine">Cada vez que corro un lote nuevo, publico el recálculo ahí — con los datos
    crudos y lo que cambió de lugar. Es también donde hay gente tomando esta misma decisión.
    Entrar es gratis.</p>
  </section>
"""


def _verdict_data(cfg, models):
    """Calcula el veredicto UNA vez. Lo consumen el bloque Y la tabla (para marcar
    las filas), asi que es literalmente imposible que se contradigan entre si.

    Solo emitimos veredicto donde el criterio de la banda COINCIDE con el de la
    pagina. Antes se emitia siempre, con calidad GLOBAL, y el resultado era que
    /tool-calling/, /open-source/, /barato/ y /en-espanol/ mostraban los cuatro el
    mismo veredicto ("usa DeepSeek V4 Flash"), ignorando su propio criterio. En
    /open-source/ el "villano" era GPT-5.6 Sol, propietario, que no deberia ni
    figurar ahi. Donde no puedo sostener el veredicto, no lo invento: lo omito.
    """
    from bands import verdict as _verdict

    crit = cfg.get("criterion")
    if crit not in ("pillar", "open_source"):
        return None
    pool = [m for m in models if (m.get("runs") or 0) >= 50]
    if crit == "open_source":
        pool = [m for m in pool if m.get("open_source")]
    pil = cfg.get("pillar") if crit == "pillar" else None
    v = _verdict(pool, pil, calls_per_month=3000)
    return v if (v and "best" in v) else None


def verdict_block(cfg, models):
    """El veredicto, ANTES de la tabla. La tabla pasa a ser evidencia, no output.

    Antes, estas paginas terminaban en una tabla muda y diferian la decision al
    lector ("depende de tu caso", "ajustalo en la calculadora"). El emprendedor
    se iba con datos y sin decision.

    Lo que hace posible decidir: los modelos de la cima EMPATAN estadisticamente
    en calidad (sus IC95 no se distinguen), asi que la decision real es de COSTO.
    """
    v = _verdict_data(cfg, models)
    if not v:
        return ""

    pil = cfg.get("pillar") if cfg.get("criterion") == "pillar" else None
    leader, b = v["leader"], v["best"]
    same = leader["name"] == b["name"]

    # Banda demasiado ancha => el instrumento no separa. Se dice.
    if v.get("inconclusive"):
        pct = round(v["band_share"] * 100)
        return f"""  <section class="verdict verdict-open">
    <h2>La respuesta corta</h2>
    <p class="verdict-lead">Acá el benchmark <strong>no logra separar a los modelos</strong>:
    {v['band_size']} de {v['pool_size']} ({pct}% del catálogo) quedan dentro del margen de error
    en esta tarea. Cuando la medición no distingue, <strong>lo honesto es decirlo</strong>, no
    inventar un ganador.</p>
    <p class="verdict-lead">Con esa salvedad: el de mayor calidad medida es
    <strong>{esc(leader['name'])}</strong> ({leader['quality']:.2f}/10). Si el presupuesto manda,
    <strong>{esc(b['name'])}</strong> queda dentro del mismo grupo por
    <strong>≈${b['cost_month']:,.0f}/mes</strong>. Pero acá, más que nunca:
    <strong>prueba los dos con tus propios prompts</strong>: este benchmark no va a decidir por ti.</p>
  </section>
"""

    cards = [
        f"""<div class="verdict-card verdict-best">
        <span class="verdict-tag">{'El mejor, y además el más barato' if same else 'La mejor compra'}</span>
        <strong>{esc(b['name'])}</strong>
        <span class="verdict-cost">≈${b['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">calidad {b['quality']:.2f}/10{'' if same else f" · empata con {esc(leader['name'])}, que encabeza la tabla, y cuesta menos"}</span>
        {f'<span class="verdict-sub">También: {esc(b["sub"])}</span>' if b.get("sub") else ''}
      </div>"""
    ]
    if not same:
        cards.append(f"""<div class="verdict-card">
        <span class="verdict-tag">La mejor calidad medida</span>
        <strong>{esc(leader['name'])}</strong>
        <span class="verdict-cost">≈${leader['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">calidad {leader['quality']:.2f}/10 · es el #1 de la tabla. La diferencia con el de arriba está dentro del margen de error</span>
        {f'<span class="verdict-sub">También: {esc(leader["sub"])}</span>' if leader.get("sub") else ''}
      </div>""")
    if "priciest" in v and v["priciest"]["name"] not in (b["name"], leader["name"]):
        p = v["priciest"]
        cards.append(f"""<div class="verdict-card verdict-costly">
        <span class="verdict-tag">Lo que te ahorras</span>
        <strong>{esc(p['name'])}</strong>
        <span class="verdict-cost">≈${p['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">{p['times']}× más caro por {p['quality_gap']:+.2f} de calidad — dentro del margen de error</span>
        {f'<span class="verdict-sub">También: {esc(p["sub"])}</span>' if p.get("sub") else ''}
      </div>""")
    if "local" in v:
        l = v["local"]
        cards.append(f"""<div class="verdict-card">
        <span class="verdict-tag">Si tienes hardware propio</span>
        <strong>{esc(l['name'])}</strong>
        <span class="verdict-cost">≈${l['cost_month']:,.0f}/mes</span>
        <span class="verdict-note">calidad {l['quality']:.2f}/10 · corre local, sin API</span>
      </div>""")

    preset = {"Agentes": "agentes", "Coding": "coding",
              "Contenido": "contenido", "Razonamiento": "razonamiento"}.get(pil or "", "")
    qs = f"?preset={preset}&amp;calls=3000" if preset else "?calls=3000"

    lead = (f"<strong>{v['band_size']} modelos empatan</strong> en calidad para esta tarea: "
            f"la diferencia entre ellos es más chica que el margen de error de la medición. "
            f"Cuando la calidad empata, <strong>la decisión es de precio</strong>.")
    if same:
        lead = (f"<strong>{esc(leader['name'])}</strong> encabeza la tabla en calidad "
                f"<em>y</em> es el más barato de los {v['band_size']} que empatan con él. "
                f"Caso fácil: no hay que elegir entre calidad y precio.")

    return f"""  <section class="verdict">
    <h2>La respuesta corta</h2>
    <p class="verdict-lead">{lead}</p>
    <div class="verdict-grid">
      {''.join(cards)}
    </div>
    <p class="verdict-foot">Cálculo sobre <strong>3.000 llamadas/mes</strong> (≈100 por día: una respuesta
    de agente o un borrador de texto por llamada). ¿Otro volumen, o te importa más la velocidad?
    Ajusta los pesos en la <a href="/{qs}">calculadora</a>.
    Los modelos citados están en la tabla de abajo, marcados.</p>
  </section>
"""


# ¿QUÉ PÁGINAS LLEVAN LA SEGUNDA TABLA? Lo decide el dato, no la intuición.
#
# La v1 la activaba a mano en agentes y n8n con el argumento «ahí el eje satura». Medido
# el 17-ago-2026, ese argumento era falso: NINGÚN corte satura (1-3% de notas perfectas).
# Y el criterio correcto —cuánto se parecen los dos órdenes— decía lo contrario:
#
#     mejor-llm-en-espanol      +0,244   ← donde MÁS aporta, y no la tenía
#     mejor-llm-para-contenido  +0,244
#     mejor-llm-para-agentes    +0,826   ← donde la había puesto
#
# Si ordenar por capacidad y por capacidad-precio dan órdenes PARECIDOS, la segunda tabla
# repite la primera y sobra — que es por lo que v4.1 revirtió una con r=0,943. Si dan
# órdenes distintos, cada una responde una pregunta distinta y las dos valen.
UMBRAL_SEGUNDA_TABLA = 0.70

# Excepciones con motivo: no toda página con correlación baja la necesita.
SIN_SEGUNDA_TABLA = {
    # Ya ordena por precio: sería la misma página dos veces.
    "mejor-llm-barato",
    # Acá el precio NO debe decidir. Si tu agente procesa credenciales de clientes, el
    # ahorro no compra nada — es el único eje donde pagar de más sí compra algo medible.
    "mejor-llm-seguro-datos-clientes",
}


def _lleva_segunda_tabla(cfg, models):
    """True si ordenar por capacidad y por capacidad-precio dan órdenes distintos."""
    if cfg["slug"] in SIN_SEGUNDA_TABLA:
        return False
    from scoring import cost_score_log
    vals = [(score_for(m, cfg), m) for m in models if score_for(m, cfg)]
    if len(vals) < 10:
        return False
    por_q = sorted(vals, key=lambda x: -x[0])
    por_v = sorted(vals, key=lambda x: -(0.7 * x[0]
                                         + 0.3 * cost_score_log(cost_for_calls(x[1]) / 1000.0)))
    rq = {id(m): i for i, (_, m) in enumerate(por_q)}
    rv = {id(m): i for i, (_, m) in enumerate(por_v)}
    xs = [rq[k] for k in rq]
    ys = [rv[k] for k in rq]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = (sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5
    return bool(den) and (num / den) < UMBRAL_SEGUNDA_TABLA


def tabla_valor(cfg, models):
    """SEGUNDA TABLA: calidad por lo que cuesta. Solo donde el eje satura.

    POR QUÉ (17-ago-2026). Cristian, mirando /mejor-llm-para-agentes/: *"tendría dos
    tablas: 100% calidad, y un ponderado costo-calidad"*. Lo dijo después de ver que el
    top lo ocupaban tres Claude a $23-39 por mil llamadas y que **Qwen 3.7 Flash no
    aparecía** — con la tarea real casi perfecta a **$0.20**, 190 veces más barato.

    Las dos tablas se justifican solas: el orden de una y otra correlaciona **+0,005**.
    No dicen lo mismo. (En v4.1 se revirtió una segunda tabla de «mejor valor» porque
    correlacionaba r=0,943 con la primera — ahí sí sobraba. La diferencia es que el eje
    agéntico **satura**: 36 de 75 modelos empatan en 1,00, y cuando media población
    empata, lo que decide es el precio.)

    La curva de costo es `cost_score_log`, la MISMA que ya usa el resto del repo. Inventar
    otra fórmula acá sería tener dos definiciones de «barato».
    """
    from scoring import cost_score_log
    vals = []
    for m in models:
        q = score_for(m, cfg)
        if not q:
            continue
        c = cost_for_calls(m) / 1000.0          # costo por llamada
        vals.append((0.7 * q + 0.3 * cost_score_log(c), q, m))
    vals.sort(key=lambda x: -x[0])
    filas = []
    for i, (v, q, m) in enumerate(vals[:8], 1):
        nm = f"<strong>{esc(m['name'])}</strong>" if i == 1 else esc(m["name"])
        filas.append(
            f"<tr><td>{i}</td><td>{nm}</td><td><strong>{v:.2f}</strong></td>"
            f"<td>{q:.1f}</td><td>{fmt_usd(cost_for_calls(m))}</td>"
            f"<td>{round(m.get('tokens_per_second') or 0)} tok/s</td></tr>")
    return f"""<section class="results">
    <div class="results-header">
      <h2>La misma capacidad, por lo que cuesta</h2>
      <p class="meta">La tabla de arriba ordena por capacidad y nada más — es la respuesta a
      «¿quién lo hace mejor?». Ésta responde la otra pregunta, la de producción:
      <strong>de los que pueden, cuál conviene</strong>. Fórmula: 70% capacidad + 30% precio,
      con la misma curva de costo que usa el resto del benchmark.</p>
      <p class="meta">Vale la pena mirarla porque <strong>este eje satura</strong>: casi la
      mitad de los modelos medidos resuelven la tarea perfecta. Cuando tantos empatan en
      capacidad, lo que decide es el precio — y los dos órdenes casi no se parecen.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead><tr><th scope="col">#</th><th scope="col">Modelo</th>
      <th scope="col">Calidad×precio</th><th scope="col">{esc(score_label(cfg))}</th>
      <th scope="col">$/1.000 llamadas</th><th scope="col">Velocidad</th></tr></thead>
      <tbody>
        {chr(10) + "        ".join(filas)}
      </tbody>
    </table></div>
  </section>"""


def render_ranking(cfg, models):
    all_ranked = rank_models(models, cfg)
    if not all_ranked:
        return None
    ranked = all_ranked[:8]

    # Los modelos que el veredicto cita DEBEN estar en la tabla, marcados. Si el
    # recomendado no entra al top-8 por calidad (pasa: es el mas barato de la banda,
    # no el mas capaz), se INSERTA — porque el pie del veredicto promete que "los
    # modelos citados estan en la tabla de abajo" y esa promesa tiene que ser cierta.
    v = _verdict_data(cfg, models)
    badges = {}
    if v:
        if v.get("best"):
            badges[v["best"]["name"]] = "← la mejor compra"
        if v.get("priciest") and v["priciest"]["name"] not in badges:
            badges[v["priciest"]["name"]] = "← el caro"
        names = {m.get("name") for m in ranked}
        for extra in [v.get("best"), v.get("priciest")]:
            if extra and extra["name"] not in names:
                m = next((x for x in all_ranked if x.get("name") == extra["name"]), None)
                if m is not None:
                    ranked.append(m)
                    names.add(extra["name"])

    url = f"{SITE}/{cfg['slug']}/"
    tests_k = fmt_k(get_counts()["total_runs"])
    desc = (f"{cfg['h1']} con {tests_k} runs reales: ranking por {cfg['case']}. "
            f"Incluye costos para volumen, análisis del top 3 y posición de modelos frontier. #1: {ranked[0].get('name')}.")
    today = date.today().isoformat()
    # El numero de fila es la posicion REAL en el ranking completo, no el indice
    # de la tabla: si insertamos a alguien del puesto 24, tiene que decir 24.
    pos_of = {m.get("name"): i + 1 for i, m in enumerate(all_ranked)}
    rows = "\n        ".join(
        row_ranking(pos_of.get(m.get("name"), i + 1), m, cfg, top=(i == 0), badges=badges)
        for i, m in enumerate(ranked)
    )
    dataset_ld = json.dumps(dataset_schema(cfg, ranked), ensure_ascii=False, indent=2)
    body = f"""  <section class="hero">
    <h1>{esc(cfg['h1'])}</h1>
    <p class="lead">{cfg['lead']}</p>
    <p class="meta">Última actualización: {today} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos en GitHub</a></p>
  </section>
{verdict_block(cfg, models)}
  <section class="results">
    <div class="results-header">
      <h2>Ranking: {esc(cfg['h1'])}</h2>
      <p class="meta">{({'pillar':'Ordenado por <strong>capacidad pura en esta tarea</strong>: solo calidad, sin ponderar costo ni velocidad. Quien busca el mejor para esta tarea pregunta quién la hace mejor — el precio se muestra aparte, para decidir después.','suite':'Ordenado por calidad en esta suite, sin ponderar costo ni velocidad.','cost':'Ordenado por costo total (input + output) con score global ≥ 6,8.','open_source':'Ordenado por score global, filtrando solo modelos open source.'}[cfg['criterion']])}</p>
    </div>
    {table_head(cfg)}
      <tbody>
        {rows}
      </tbody>
    </table></div>
    <p class="meta">Filtra por presupuesto, calidad mínima o tarea en la <a href="/">calculadora interactiva</a>.</p>
  </section>
  {tabla_valor(cfg, all_ranked) if _lleva_segunda_tabla(cfg, all_ranked) else ""}
  {reading_guide(cfg, ranked)}
  {top3_explained(cfg, ranked)}
  {analysis(cfg, ranked)}
  {cost_comparison(cfg, ranked)}
  {frontier_in_dimension(cfg, models)}
  {funnel_block()}
  {methodology()}
  {related_pages(cfg)}
  <script type="application/ld+json">
{dataset_ld}
  </script>
  {faq(cfg, ranked)}
  <section class="cta-block">
    <h2>Prueba la calculadora con tu caso real</h2>
    <p>Ajusta presupuesto, calidad mínima y tipo de tarea sobre 100+ modelos. En 30 segundos tienes tu ranking personalizado.</p>
    <a href="/" class="cta-primary">Ir a la calculadora →</a>
  </section>"""
    return page_shell(cfg["title"], desc, cfg["intent_kw"], url, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug")
    args = ap.parse_args()
    models = load_models()
    _cargar_puestos(models)   # puestos en el índice global, para la columna de contraste
    for cfg in RANKINGS:
        if args.slug and cfg["slug"] != args.slug:
            continue
        out = render_ranking(cfg, models)
        if not out:
            print(f"⚠️  {cfg['slug']}: sin modelos para el criterio")
            continue
        d = DOCS / cfg["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(out, encoding="utf-8")
        n = len(rank_models(models, cfg)[:8])
        print(f"✓ {cfg['slug']}: top {n} → docs/{cfg['slug']}/index.html")


if __name__ == "__main__":
    main()
