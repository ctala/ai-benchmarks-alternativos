# MiniMax M3 — sales_outreach/lead_qualification

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.55 | quality: 9.24
- latency_total: 57.605s | tokens_per_second: 18.9
- input_tokens: 403 | output_tokens: 1091
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas sugiere budget limitado, pero no descartable.",
      "authority": "Alta. CEO es el ultimate decision maker.",
      "need": "Claro. 'Automatizar soporte' encaja directamente con el producto.",
      "timeline": "Vago. 'Estamos viendo opciones' indica fase de exploración, sin urgencia."
    },
    "action": "Nurturing + calificación. Enviar contenido educativo (casos de uso para startups pequeñas), intentar agendar discovery call para entender budget y timeline reales.",
    "reason": "Authority y need son sólidos, pero la falta de budget explícito y timeline indefinido impiden priorización alta. Vale la pena cultivar — los CEOs de startups que automatizan temprano suelen convertirse en cuentas de alto LTV."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa de 200 empleados con Serie B recién levantada = capital disponible.",
      "authority": "Alta. VP of Operations tiene poder de decisión sobre herramientas operacionales y de soporte.",
      "need": "Alto. Solicitó demo por iniciativa propia tras webinar = dolor activo, no curiosidad pasiva.",
      "timeline": "Urgente. 'Antes de Q3' da un deadline concreto (1-2 trimestres)."
    },
    "action": "Hot lead. Asignar a AE senior inmediatamente. Agendar demo personalizada en menos de 48h, preparar caso de uso relevante para empresa Serie B, involucrar al CEO/fundador si aplica.",
    "reason": "Reúne las 4 condiciones BANT. Señales comportamentales (demo solicitada, asistencia a webinar, lenguaje de urgencia) confirman intención real. Riesgo de perderla si el ciclo de respuesta es lento."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido. Pidió PDF con precios, pero como research, no como intención de compra.",
      "authority": "Muy baja. Intern no tiene poder de decisión ni influencia en budget.",
      "need": "Indirecto. La necesidad es de su jefe, no de él. No hay pain articulated.",
      "timeline": "Inexistente. Solo 'investigar herramientas' = far future."
    },
    "action": "Low touch. Enviar el PDF solicitado con un email genérico. Agregar a secuencia de nurturing para mantener visibilidad, pero NO invertir tiempo de AE. Si el jefe aparece en el radar, re-calificar.",
    "reason": "Es un researcher, no un buyer. Malgastar tiempo de ventas aquí reduce capacidad de cierre en leads como Ana. El lead real (el jefe) no está identificado aún."
  }
]
```

**Resumen ejecutivo:**
| Lead | Score | Acción prioritaria |
|------|-------|---------------------|
| Ana Gomez | **9** | Demo ASAP, fast-track |
| Juan Perez | **6** | Nurturing + discovery |
| Carlos Ruiz | **2** | Self-service (PDF) |