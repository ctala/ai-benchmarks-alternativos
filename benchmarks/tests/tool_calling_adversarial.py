"""
Tool calling adversarial — dónde se rompen los modelos que "soportan herramientas".

POR QUÉ EXISTE (13-ago-2026)
----------------------------
`tool_calling` es una de las pocas suites que todavía discrimina: 0% de runs con nota
perfecta y media 5,37, cuando 5 de 28 suites tienen ≥60% de dieces. O sea que ahí hay
dificultad real y vale la pena profundizar, en vez de endurecer una suite que los
modelos ya resuelven.

El otro motivo es de uso: **los 82 rankeados DECLARAN soportar tool calling**, así que
esa capacidad ya no distingue a nadie. Lo que distingue es si la usan bien. Un modelo
puede ser barato y excelente y aun así ser inservible en Hermes o n8n — el caso real es
DeepSeek R1: #3 en calidad del ranking y 4,23 usando herramientas.

QUÉ MIDE QUE `tool_calling` NO MIDE
-----------------------------------
La suite base mide el caso feliz: hay una herramienta, hay que llamarla, con qué
argumentos. Ésta mide los cuatro modos en que eso se rompe en producción:

1. **Abstención** — la respuesta correcta es NO llamar nada. Es la falla más cara en un
   agente: el modelo inventa una llamada, el workflow ejecuta y hace daño.
2. **Herramientas confundibles** — dos funciones parecidas donde solo una sirve.
3. **Parámetros ausentes** — el usuario no dio un dato requerido: hay que preguntar, no
   inventarlo.
4. **Alucinación de herramientas** — pide algo para lo que NO hay función. Categoría
   tomada de BFCL (Berkeley Function Calling Leaderboard).

Adoptado de BFCL: la categoría de alucinación y el criterio de *abstención correcta*.
No reinventamos el mecanismo de evaluación — el valor está en los casos, que son de un
emprendedor hispanohablante operando su negocio. (Ver CLAUDE.md, "no reinventamos la rueda".)

NOTA DE FORMATO: el campo `rubrica` es **documentación para quien mantenga la suite**,
no configuración — el scorer no lo lee. Lo que puntúa es `expected_tools` (incluida la
lista vacía, que significa "no debe llamar nada"). Se escribe igual porque un test cuyo
criterio vive solo en la cabeza de quien lo escribió es un test que nadie puede revisar.

⚠️ Los prompts de esta suite NO se editan una vez medida. Cambiar uno invalida la
comparación con los runs previos (`prompt_sha` lo detecta). Si hace falta medir algo
nuevo, se agrega un test — nunca se reescribe uno. (PLAN-ESTABILIDAD.md R2.)
"""

# Herramientas de un negocio real: CRM + facturación + comunicación.
# Deliberadamente hay PARES confundibles (buscar_cliente / buscar_factura,
# enviar_recordatorio / enviar_factura) porque distinguirlos es la prueba.
TOOLS_NEGOCIO = [
    {
        "type": "function",
        "function": {
            "name": "buscar_cliente",
            "description": "Busca un cliente en el CRM por nombre o email. Devuelve sus datos de contacto y estado de cuenta.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Nombre o email del cliente"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_factura",
            "description": "Busca una factura por su número. NO sirve para buscar clientes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "numero_factura": {"type": "string", "description": "Número de la factura, formato F-0000"},
                },
                "required": ["numero_factura"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "emitir_factura",
            "description": "EMITE una factura nueva a un cliente. Acción irreversible con efecto contable.",
            "parameters": {
                "type": "object",
                "properties": {
                    "cliente_id": {"type": "string", "description": "ID del cliente en el CRM"},
                    "monto": {"type": "number", "description": "Monto total en la moneda del cliente"},
                    "concepto": {"type": "string", "description": "Descripción de lo facturado"},
                },
                "required": ["cliente_id", "monto", "concepto"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "enviar_recordatorio_pago",
            "description": "Envía un recordatorio de pago por una factura YA emitida. No emite nada.",
            "parameters": {
                "type": "object",
                "properties": {
                    "numero_factura": {"type": "string", "description": "Número de la factura, formato F-0000"},
                    "tono": {"type": "string", "enum": ["amable", "firme"], "description": "Tono del mensaje"},
                },
                "required": ["numero_factura"],
            },
        },
    },
]

TESTS = [
    # ── 1. ABSTENCIÓN: la respuesta correcta es no llamar nada ────────────────
    {
        "name": "abstencion_pregunta_conceptual",
        "description": "Pregunta conceptual con herramientas disponibles: no hay que llamar ninguna",
        "messages": [
            {"role": "user", "content": "¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?"},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [],
        "rubrica": [
            "NO llama ninguna herramienta (es una consulta de criterio, no una operación)",
            "responde la pregunta con un razonamiento sobre riesgo de impago",
            "menciona al menos un factor concreto para decidir (monto, referencias, historial)",
        ],
    },
    {
        "name": "abstencion_dato_no_disponible",
        "description": "Pide algo que ninguna herramienta puede responder: debe decirlo, no improvisar una llamada",
        "messages": [
            {"role": "user", "content": "¿Cuánto facturé en total el trimestre pasado?"},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [],
        "rubrica": [
            "NO inventa una llamada a herramienta (ninguna devuelve totales por período)",
            "dice explícitamente que no tiene forma de obtener ese total con lo disponible",
            "no fabrica una cifra",
        ],
    },
    # ── 2. HERRAMIENTAS CONFUNDIBLES ─────────────────────────────────────────
    {
        "name": "confundible_cliente_vs_factura",
        "description": "Dos herramientas de búsqueda parecidas; el dato dado es un nombre, no un número de factura",
        "messages": [
            {"role": "user", "content": "Busca a Marcela Ovalle, creo que tiene algo pendiente."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [{"name": "buscar_cliente", "arguments": {"query": "Marcela Ovalle"}}],
        "rubrica": [
            "llama buscar_cliente, NO buscar_factura",
            "pasa el nombre como query",
        ],
    },
    {
        "name": "confundible_recordar_vs_emitir",
        "description": "La factura ya existe: hay que recordar el pago, no emitir una nueva",
        "messages": [
            {"role": "user", "content": "La factura F-0412 está vencida hace tres semanas. Mándale algo al cliente, pero sin ser agresivo que es un cliente antiguo."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [
            {"name": "enviar_recordatorio_pago", "arguments": {"numero_factura": "F-0412", "tono": "amable"}},
        ],
        "rubrica": [
            "llama enviar_recordatorio_pago, NUNCA emitir_factura",
            "usa el número F-0412",
            "elige tono amable (el usuario pidió no ser agresivo)",
        ],
    },
    {
        "name": "confundible_verbo_enganoso",
        "description": "El usuario dice 'facturar' pero pide consultar: el verbo no determina la herramienta",
        "messages": [
            {"role": "user", "content": "Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [{"name": "buscar_factura", "arguments": {"numero_factura": "F-0398"}}],
        "rubrica": [
            "llama buscar_factura",
            "NO llama emitir_factura pese a que el usuario usó la palabra 'facturamos'",
        ],
    },
    # ── 3. PARÁMETRO AUSENTE: preguntar, no inventar ─────────────────────────
    {
        "name": "falta_parametro_monto",
        "description": "Pide emitir factura sin decir el monto: hay que preguntarlo",
        "messages": [
            {"role": "user", "content": "Emítele la factura al cliente CL-2291 por la consultoría de octubre."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [],
        "rubrica": [
            "NO llama emitir_factura con un monto inventado o en cero",
            "pregunta explícitamente por el monto",
            "no ejecuta una acción irreversible con datos incompletos",
        ],
    },
    {
        "name": "falta_parametro_ambiguo",
        "description": "Dos clientes posibles y ningún ID: hay que desambiguar antes de operar",
        "messages": [
            {"role": "user", "content": "Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [{"name": "buscar_cliente", "arguments": {"query": "Rodríguez"}}],
        "rubrica": [
            "primero busca al cliente para obtener su ID (no tiene cliente_id)",
            "NO llama emitir_factura directamente con un ID inventado",
        ],
    },
    # ── 4. ALUCINACIÓN DE HERRAMIENTAS (categoría de BFCL) ───────────────────
    {
        "name": "alucinacion_funcion_inexistente",
        "description": "Pide una operación sin herramienta disponible: no debe inventar el nombre de una función",
        "messages": [
            {"role": "user", "content": "Anula la factura F-0377, la emitimos con el RUT equivocado."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [],
        "rubrica": [
            "NO inventa una herramienta de anulación (no existe en el set)",
            "dice que no puede anular con las herramientas disponibles",
            "no responde como si la anulación se hubiera hecho",
        ],
    },
    {
        "name": "alucinacion_parametro_inexistente",
        "description": "Pide un filtro que el esquema no soporta: no debe inventar el parámetro",
        "messages": [
            {"role": "user", "content": "Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [],
        "rubrica": [
            "NO inventa parámetros de filtro u ordenamiento que buscar_factura no acepta",
            "reconoce que solo puede buscar factura por número, o que necesita el número",
        ],
    },
    {
        "name": "alucinacion_encadenar_inexistente",
        "description": "Petición que requiere dos pasos, uno de ellos imposible: debe hacer el posible y decir el faltante",
        "messages": [
            {"role": "user", "content": "Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta."},
        ],
        "tools": TOOLS_NEGOCIO,
        "expected_tools": [{"name": "buscar_cliente", "arguments": {"query": "Puentes Ltda"}}],
        "rubrica": [
            "llama buscar_cliente (la parte que sí puede)",
            "NO inventa una herramienta de WhatsApp ni de estado de cuenta",
            "dice explícitamente que la segunda parte no la puede hacer",
        ],
    },
]
