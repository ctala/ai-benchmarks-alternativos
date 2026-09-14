# DeepSeek V4.1 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 16.379s | tokens_per_second: 79.7
- input_tokens: 126 | output_tokens: 1306

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El verde mentiroso**

Tu workflow terminó en verde. Nadie recibió el email. Nadie se enteró.

Pasa todo el tiempo, y casi siempre por una de estas:

- **0 items de entrada.** Un Filter, un IF o un trigger que no devolvió nada. El nodo no se ejecuta, no hay error, el canvas se pone verde.
- **Continue On Fail.** Un HTTP Request con 401, un nodo que revienta, y el flujo sigue como si nada. El error queda enterrado en esa ejecución y en ningún otro sitio.
- **Respond to Webhook antes del trabajo real.** El cliente recibe 200, tú te quedas tranquilo, y el resto del flujo muere en silencio.
- **Code nodes con try/catch.** Te comiste la excepción tú mismo.
- **Ramas muertas.** Un Switch donde ninguna condición se cumple y el flujo simplemente termina.

**Cómo detectarlo**

1. Deja de mirar el estado. Mira `items` por nodo en el panel de ejecuciones. Un 0 en un nodo que debería procesar algo es la señal.
2. Añade un validador al final: un IF que compruebe que existe el resultado esperado. Si no, `Stop and Error` con mensaje explícito. Que falle ruidosamente.
3. Audita cada Continue On Fail. Si tienes uno, debería tener un motivo escrito al lado.
4. Instrumenta: manda a Slack o a una tabla el conteo de items procesados por ejecución. Alerta cuando sea 0.
5. Verifica el efecto, no la ejecución. ¿Se creó la fila? ¿Llegó el mensaje? Esa es la única métrica que importa.

El status es una opinión. Los items procesados son un hecho.