# Claude Fable 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 16.001s | tokens_per_second: 62.1
- input_tokens: 410 | output_tokens: 994
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y estrategias de acción claras para cada lead.

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto; startups de 5 personas suelen tener budget limitado",
      "authority": "Alto - es CEO, decision maker final",
      "need": "Confirmado - busca activamente automatizar soporte",
      "timeline": "Indefinido - 'estamos viendo opciones' sugiere fase exploratoria temprana"
    },
    "action": "Nurture con seguimiento ligero",
    "reason": "Tiene autoridad y need real, pero está en fase de exploración sin urgencia ni budget confirmado. Enviar contenido relevante (case studies de startups), ofrecer una llamada corta de discovery para calificar presupuesto. No priorizar sobre leads calientes."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Fuerte señal positiva - empresa acaba de levantar Serie B, hay capital disponible",
      "authority": "Alta - VP of Operations, probable decision maker o influencer clave con acceso directo al budget",
      "need": "Confirmado - pidió demo proactivamente tras webinar",
      "timeline": "Definido y urgente - 'antes de Q3' es un deadline concreto"
    },
    "action": "Pasar a ventas inmediatamente (SQL)",
    "reason": "Cumple los 4 criterios BANT. Timeline explícito + funding reciente + solicitud de demo = lead caliente. Agendar demo en las próximas 24-48 horas con un AE senior. Prioridad máxima."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido - sin visibilidad ni acceso al presupuesto",
      "authority": "Nula - es intern, actúa por encargo de su jefe (el decision maker real es desconocido)",
      "need": "Vaga - 'investigar herramientas de IA' es exploración genérica, no un problema definido",
      "timeline": "Indefinido - sin urgencia aparente"
    },
    "action": "Enviar material automatizado + intentar identificar al decision maker",
    "reason": "No califica para atención de ventas. Enviar el PDF/pricing solicitado vía secuencia automatizada y preguntar quién lidera la evaluación para intentar llegar al jefe. Mantener en nurturing de bajo costo; puede ser puerta de entrada a la cuenta, pero no invertir tiempo humano aún."
  }
]
```

**Resumen de priorización:** Ana (9) → contactar hoy. Juan (5) → discovery call esta semana. Carlos (2) → automatizar y mapear la cuenta.