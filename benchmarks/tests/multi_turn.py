"""
Tests multi-turno: conversaciones de varios mensajes.
Evalua la capacidad del modelo de mantener contexto, iterar, y manejar
cambios de opinion o requisitos a lo largo de una conversacion.

Critico para agentes reales donde las interacciones son de 5-20 turnos.
"""

TESTS = [
    {
        "name": "content_iteration",
        "description": "Iterar sobre un blog post con feedback del usuario",
        "messages": [
            {"role": "system", "content": "Eres un redactor de contenido para un blog de startups en espanol."},
            {"role": "user", "content": "Escribe un titulo y primer parrafo para un articulo sobre por que las startups deberian automatizar su soporte al cliente con IA."},
            {"role": "assistant", "content": "# Por que las startups deberian automatizar su soporte con IA\n\nEn un mercado cada vez mas competitivo, las startups enfrentan el desafio de ofrecer un soporte al cliente excepcional con recursos limitados. La inteligencia artificial ofrece una solucion: chatbots inteligentes, clasificacion automatica de tickets, y respuestas personalizadas que pueden manejar el 80% de las consultas sin intervencion humana, liberando al equipo para enfocarse en los casos que realmente requieren atencion personal."},
            {"role": "user", "content": "No me gusta el titulo, es muy generico. Y el primer parrafo empieza con 'En un mercado cada vez mas competitivo' que es un cliche terrible. Reescribelo con un hook mas provocador y sin cliches. Quiero que el lector se sienta identificado porque ha vivido el problema."},
        ],
        "criteria": {
            "min_words": 80,
            "required_sections": [],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": [
                "en un mercado cada vez mas competitivo",
                "en la era digital",
                "en el mundo actual",
                "no es de extranar",
                "es importante senalar",
            ],
        },
    },
    {
        "name": "support_escalation",
        "description": "Conversacion de soporte que escala en complejidad",
        "messages": [
            {"role": "system", "content": "Eres un agente de soporte para TechFlow, una plataforma de automatizacion. Responde siempre en espanol. Politicas: 1) Siempre pide el email del cliente primero. 2) Los reembolsos solo aplican dentro de 30 dias. 3) Nunca des acceso a cuentas sin verificacion. 4) Escala a un humano si el cliente pide hablar con un supervisor."},
            {"role": "user", "content": "Hola, mi automatizacion dejo de funcionar."},
            {"role": "assistant", "content": "Hola! Lamento escuchar que tienes problemas con tu automatizacion. Para poder ayudarte, necesito verificar tu cuenta. Me puedes compartir el email asociado a tu cuenta de TechFlow?"},
            {"role": "user", "content": "Si, es maria@startup.cl. Mira, llevo 3 dias sin poder usar la plataforma y estoy perdiendo clientes. Ya pague $200 dolares este mes y el servicio no funciona."},
            {"role": "assistant", "content": "Entiendo tu frustracion, Maria. 3 dias sin servicio es inaceptable y lamento mucho la situacion. Voy a revisar tu cuenta maria@startup.cl de inmediato.\n\nPuedo ver que hay un issue abierto con tu workflow de automatizacion. Mientras lo resuelvo, te cuento que opciones tenemos:\n\n1. **Solucion tecnica**: Puedo guiarte para reactivar el workflow manualmente\n2. **Compensacion**: Puedo aplicar un credito proporcional por los dias sin servicio\n\nCual prefieres empezar?"},
            {"role": "user", "content": "Quiero las dos cosas. Pero ademas quiero un reembolso completo de los $200 porque llevo un mes con problemas intermitentes. Y si no me lo dan, quiero hablar con un supervisor."},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["reembolso", "supervisor"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "reconoce la frustracion del cliente",
                "ofrece la solucion tecnica",
                "aborda el reembolso segun politica de 30 dias",
                "escala a supervisor porque el cliente lo pidio",
                "no promete el reembolso completo sin autorizacion",
            ],
        },
    },
    {
        "name": "requirements_change",
        "description": "El usuario cambia los requisitos a mitad de camino",
        "messages": [
            {"role": "system", "content": "Eres un asistente tecnico para emprendedores que trabajan con N8N."},
            {"role": "user", "content": "Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet."},
            {"role": "assistant", "content": "Perfecto, ese workflow es bastante directo. Te explico los pasos:\n\n1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)\n2. **Extraer datos**: Function node para parsear remitente, asunto, fecha\n3. **Guardar**: Google Sheets node para agregar una fila\n\nLos campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?"},
            {"role": "user", "content": "En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno."},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["Notion", "Slack", "filtr"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "adapta el workflow al cambio sin quejarse",
                "reemplaza Google Sheets por Notion",
                "agrega filtro por asunto con propuesta o cotizacion",
                "agrega notificacion a Slack",
                "mantiene la estructura del workflow original",
            ],
        },
    },
    {
        "name": "debugging_conversation",
        "description": "Debug iterativo de un problema tecnico",
        "messages": [
            {"role": "system", "content": "Eres un asistente tecnico experto en APIs y automatizacion. Ayuda a diagnosticar problemas paso a paso."},
            {"role": "user", "content": "Mi API de OpenRouter me da error 429 todo el tiempo. No puedo hacer ni una llamada."},
            {"role": "assistant", "content": "Error 429 es 'Too Many Requests' - significa que estas excediendo el rate limit. Vamos a diagnosticarlo:\n\n1. Cuantas requests/minuto estas haciendo aproximadamente?\n2. Que modelo estas usando? (algunos tienen limites mas bajos)\n3. Estas usando la API key correcta? (las keys gratuitas tienen limites muy bajos)"},
            {"role": "user", "content": "Estoy haciendo como 5 requests por minuto, usando DeepSeek V3. Tengo una API key con creditos pagados, unos $20 de saldo."},
            {"role": "assistant", "content": "5 req/min con DeepSeek deberia funcionar sin problemas - el limite es 300 RPM. Algo mas esta pasando. Vamos a verificar:\n\n1. Estas reutilizando la misma instancia del cliente o creando una nueva por cada request?\n2. Tienes algun retry automatico que podria estar multiplicando los requests?\n3. Me puedes mostrar el header completo de la respuesta 429? Especificamente los headers `x-ratelimit-*`"},
            {"role": "user", "content": "Acabo de revisar y resulta que tengo un loop en mi codigo que hace retry infinito cuando recibe un error. Asi que cada 429 genera como 100 requests mas. Pero no se como arreglarlo bien, como deberia implementar los retries?"},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["retry", "backoff"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "exponential backoff",
                "numero maximo de retries",
                "respetar el header Retry-After",
                "no reintentar inmediatamente",
            ],
        },
    },
]
