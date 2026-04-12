"""
Tests de function calling / tool use.
Critico para agentes en OpenClaw y N8N.
"""

TOOLS_CALENDAR = [
    {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "Crea un evento en el calendario",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Titulo del evento"},
                    "date": {"type": "string", "description": "Fecha en formato YYYY-MM-DD"},
                    "time": {"type": "string", "description": "Hora en formato HH:MM"},
                    "duration_minutes": {"type": "integer", "description": "Duracion en minutos"},
                    "description": {"type": "string", "description": "Descripcion del evento"},
                },
                "required": ["title", "date", "time", "duration_minutes"],
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
                    "to": {"type": "string", "description": "Direccion de email del destinatario"},
                    "subject": {"type": "string", "description": "Asunto del email"},
                    "body": {"type": "string", "description": "Cuerpo del email"},
                },
                "required": ["to", "subject", "body"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_task",
            "description": "Crea una tarea en el gestor de tareas",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Titulo de la tarea"},
                    "due_date": {"type": "string", "description": "Fecha limite YYYY-MM-DD"},
                    "priority": {"type": "string", "enum": ["low", "medium", "high", "urgent"]},
                    "assignee": {"type": "string", "description": "Persona asignada"},
                },
                "required": ["title", "priority"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Busca informacion en la web",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Consulta de busqueda"},
                },
                "required": ["query"],
            },
        },
    },
]

TESTS = [
    {
        "name": "single_tool_calendar",
        "description": "Llamar una sola herramienta - crear evento",
        "messages": [
            {"role": "user", "content": "Agenda una reunion de proyecto para el 15 de mayo de 2026 a las 10:00 AM, duracion 60 minutos. Titulo: 'Sprint Planning Q2'."},
        ],
        "tools": TOOLS_CALENDAR,
        "expected_tools": [
            {
                "name": "create_calendar_event",
                "arguments": {
                    "title": "Sprint Planning Q2",
                    "date": "2026-05-15",
                    "time": "10:00",
                    "duration_minutes": 60,
                },
            }
        ],
    },
    {
        "name": "multi_tool_sequential",
        "description": "Llamar multiples herramientas en secuencia",
        "messages": [
            {"role": "user", "content": "Necesito que hagas lo siguiente:\n1. Crea una tarea urgente titulada 'Revisar contrato cliente ABC' con fecha limite 2026-05-10\n2. Envia un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitamos revision antes del 10 de mayo"},
        ],
        "tools": TOOLS_CALENDAR,
        "expected_tools": [
            {
                "name": "create_task",
                "arguments": {
                    "title": "Revisar contrato cliente ABC",
                    "priority": "urgent",
                    "due_date": "2026-05-10",
                },
            },
            {
                "name": "send_email",
                "arguments": {
                    "to": "legal@empresa.com",
                    "subject": "Contrato ABC - Revision urgente",
                },
            },
        ],
    },
    {
        "name": "tool_with_reasoning",
        "description": "Decidir que herramienta usar basado en contexto",
        "messages": [
            {"role": "system", "content": "Eres un asistente ejecutivo. Usa las herramientas disponibles cuando sea apropiado."},
            {"role": "user", "content": "Manana tengo una presentacion importante a las 3 PM. Necesito prepararme. Crea un recordatorio para hoy a las 5 PM para repasar las slides, y busca en la web 'mejores practicas para presentaciones ejecutivas'."},
        ],
        "tools": TOOLS_CALENDAR,
        "expected_tools": [
            {"name": "create_calendar_event", "arguments": {}},
            {"name": "search_web", "arguments": {"query": "mejores practicas para presentaciones ejecutivas"}},
        ],
    },
    {
        "name": "no_tool_needed",
        "description": "No deberia llamar herramientas cuando no son necesarias",
        "messages": [
            {"role": "user", "content": "Cual es la capital de Francia?"},
        ],
        "tools": TOOLS_CALENDAR,
        "expected_tools": [],  # No deberia usar tools
    },
]
