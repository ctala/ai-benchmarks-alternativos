# Nemotron 3 Super — sales_outreach/lead_qualification

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.18 | quality: 10.0
- latency_total: 7.523s | tokens_per_second: 93.2
- input_tokens: 264 | output_tokens: 701

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
      "lead": "Juan Perez, CEO de una startup de 5 personas. Dice que 'estamos viendo opciones para automatizar nuestro soporte'. No menciono presupuesto. Llego via el blog.",
      "score": 5,
      "bant": {
        "budget": "No mencionado — startup pequeña, posible limitación de recursos.",
        "authority": "Alta — es CEO, toma decisiones finales.",
        "need": "Media — está evaluando opciones, pero sin urgencia ni compromiso claro.",
        "timeline": "Baja — no hay fecha ni presión temporal."
      },
      "action": "Nurture — enviar contenido educativo sobre ROI de automatización de soporte y casos de uso en startups similares. Programar seguimiento en 2-3 semanas.",
      "reason": "Tiene autoridad y necesidad latente, pero falta presupuesto definido y timeline. Es un lead de mediano potencial que requiere cultivo antes de pasar a ventas."
    },
    {
      "lead": "Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que 'necesitamos resolver esto antes de Q3'. Su empresa acaba de levantar Serie B.",
      "score": 9,
      "bant": {
        "budget": "Alta — acaba de levantar Serie B, implica capacidad de gasto reciente.",
        "authority": "Alta — VP of Operations tiene autoridad para aprobar soluciones operativas.",
        "need": "Alta — expresó necesidad clara y específica: resolver antes de Q3.",
        "timeline": "Alta — plazo definido (antes de Q3), indica urgencia."
      },
      "action": "Priorizar — asignar a ejecutivo de ventas inmediatamente. Preparar demo personalizada enfocada en eficiencia operativa y escalabilidad post-Serie B.",
      "reason": "Cumple con todos los criterios BANT de forma fuerte: presupuesto reciente, autoridad clara, necesidad explícita y timeline urgente. Es un lead calificado listo para conversión."
    },
    {
      "lead": "Carlos Ruiz, intern de marketing. Dice que su jefe le pidio 'investigar herramientas de IA'. Quiere un PDF con precios.",
      "score": 3,
      "bant": {
        "budget": "Baja — es un intern, no tiene poder de gasto; solo recopila información.",
        "authority": "Muy baja — no es decision maker, solo ejecutor de tarea asignada.",
        "need": "Media — hay un encargo, pero es de investigación, no de compra inmediata.",
        "timeline": "Baja — no hay indicación de prisa; probablemente fase de exploration temprana."
      },
      "action": "Nurture de bajo esfuerzo — enviar PDF de precios y caso de uso genérico. Agregar a lista de nurturing para seguimiento pasivo. No invertir tiempo de ventas.",
      "reason": "Aunque hay interés y necesidad indirecta, carece de autoridad y presupuesto. Es un lead de bajo valor inmediato, pero podría convertirse en un influencer futuro si su jefe decide comprar. No vale la pena esfuerzo de ventas ahora."
    }
  ]
}