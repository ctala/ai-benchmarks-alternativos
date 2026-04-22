"""
Tests de traduccion y calidad multiidioma.
Critico para startups LATAM que operan en espanol e ingles.
Pilar: CONTENIDO & MARKETING
"""

TESTS = [
    {
        "name": "translate_marketing_es_en",
        "description": "Traducir copy de marketing espanol a ingles manteniendo tono",
        "messages": [
            {"role": "system", "content": "Eres un traductor profesional especializado en contenido de marketing para startups. Mantiene el tono, las metaforas y el impacto emocional. No traduces literalmente."},
            {"role": "user", "content": """Traduce este copy de landing page de espanol a ingles. Mantiene el tono cercano y energico. No traduzcas literalmente, adapta para audiencia americana.

ORIGINAL:
"Deja de perder horas haciendo lo que una IA hace en segundos.
AutoFlow automatiza tus procesos mas tediosos para que te enfoques en lo que realmente importa: hacer crecer tu startup.

Sin codigo. Sin dolores de cabeza. Sin excusas.

Mas de 500 startups en LATAM ya lo usan. Tu cuando empiezas?"

Devuelve SOLO la traduccion. Nada mas."""},
        ],
        "criteria": {
            "min_words": 30,
            "required_sections": ["AutoFlow", "startup"],
            "language": "en",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": [],
        },
    },
    {
        "name": "translate_technical_en_es",
        "description": "Traducir documentacion tecnica ingles a espanol sin perder precision",
        "messages": [
            {"role": "user", "content": """Traduce esta documentacion tecnica de ingles a espanol. Mantiene los terminos tecnicos en ingles cuando es lo standard (API, endpoint, token, etc). No inventes traducciones forzadas.

ORIGINAL:
"To authenticate with the API, include your Bearer token in the Authorization header. Rate limits are set at 100 requests per minute for the free tier. If you exceed the rate limit, the API returns a 429 status code with a Retry-After header indicating when you can resume. Webhook endpoints must respond within 30 seconds or the delivery will be marked as failed and retried up to 3 times with exponential backoff."

Devuelve SOLO la traduccion."""},
        ],
        "criteria": {
            "min_words": 40,
            "required_sections": ["API", "token", "Bearer", "webhook"],
            "language": "es",
        },
    },
    {
        "name": "detect_language_issues",
        "description": "Detectar problemas de idioma en texto generado (caracteres chinos, spanglish, etc)",
        "messages": [
            {"role": "system", "content": "Revisa el siguiente texto en espanol y reporta TODOS los problemas de idioma que encuentres. Responde en JSON."},
            {"role": "user", "content": """Revisa este texto generado por una IA para un blog en espanol:

"La inteligencia artificial ha revolucionado el mundo de las startups. En特别是在拉丁美洲, los emprendedores estan leveraging nuevas herramientas para scale their businesses. El machine learning permite optimize los procesos de manera unprecedented.

Las companies que adoptan AI tempranamente tienen un competitive advantage significativo. Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit para tu organización."

Devuelve un JSON con:
{"problemas": [{"tipo": "chino|spanglish|cliche|gramatical", "texto": "...", "correccion": "..."}], "score_idioma": 0-10, "veredicto": "publicable|necesita_edicion|inaceptable"}"""},
        ],
        "criteria": {
            "min_words": 30,
            "required_sections": ["problemas", "score", "veredicto"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "detecta caracteres chinos",
                "detecta spanglish leveraging scale optimize",
                "veredicto inaceptable o necesita edicion",
            ],
        },
    },
]
