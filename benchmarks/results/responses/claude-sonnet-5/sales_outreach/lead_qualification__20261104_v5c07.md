# Claude Sonnet 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 15.162s | tokens_per_second: 85.2
- input_tokens: 410 | output_tokens: 1292

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de calificacion de leads. Evalua cada lead con un score 1-10 y decide la accion.

Framework BANT:
- Budget: tiene presupuesto?
- Authority: es decision maker?
- Need: tiene el problema que resolvemos?
- Timeline: necesita solucion pronto?

Responde en JSON: {"score": N, "bant": {"budget": "...", "authority": "...", "need": "...", "timeline": "..."}, "action": "...", "reason": "..."}

**user:**

Lead 1: Juan Perez, CEO de una startup de 5 personas. Dice que "estamos viendo opciones para automatizar nuestro soporte". No menciono presupuesto. Llego via el blog.

Lead 2: Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que "necesitamos resolver esto antes de Q3". Su empresa acaba de levantar Serie B.

Lead 3: Carlos Ruiz, intern de marketing. Dice que su jefe le pidio "investigar herramientas de IA". Quiere un PDF con precios.

Califica los 3 leads.


## Respuesta completa

# Calificación de Leads

```json
[
  {
    "lead": "Juan Perez - CEO Startup",
    "score": 6,
    "bant": {
      "budget": "Desconocido - no mencionado, pero startup de 5 personas sugiere presupuesto limitado/ajustado",
      "authority": "Alta - es CEO, decision maker directo en empresa pequeña",
      "need": "Confirmado pero exploratorio - 'viendo opciones' indica etapa temprana de investigación, no dolor urgente articulado",
      "timeline": "No definido - sin fecha ni urgencia expresada"
    },
    "action": "Nurture + calificar presupuesto",
    "reason": "Authority alta compensa la falta de info en budget/timeline. Es un lead de calidad media-alta por ser decision maker, pero está en fase de exploración (llegó vía blog = investigación pasiva). Enviar contenido educativo y hacer 1-2 preguntas de calificación (presupuesto estimado, timeline) antes de agendar llamada comercial. No descartar, pero no es prioridad inmediata."
  },
  {
    "lead": "Ana Gomez - VP Operations",
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad - empresa con 200 empleados + Serie B reciente = capital disponible para inversión",
      "authority": "Alta - VP of Operations típicamente tiene poder de decisión o fuerte influencia en compras de este tipo",
      "need": "Explícito y validado - participó en webinar relevante y solicitó demo activamente (acción, no solo interés pasivo)",
      "timeline": "Urgente y específico - 'antes de Q3' da un deadline concreto y genera presión de cierre"
    },
    "action": "Escalar a ventas inmediatamente - agendar demo prioritaria",
    "reason": "Lead caliente en los 4 pilares de BANT. Combinación ideal: dinero fresco (Serie B), cargo con autoridad, necesidad validada por comportamiento (pidió demo) y deadline claro. Asignar a un rep senior y contactar en <24h para no perder momentum."
  },
  {
    "lead": "Carlos Ruiz - Intern Marketing",
    "score": 2,
    "bant": {
      "budget": "Desconocido - el intern no maneja ni conoce esta información",
      "authority": "Nula - es intern, solo está ejecutando una tarea asignada, no es decision maker",
      "need": "Indirecto - el que tiene el problema real es 'su jefe', no hay contacto directo con el decision maker",
      "timeline": "Sin indicios - tarea de investigación básica, no hay presión de negocio visible"
    },
    "action": "Enviar PDF automatizado + nurture de bajo esfuerzo (no asignar a ventas)",
    "reason": "Score bajo porque no hay acceso a quien realmente decide. Es válido responder (entregar el PDF solicitado) para no cerrar la puerta, pero no vale la pena invertir tiempo comercial activo. Si es posible, incluir en el PDF un CTA para que 'su jefe' se registre directamente y así identificar al verdadero lead calificado."
  }
]
```

## Resumen y priorización

| Lead | Score | Prioridad | Próxima acción |
|------|-------|-----------|-----------------|
| Ana Gomez | 9/10 | 🔴 Alta | Contactar en <24h, agendar demo |
| Juan Perez | 6/10 | 🟡 Media | Nurture + preguntas de calificación |
| Carlos Ruiz | 2/10 | 🟢 Baja | PDF automatizado, no asignar rep |