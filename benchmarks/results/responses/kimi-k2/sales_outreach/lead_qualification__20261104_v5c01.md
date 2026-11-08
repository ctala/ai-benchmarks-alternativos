# Kimi K2 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 3.96 | quality: 3.33
- latency_total: 14.493s | tokens_per_second: 44.2
- input_tokens: 280 | output_tokens: 641

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
    "score": 5,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto, startup pequeña puede tener recursos limitados",
      "authority": "Alto - es CEO, tiene poder de decisión total",
      "need": "Medio - interés exploratorio ('estamos viendo opciones'), no urgencia declarada",
      "timeline": "Desconocido - sin fecha específica, modo investigación temprana"
    },
    "action": "Nurture con contenido de valor - enviar case studies de startups similares y pedir call de discovery para entender presupuesto y urgencia",
    "reason": "CEO con poder de decisión pero en etapa muy temprana de investigación. Falta claridad en budget y timeline. No es prioritario pero merece seguimiento educativo."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto - Serie B reciente, empresa establecida de 200 personas, capacidad de inversión confirmada",
      "authority": "Alto - VP of Operations, típicamente owner del proceso y recomendador clave o decisor",
      "need": "Alto - necesidad explícita y cuantificable (antes de Q3)",
      "timeline": "Alto - deadline claro (Q3), urgencia real"
    },
    "action": "Contacto inmediato - llamada en las próximas 2-4 horas, preparar demo personalizada, involucrar a AE senior y potencialmente C-level",
    "reason": "Lead caliente con todas las señales de compra: budget confirmado por contexto, autoridad, necesidad explícita y timeline urgente. Alta probabilidad de cierre rápido."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido - intern no tiene visibilidad, solo pide PDF de precios sin contexto",
      "authority": "Muy bajo - intern de marketing, solo investiga por encargo, cero poder de decisión",
      "need": "Bajo - tarea delegada genérica ('investigar herramientas de IA'), sin problema específico",
      "timeline": "Desconocido - probablemente sin urgencia, solo recopilación de información"
    },
    "action": "Automated nurture únicamente - enviar PDF con precios y contenido educativo, NO asignar SDR. Intentar identificar al decision maker real si es posible.",
    "reason": "Gatekeeper de bajo nivel sin influencia en decisión. Inversión de tiempo del equipo de ventas no justificada. Riesgo alto de quedar atrapado en ciclo de 'solo está investigando'."
  }
]
```