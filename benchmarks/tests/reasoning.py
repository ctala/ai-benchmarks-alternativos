"""
Tests de razonamiento multi-paso.
Evalua capacidad de analisis y logica, critico para agentes autonomos.
"""

TESTS = [
    {
        "name": "business_analysis",
        "description": "Analisis de negocio con datos",
        "messages": [
            {"role": "user", "content": """Analiza estos datos de mi SaaS:

Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC $78, LTV $408

Necesito:
1. Calcula las metricas clave (churn rate, growth rate, LTV/CAC ratio, net revenue retention)
2. Identifica tendencias preocupantes
3. Sugiere 3 acciones concretas basadas en los datos
4. Proyecta abril si las tendencias continuan"""},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["churn", "growth", "LTV", "CAC", "abril"],
            "language": "es",
        },
    },
    {
        "name": "logical_reasoning",
        "description": "Problema de logica pura",
        "messages": [
            {"role": "user", "content": """Resuelve este problema paso a paso:

En una empresa hay 5 equipos (A, B, C, D, E). Se sabe que:
1. El equipo A tiene mas miembros que B pero menos que C
2. D tiene el mismo numero que A
3. E tiene menos miembros que todos
4. La suma total es 60 personas
5. Ningun equipo tiene menos de 5 personas
6. C tiene exactamente el doble que E
7. B tiene 10 personas

Cuantas personas tiene cada equipo? Muestra el razonamiento paso a paso."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["paso", "equipo", "personas"],
            "language": "es",
        },
    },
    {
        "name": "multi_constraint_decision",
        "description": "Toma de decision con multiples restricciones",
        "messages": [
            {"role": "user", "content": """Ayudame a elegir un stack tecnologico para un MVP. Restricciones:

- Presupuesto: $5,000 total (infra + herramientas)
- Timeline: 6 semanas
- Equipo: 1 fullstack dev (sabe React, Python, basico de Go)
- Producto: marketplace de servicios freelance (como Fiverr pero nicho)
- Requisitos: auth, pagos, chat en tiempo real, busqueda, admin panel
- Escala esperada: 500 usuarios primer mes, 5,000 en 6 meses
- Debe ser facil de mantener por 1 persona

Compara al menos 3 opciones de stack, analiza pros/contras de cada uno, y recomienda uno con justificacion. Incluye costos estimados de infraestructura mensual."""},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["opcion", "pros", "contras", "costo", "recomend"],
            "language": "es",
        },
    },
]
