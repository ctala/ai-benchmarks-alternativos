# GLM 5 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5`
- success: True  | final: 4.03 | quality: 3.33
- latency_total: 11.198s | tokens_per_second: 47.9
- input_tokens: 249 | output_tokens: 536

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
    "score": 4,
    "bant": {
      "budget": "Desconocido - No mencionó presupuesto, empresa pequeña (5 personas).",
      "authority": "Alto - Es el CEO, probable tomador de decisiones.",
      "need": "Medio - Tiene interés en automatizar soporte, pero está en etapa inicial de 'ver opciones'.",
      "timeline": "Bajo - Sin urgencia definida."
    },
    "action": "Asignar a Nurture / Enviar secuencia de emails educativos y agendar llamada de descubrimiento.",
    "reason": "El lead tiene autoridad y un problema real, pero llegó por el blog sin intención de compra inmediata ni presupuesto definido. Requiere maduración."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto - Empresa de 200 empleados que acaba de levantar Serie B (tiene capital).",
      "authority": "Alto - VP of Operations, típicamente un tomador de decisiones clave o influyente.",
      "need": "Alto - Pidió una demostración activa después de un webinar.",
      "timeline": "Alto - Urgencia clara, necesita resolverlo antes de Q3."
    },
    "action": "Contacto inmediato por ventas (Call SDR/AE) para agendar la demo y enviar propuesta.",
    "reason": "Cumple con todos los criterios BANT. Tiene urgencia, presupuesto gracias al Serie B, autoridad y necesidad explícita. Es un lead altamente cualificado y listo para cerrar."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido - Solo pide un PDF con precios.",
      "authority": "Bajo - Es un pasante de marketing, no es el tomador de decisiones.",
      "need": "Bajo - Solo le pidieron 'investigar', no hay un problema o dolor específico definido.",
      "timeline": "Bajo - Tarea de investigación sin fecha límite de implementación."
    },
    "action": "Enviar material solicitado (PDF) y agregar a newsletter. No asignar a ventas.",
    "reason": "Es un investigador de bajo nivel sin autoridad para comprar y sin una necesidad específica más allá de cumplir un encargo de su jefe. No vale la pena el tiempo del equipo de ventas aún."
  }
]
```