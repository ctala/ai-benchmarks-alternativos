# Kimi K2.6 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.01 | quality: 8.88
- latency_total: 49.382s | tokens_per_second: 32.5
- input_tokens: 279 | output_tokens: 1607
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "lead_1": {
    "score": 6,
    "bant": {
      "budget": "No mencionado. Startup pequeña, riesgo de limitación presupuestaria.",
      "authority": "Alto. Es CEO, tiene poder de decisión.",
      "need": "Moderado. Expresó interés en automatizar soporte, pero está en etapa de exploración temprana ('viendo opciones').",
      "timeline": "Indefinido. Solo está evaluando alternativas sin fecha de decisión clara."
    },
    "action": "Nutrir (Nurture). Enviar contenido educativo y case studies. No asignar SDR todavía.",
    "reason": "Es el decision maker y tiene una necesidad real, pero falta presupuesto confirmado y no hay urgencia ni timeline definido. Llegó por blog, indicando intención de investigación temprana."
  },
  "lead_2": {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa de 200 empleados con Serie B recién levantada; tiene capacidad de inversión.",
      "authority": "Alto. VP of Operations es típicamente decision maker o al menos evaluador principal con alto peso.",
      "need": "Alto. Solicitó demo tras webinar; tiene un problema concreto que resolver.",
      "timeline": "Muy definido y urgente. Necesita solución antes de Q3."
    },
    "action": "Prioridad máxima. Contacto inmediato de ventas (SQL). Agendar demo con AE en menos de 24h.",
    "reason": "Lead altamente calificado: tiene autoridad, necesidad confirmada, presupuesto implícito por etapa de crecimiento y un deadline inminente (Q3). Es oportunidad de cierre rápido."
  },
  "lead_3": {
    "score": 2,
    "bant": {
      "budget": "Desconocido. No maneja presupuesto.",
      "authority": "Muy bajo. Es intern; solo investiga por encargo de su jefe.",
      "need": "Bajo/Indirecto. La necesidad es de su jefe, no suya.",
      "timeline": "No definido."
    },
    "action": "Descartar para seguimiento de ventas. Enviar auto-responder con PDF/web de precios y pasar a campaña de nurturing genérica.",
    "reason": "No es decision maker ni influencer estratégico. Está en fase de recolección de información sin poder de compra. No justifica tiempo de un vendedor."
  }
}
```