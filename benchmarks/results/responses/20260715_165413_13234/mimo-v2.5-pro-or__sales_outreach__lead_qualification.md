# MiMo-V2.5 Pro — sales_outreach/lead_qualification

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 28.978s | tokens_per_second: 38.5
- input_tokens: 264 | output_tokens: 1115
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

# Evaluación de Leads - Framework BANT

```json
{
  "lead": "Juan Perez",
  "score": 4,
  "bant": {
    "budget": "Desconocido - No menciona presupuesto. Startup de 5 personas sugiere fondos limitados",
    "authority": "Alto - CEO y fundador, decisor principal",
    "need": "Moderado - Menciona automatizar soporte, pero sin urgencia clara ('estamos viendo opciones')",
    "timeline": "Bajo - Sin fecha definida, solo explorando opciones"
  },
  "action": "Nurture",
  "reason": "Tiene autoridad pero falta información clave. Está en fase de exploración temprana. Enviar contenido educativo, casos de éxito de startups similares y agendar llamada de discovery para entender presupuesto y urgencia real."
}
```

```json
{
  "lead": "Ana Gomez",
  "score": 9,
  "bant": {
    "budget": "Alto - Serie B reciente indica capital fresco disponible para herramientas",
    "authority": "Alto - VP of Operations, típicamente dueña del proceso de soporte/operaciones",
    "need": "Alto - Declara necesidad explícita: 'necesitamos resolver esto'",
    "timeline": "Alto - Deadline claro: antes de Q3"
  },
  "action": "Prioridad máxima - Asignar a ejecutivo de cuentas senior, enviar propuesta personalizada en 24h",
  "reason": "Lead ideal: tiene presupuesto (Serie B), autoridad (VP), necesidad declarada y urgencia concreta. Es el tipo de deal que hay que acelerar con demo ejecutiva y propuesta de valor a medida."
}
```

```json
{
  "lead": "Carlos Ruiz",
  "score": 2,
  "bant": {
    "budget": "Desconocido - No tiene visibilidad del presupuesto organizacional",
    "authority": "Muy bajo - Es intern, no es decisor. Solo ejecuta instrucciones de su jefe",
    "need": "Bajo - No describe un problema, solo pide información de precios",
    "timeline": "Desconocido - Sin urgencia aparente"
  },
  "action": "Enviar PDF + pedir intro al decisor",
  "reason": "Lead frío. Es un investigador, no un comprador. Enviar el PDF solicitado pero pedir explícitamente: '¿Podrías conectarnos con tu jefe para entender mejor el contexto y ofrecer una demo personalizada?' Si no hay intro al decisor en 1-2 semanas, mover a nurture pasivo."
}
```

---

## Resumen Visual

| Lead | Score | Veredicto |
|------|-------|-----------|
| 🟢 **Ana Gomez** | **9/10** | 🔥 Lead caliente - Actuar ya |
| 🟡 **Juan Perez** | **4/10** | 📧 Nurture - Descubrir más |
| 🔴 **Carlos Ruiz** | **2/10** | ❄️ Lead frío - Buscar al decisor |

> **Prioridad de recursos:** Ana >> Juan >> Carlos. La Serie B de Ana es una señal de oro — hay dinero disponible y una fecha límite.