# GPT-5.4 — content_verificable/audiencia_que_ya_sabe

- model_id: `gpt-5.4`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 5.938s | tokens_per_second: 69.2
- input_tokens: 101 | output_tokens: 411
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y perspectivas para detectar problemas en workflows de n8n.

## Respuesta completa

A veces el peor fallo en n8n no es el rojo. Es el verde.

Un workflow puede terminar en **“success”** y, aun así, no haber producido ningún efecto real. No porque n8n “mienta”, sino porque el estado de ejecución solo confirma que **los nodos terminaron sin error técnico**. No garantiza que haya habido trabajo útil.

Pasa mucho en tres casos:

1. **Entrada vacía**: el trigger dispara, pero llega un payload vacío o una lista sin items. Todo corre “bien”, solo que no había nada que procesar.  
2. **Filtros demasiado agresivos**: un IF, un Switch o una expresión mal afinada deja el flujo sin items a mitad de camino. La ejecución sigue, pero aguas abajo ya no hay nada.  
3. **Falsos positivos de APIs**: una llamada responde 200/202, pero el sistema externo no creó, actualizó ni encoló nada relevante.

La forma práctica de detectarlo no es mirar solo el badge verde, sino definir **señales de trabajo real**.

Algunas que funcionan bien:

- **Cuenta de items por tramo**: si un nodo clave recibe 120 items y el siguiente entrega 0, eso no es “success”, es una pista.  
- **Checks de efecto**: no te quedes con el status code; valida IDs creados, filas afectadas, mensajes enviados, archivos subidos.  
- **Ramas explícitas de “no-op”**: si no hay items, trátalo como estado propio y notifícalo. Mejor un “no había nada que hacer” que un éxito ambiguo.  
- **Métricas mínimas**: items entrantes, items procesados, items descartados, acciones exitosas.

La idea clave: **“success” no significa “impacto”**. Si tu workflow importa, mide el resultado de negocio, no solo que la tubería no explotó.