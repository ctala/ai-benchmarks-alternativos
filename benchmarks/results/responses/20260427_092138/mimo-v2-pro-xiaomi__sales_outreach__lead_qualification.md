# MiMo V2-Pro (Xiaomi direct) — sales_outreach/lead_qualification

- model_id: `mimo-v2-pro`
- success: True  | final: 7.87 | quality: 9.64
- latency_total: 22.079s | tokens_per_second: 45.0
- input_tokens: 264 | output_tokens: 994
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionó presupuesto. Startup de 5 personas sugiere presupuesto limitado.",
      "authority": "CEO = decision maker. ✅ Alto.",
      "need": "Existe pero es exploratorio: 'estamos viendo opciones'. No es urgente ni prioritario.",
      "timeline": "No definido. 'Estamos viendo' indica etapa temprana de investigación."
    },
    "action": "Nurturing con contenido de valor (casos de uso, ROI de automatización). Agendar call en 2-3 semanas.",
    "reason": "Buena autoridad pero lead frío. Necesita educación antes de una conversación comercial seria."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Empresa post-Serie B = capital fresco disponible. ✅ Alto.",
      "authority": "VP of Operations tiene peso en decisiones de herramientas operativas. ✅ Alto.",
      "need": "Explícito y urgente: 'necesitamos resolver esto'. ✅ Alto.",
      "timeline": "Antes de Q3 = deadline concreto. ✅ Alto."
    },
    "action": "Prioridad ALTA. Enviar propuesta personalizada y agendar demo ejecutiva en las próximas 48h.",
    "reason": "Lead caliente con los 4 criterios BANT cubiertos. Serie B + deadline = alta probabilidad de cierre rápido."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. Un intern no tiene visibilidad del presupuesto.",
      "authority": "Ninguna. Es un intern ejecutando una tarea delegada. ❌",
      "need": "Indirecto. Su jefe pidió investigación, no se conoce la urgencia real del problema.",
      "timeline": "No definido. Es investigación, no un proyecto con deadline."
    },
    "action": "Enviar PDF con info general + intentar escalar: pedir una call con su jefe (el verdadero decisor).",
    "reason": "Lead frío con cero autoridad. No invertir tiempo comercial directo, pero usar como puerta de entrada al decision maker."
  }
]
```

### Resumen rápido

| Lead | Score | Perfil |
|------|-------|--------|
| **Ana Gomez** | **9** 🔥 | Lead caliente. BANT completo. Acción inmediata. |
| **Juan Perez** | **5** ⚡ | Potencial medio. Necesita nurturing y educación. |
| **Carlos Ruiz** | **2** 🧊 | Lead frío. Canal de entrada, no el comprador. |