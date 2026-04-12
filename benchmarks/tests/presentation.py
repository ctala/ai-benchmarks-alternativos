"""
Tests de generacion de presentaciones y reportes.
"""

TESTS = [
    {
        "name": "slide_outline",
        "description": "Crear outline de presentacion ejecutiva",
        "messages": [
            {"role": "user", "content": """Crea el outline completo para una presentacion de 15 slides sobre el estado del proyecto "Plataforma Digital 2.0". La audiencia es el board de directores. Incluye para cada slide:
- Numero y titulo
- Bullet points del contenido (3-5 por slide)
- Tipo de visual sugerido (grafico, tabla, diagrama, imagen)
- Notas del presentador (1-2 oraciones)

La presentacion debe cubrir: estado actual, metricas de progreso, riesgos, presupuesto ejecutado vs planeado, roadmap Q2-Q3, y asks al board."""},
        ],
        "criteria": {
            "min_words": 400,
            "required_sections": ["slide", "titulo", "visual", "nota"],
            "language": "es",
        },
    },
    {
        "name": "data_report",
        "description": "Generar reporte de datos formateado",
        "messages": [
            {"role": "user", "content": """Con estos datos de ventas, genera un reporte en formato markdown con tablas y analisis:

Producto A: Ene $45K, Feb $52K, Mar $48K, Abr $61K
Producto B: Ene $23K, Feb $25K, Mar $31K, Abr $29K
Producto C: Ene $12K, Feb $15K, Mar $18K, Abr $22K

Incluye:
1. Tabla de datos mensuales con totales por producto y por mes
2. Tabla de crecimiento % mes a mes
3. Analisis de tendencias
4. Producto estrella y producto preocupante
5. Proyeccion para mayo basada en tendencia"""},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["tabla", "producto", "crecimiento", "tendencia", "mayo"],
            "language": "es",
        },
    },
]
