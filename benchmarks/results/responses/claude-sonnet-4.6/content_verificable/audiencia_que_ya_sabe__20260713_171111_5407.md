# Claude Sonnet 4.6 (ultimo Anthropic) — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 11.73s | tokens_per_second: 36.7
- input_tokens: 124 | output_tokens: 430
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando el problema específico y ofreciendo soluciones prácticas.

## Respuesta completa

# El éxito que miente

Tu workflow terminó. Verde. Sin errores. Y el dato nunca llegó a destino.

Bienvenido al problema más silencioso de n8n.

---

**Por qué pasa**

El nodo HTTP Request recibió un 200. El nodo de Slack respondió `ok: true`. N8n marcó la ejecución como exitosa porque, técnicamente, lo fue: hizo exactamente lo que le pediste. El problema es que lo que le pediste estaba mal.

Los casos más comunes:

- **Filtros que descartan todo.** Un IF o un Filter con condición incorrecta deja el array vacío. Los nodos siguientes no ejecutan, pero n8n no lo considera un error.
- **Upserts silenciosos.** Escribes en Airtable o en Postgres con "update if exists". No existía nada. No se insertó nada. Status: 200.
- **Webhooks que responden antes de procesar.** Confirmas recepción al inicio del workflow y luego algo falla downstream. El emisor cree que todo está bien.

---

**Cómo detectarlo**

Añade un nodo **IF** al final de tu rama crítica que verifique que el output tiene sentido: que el array no está vacío, que el ID devuelto existe, que el contador es mayor que cero.

Si la condición no se cumple, lleva ese ramal a un **nodo de error manual** (`throw`) o, mejor, a un mensaje en Slack con contexto real: qué workflow, qué datos esperabas, qué llegó.

Los errores ruidosos son tus amigos. El silencio verde es lo que te quita el sueño.