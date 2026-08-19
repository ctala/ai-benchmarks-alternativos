# Kimi K2.5 (NIM) — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.32 | quality: 9.48
- latency_total: 165.424s | tokens_per_second: 7.9
- input_tokens: 279 | output_tokens: 1305
- judge_score: 4.8 | justificación: 

## Respuesta completa

 ```json
{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 6,
      "bant": {
        "budget": "Desconocido - Startup pequeña (5 personas) sugiere presupuesto limitado, pero no confirmado",
        "authority": "Alto - Es CEO, tiene poder de decisión total",
        "need": "Medio - Interés real en automatización de soporte, pero en etapa de exploración temprana ('viendo opciones')",
        "timeline": "Bajo - No menciona urgencia ni fecha específica"
      },
      "action": "Calificación rápida - Agendar llamada de descubrimiento para validar budget y definir timeline. Enviar case studies de startups similares.",
      "reason": "Tiene autoridad y necesidad real, pero falta claridad en capacidad de pago y urgencia. Potencial de conversión medio si se confirman recursos."
    },
    {
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Alto - Empresa de 200 empleados post-Serie B con capacidad financiera confirmada",
        "authority": "Alto - VP of Operations tiene poder de decisión sobre procesos operativos",
        "need": "Alto - Solicitó demo activamente tras webinar, interés de compra demostrado",
        "timeline": "Alto - Deadline definido (antes de Q3), urgencia real"
      },
      "action": "Prioridad máxima - Contacto inmediato (within 1 hour). Preparar demo personalizada enfocada en ROI y escalabilidad. Involucrar a Account Executive senior.",
      "reason": "Lead calificado completamente (BANT completo). Empresa en crecimiento con presupuesto, decisor con poder, necesidad urgente y timeline definido. Alta probabilidad de cierre rápido."
    },
    {
      "name": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido/Bajo - Intern sin acceso a información financiera, solo recolectando datos",
        "authority": "Muy bajo - No es decision maker, solo investigador delegado",
        "need": "Bajo - Necesidad de terceros (su jefe), no siente el dolor directamente",
        "timeline": "Desconocido - Solo busca información (PDF), sin urgencia mencionada"
      },
      "action": "Nurturing pasivo - Enviar brochure/precios pero NO invertir tiempo de ventas. Añadir a campaña de email marketing educativo. Intentar identificar al decision maker real.",
      "reason": "Lead muy temprano en el funnel (tire kicker). Falta autoridad, budget no validado y necesidad indirecta. Riesgo de perder tiempo si se trata como oportunidad real."
    }
  ],
  "summary": "Priorizar inmediatamente a Ana Gomez (Lead 2). Juan Perez requiere calificación de budget. Carlos Ruiz va a nurturing automatizado hasta que escale el contacto."
}
```