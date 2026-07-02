"""
Tests de orquestacion y capacidad como agente orquestador.
Evalua si el modelo puede planificar, descomponer tareas, decidir que herramientas
usar en que orden, manejar dependencias entre pasos, y reaccionar a errores.

Critico para uso en OpenClaw y N8N donde el modelo actua como cerebro del agente.
"""

TOOLS_REGISTRY = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Busca informacion en la web",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "La consulta de busqueda"},
                    "max_results": {"type": "integer", "description": "Numero maximo de resultados"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Lee el contenido de un archivo",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Ruta del archivo"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Escribe contenido en un archivo",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Ruta del archivo"},
                    "content": {"type": "string", "description": "Contenido a escribir"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Envia un email",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {"type": "string", "description": "Destinatario"},
                    "subject": {"type": "string", "description": "Asunto"},
                    "body": {"type": "string", "description": "Cuerpo del email"},
                    "attachments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Rutas de archivos adjuntos",
                    },
                },
                "required": ["to", "subject", "body"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_database",
            "description": "Ejecuta una consulta SQL en la base de datos",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Consulta SQL"},
                    "database": {"type": "string", "description": "Nombre de la base de datos"},
                },
                "required": ["query", "database"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "Crea un evento en el calendario",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "date": {"type": "string", "description": "Fecha ISO 8601"},
                    "duration_minutes": {"type": "integer"},
                    "attendees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Emails de asistentes",
                    },
                },
                "required": ["title", "date", "duration_minutes"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "http_request",
            "description": "Hace una peticion HTTP a una API",
            "parameters": {
                "type": "object",
                "properties": {
                    "method": {"type": "string", "enum": ["GET", "POST", "PUT", "DELETE"]},
                    "url": {"type": "string"},
                    "headers": {"type": "object"},
                    "body": {"type": "string"},
                },
                "required": ["method", "url"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_script",
            "description": "Ejecuta un script en el servidor",
            "parameters": {
                "type": "object",
                "properties": {
                    "language": {"type": "string", "enum": ["python", "bash", "node"]},
                    "code": {"type": "string", "description": "Codigo a ejecutar"},
                },
                "required": ["language", "code"],
            },
        },
    },
]


TESTS = [
    {
        "name": "multi_step_research_plan",
        "description": "Planificar investigacion multi-paso con dependencias",
        "messages": [
            {"role": "system", "content": """Eres un agente orquestador con acceso a multiples herramientas.
Tu trabajo es PLANIFICAR la secuencia de acciones necesarias y ejecutar la primera accion.
Cuando planifiques, indica claramente:
1. El orden de los pasos
2. Las dependencias entre pasos (que paso necesita el resultado de cual)
3. Que pasos se pueden ejecutar en paralelo"""},
            {"role": "user", "content": """Necesito preparar un reporte sobre el estado del mercado de IA en Chile para una presentacion manana.

El reporte debe incluir:
- Las 5 principales startups de IA en Chile con su funding
- Comparacion con el mercado de IA en Colombia y Mexico
- Datos de inversion VC en tecnologia en Chile 2025-2026
- Un resumen ejecutivo de 1 pagina

Planifica los pasos necesarios y ejecuta el primero."""},
        ],
        "tools": TOOLS_REGISTRY,
        "criteria": {
            "min_words": 100,
            "required_sections": ["paso", "paralelo"],
            "language": "es",
        },
        "expected_tools": [
            {"name": "search_web", "arguments": {"query": "startups IA Chile"}},
        ],
    },
    {
        "name": "error_recovery_orchestration",
        "description": "Reaccionar a errores y replantear la estrategia",
        "messages": [
            {"role": "system", "content": """Eres un agente orquestador. Tienes acceso a herramientas pero algunas pueden fallar.
Cuando una herramienta falla, debes:
1. Diagnosticar por que fallo
2. Proponer una alternativa
3. Ajustar el plan general"""},
            {"role": "user", "content": "Necesito obtener los datos de ventas del mes pasado y enviar un resumen al equipo."},
            {"role": "assistant", "content": "Voy a consultar la base de datos para obtener los datos de ventas.", "tool_calls": [
                {"id": "call_1", "type": "function", "function": {"name": "query_database", "arguments": "{\"query\": \"SELECT * FROM sales WHERE month = '2026-03'\", \"database\": \"production\"}"}}
            ]},
            {"role": "tool", "tool_call_id": "call_1", "content": "ERROR: Connection refused - database 'production' is currently under maintenance. Expected recovery: 2 hours."},
            {"role": "user", "content": "La base de datos esta en mantenimiento. Que hacemos? Necesito enviar el reporte antes de las 5pm."},
        ],
        "tools": TOOLS_REGISTRY,
        "criteria": {
            "min_words": 80,
            "required_sections": ["alternativ"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "buscar fuente alternativa de datos",
                "puede haber backup, replica, o export reciente",
                "considerar cache local o reportes anteriores",
                "ajustar timeline segun restriccion de las 5pm",
            ],
        },
    },
    {
        "name": "complex_workflow_decomposition",
        "description": "Descomponer un workflow complejo en pasos atomicos",
        "messages": [
            {"role": "system", "content": """Eres un agente orquestador experto en automatizacion.
Descompone tareas complejas en pasos atomicos ejecutables.
Usa las herramientas disponibles para ejecutar cada paso."""},
            {"role": "user", "content": """Automatiza este proceso de onboarding para un nuevo cliente:

1. El cliente envio sus datos por email (nombre: Andres Morales, empresa: DataPulse SpA, email: andres@datapulse.cl)
2. Hay que crear su cuenta en nuestro sistema (API endpoint: POST /api/v1/accounts)
3. Generar una API key para el
4. Enviarle un email de bienvenida con sus credenciales
5. Agendar una llamada de kickoff para la proxima semana
6. Notificar al equipo de Customer Success en Slack

Ejecuta los pasos en orden. Para cada paso, usa la herramienta apropiada."""},
        ],
        "tools": TOOLS_REGISTRY,
        "criteria": {
            "min_words": 50,
            "required_sections": [],
        },
        "expected_tools": [
            {"name": "http_request", "arguments": {"method": "POST", "url": "/api/v1/accounts"}},
        ],
    },
    {
        "name": "tool_selection_precision",
        "description": "Elegir la herramienta correcta cuando varias podrian servir",
        "messages": [
            {"role": "system", "content": """Eres un agente orquestador. Elige SIEMPRE la herramienta mas apropiada.
No uses herramientas innecesarias. Si algo no requiere herramienta, no la uses.
Explica brevemente por que elegiste esa herramienta sobre las alternativas."""},
            {"role": "user", "content": """Tengo que hacer estas 4 tareas. Para cada una, indica que herramienta usarias y por que. Luego ejecuta la tarea 1.

Tarea 1: Verificar si el servidor de produccion esta respondiendo (URL: https://api.example.com/health)
Tarea 2: Obtener el conteo de usuarios activos del ultimo mes
Tarea 3: Calcular el promedio de 3 numeros: 45, 67, 89
Tarea 4: Encontrar articulos recientes sobre competidores"""},
        ],
        "tools": TOOLS_REGISTRY,
        "criteria": {
            "min_words": 80,
            "required_sections": [],
        },
        "expected_tools": [
            {"name": "http_request", "arguments": {"method": "GET", "url": "https://api.example.com/health"}},
        ],
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "tarea 1: http_request GET al health endpoint",
                "tarea 2: query_database con SELECT COUNT",
                "tarea 3: no necesita herramienta, calculo simple",
                "tarea 4: search_web",
            ],
        },
    },
    {
        "name": "parallel_vs_sequential_judgment",
        "description": "Decidir que se puede paralelizar y que no",
        "messages": [
            {"role": "system", "content": """Eres un agente orquestador que optimiza la ejecucion.
Clasifica cada tarea como parallelizable o secuencial, justificando por que.
Las tareas paralelas se ejecutan al mismo tiempo para mayor velocidad.
Las tareas secuenciales dependen del resultado de una tarea anterior."""},
            {"role": "user", "content": """Tengo estas 6 tareas para preparar el lanzamiento de un producto:

A. Buscar precios de competidores en el mercado
B. Generar la descripcion del producto basada en las specs tecnicas (archivo: /docs/specs.md)
C. Calcular el precio optimo basado en costos + margen + precios de competidores
D. Crear la landing page con la descripcion y precio
E. Enviar email al equipo de marketing con el enlace de la landing
F. Publicar anuncio en redes sociales

Analiza las dependencias y presenta:
1. Un diagrama de dependencias (que tarea depende de cual)
2. Un plan de ejecucion optimizado (que se puede hacer en paralelo)
3. El tiempo estimado si cada tarea toma ~5 minutos

Ejecuta las tareas que se pueden iniciar inmediatamente."""},
        ],
        "tools": TOOLS_REGISTRY,
        "criteria": {
            "min_words": 100,
            "required_sections": ["dependencia", "paralel"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "A y B son independientes y pueden ser paralelas",
                "C depende de A (precios competidores)",
                "D depende de B y C (descripcion y precio)",
                "E depende de D (necesita el enlace)",
                "F depende de D (necesita el contenido)",
                "E y F pueden ser paralelas entre si",
                "camino critico: A->C->D->E (o F)",
            ],
        },
    },
]
