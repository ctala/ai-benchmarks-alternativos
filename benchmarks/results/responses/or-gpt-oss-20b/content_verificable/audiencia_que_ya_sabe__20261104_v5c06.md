# GPT-OSS 20B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 7.467s | tokens_per_second: 116.5
- input_tokens: 152 | output_tokens: 870

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

En n8n, la respuesta “success” no siempre implica que algo haya ocurrido.  
El flujo se marca como exitoso cuando **todas** las nodos se completan sin lanzar un error, pero si el flujo no recibe datos de entrada o si todas las condiciones se saltan, la ejecución sigue siendo “success” aunque prácticamente no haya hecho nada.

### Por qué sucede

1. **Webhooks sin payload** – Si un Webhook recibe un request vacío, el nodo devuelve *success* inmediatamente, a menos que tengas un nodo que verifique la presencia de datos.  
2. **Condiciones vacías** – Un nodo *If* que siempre evalúa a `false` deja la ejecución sin salida, pero no marca error.  
3. **Cron sin acción** – Un cron que desencadena un flujo que solo comprueba algo y no escribe, siempre llega a *success*.  
4. **Nodos con salida opcional** – Los nodos que no generan datos cuando la condición no se cumple (por ejemplo, *Set* con `add` vacío) siguen como “exitosos”.

### Cómo detectarlo

| Técnica | ¿Qué revisas? | Ejemplo rápido |
|---------|---------------|----------------|
| **Verificar `executionData`** | `{{$json["items"]?.length}}` | Si longitud = 0 → nada procesado |
| **Nodo `Set` con `{{$node["Webhook"].json["payload"]}}`** | Si vacío, envía alerta |
| **Nodo `IF` con `{{$json}}`** | Output “false” → no se ejecutó nada |
| **Webhook Response personalizado** | `{{$json["error"] ? "Error" : "Procesado"}}` |
| **Logs de ejecución** | UI → Execution > Summary → “Data length” o “Heartbeat” |  

En la práctica:  
1. Añade un nodo *Set* al inicio para grabar la longitud del payload.  
2. Usa un nodo *If* para comprobar esa longitud y redirige a un nodo *HTTP Response* con un mensaje “No payload recibido”.  
3. Si la condición es verdadera, sigue con tu lógica habitual.  

Así, cuando revises el historial de ejecuciones, verás que los flujos que retornan *success* pero con `items.length = 0` son los que realmente no hicieron nada. Mantén los flujos visibles y evita la confusión de “todo ok” cuando nada sucedió.