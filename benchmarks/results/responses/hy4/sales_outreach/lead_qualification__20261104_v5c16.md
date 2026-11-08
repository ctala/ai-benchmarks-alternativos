# Tencent Hy4 — sales_outreach/lead_qualification

- model_id: `tencent/hy4`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 7.604s | tokens_per_second: 77.7
- input_tokens: 286 | output_tokens: 591

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

{
  "leads": [
    {
      "lead": "Lead 1: Juan Perez",
      "score": 6,
      "bant": {
        "budget": "Desconocido / no mencionado",
        "authority": "Alta: es CEO de una startup pequeña, probable decision maker",
        "need": "Medio: está explorando automatización de soporte, pero aún en etapa temprana",
        "timeline": "Desconocido / sin urgencia explícita"
      },
      "action": "Nurturing + discovery call",
      "reason": "Buen perfil por autoridad y ajuste inicial de necesidad, pero faltan presupuesto y timeline. Viene por inbound de blog, por lo que conviene educar y calificar con preguntas BANT antes de pasar a ventas activas."
    },
    {
      "lead": "Lead 2: Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Alto: empresa con Serie B reciente, probable capacidad de inversión",
        "authority": "Alta: VP of Operations con influencia operativa y probable poder de decisión o acceso directo al decisor",
        "need": "Alta: pidió demo tras webinar, muestra interés concreto",
        "timeline": "Alta: necesita resolver antes de Q3"
      },
      "action": "Priorizar demo + contacto inmediato por SDR/AE",
      "reason": "Cumple fuertemente BANT: señales de presupuesto, autoridad, necesidad y urgencia temporal. Es el lead más calificado y debe atenderse con prioridad, confirmando quién firma y el proceso de compra."
    },
    {
      "lead": "Lead 3: Carlos Ruiz",
      "score": 3,
      "bant": {
        "budget": "Desconocido: solo pide precios, sin contexto de compra",
        "authority": "Baja: es intern, investiga por pedido de su jefe",
        "need": "Medio-bajo: interés general en herramientas de IA, sin problema definido",
        "timeline": "Desconocido / sin urgencia"
      },
      "action": "Enviar contenido + intentar llegar al jefe/decisor",
      "reason": "No es decision maker y la solicitud parece investigación inicial. Vale como puerta de entrada, pero requiere identificar al jefe, el caso de uso y el timeline antes de invertir esfuerzo comercial."
    }
  ]
}