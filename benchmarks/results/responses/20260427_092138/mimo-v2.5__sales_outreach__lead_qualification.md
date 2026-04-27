# MiMo V2.5 (Xiaomi) — sales_outreach/lead_qualification

- model_id: `mimo-v2.5`
- success: True  | final: 7.92 | quality: 9.48
- latency_total: 10.037s | tokens_per_second: 88.5
- input_tokens: 264 | output_tokens: 888
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado. CEO de startup de 5 personas = probablemente presupuesto limitado pero con capacidad de decisión.",
      "authority": "Alto. Es CEO, decision maker directo.",
      "need": "Alto. Está evaluando activamente opciones para automatizar soporte.",
      "timeline": "Bajo. Dice 'estamos viendo opciones' sin urgencia definida."
    },
    "action": "Nurture",
    "reason": "Tiene autoridad y necesidad clara, pero falta confirmar presupuesto y timeline. Enviar contenido de valor (casos de éxito, ROI) para moverlo hacia una conversación más concreta. No está listo para demo aún."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa con Serie B recién cerrada = capital fresco y disposición para invertir.",
      "authority": "Alto. VP of Operations = tomadora de decisiones o sponsor clave.",
      "need": "Alto. Pidió demo activamente y confirmó que necesitan resolver el problema.",
      "priority": "Alto. Timeline definido: 'antes de Q3'. Urgencia confirmada."
    },
    "action": "Agendar demo urgente",
    "reason": "Lead de alta calidad. BANT casi completo: tiene presupuesto (Serie B), autoridad (VP Ops), necesidad confirmada y timeline urgente. Prioridad máxima. Contactar hoy mismo."
  },
  {
    "score": 3,
    "bant": {
      "budget": "Bajo. Intern sin poder de decisión ni acceso a presupuesto.",
      "authority": "Bajo. Intern ejecuta tareas asignadas, no decide.",
      "need": "Medio. Su jefe tiene una necesidad, pero está en fase muy temprana de investigación.",
      "timeline": "Bajo. Sin urgencia. Solo pide un PDF."
    },
    "action": "Qualify con jefe directo",
    "reason": "No califica como lead. Es un investigador asignado. Enviar PDF sí, pero intentar capturar el email del jefe/director que pidió la investigación. Ofrecer 'una llamada corta para personalizar la info' e incluir al manager."
  }
]
```