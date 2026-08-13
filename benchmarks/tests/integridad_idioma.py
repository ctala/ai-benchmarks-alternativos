"""
Integridad de idioma — que el texto salga ENTERO en el idioma pedido.

POR QUÉ EXISTE ESTA SUITE (12-ago-2026)
---------------------------------------
Fallo real de producción, no hipotético: en el pipeline de noticias de Eco un modelo
escribía en español perfecto y, en medio de un artículo, metía una palabra en chino.
Para un workflow que **publica sin revisión humana** eso no es un defecto menor: es un
artículo quemado.

Y el benchmark ya tenía la evidencia guardada sin saberlo. Al implementar el scorer
`language_check` (12-ago-2026) se re-puntuaron 755 respuestas viejas y aparecieron dos
fugas reales que llevaban meses en el repo sin que nada chillara:

    nim-step-3.5-flash → 硬件 ("hardware")     en un artículo en español
    mimo-v2.5-or       → 直接 ("directamente") en otro

Había UN test de idioma (`news_spanish_only`, dentro de `news_seo_writing`) y su score
caía al `else: return 5.0` porque el tipo `language_check` no tenía verificador. O sea:
la trampa existía, la respuesta estaba guardada, y el instrumento decía 5,00.

POR QUÉ SUITE NUEVA Y NO MÁS TESTS EN `news_seo_writing`
--------------------------------------------------------
Agregar tests a una suite existente le baja la cobertura a los 119 modelos ya medidos.
Con `MIN_SUITE_COVERAGE = 0.80`, meter 3 tests nuevos en una suite de 5 dejaría a todos
en 62% y el gate excluiría la suite **para todo el mundo**. Suite nueva = nadie pierde
cobertura y los que la rindan estrenan el eje.

DISEÑO — las tres reglas que ya se pagaron
------------------------------------------
1. **No inducir el resultado.** Ninguna instrucción dice "no uses caracteres chinos" ni
   "responde solo en español" más de lo que diría un prompt real. Un test que avisa de
   la trampa no mide nada: mide obediencia.
2. **Lo único que varía es el material.** El idioma del insumo (inglés, chino, mixto) es
   la variable; la tarea es siempre la misma.
3. **Verdad objetiva.** `language_check` es binario para CJK: un solo carácter y es 0.
   No hay juez opinando si "se entiende igual".

EJE PROPIO, FUERA DE LA CALIDAD TITULAR (por ahora)
---------------------------------------------------
Se expone como dimensión separada, igual que long-context y seguridad. Meterla en la
calidad titular reordenaría el ranking, y el runbook es explícito: eso no se hace sin
decisión deliberada. Queda como candidato a promoverse en la próxima versión.
"""

SYSTEM_PROMPT_ES = """Eres un periodista que escribe para un medio digital latinoamericano.
Escribes para lectores hispanohablantes de México, Chile, Argentina, Colombia y España.
Tu trabajo es tomar material de origen y redactar en español neutro, claro y directo."""


TESTS = [
    {
        "name": "fuente_inglesa_articulo_largo",
        "description": "Artículo largo en español desde material en inglés (el caso Eco real)",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_ES},
            {"role": "user", "content": """Redacta una nota de 700-900 palabras a partir de este material:

TITLE: "Nebius Deploys 200,000 Blackwell GPUs Across Three New Data Centers"
SOURCE: "Amsterdam-based Nebius announced the deployment of 200,000 NVIDIA Blackwell
GPUs across three new data centers in Finland, Israel and Kansas City. The company said
the buildout represents $3.2 billion in capital expenditure and will nearly triple its
inference capacity. CEO Arkady Volozh said the expansion targets 'the inference
bottleneck that is throttling agentic workloads in production'. The Finland site will
run on hydroelectric power. Nebius reported $412 million in annualized revenue run-rate,
up from $170 million a year earlier, and said 60% of new capacity is already contracted
under multi-year agreements with enterprise customers."

Estructura: titular, entradilla, desarrollo con subtítulos, cierre con implicancias
para la región."""},
        ],
        "criteria": {
            "min_words": 600,
            "required_sections": ["Nebius", "GPU"],
            "language": "es",
        },
        # La trampa: el 100% del material es inglés y el texto pedido es largo. La fuga
        # de idioma aparece cuando el modelo lleva rato generando, no en la primera línea.
        "expected_answer": {
            "type": "language_check",
            "required_language": "es",
            "reject_cjk": True,
            "reject_long_english": True,
        },
    },
    {
        "name": "fuente_china_sin_avisar",
        "description": "Material de origen en chino; la salida debe ser español limpio",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_ES},
            {"role": "user", "content": """Redacta una nota de 400-600 palabras con este material:

标题：智谱AI发布GLM-5.2，上下文窗口扩展至100万tokens
内容：北京智谱华章科技有限公司今日发布了GLM-5.2大语言模型。该模型的上下文窗口从
20万tokens扩展到100万tokens，推理成本较上一代下降了约40%。公司表示，新模型在代码
生成和工具调用方面有显著提升。GLM-5.2已在多个云平台上线，面向企业客户提供API服务。
公司称已有超过3000家企业客户使用其模型服务。

Escribe la nota para un lector latinoamericano que no lee chino."""},
        ],
        "criteria": {
            "min_words": 350,
            "required_sections": ["GLM"],
            "language": "es",
        },
        # La trampa más dura: el material está ENTERO en el idioma que no debe filtrarse.
        # Copiar un nombre propio o una cifra tal cual es el error natural acá.
        "expected_answer": {
            "type": "language_check",
            "required_language": "es",
            "reject_cjk": True,
            "reject_long_english": True,
        },
    },
    {
        "name": "jerga_tecnica_densa",
        "description": "Tema técnico denso en inglés: ¿traduce o se pasa al inglés?",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_ES},
            {"role": "user", "content": """Explica en 400-500 palabras, para un fundador sin
formación técnica, qué significa este cambio y por qué le importa:

"Speculative decoding with a 1B draft model cuts time-to-first-token by 40% on 70B
targets, but only when the acceptance rate stays above 0.7. Below that, the verification
overhead dominates and you end up slower than greedy decoding. Batch size interacts
badly: at batch 32+ the draft model contends for the same KV cache bandwidth."

No uses viñetas, escribe en párrafos."""},
        ],
        "criteria": {
            "min_words": 350,
            "required_sections": ["tokens"],
            "language": "es",
        },
        # Un término técnico en inglés NO es una respuesta en inglés: el scorer usa
        # palabras funcionales (artículos, preposiciones), no vocabulario. Lo que castiga
        # es un párrafo entero que se pasó de idioma.
        "expected_answer": {
            "type": "language_check",
            "required_language": "es",
            "reject_cjk": True,
            "reject_long_english": True,
        },
    },
    {
        "name": "conversacion_mixta_es_en",
        "description": "El usuario mezcla español e inglés; la respuesta debe ser español",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_ES},
            {"role": "user", "content": """Necesito que me escribas el resumen ejecutivo, unas
450 palabras, de esto que me pasó el board. Some of it is in English, sorry:

"Q3 closed at $1.2M ARR, up 34% QoQ. Churn came down to 2.1% monthly from 3.8%. The
main driver was the onboarding revamp — activation within 7 days went from 41% to 68%.
CAC payback is now 11 months. We burned $340K in Q3 and have 14 months of runway.
The board wants a decision on whether to raise a bridge or push for profitability."

Dame el resumen y tu lectura de qué conviene."""},
        ],
        "criteria": {
            "min_words": 380,
            "required_sections": ["ARR"],
            "language": "es",
        },
        # Trampa de arrastre: cuando el usuario escribe mitad en inglés, muchos modelos
        # responden en inglés "por espejo". Es el caso más frecuente en soporte real.
        "expected_answer": {
            "type": "language_check",
            "required_language": "es",
            "reject_cjk": True,
            "reject_long_english": True,
        },
    },
]
