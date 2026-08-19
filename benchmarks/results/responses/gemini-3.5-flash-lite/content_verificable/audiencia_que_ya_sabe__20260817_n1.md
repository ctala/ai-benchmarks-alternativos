# Gemini 3.5 Flash Lite — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 3.85s | tokens_per_second: 126.7
- input_tokens: 93 | output_tokens: 488

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Te ha pasado? Miras el historial de ejecución en n8n: todo verde, estado *Success*, latencia baja. Te vas a tomar un café feliz. Luego abres la herramienta destino y... no hay nada. Cero registros. El clásico "funciona en mi máquina" versión automatización.

Un *Success* en n8n solo significa una cosa: **el motor llegó al último nodo sin que ningún bloque lanzara un error crítico.** No significa que el objetivo del negocio se haya cumplido. 

Aquí te dejo los tres culpables habituales de este fantasma y cómo cazarlos antes de que arruinen tus datos:

**1. El "Falso Positivo" de la API (HTTP Request)**
Un `200 OK` no garantiza que la operación sea válida. Muchas APIs devuelven un 200 con un JSON interno que dice `"success": false` o acumulan el error en un array de `errors`. 
* **Solución:** Añade siempre un nodo *If* post-petición que valide la respuesta de negocio del servidor, no el código de estado HTTP. Si hay error, fuerza una excepción con el nodo *Stop and Error*.

**2. Listas vacías en bucles (Looping silencioso)**
Si tu nodo *Code* o *Item Lists* procesa un array que llegó vacío (por un filtro muy agresivo o un cambio en el schema de entrada), el workflow salta el bucle, llega al final y... *Success*.
* **Solución:** Usa un nodo *If* al inicio para comprobar que la longitud del array es mayor a 0. Si está vacío, ramifica hacia una alerta (Telegram/Slack) que te avise: "Flujo ejecutado sin datos".

**3. El purgatorio del reintento infinito**
Si configuras políticas de reintento mal estructuradas, el workflow puede quedar en un limbo asíncrono o terminar reportando éxito tras agotar intentos en una lógica condicional mal cerrada.

**La regla de oro:** Nunca confíes en el verde de n8n. Diseña tus workflows asumiendo que **todo va a fallar**. Valida explícitamente la salida de cada nodo crítico y haz que tus flujos griten cuando no pase nada.