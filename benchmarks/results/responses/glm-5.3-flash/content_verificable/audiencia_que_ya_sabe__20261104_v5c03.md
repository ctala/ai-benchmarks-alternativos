# GLM 5.3 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 21.076s | tokens_per_second: 71.2
- input_tokens: 107 | output_tokens: 1501

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## Tu workflow dice «success». Tu negocio dice que no pasó nada.

n8n marca una ejecución como exitosa cuando ningún nodo lanza error. Nada más. Y ahí está la trampa: hay tres formas clásicas de terminar en verde sin haber hecho trabajo real.

**1. El branch vacío.** Un IF o Switch que no matchea ninguna ruta —o cuya ruta activa no tiene nodos— cierra la ejecución limpiamente. Success.

**2. El filtro que devuelve cero items.** Cuando un nodo entrega 0 items, n8n se salta silenciosamente todo el downstream. El workflow "corrió", pero ni tu HTTP Request ni tu write a la base de datos se ejecutaron.

**3. El 200 mentiroso.** Muchas APIs responden status 200 con `{"error": ...}` en el body. n8n no interpreta semántica: nodo en verde, integración rota.

**Cómo detectarlo:**

- **Stop and Error al final.** Un Code node que evalúe `$input.all().length === 0` y lance error convierte el "no hubo items" en un fallo visible en tu historial de ejecuciones.

- **Valida el efecto, no la ejecución.** Después del nodo crítico (crear registro, enviar mensaje), verifica el resultado real: un SELECT, una llamada de lectura. Nunca confíes en el status del nodo que supuestamente escribió.

- **Audita por items, no por status.** Vía la API de n8n, inspecciona `resultData.runData` y cuenta items procesados por nodo. Un watchdog que compare "ejecuciones verdes con 0 items procesados" es tu mejor alerta temprana.

El status de ejecución te dice que nada explotó. No te dice que algo pasó. Son preguntas distintas — y solo una de las dos debería marcar tus SLAs.