# Gemini 3.1 Flash Lite (GA) — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 2.973s | tokens_per_second: 148.7
- input_tokens: 93 | output_tokens: 442

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Aquí tienes el borrador para tu newsletter:

***

### El síndrome del falso positivo: Cuando tu workflow dice "OK" pero miente

Todos hemos caído en la trampa: revisas el historial de ejecución en n8n, ves una hilera de checks verdes, pero el resultado final en tu base de datos o CRM está vacío. El workflow reporta un `success` rotundo, pero la lógica de negocio se quedó a mitad de camino.

¿Por qué ocurre esto? Generalmente, por **nodos que no disparan errores cuando no encuentran datos**.

Un caso clásico: un nodo *HTTP Request* o un *Get* de Airtable que, al recibir un filtro demasiado restrictivo, devuelve un array vacío. Para n8n, la ejecución fue impecable: el nodo se ejecutó, no hubo timeout, no hubo 404, simplemente no hubo *input*. Si el siguiente nodo en la cadena es un *Set* o un *Upsert* que espera datos que no llegaron, simplemente no hace nada. El workflow termina su ciclo felizmente, marcando un éxito que es, en la práctica, un fallo silencioso.

**Cómo detectarlo antes de que sea tarde:**

1.  **Validación explícita:** No asumas que el nodo anterior devolvió algo. Añade un nodo *If* después de las consultas críticas para verificar si `{{ $json }}` está vacío. Si lo está, fuerza un error con un nodo *Error Trigger* o envía una notificación a Slack/Discord.
2.  **El "Stop and Fail":** Si el flujo depende de un dato esencial, usa la opción "Continue On Fail: False" o, mejor aún, un nodo *Switch* que redirija a un flujo de "Alerta de inconsistencia" si el array de entrada está vacío.
3.  **Logging de conteo:** Añade un nodo *Code* al inicio de procesos críticos que registre `items.length`. Si el número es 0, que el workflow se detenga ahí.

No confíes en el verde. Confía en la validación.