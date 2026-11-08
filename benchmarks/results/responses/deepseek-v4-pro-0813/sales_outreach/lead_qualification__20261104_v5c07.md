# DeepSeek V4 Pro (0813) — sales_outreach/lead_qualification

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 6.991s | tokens_per_second: 54.8
- input_tokens: 261 | output_tokens: 383

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
    "lead": "Juan Perez",
    "score": 6,
    "bant": {
      "budget": "Desconocido",
      "authority": "Sí, es CEO",
      "need": "Sí, buscan automatizar soporte",
      "timeline": "Indefinido"
    },
    "action": "Nutrir y calificar",
    "reason": "Tiene autoridad y necesidad clara, pero falta validar presupuesto y urgencia. Llegó por contenido, está en etapa temprana."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Probable (Serie B reciente)",
      "authority": "Sí, VP of Operations",
      "need": "Sí, explícito",
      "timeline": "Antes de Q3"
    },
    "action": "Contactar de inmediato",
    "reason": "Lead casi perfecto: autoridad, necesidad urgente, presupuesto probable por financiamiento reciente y mostró intención activa al pedir demo."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "No, es intern",
      "need": "Indirecta (investiga para su jefe)",
      "timeline": "Indefinido"
    },
    "action": "Enviar material informativo",
    "reason": "Sin autoridad ni urgencia. Solo busca información general. Baja probabilidad de conversión; mantener en lista de bajo contacto."
  }
]
```