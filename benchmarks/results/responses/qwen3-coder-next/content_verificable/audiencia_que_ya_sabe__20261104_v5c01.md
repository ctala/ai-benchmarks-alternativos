# Qwen3-Coder-Next (OpenRouter FP8) — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 5.736s | tokens_per_second: 74.6
- input_tokens: 109 | output_tokens: 428

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Cuando tu workflow dice “success”… pero no hizo nada**  

Has configurado un workflow en n8n, lo ejecutas y recibes un *“success”* en el nodo final. ¿Todo OK? No tan rápido.  

El problema más sutil (y común) es que un workflow puede completarse sin errores —y sin hacer lo que supposed to do— simplemente porque *algún nodo no se ejecutó*. Esto ocurre cuando:  

- Un nodo previo falla silenciosamente (por ejemplo, un *Filter* que devuelve 0 items, o un *Switch* que no coincide con ninguna condición).  
- Un webhook recibe una petición vacía o sin los datos esperados, y el flujo sigue “normalmente” con datos nulos.  
- Un cron dispara el flujo, pero la condición inicial (por ejemplo, un *If* o *Function* node) lo deriva a un camino sin salida.  

**Cómo detectarlo:**  
- **Habita el nodo “Debug”** entre etapas críticas: no solo al final. Verás si el flujo continúa con items vacíos o undefined.  
- **Usa `{{ $input.all().length }}`** en nodos finales para validar que hubo datos de entrada.  
- **Activa logs en el editor**: n8n los guarda 24h por defecto. Filtra por *“No items returned”* o *“0 items”* para encontrar flujos que no procesaron nada.  
- **Agrega un nodo final “Slack” o “Email”** que solo se dispare si `items.length === 0`. Es un *sentinel* útil.  

La clave: *success ≠ éxito funcional*. Tu workflow no está roto: está incompleto.  

¿Tienes un caso donde “success” te engañó? Compártelo en reply — vamos a desentrañarlo juntos.