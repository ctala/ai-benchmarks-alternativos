# MiMo V2.5-Pro (Xiaomi) — sales_outreach/lead_qualification

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.97 | quality: 9.64
- latency_total: 21.118s | tokens_per_second: 53.1
- input_tokens: 264 | output_tokens: 1122
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas sugiere presupuesto limitado.",
      "authority": "Alto - CEO, máximo decisor.",
      "need": "Medio - Tiene necesidad (automatizar soporte), pero está en fase exploratoria.",
      "timeline": "Bajo - 'Estamos viendo opciones' no indica urgencia."
    },
    "action": "Nurture con contenido educativo",
    "reason": "Es el decisor y tiene una necesidad válida, pero el contexto (startup pequeña, sin presupuesto definido, sin urgencia) lo coloca en fase temprana. Enviar caso de estudio de startups similares, agendar call discovery en 2-4 semanas para madurar el lead."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto - Serie B reciente indica capital fresco disponible.",
      "authority": "Alto - VP of Operations, influencer clave o decisor directo en este tipo de compra.",
      "need": "Alto - Necesidad explícita y definida.",
      "timeline": "Alto - 'Antes de Q3' es un deadline claro y urgente."
    },
    "action": "Prioridad máxima: agendar demo y asignar AE inmediatamente",
    "reason": "Lead casi perfecto según BANT. Empresa con financiación, autoridad real, necesidad confirmada y timeline urgente. Esto es un deal cualificado. Responder en menos de 1 hora, personalizar la demo a operaciones y preparar propuesta comercial."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido - Es intern, no tiene visibilidad del presupuesto.",
      "authority": "Muy bajo - Intern sin poder de decisión, solo ejecuta una tarea asignada.",
      "need": "Indirecto - Su jefe tiene la necesidad, pero Carlos es solo un canal.",
      "timeline": "Bajo - Quiere un PDF = fase de investigación, sin urgencia real."
    },
    "action": "Enviar PDF y tratar de escalar al decisor",
    "reason": "Lead débil por falta de autoridad. Enviar el material solicitado de forma cordial, pero intentar escalar: '¿Podríamos agendar una llamada breve con tu jefe para entender mejor su caso de uso?' Si no hay apertura, mover a nurture de bajo esfuerzo."
  }
]
```

## Resumen visual

| Lead | Score | Perfil | Acción clave |
|------|-------|--------|--------------|
| 🟡 Juan Perez | **5/10** | Decisor explorando, sin urgencia | Nurture + discovery call |
| 🟢 Ana Gomez | **9/10** | Deal cualificado, BANT completo | **Responder AHORA, demo + AE** |
| 🔴 Carlos Ruiz | **2/10** | Intern sin autoridad | Enviar PDF + escalar al jefe |

> **Prioridad de atención:** Ana Gomez → Juan Perez → Carlos Ruiz