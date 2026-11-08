# Mistral Large 3 675B — sales_outreach/lead_qualification

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.32 | quality: 3.33
- latency_total: 5.081s | tokens_per_second: 89.6
- input_tokens: 253 | output_tokens: 455

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de calificacion de leads. Evalua cada lead con un score 1-10 y decide la accion.

Framework BANT:
- Budget: tiene presupuesto?
- Authority: es decision maker?
- Need: tiene el problema que resolvemos?
- Timeline: necesita solucion pronto?

Responde en JSON: {"score": N, "bant": {"budget": "...", "authority": "...", "need": "...", "timeline": "..."}, "action": "...", "reason": "..."}

**user:**

Lead 1: Juan Perez, CEO de una startup de 5 personas. Dice que "estamos viendo opciones para automatizar nuestro soporte". No menciono presupuesto. Llego via el blog.

Lead 2: Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que "necesitamos resolver esto antes de Q3". Su empresa acaba de levantar Serie B.

Lead 3: Carlos Ruiz, intern de marketing. Dice que su jefe le pidio "investigar herramientas de IA". Quiere un PDF con precios.

Califica los 3 leads.


## Respuesta completa

```json
[
    {
        "score": 6,
        "bant": {
            "budget": "No mencionado (neutral, podría ser bajo en startup pequeña)",
            "authority": "Alto (CEO, decision maker)",
            "need": "Sí (automatizar soporte, problema que resolvemos)",
            "timeline": "No claro (dice 'viendo opciones', no urgente)"
        },
        "action": "Nurture con contenido educativo (casos de éxito para startups, ROI de automatización)",
        "reason": "Decision maker con necesidad clara, pero falta claridad en presupuesto y timeline. Lead frío por origen (blog), requiere calentamiento."
    },
    {
        "score": 9,
        "bant": {
            "budget": "Alto (empresa en Serie B, probable presupuesto asignado)",
            "authority": "Alto (VP of Operations, influencer clave)",
            "need": "Sí (necesidad explícita)",
            "timeline": "Corto (antes de Q3, ~2-3 meses)"
        },
        "action": "Contacto prioritario (agendar demo técnica + reunión con sales para alinear con Q3)",
        "reason": "Cumple casi todos los criterios BANT con alta puntuación. Timeline claro y autoridad para avanzar. Origen (webinar) indica interés activo."
    },
    {
        "score": 3,
        "bant": {
            "budget": "No mencionado (irrelevante en este caso)",
            "authority": "Bajo (intern, no decision maker)",
            "need": "Indirecto (su jefe investiga, no hay dolor claro)",
            "timeline": "No claro (solo pide PDF, sin urgencia)"
        },
        "action": "Enviar PDF genérico + preguntar: '¿Podría conectarme con la persona encargada de evaluar herramientas de IA?'",
        "reason": "Baja autoridad y necesidad no confirmada. Lead frío con bajo potencial de conversión directa, pero oportunidad para escalar."
    }
]
```