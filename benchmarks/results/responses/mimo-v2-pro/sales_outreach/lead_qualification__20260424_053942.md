# MiMo-V2-Pro — sales_outreach/lead_qualification

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.67 | quality: 9.64
- latency_total: 18.866s | tokens_per_second: 58.8
- input_tokens: 264 | output_tokens: 1110
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 5,
      "bant": {
        "budget": "Desconocido. Startup de 5 personas, probablemente presupuesto limitado.",
        "authority": "Alto. Es CEO, es el tomador de decisiones.",
        "need": "Medio. Menciona automatización de soporte, pero está en etapa exploratoria ('estamos viendo opciones').",
        "timeline": "Bajo. No hay urgencia expresada."
      },
      "action": "Nurture - Enviar contenido educativo y agendar llamada de descubrimiento en 2-3 semanas.",
      "reason": "Tiene autoridad y una necesidad incipiente, pero está en modo exploración temprana sin presupuesto definido ni urgencia. Hay que madurar el lead con contenido de valor antes de avanzar."
    },
    {
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Alto. Empresa de 200 empleados que acaba de cerrar Serie B = capital fresco disponible.",
        "authority": "Alto. VP of Operations, rol ejecutivo con poder de decisión.",
        "need": "Alto. Pidió demo activamente y verbalizó el problema con claridad.",
        "timeline": "Alto. Plazo explícito: 'antes de Q3'."
      },
      "action": "Prioridad alta - Agendar demo inmediatamente y preparar propuesta personalizada.",
      "reason": "Lead caliente. Cumple los 4 criterios BANT de forma sólida. Empresa en crecimiento con presupuesto recién levantado, tomadora de decisiones, necesidad clara y urgencia definida. Máxima prioridad comercial."
    },
    {
      "name": "Carlos Ruiz",
      "score": 3,
      "bant": {
        "budget": "Desconocido. No tiene acceso a información financiera.",
        "authority": "Nulo. Es un intern; no toma decisiones.",
        "need": "Indirecto. Su jefe tiene interés, pero él solo ejecuta una tarea de investigación.",
        "timeline": "Desconocido. No hay urgencia expresada."
      },
      "action": "Enviar PDF solicitado + pedir amablemente una intro con su jefe. Incluir un caso de estudio que justifique una reunión con el decisor real.",
      "reason": "Lead frío en su forma actual. Sin autoridad ni presupuesto. Sin embargo, hay señal de que en la organización hay interés (su jefe pidió la investigación). La estrategia debe ser escalar al verdadero tomador de decisiones."
    }
  ]
}
```

### Resumen rápido

| Lead | Score | Veredicto |
|------|-------|-----------|
| **Ana Gomez** | 🟢 **9** | Lead caliente → acción inmediata |
| **Juan Perez** | 🟡 **5** | Lead tibio → nurture con contenido |
| **Carlos Ruiz** | 🔴 **3** | Lead frío → escalar al decisor |