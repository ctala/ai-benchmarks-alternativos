"""
Tests de estrategia de negocio para emprendedores.
Cubre: analisis de competencia, pricing, validacion de modelo de negocio.
Pilar: RAZONAMIENTO / ESTRATEGIA
"""

TESTS = [
    {
        "name": "competitor_analysis",
        "description": "Analizar competidores y generar tabla comparativa",
        "messages": [
            {"role": "system", "content": "Eres un analista de estrategia para startups. Sé riguroso con los datos y honesto cuando no tengas certeza."},
            {"role": "user", "content": """Soy fundador de una startup de email marketing para pymes en LATAM. Mis 3 competidores principales son Mailchimp, Brevo (ex-Sendinblue), y una startup local llamada "EnviaMas".

Con la informacion que tengas (si no la tienes, dilo):
1. Genera una tabla comparativa con: pricing, features principales, mercado target, fortalezas, debilidades
2. Identifica 3 gaps de mercado que yo podria explotar
3. Sugiere un posicionamiento diferenciador para mi startup
4. Que deberia hacer en los proximos 90 dias?

Se especifico. No me des consejos genericos."""},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["tabla", "gap", "posicionamiento", "90 dias"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "Mailchimp es caro para pymes latam",
                "localizacion o idioma como diferenciador",
                "EnviaMas es inventada debe decir que no la conoce",
            ],
        },
    },
    {
        "name": "pricing_strategy",
        "description": "Definir estrategia de pricing con datos",
        "messages": [
            {"role": "user", "content": """Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)"""},
        ],
        "criteria": {
            "min_words": 250,
            "required_sections": ["LTV", "CAC", "churn", "escenario", "recomendacion"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "LTV/CAC ratio actual es 7x",
                "churn de 7% es alto para SaaS",
                "subir precio puede aumentar churn",
                "grandfather o gradual es menos riesgoso",
            ],
        },
    },
    {
        "name": "business_model_validation",
        "description": "Validar modelo de negocio con pensamiento critico",
        "messages": [
            {"role": "user", "content": """Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto."""},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["riesgo", "LATAM", "assumption", "fracas", "validar"],
            "language": "es",
        },
        "expected_answer": {
            "type": "depth_check",
            "penalize_generic": [
                "gran oportunidad",
                "mercado en crecimiento",
                "potencial enorme",
                "excelente idea",
            ],
        },
    },
]
