# Ling 3.0 Flash — sales_outreach/lead_qualification

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.432s | tokens_per_second: 364.2
- input_tokens: 303 | output_tokens: 1250
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando un análisis detallado y estructurado de cada lead.

## Respuesta completa

```json
{
  "leads": [
    {
      "lead": "Juan Perez - CEO startup de 5 personas",
      "score": 3,
      "bant": {
        "budget": "Bajo - No mencionó presupuesto. Startup de 5 personas con recursos limitados.",
        "authority": "Alto - Es CEO, sí es decisor.",
        "need": "Bajo - Interés exploratorio ('estamos viendo opciones'), no hay dolor concreto ni definido.",
        "timeline": "Bajo - No hay urgencia ni fecha mencionada."
      },
      "action": "Nurture",
      "reason": "Juan tiene autoridad como CEO pero su empresa es muy pequeña, no hay presupuesto visible ni necesidad urgente definida. Llegó de forma pasiva vía blog. Se debe nutrir con contenido educativo sobre automatización de soporte para escalar startups y mantenerlo en pipeline hasta que demuestre intención de compra."
    },
    {
      "lead": "Ana Gomez - VP of Operations, empresa de 200 empleados",
      "score": 9,
      "bant": {
        "budget": "Alto - Empresa acaba de levantar Serie B, tiene capital fresco asignado.",
        "authority": "Alto - VP of Operations en empresa de 200 empleados es decisor clave en operaciones.",
        "need": "Alto - Pidió demo activamente después de un webinar, indica problema real.",
        "timeline": "Alto - 'Necesitamos resolver esto antes de Q3' = urgencia clara."
      },
      "action": "Priorizar / Agendar demo inmediata",
      "reason": "Lead BANT completo: presupuesto (Serie B), autoridad (VP Operations), necesidad demostrada (pidió demo), y timeline urgente (antes de Q3). Es el lead más calificado. Se debe agendar demo lo antes posible y asignar a un AE senior."
    },
    {
      "lead": "Carlos Ruiz - Intern de marketing",
      "score": 1,
      "bant": {
        "budget": "Muy bajo - Un intern no maneja presupuesto.",
        "authority": "Muy bajo - Es intern, no es decisor. Su jefe es quien decide.",
        "need": "Bajo - No es su dolor, solo le pidieron investigar. Quiere un PDF de precios, no una solución.",
        "timeline": "Bajo - No mencionó fecha ni urgencia."
      },
      "action": "Descartar / Enviar PDF pasivo",
      "reason": "Carlos es un intern sin presupuesto ni autoridad de decisión. No tiene necesidad propia, solo está ejecutando una tarea asignada. Enviar el PDF de precios y hacer nurturing pasivo. Si hay oportunidad, intentar escalar la conversación al jefe de Carlos, pero el lead tiene muy baja probabilidad de conversión."
    }
  ]
}
```