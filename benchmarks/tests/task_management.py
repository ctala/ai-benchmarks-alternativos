"""
Tests de gestion de tareas, recordatorios y planificacion.
Evalua la capacidad del modelo como asistente personal.
"""

TESTS = [
    {
        "name": "extract_action_items",
        "description": "Extraer action items de notas de reunion",
        "messages": [
            {"role": "system", "content": "Eres un asistente que organiza notas de reunion."},
            {"role": "user", "content": """Aqui estan las notas de la reunion de hoy:

Reunion de equipo - 11 abril 2026
Asistentes: Maria (PM), Carlos (Dev), Ana (Diseno), Pedro (QA)

- Maria comento que el deadline del proyecto Alpha es el 30 de abril
- Carlos necesita terminar el API de pagos antes del 20 de abril
- Ana va a entregar los mockups del dashboard el lunes 14
- Pedro dijo que faltan escribir tests para el modulo de autenticacion, lo hara esta semana
- Maria pidio a Carlos que documente los endpoints antes del viernes 18
- Se acordo hacer daily standups a las 9:30 AM empezando manana

Extrae todos los action items con: responsable, tarea, fecha limite, y prioridad sugerida. Formatea como tabla."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["Maria", "Carlos", "Ana", "Pedro", "fecha", "prioridad"],
            "language": "es",
        },
    },
    {
        "name": "weekly_planning",
        "description": "Crear plan semanal estructurado",
        "messages": [
            {"role": "user", "content": """Soy product manager. Mi semana tiene estas restricciones:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Necesito meter estas tareas en la semana:
1. Preparar presentacion para la demo (3 horas)
2. Revisar PRDs pendientes (2 horas)
3. Escribir OKRs Q3 (4 horas)
4. Responder emails de stakeholders (1 hora diaria)
5. Revisar metricas del producto (1 hora)
6. One-on-one con 3 reportes directos (30 min cada uno)

Crea un plan semanal detallado con bloques de tiempo especificos."""},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["lunes", "martes", "miercoles", "jueves", "viernes"],
            "language": "es",
        },
    },
    {
        "name": "project_breakdown",
        "description": "Desglosar un proyecto en tareas",
        "messages": [
            {"role": "user", "content": "Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista."},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["fase", "tarea", "semana", "dependencia"],
            "language": "es",
        },
    },
]
