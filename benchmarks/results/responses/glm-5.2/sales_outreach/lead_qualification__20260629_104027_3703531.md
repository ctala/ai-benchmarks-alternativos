# GLM 5.2 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.64 | quality: 8.88
- latency_total: 34.535s | tokens_per_second: 41.8
- input_tokens: 255 | output_tokens: 1442
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Lead 1",
    "score": 5,
    "bant": {
      "budget": "Desconocido. Startup de 5 personas, no mencionó presupuesto.",
      "authority": "Alto. Es el CEO.",
      "need": "Sí. Quiere automatizar el soporte.",
      "timeline": "Bajo/Desconocido. Está 'viendo opciones', lo que indica una etapa de exploración temprana."
    },
    "action": "Agendar llamada de descubrimiento (Discovery Call).",
    "reason": "Tiene la autoridad y la necesidad, pero falta definir el presupuesto y el tiempo de implementación. No es urgente, pero es un buen contacto inicial."
  },
  {
    "lead": "Lead 2",
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar Serie B.",
      "authority": "Alto. Es VP of Operations.",
      "need": "Sí. Pidió una demo, lo que indica que busca resolver un problema operativo.",
      "timeline": "Alto. Necesita resolverlo antes de Q3."
    },
    "action": "Asignar a ventas prioritarias y agendar la demo inmediatamente.",
    "reason": "Lead altamente cualificado. Cumple perfectamente con el framework BANT. Tiene urgencia, presupuesto y autoridad."
  },
  {
    "lead": "Lead 3",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Pide precios, pero no hay contexto de presupuesto aprobado.",
      "authority": "Bajo. Es un interno de marketing, no es el tomador de decisiones.",
      "need": "Sí. Su jefe le pidió investigar herramientas de IA.",
      "timeline": "Bajo. Está en fase de recopilación de información."
    },
    "action": "Enviar el PDF de precios y añadir a campañas de nutrición (Marketing).",
    "reason": "Falta de autoridad (es un interno investigando) y etapa muy temprana del embudo. No está listo para ventas directas."
  }
]
```