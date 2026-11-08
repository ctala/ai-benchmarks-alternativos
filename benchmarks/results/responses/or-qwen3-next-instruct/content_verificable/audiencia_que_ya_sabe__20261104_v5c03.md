# Qwen 3-Next 80B Instruct — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.56 | quality: 10.0
- latency_total: 1.949s | tokens_per_second: 204.2
- input_tokens: 109 | output_tokens: 398

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Tu workflow devuelve “success”… pero nada pasó?

Sí. Eso pasa. Y no es un bug. Es un diseño.

n8n marca un workflow como “success” si todos los nodos se ejecutaron sin errores —no si hicieron lo que *esperabas*. Un HTTP Request puede responder 200… pero el endpoint no guardó nada. Un Webhook puede recibir el payload… pero tu filtro lo descartó silenciosamente. Un Function Node puede retornar `null`… y el siguiente nodo lo pasa como si nada.

El problema no es la ejecución. Es la *verificación implícita*.

Aquí cómo detectarlo:

1. **Revisa los outputs de cada nodo.** No asumas que “si no hay error, funcionó”. Usa un Debug Node después de cada paso crítico.  
2. **Haz que tu workflow “grite” si no hace lo que debe.** Añade un nodo de condición: si `{{ $json.data.count === 0 }}`, dispara un webhook a Slack o un email.  
3. **Usa “Set” para validar estados.** Antes de terminar, crea un campo como `workflowStatus: "completed"` y úsalo como checkpoint. Si no está, sabes que algo se rompió en silencio.  
4. **Monitorea el historial de ejecuciones con filtros.** Busca ejecuciones con “success” pero con 0 items en el output del último nodo. Es la firma del silencio.

Un workflow que no se verifica, es un workflow que se desmorona en producción.

No confíes en el “success”. Confía en los datos que confirmas.

—  
¿Tienes un caso donde esto te pasó? Responde y te mando un template de checkpoint para evitarlo.