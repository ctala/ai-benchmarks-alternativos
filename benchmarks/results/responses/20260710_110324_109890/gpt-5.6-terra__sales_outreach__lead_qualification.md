# GPT-5.6 Terra — sales_outreach/lead_qualification

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.12 | quality: 9.16
- latency_total: 4.61s | tokens_per_second: 97.4
- input_tokens: 242 | output_tokens: 449
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado; posible restricción por ser una startup de 5 personas.",
      "authority": "Alta: es CEO y probablemente decision maker.",
      "need": "Media-alta: está evaluando automatizar soporte, pero no detalló dolor o requisitos.",
      "timeline": "No definido."
    },
    "action": "Enviar email de calificación y ofrecer una llamada breve de discovery.",
    "reason": "Tiene autoridad y una necesidad relevante, pero faltan confirmar presupuesto, urgencia y alcance del problema. Al venir por blog, aún está en fase exploratoria."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto potencial: empresa de 200 empleados y reciente levantamiento de Serie B.",
      "authority": "Alta: VP of Operations suele influir fuertemente o decidir sobre herramientas operativas.",
      "need": "Alta: expresó una necesidad explícita de resolver el problema.",
      "timeline": "Alta urgencia: necesita solución antes de Q3."
    },
    "action": "Prioridad alta: contactar inmediatamente, agendar demo y preparar propuesta/plan de implementación.",
    "reason": "Lead altamente calificado: solicitó demo, tiene una fecha límite clara, capacidad financiera probable y un rol con autoridad relevante."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Desconocido; solicita precios para investigación, no indica capacidad de compra.",
      "authority": "Baja: es intern y no es decision maker.",
      "need": "Baja-media: existe interés en herramientas de IA, pero la necesidad concreta no está validada.",
      "timeline": "No definido."
    },
    "action": "Enviar PDF de precios y material educativo; nutrir el lead y solicitar contacto del responsable de evaluación.",
    "reason": "Es un investigador sin autoridad directa y sin urgencia declarada. Puede ser una puerta de entrada, pero requiere identificar al manager o decisor antes de invertir tiempo comercial."
  }
]