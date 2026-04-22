"""
Tests de ventas y outreach para emprendedores.
Cubre: cold email, lead qualification, follow-up.
Pilar: CONTENIDO & MARKETING / VENTAS
"""

TESTS = [
    {
        "name": "cold_email_personalized",
        "description": "Escribir cold email personalizado sin ser spam",
        "messages": [
            {"role": "system", "content": """Eres un experto en cold outreach B2B. Reglas:
- NUNCA uses frases genericas como "Espero que este email te encuentre bien"
- El email debe ser corto (max 150 palabras)
- Personalizado al destinatario
- Un solo CTA claro
- No vendas, genera curiosidad"""},
            {"role": "user", "content": """Escribe un cold email para:
- Destinatario: Maria Lopez, Head of Marketing en FintechCo (startup fintech en Colombia, 50 empleados, Serie A)
- Mi producto: herramienta de automatizacion de contenido con IA para startups
- Dato de personalizacion: Maria publico un post en LinkedIn la semana pasada sobre "como escalar content marketing sin contratar"
- Objetivo: conseguir una call de 15 min

Escribe SOLO el email (subject + body). Nada mas."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["Maria", "FintechCo", "LinkedIn"],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": [
                "espero que este email te encuentre bien",
                "me gustaria presentarme",
                "somos una empresa lider",
                "solucion innovadora",
                "no dude en contactarme",
            ],
        },
    },
    {
        "name": "lead_qualification",
        "description": "Evaluar un lead con datos parciales y decidir accion",
        "messages": [
            {"role": "system", "content": """Eres un agente de calificacion de leads. Evalua cada lead con un score 1-10 y decide la accion.

Framework BANT:
- Budget: tiene presupuesto?
- Authority: es decision maker?
- Need: tiene el problema que resolvemos?
- Timeline: necesita solucion pronto?

Responde en JSON: {"score": N, "bant": {"budget": "...", "authority": "...", "need": "...", "timeline": "..."}, "action": "...", "reason": "..."}"""},
            {"role": "user", "content": """Lead 1: Juan Perez, CEO de una startup de 5 personas. Dice que "estamos viendo opciones para automatizar nuestro soporte". No menciono presupuesto. Llego via el blog.

Lead 2: Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que "necesitamos resolver esto antes de Q3". Su empresa acaba de levantar Serie B.

Lead 3: Carlos Ruiz, intern de marketing. Dice que su jefe le pidio "investigar herramientas de IA". Quiere un PDF con precios.

Califica los 3 leads."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["score", "action"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "Ana es el mejor lead score alto",
                "Juan es medio no confirmo presupuesto",
                "Carlos es bajo es intern no decision maker",
            ],
        },
    },
    {
        "name": "campaign_optimization",
        "description": "Optimizar campana de marketing con datos reales",
        "messages": [
            {"role": "user", "content": """Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?"""},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["CTR", "CPC", "CPA", "presupuesto", "A/B"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "CPA campana A es 46.67",
                "CPA campana B es 75",
                "CPA campana C es 88.89",
                "campana A tiene mejor CPA escalar",
                "campana C tiene peor CPA pero alta intencion",
            ],
        },
    },
]
