# Claude Opus 5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 31.062s | tokens_per_second: 61.7
- input_tokens: 410 | output_tokens: 1915

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
    "lead": "Juan Perez — CEO, startup 5 personas",
    "score": 5,
    "bant": {
      "budget": "Desconocido. No mencionó presupuesto y una startup de 5 personas suele tener capacidad limitada. Riesgo de quedar por debajo del ticket mínimo.",
      "authority": "Fuerte. Como CEO de 5 personas es el decisor único; no hay comité de compra.",
      "need": "Tibia pero real. 'Estamos viendo opciones' indica exploración, no dolor urgente. Con 5 personas el volumen de soporte probablemente aún es manejable manualmente.",
      "timeline": "Ausente. Ninguna señal de fecha o evento forzante."
    },
    "action": "Nurture con toque humano: email personal ofreciendo llamada corta de 15 min de diagnóstico (no demo). Secuencia de contenido sobre automatización de soporte para equipos pequeños.",
    "reason": "Acceso directo al decisor es valioso y barato de aprovechar, pero sin presupuesto ni timeline no justifica ciclo de venta completo. La llamada corta sirve para calificar budget y descartar rápido si no encaja. Nota: si la startup está en crecimiento acelerado puede convertirse en buen lead en 2-3 trimestres — vale mantenerlo tibio, no cerrarlo."
  },
  {
    "lead": "Ana Gomez — VP of Operations, 200 empleados",
    "score": 9,
    "bant": {
      "budget": "Fuerte. Serie B reciente = capital disponible y presión por escalar operaciones con eficiencia. Empresa de 200 empleados tiene línea presupuestal para herramientas.",
      "authority": "Fuerte, con matiz. VP of Ops es dueña del problema y típicamente decisora o sponsor principal. Probablemente requiere firma de CFO o CEO según el monto — hay que mapearlo.",
      "need": "Explícita y validada. Pidió demo activamente y verbalizó el problema como algo que 'necesitamos resolver'.",
      "timeline": "Explícito. Antes de Q3, con evento forzante implícito (escalar post-Serie B)."
    },
    "action": "Contacto inmediato (<2 horas si es posible). Agendar la demo solicitada esta misma semana, personalizada a operaciones/soporte. En la llamada: mapear proceso de aprobación, monto de presupuesto y quién más firma.",
    "reason": "BANT completo con timeline autoimpuesto y capital fresco. Es el perfil de mayor probabilidad de cierre y mayor ticket del lote. El único riesgo es velocidad: post-Serie B suele evaluar varios vendors en paralelo, así que la ventaja competitiva está en tiempo de respuesta. No es 10 porque falta confirmar monto de presupuesto y proceso de aprobación."
  },
  {
    "lead": "Carlos Ruiz — Intern de marketing",
    "score": 2,
    "bant": {
      "budget": "Ausente. Un intern no tiene control ni visibilidad presupuestal.",
      "authority": "Ausente. Cero poder de decisión. Es un recopilador de información.",
      "need": "Indirecta y vaga. 'Herramientas de IA' es demasiado amplio — no hay evidencia de que el problema que resolvemos sea el problema real de la empresa.",
      "timeline": "Desconocido. Podría ser un research exploratorio sin intención de compra en el corto plazo."
    },
    "action": "Enviar el PDF de precios (o página de pricing) y responder amablemente. Incluir una pregunta puente: '¿te ayudo agendando 15 min con tu jefe/a para ver si aplica a su caso?'. Mantener en nurture automatizado, sin asignar a ventas.",
    "reason": "El lead en sí no es calificable, pero es un puente potencial hacia quien sí decide. El costo de atenderlo bien es casi cero y negarle información solo cierra la puerta. Advertencia importante: el 'jefe' detrás puede ser un buen lead o esto puede ser research competitivo — no compartir información sensible de arquitectura, roadmap o descuentos personalizados. Si el intern nombra a su jefe/a y la empresa encaja en nuestro perfil ideal, escalar el score y reasignar."
  }
]
```

**Priorización sugerida:** Ana (acción hoy) → Juan (esta semana, bajo esfuerzo) → Carlos (respuesta automatizada + intento de puente).