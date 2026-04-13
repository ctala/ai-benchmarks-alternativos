"""
Tests de redaccion de noticias SEO para ecosistemastartup.com
Simula el workflow real de N8N: extracto en ingles -> articulo completo en espanol.
"""

SYSTEM_PROMPT_NEWS = """Eres un periodista especializado en startups, tecnologia e innovacion en Latinoamerica.
Escribes para ecosistemastartup.com, un medio digital enfocado en el ecosistema emprendedor.

Reglas de redaccion:
- Escribes SIEMPRE en espanol, sin importar el idioma del input
- Tono: profesional pero accesible, informativo, con datos concretos
- Estructura: usa subtitulos H2 (## en markdown), nunca H1
- Incluye siempre una seccion "Que significa esto para tu startup"
- Cita fuentes verificables cuando menciones datos
- No inventes datos, cifras ni citas que no esten en el extracto proporcionado
- Termina con una conclusion que invite a la reflexion
- No uses cliches como "en la era digital", "revolucionario", "game changer"
- Incluye palabras clave SEO de forma natural, no forzada"""

TESTS = [
    {
        "name": "news_seo_article_full",
        "description": "Articulo completo de noticia SEO desde extracto en ingles",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_NEWS},
            {"role": "user", "content": """Escribe un articulo completo (1,500-2,500 palabras) basado en este extracto:

TITULO: "Mistral AI Raises $2B Series C, Launches Devstral for Coding"
EXTRACTO: "French AI startup Mistral AI has closed a $2 billion Series C round led by General Catalyst, valuing the company at $15 billion. The round included participation from Lightspeed Venture Partners and Andreessen Horowitz. Alongside the funding, Mistral announced Devstral, a new open-source coding model under Apache 2.0 license that scores 7.65 on the SWE-Bench coding benchmark, outperforming models from OpenAI and Google. CEO Arthur Mensch stated that open-source AI is critical for European sovereignty. The company now has 800 employees across Paris, London, and San Francisco."
FUENTE: TechCrunch, April 2026

El articulo debe incluir:
- Titulo SEO (max 60 caracteres)
- Al menos 4 subtitulos H2
- Seccion "Que significa esto para tu startup"
- Fuentes citadas
- Conclusion
- Meta descripcion (max 155 caracteres)
- 5 palabras clave SEO sugeridas"""},
        ],
        "criteria": {
            "min_words": 1200,
            "required_sections": ["##", "startup", "fuente", "conclusion", "meta", "palabra"],
            "language": "es",
        },
    },
    {
        "name": "news_json_output_strict",
        "description": "Salida JSON estricta para workflow N8N (7 claves)",
        "messages": [
            {"role": "system", "content": "Eres un sistema de procesamiento de noticias. Responde UNICAMENTE con JSON valido. Sin markdown, sin explicaciones, sin code blocks."},
            {"role": "user", "content": """Genera un JSON con EXACTAMENTE estas 7 claves en este orden, basado en el extracto:

EXTRACTO: "Google DeepMind released Gemma 4, an open-source AI model family under Apache 2.0 license. The 31B dense model ranks #3 on the Arena leaderboard. Available in four sizes: E2B, E4B, 26B MoE, and 31B dense."

Claves requeridas (en este orden exacto):
1. "Fuentes": array de URLs de fuentes ["https://..."]
2. "Categoria": string, una de: "Inteligencia Artificial", "Startups", "Fintech", "Emprendimiento"
3. "Palabras_Clave": array de 5 strings
4. "Contenido_HTML": string con HTML del articulo (usa <h2>, NO uses <h1>, minimo 500 palabras)
5. "Meta_Titulo": string, maximo 60 caracteres
6. "Meta_Descripcion": string, maximo 155 caracteres
7. "Slug": string en formato kebab-case

IMPORTANTE: El Contenido_HTML debe empezar con <h2>, NUNCA con <h1>. El Meta_Titulo debe tener maximo 60 caracteres."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["Fuentes", "Categoria", "Contenido_HTML", "Meta_Titulo", "Slug"],
            "language": "es",
        },
        "expected_answer": {
            "type": "json_valid",
            "required_keys": ["Fuentes", "Categoria", "Palabras_Clave", "Contenido_HTML", "Meta_Titulo", "Meta_Descripcion", "Slug"],
        },
    },
    {
        "name": "news_spanish_only",
        "description": "Verificar que responda 100% en espanol sin caracteres chinos",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_NEWS},
            {"role": "user", "content": """Write a 500-word article in Spanish about this news:

"SambaNova Systems unveiled the SN50 chip, claiming 5x faster inference than competitors and 3x lower total cost of ownership than GPUs. The chip is designed for enterprise AI workloads and supports models up to 1 trillion parameters. Early benchmarks show 580 tokens per second on Llama 3.1 70B."

Remember: the ENTIRE article must be in Spanish. Include a section about what this means for Latin American startups."""},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["startup", "latinoamerica"],
            "language": "es",
        },
        "expected_answer": {
            "type": "language_check",
            "required_language": "es",
            "reject_cjk": True,
            "reject_long_english": True,
        },
    },
    {
        "name": "news_no_hallucination_sources",
        "description": "No inventar datos que no esten en el extracto",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_NEWS + "\n\nREGLA CRITICA: NO inventes datos, cifras, citas ni nombres que no esten en el extracto. Si no tienes un dato, no lo incluyas."},
            {"role": "user", "content": """Escribe un articulo de 800 palabras basado UNICAMENTE en estos datos:

EXTRACTO: "Chilean startup NotCo raised $85 million in a Series D round led by Tiger Global. The food-tech company, founded by Matias Muchnick in 2015, uses AI to create plant-based alternatives. NotCo products are available in 8 countries. The company's valuation reached $1.5 billion."

DATOS DISPONIBLES (solo estos):
- Fundador: Matias Muchnick
- Ano fundacion: 2015
- Ronda: Serie D, $85M
- Lider ronda: Tiger Global
- Valuacion: $1.5B
- Paises: 8 (no se especifican cuales)
- Producto: alternativas plant-based con IA

NO INVENTES:
- Nombres de otros inversionistas (solo se menciona Tiger Global)
- Nombres de productos especificos
- Cifras de revenue o empleados
- Citas del fundador (no hay quotes en el extracto)
- Nombres de los 8 paises"""},
        ],
        "criteria": {
            "min_words": 400,
            "required_sections": ["NotCo", "Muchnick", "Tiger Global", "85"],
            "language": "es",
        },
        "expected_answer": {
            "type": "hallucination_check",
            "should_not_contain_fabricated": True,
            "known_facts": ["Matias Muchnick", "2015", "85", "Tiger Global", "1.5", "8 paises"],
        },
    },
    {
        "name": "news_perplexity_enrichment",
        "description": "Integrar datos de Perplexity con extracto original",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT_NEWS},
            {"role": "user", "content": """Escribe un articulo de 1,000 palabras integrando el EXTRACTO ORIGINAL con los DATOS ADICIONALES de Perplexity.

EXTRACTO ORIGINAL:
"DeepSeek released V4, their latest open-source AI model under MIT license. The model costs $0.30 per million input tokens."

DATOS ADICIONALES (de Perplexity):
- URLs fuentes: ["https://deepseek.com/blog/v4-release", "https://techcrunch.com/2026/03/deepseek-v4"]
- Puntos clave:
  * DeepSeek V4 usa arquitectura MoE con 236B parametros totales, 21B activos
  * Entrenado con 15T tokens
  * Cache de tokens cuesta solo $0.03/M (90% descuento)
  * La empresa esta en Hangzhou, China, spin-off de High-Flyer hedge fund
  * Compite directamente con GPT-4o y Claude Sonnet
- Datos adicionales:
  * DeepSeek tiene ~300 empleados
  * Recaudaron $0 en funding externo (autofinanciados por High-Flyer)

IMPORTANTE:
- Las URLs de Perplexity deben aparecer en la seccion de Fuentes
- Integra ambas fuentes coherentemente
- No pierdas datos clave de ninguna fuente"""},
        ],
        "criteria": {
            "min_words": 600,
            "required_sections": ["DeepSeek", "V4", "MoE", "High-Flyer", "fuente", "deepseek.com", "techcrunch"],
            "language": "es",
        },
    },
]
