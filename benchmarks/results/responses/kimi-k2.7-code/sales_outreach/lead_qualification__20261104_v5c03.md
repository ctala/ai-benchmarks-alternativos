# Kimi K2.7 Code — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 3.94 | quality: 3.33
- latency_total: 18.338s | tokens_per_second: 58.3
- input_tokens: 278 | output_tokens: 1069

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
{
  "leads": [
    {
      "score": 6,
      "bant": {
        "budget": "No menciono presupuesto; startup de 5 personas sugiere recursos limitados.",
        "authority": "CEO; es decision maker.",
        "need": "Identifico necesidad: quiere automatizar soporte, aunque aun esta en etapa exploratoria.",
        "timeline": "Vago ('estamos viendo opciones'); no hay urgencia clara."
      },
      "action": "Enviar case studies y contenido de nurture enfocado en startups; programar llamada de descubrimiento suave en 1-2 semanas.",
      "reason": "Buena autoridad y necesidad real, pero falta presupuesto declarado y timeline. No es prioritario pero vale seguimiento."
    },
    {
      "score": 9,
      "bant": {
        "budget": "Alta probabilidad de presupuesto: empresa de 200 empleados y reciente Serie B.",
        "authority": "VP of Operations; decisor clave o influyente directo en operaciones.",
        "need": "Necesidad explicita; solicito demo tras webinar.",
        "timeline": "Definido y urgente: 'antes de Q3'."
      },
      "action": "Prioridad maxima: contactar en menos de 24h para agendar demo personalizada y avanzar propuesta.",
      "reason": "Lead calificado fuerte en las cuatro dimensiones BANT. Alta intencion de compra y capacidad economica."
    },
    {
      "score": 3,
      "bant": {
        "budget": "Desconocido; solo pide PDF de precios, sin contexto de presupuesto.",
        "authority": "Intern de marketing; no es decision maker.",
        "need": "Necesidad indirecta y poco definida: su jefe le pidio investigar herramientas de IA generica.",
        "timeline": "Investigacion temprana; sin fecha ni urgencia."
      },
      "action": "No asignar AE; enviar brochure/PDF de precios y material educativo. Intentar descubrir quien es el decision maker para redirigir el contacto.",
      "reason": "Bajo poder de decision, necesidad vaga y sin timeline. Es un investigador, no un comprador potencial a corto plazo."
    }
  ]
}
```