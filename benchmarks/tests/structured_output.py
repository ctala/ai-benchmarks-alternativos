"""
Tests de salida estructurada (JSON).
Critico para N8N y automatizaciones donde el output debe ser parseable.
Valida que el modelo devuelva JSON valido y con la estructura correcta.
"""

TESTS = [
    {
        "name": "json_simple_extraction",
        "description": "Extraer datos en JSON simple",
        "messages": [
            {"role": "system", "content": "Responde SOLO con JSON valido, sin markdown, sin explicaciones."},
            {"role": "user", "content": """Extrae los datos de este texto en JSON:

"Maria Garcia, 28 anos, ingeniera de software. Trabaja en Google Chile desde 2023. Email: maria@google.com. Salario: $95,000 USD."

Formato: {"name": "", "age": 0, "role": "", "company": "", "email": "", "salary": 0}"""},
        ],
        "criteria": {
            "min_words": 5,
            "required_sections": ["name", "age", "email", "salary"],
            "language": "en",
        },
        "expected_answer": {
            "type": "json_valid",
            "required_keys": ["name", "age", "role", "company", "email", "salary"],
            "expected_values": {"name": "Maria Garcia", "age": 28, "salary": 95000},
        },
    },
    {
        "name": "json_array_classification",
        "description": "Clasificar multiples items en JSON array",
        "messages": [
            {"role": "system", "content": "Responde SOLO con un JSON array valido. Sin explicaciones ni markdown."},
            {"role": "user", "content": """Clasifica estos emails de soporte. Para cada uno devuelve: category (billing/shipping/technical/general), priority (low/medium/high/urgent), sentiment (positive/negative/neutral).

1. "Mi pedido no ha llegado y ya pasaron 10 dias. Necesito una solucion YA."
2. "Hola, queria saber si tienen envio internacional. Gracias!"
3. "Me cobraron dos veces en mi tarjeta. EXIJO un reembolso inmediato."
4. "La app no carga desde la actualizacion. Error 500 al iniciar sesion."

Formato: [{"id": 1, "category": "", "priority": "", "sentiment": ""}, ...]"""},
        ],
        "criteria": {
            "min_words": 10,
            "required_sections": ["category", "priority", "sentiment"],
            "language": "en",
        },
        "expected_answer": {
            "type": "json_valid",
            "is_array": True,
            "expected_length": 4,
            "sample_check": {"id_1_category": "shipping", "id_3_category": "billing", "id_3_priority": "urgent"},
        },
    },
    {
        "name": "json_nested_complex",
        "description": "Generar JSON complejo anidado para N8N workflow",
        "messages": [
            {"role": "system", "content": "Responde SOLO con JSON valido. Sin markdown code blocks, sin explicaciones."},
            {"role": "user", "content": """Genera un JSON con la estructura de un plan de proyecto:

{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [{"name": "", "role": "", "allocation_pct": 0}],
  "phases": [
    {
      "name": "",
      "start": "",
      "end": "",
      "tasks": [{"title": "", "assignee": "", "hours": 0, "depends_on": null}]
    }
  ],
  "budget": {"total": 0, "breakdown": {"design": 0, "development": 0, "testing": 0}}
}

Llena con datos realistas. El equipo tiene 1 disenador, 2 developers, 1 QA. Presupuesto $25,000."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["project", "phases", "budget"],
            "language": "en",
        },
        "expected_answer": {
            "type": "json_valid",
            "required_keys": ["project", "start_date", "team", "phases", "budget"],
        },
    },
    {
        "name": "json_strict_no_extra",
        "description": "JSON estricto sin texto extra (comun que modelos agreguen explicaciones)",
        "messages": [
            {"role": "system", "content": "IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro."},
            {"role": "user", "content": 'Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}'},
        ],
        "criteria": {
            "min_words": 3,
            "required_sections": ["status", "count", "items"],
            "language": "en",
        },
        "expected_answer": {
            "type": "json_exact",
            "expected": {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]},
        },
    },
]
