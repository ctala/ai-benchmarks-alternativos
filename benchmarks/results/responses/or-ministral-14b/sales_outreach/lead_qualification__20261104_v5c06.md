# Ministral 14B — sales_outreach/lead_qualification

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 4.36 | quality: 3.33
- latency_total: 13.125s | tokens_per_second: 43.1
- input_tokens: 253 | output_tokens: 566

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
        "score": 4,
        "bant": {
            "budget": "Desconocido (no mencionado)",
            "authority": "Parcial (CEO, pero no hay claridad sobre decisión final o presupuesto)",
            "need": "Potencial (automatizar soporte, pero no hay urgencia o problema definido)",
            "timeline": "Indefinido (no menciona plazo)"
        },
        "action": "Nurturing a largo plazo (email con caso de éxito + oferta educativa gratuita). Seguimiento en 3 meses.",
        "reason": "Aunque Juan es CEO (alta autoridad), la falta de claridad en presupuesto, necesidad concreta y timeline lo hace un lead frío. La startup podría ser prometedora, pero requiere más engagement para calificar. **No prioritario para demo o venta directa.**"
    },
    {
        "score": 9,
        "bant": {
            "budget": "Alto (empresa en Serie B con 200 empleados; capacidad de inversión probable)",
            "authority": "Alta (VP of Operations, decision-maker en operaciones)",
            "need": "Claro (resolver problema de soporte/automatización antes de Q3)",
            "timeline": "Urgente (plazo definido: Q3)"
        },
        "action": **"Prioridad ABSOLUTA: Programar demo en 48h.** Enviar caso de éxito relevante a su industria y preguntar directamente por presupuesto y roles involucrados en la decisión.",
        "reason": "Cumple casi todos los criterios BANT: autoridad clara, necesidad urgente, presupuesto probable (Serie B) y timeline definido. El hecho de que haya pedido una demo (no solo información) aumenta su calificación. **Lead caliente.**"
    },
    {
        "score": 1,
        "bant": {
            "budget": "Desconocido (no mencionado; además, pide solo PDF de precios)",
            "authority": "Nula (es un *intern*, sin poder de decisión)",
            "need": "Vago (herramientas de IA, sin problema específico)",
            "timeline": "Indefinido (no hay urgencia)"
        },
        "action": "Descartar o responder con un email genérico de agradecimiento + oferta de webinar/recurso educativo. **No invertir tiempo en seguimiento.**",
        "reason": "Falta total de autoridad, presupuesto, necesidad clara y timeline. Es un lead *pasivo* (no busca comprar, sino información). **No viable.**"
    }
]
```