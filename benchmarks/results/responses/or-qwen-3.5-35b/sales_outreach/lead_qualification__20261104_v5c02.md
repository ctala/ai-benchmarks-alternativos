# Qwen 3.5 35B — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 4.48 | quality: 3.33
- latency_total: 5.549s | tokens_per_second: 104.2
- input_tokens: 262 | output_tokens: 578

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
    "score": 3,
    "bant": {
      "budget": "No especificado. Al ser una startup pequeña de 5 personas y no haber mención de presupuesto, es incierto si tienen fondos asignados.",
      "authority": "Alto. Es CEO, por lo que tiene autoridad total para decidir en una empresa tan pequeña.",
      "need": "Medio. Menciona que están 'viendo opciones', lo que indica un interés inicial pero no necesariamente una urgencia o dolor agudo inmediato.",
      "timeline": "Bajo. La frase 'viendo opciones' sugiere una fase de exploración temprana sin un plazo definido."
    },
    "action": "Nurturing (Educación)",
    "reason": "Es un lead con autoridad pero falta confirmación de presupuesto y urgencia. Necesita más contenido educativo para calentar el interés antes de intentar vender."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Acaban de levantar Serie B, lo que garantiza liquidez y capacidad de gasto significativa.",
      "authority": "Alto. Como VP of Operations, toma decisiones operativas y suele tener la autoridad para aprobar compras de software.",
      "need": "Alto. Pidió una demo activamente tras un webinar, indicando un interés fuerte.",
      "timeline": "Alto. Tiene un deadline claro: resolverlo antes del Q3 (cuarto trimestre)."
    },
    "action": "Venta Directa / Agendar Demo",
    "reason": "Lead ideal (Hot Lead). Cumple todos los criterios BANT con alta intensidad: tiene dinero, autoridad, necesidad clara y prisa. Requiere atención inmediata de ventas."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido/Inexistente. Un intern generalmente no maneja el presupuesto ni la aprobación final.",
      "authority": "Nulo. Es un pasante; su objetivo es investigar, no comprar. Necesita la aprobación de su jefe.",
      "need": "Bajo. La necesidad es interna (investigar para el jefe), no es una decisión operativa propia.",
      "timeline": "Bajo. Solo pide un PDF informativo, sin plazos de implementación."
    },
    "action": "Descartar / Auto-responder",
    "reason": "No es el buyer persona. Aunque muestra interés, carece de autoridad y probablemente de presupuesto. Enviarle información general y esperar a que su jefe contacte es más eficiente que invertir tiempo de ventas ahora."
  }
]
```