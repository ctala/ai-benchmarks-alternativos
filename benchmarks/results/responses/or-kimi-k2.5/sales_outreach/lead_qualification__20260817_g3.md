# Kimi K2.5 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 3.54 | quality: 3.33
- latency_total: 82.697s | tokens_per_second: 27.1
- input_tokens: 279 | output_tokens: 2241

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

```json
[
  {
    "score": 6,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas con recursos presumiblemente limitados, aunque como CEO tiene control total sobre ellos.",
      "authority": "Alto. Es el CEO, por lo tanto es el decision maker final.",
      "need": "Moderado. Tiene interés real en automatizar soporte, pero se encuentra en etapa exploratoria ('viendo opciones').",
      "timeline": "Indefinido. No hay urgencia declarada; está evaluando alternativas sin fecha límite."
    },
    "action": "Nutrir con contenido educativo (case studies, guías) y programar un llamado de descubrimiento ligero. No forzar una demo de ventas aún.",
    "reason": "Es un decisor con una necesidad real, pero está en fase temprana sin presupuesto ni timeline claros. Se debe construir confianza antes de avanzar en el pipeline."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa de 200 empleados que acaba de levantar Serie B, lo que indica capacidad de inversión y liquidez.",
      "authority": "Alto. Como VP of Operations, tiene alta probabilidad de ser decision maker o al menos influyente directa en la decisión.",
      "need": "Alto. Solicitó activamente una demo después de un webinar, lo que demuestra un problema consciente y activo.",
      "timeline": "Corto y definido. Expresó urgencia explícita: necesita resolverlo antes de Q3."
    },
    "action": "Prioridad máxima. Contacto inmediato por un Account Executive en menos de 2 horas. Agendar demo personalizada y preparar propuesta de valor orientada a operaciones.",
    "reason": "Perfil ideal: decisora con necesidad confirmada, urgencia clara y empresa recién capitalizada con capacidad de pago. Lead caliente con alta probabilidad de cierre."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido. Como intern de marketing, carece de visibilidad sobre el presupuesto.",
      "authority": "Muy bajo. Es un pasante investigando por encargo; no tiene poder de decisión.",
      "need": "Bajo/Indirecto. La necesidad pertenece a su jefe, no a él. Su interés se limita a recolectar información (PDF de precios).",
      "timeline": "Desconocido. No existe ninguna fecha ni sentido de urgencia declarado."
    },
    "action": "Enviar material de marketing básico (one-pager o brochure) sin asignar tiempo de ventas. Intentar identificar y contactar al jefe/director de marketing que le encargó la tarea.",
    "reason": "Lead de muy baja calidad por falta de autoridad, necesidad indirecta y ausencia de timeline. Riesgo alto de quedarse en investigación interna sin avanzar a compra."
  }
]
```