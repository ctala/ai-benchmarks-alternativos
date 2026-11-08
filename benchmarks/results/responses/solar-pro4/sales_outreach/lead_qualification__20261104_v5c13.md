# Solar Pro 4 — sales_outreach/lead_qualification

- model_id: `upstage/solar-pro4`
- success: True  | final: 4.36 | quality: 3.33
- latency_total: 13.737s | tokens_per_second: 33.0
- input_tokens: 311 | output_tokens: 453

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

[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado, pero startup de 5 personas sugiere recursos limitados.",
      "authority": "CEO (alta autoridad).",
      "need": "Alto. Busca automatizar soporte.",
      "timeline": "Media. 'Viendo opciones' sugiere investigación inicial."
    },
    "action": "Enviar contenido educativo y nutrir hasta que se defina presupuesto.",
    "reason": "Es una buena oportunidad por ser el CEO, pero la falta de presupuesto explícito y el tamaño de la startup sugieren que puede no estar listo para comprar inmediatamente."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa Serie B con 200 empleados.",
      "authority": "Alto. VP de Operations es decisor clave.",
      "need": "Alto. Necesita resolver el problema antes de Q3.",
      "timeline": "Corto. Fecha límite Q3."
    },
    "action": "Programar demo prioritaria inmediatamente.",
    "reason": "Lead caliente con autoridad, presupuesto confirmado, necesidad clara y urgencia temporal. Prioridad máxima."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido.",
      "authority": "Bajo. Intern de marketing.",
      "need": "Media. Su jefe quiere investigar, pero él no es el usuario final ni decisor.",
      "timeline": "Larga. Etapa de investigación inicial."
    },
    "action": "Enviar PDF solicitado y registrar en nurturing. No asignar recursos de venta.",
    "reason": "No es un prospecto viable actualmente. Falta autoridad y hay dudas sobre presupuesto. Es un canal para llegar al jefe, pero no merece esfuerzo directo."
  }
]