# Ministral 14B — sales_outreach/lead_qualification

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 8.378s | tokens_per_second: 81.0
- input_tokens: 253 | output_tokens: 679
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una evaluación detallada y acciones específicas para cada lead.

## Respuesta completa

```json
[
    {
        "score": 5,
        "bant": {
            "budget": "Desconocido (no mencionado)",
            "authority": "Parcial (CEO, pero no confirma urgencia o compromiso)",
            "need": "Potencial (automatizar soporte, pero no detalla dolor específico)",
            "timeline": "Indefinido (no menciona plazo)"
        },
        "action": "Nurturing (educación + seguimiento suave)",
        "reason": "Juan es un *decision-maker* (CEO), pero falta claridad en **budget**, **need** (¿qué problema exacto?) y **timeline**. Como llegó orgánicamente (blog), priorizar contenido de valor (casos de éxito, ROI de automatización) para calificar mejor antes de vender. Riesgo: podría ser un lead frío o sin presupuesto oculto."
    },
    {
        "score": 9,
        "bant": {
            "budget": "Alto (Serie B reciente, capacidad de inversión)",
            "authority": "Alta (VP of Operations, rol estratégico y operativo)",
            "need": "Claro (resolver problema de soporte antes de Q3)",
            "timeline": "Urgente (plazo definido: Q3)"
        },
        "action": "Priorizar demo + propuesta comercial (equipo de ventas)",
        "reason": "Ana cumple **todos los criterios BANT**:
        - **Budget**: Serie B implica recursos para herramientas estratégicas.
        - **Authority**: VP de Operations tiene poder de decisión y alineación con operaciones.
        - **Need**: Problema definido y crítico para su plan (antes de Q3).
        - **Timeline**: Urgencia clara.
        **Acción inmediata**: Coordinar demo con su equipo técnico/operativo para validar fit. Enviar testimonio de cliente en etapa similar (ej: empresa en crecimiento con 200+ empleados)."
    },
    {
        "score": 2,
        "bant": {
            "budget": "Desconocido (solo pide PDF de precios)",
            "authority": "Baja (intern, no decision-maker)",
            "need": "Indirecto (investigar "herramientas de IA", sin problema específico)",
            "timeline": "Indefinido (depende de su jefe)"
        },
        "action": "Descartar o nurturing pasivo (si hay recursos)",
        "reason": "Carlos **no es un lead calificado**:
        - **Authority**: Un *intern* no toma decisiones ni asigna presupuesto.
        - **Need**: Falta claridad en el problema (¿automatización? ¿IA generativa? ¿soporte?).
        - **Budget/Timeline**: Desconocidos y dependen de su jefe (sin contacto directo).
        **Excepción**: Si el equipo comercial tiene capacidad, enviar **un solo email** con un PDF genérico + pregunta para calificar a su jefe (*'¿Podrías compartirme el nombre de quien toma decisiones en este proyecto?'*). De lo contrario, descartar."
    }
]
```