"""
Tests de generacion de contenido.
Evalua la capacidad de generar texto util para uso real.
"""

TESTS = [
    {
        "name": "blog_post_es",
        "description": "Generar un blog post en espanol",
        "messages": [
            {"role": "system", "content": "Eres un redactor de contenido profesional."},
            {"role": "user", "content": "Escribe un blog post de ~500 palabras sobre las ventajas de la automatizacion con IA para pequenas empresas. Incluye titulo, introduccion, 3 secciones con subtitulos, y una conclusion con call-to-action."},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["titulo", "introduccion", "conclusion"],
            "language": "es",
        },
    },
    {
        "name": "email_profesional",
        "description": "Redactar un email profesional",
        "messages": [
            {"role": "system", "content": "Eres un asistente ejecutivo."},
            {"role": "user", "content": "Redacta un email profesional para un cliente que pidio una propuesta. El proyecto es un sitio web corporativo con e-commerce. Presupuesto estimado: $15,000 USD. Plazo: 3 meses. Incluye saludo, resumen de la propuesta, timeline, y siguiente paso."},
        ],
        "criteria": {
            "min_words": 150,
            "required_sections": ["presupuesto", "plazo", "siguiente"],
            "language": "es",
        },
    },
    {
        "name": "social_media_batch",
        "description": "Generar contenido para redes sociales",
        "messages": [
            {"role": "system", "content": "Eres un social media manager creativo."},
            {"role": "user", "content": "Genera 5 posts para LinkedIn sobre transformacion digital, cada uno con:\n- Hook (primera linea llamativa)\n- Cuerpo (3-4 lineas)\n- CTA\n- 3 hashtags relevantes\n\nVaria el tono entre educativo, inspiracional y datos duros."},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["#", "linkedin"],
            "language": "es",
        },
    },
    {
        "name": "product_description_en",
        "description": "Descripcion de producto en ingles",
        "messages": [
            {"role": "user", "content": "Write a compelling product description for a smart home device that combines a speaker, air quality monitor, and ambient light. Target audience: tech-savvy millennials. Include: headline, 3 key features with benefits, and a closing statement. Max 200 words."},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["feature", "benefit"],
            "language": "en",
        },
    },
]
