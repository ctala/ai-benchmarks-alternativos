# Qwen 3.5 397B — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 4.17 | quality: 3.33
- latency_total: 8.313s | tokens_per_second: 55.0
- input_tokens: 262 | output_tokens: 457

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
      "budget": "Desconocido (No mencionado)",
      "authority": "Alto (Es CEO y decision maker)",
      "need": "Moderado (Buscando opciones para automatizar soporte)",
      "timeline": "Indefinido (Fase de exploración temprana)"
    },
    "action": "Nurturing / Calificación adicional",
    "reason": "Tiene autoridad total y una necesidad clara, pero al ser una startup pequeña y no haber mencionado presupuesto ni urgencia, el riesgo de cierre a corto plazo es medio. Requiere educación sobre el ROI antes de vender."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto probable (Recién levantaron Serie B)",
      "authority": "Alto (VP of Operations es decision maker clave)",
      "need": "Crítico (Necesitan resolver un problema operativo)",
      "timeline": "Urgente (Antes de Q3)"
    },
    "action": "Contacto inmediato / Agendar Demo",
    "reason": "Lead ideal bajo BANT: tiene dinero reciente (Serie B), autoridad para decidir, una necesidad explícita y una fecha límite concreta. Prioridad máxima."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido (Solo pide PDF de precios)",
      "authority": "Nulo (Es becario/intern, no decide)",
      "need": "Débil (Tarea asignada de investigación, no dolor propio)",
      "timeline": "Sin urgencia definida"
    },
    "action": "Enviar recurso automático / Descalificar temporalmente",
    "reason": "Falta de autoridad es el factor limitante principal. No es el tomador de decisiones. La mejor estrategia es enviar el PDF automáticamente para no gastar tiempo de ventas humano y esperar a que contacte un perfil senior."
  }
]
```