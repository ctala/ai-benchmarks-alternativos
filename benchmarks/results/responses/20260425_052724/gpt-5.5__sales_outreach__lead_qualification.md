# GPT-5.5 — sales_outreach/lead_qualification

- model_id: `gpt-5.5`
- success: True  | final: 6.86 | quality: 8.88
- latency_total: 7.292s | tokens_per_second: 74.2
- input_tokens: 242 | output_tokens: 541
- judge_score: 4.8 | justificación: 

## Respuesta completa

[
  {
    "lead": "Lead 1 - Juan Perez",
    "score": 6,
    "bant": {
      "budget": "No mencionado. Startup pequeña de 5 personas, posible presupuesto limitado.",
      "authority": "Alta. Es CEO, probablemente decision maker.",
      "need": "Media-alta. Está evaluando opciones para automatizar soporte, lo que indica un problema relevante.",
      "timeline": "No claro. Solo está explorando opciones."
    },
    "action": "Calificar con discovery call",
    "reason": "Tiene autoridad y una necesidad alineada, pero faltan datos críticos sobre presupuesto y urgencia. Conviene agendar una llamada breve para entender volumen de soporte, prioridades y capacidad de compra."
  },
  {
    "lead": "Lead 2 - Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto potencial. Empresa de 200 empleados y recientemente levantó Serie B.",
      "authority": "Alta. VP of Operations, probablemente influye o decide en herramientas operativas.",
      "need": "Alta. Expresó una necesidad concreta de resolver el problema.",
      "timeline": "Alta urgencia. Necesita resolverlo antes de Q3."
    },
    "action": "Priorizar para venta directa y agendar demo personalizada",
    "reason": "Cumple muy bien con BANT: tiene autoridad, necesidad clara, urgencia definida y señales fuertes de presupuesto. Es el lead más calificado."
  },
  {
    "lead": "Lead 3 - Carlos Ruiz",
    "score": 3,
    "bant": {
      "budget": "No mencionado. Solo pidió información de precios.",
      "authority": "Baja. Es intern y está investigando por encargo de su jefe.",
      "need": "Baja-media. Hay interés general en herramientas de IA, pero no se identificó un problema específico.",
      "timeline": "No claro. Parece una investigación inicial."
    },
    "action": "Enviar PDF/precios y nutrir por email; pedir contacto del responsable",
    "reason": "Tiene baja autoridad y la necesidad no está bien definida. Puede ser útil como entrada a la cuenta, pero no debe priorizarse hasta identificar al decisor y el caso de uso concreto."
  }
]