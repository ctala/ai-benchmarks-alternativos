# Mistral Nemo — persistencia/proveedor_sin_webhooks

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.54 | quality: 6.67
- latency_total: 10.471s | tokens_per_second: 17.6
- input_tokens: 197 | output_tokens: 184

## Respuesta completa

Puedes crear un flujo automático que revise periódicamente si hay mensajes nuevos. Aquí te muestro cómo hacerlo:

1. Configura una función en tu plataforma como un servicio web: esta función debe revisar si hay mensajes nuevos y disparar el flujo automático en caso afirmativo. La frecuencia de revisión dependerá de cuánto tiempo puedas esperar para procesar un mensaje nuevo.
2. Utiliza un servicio de programación de tareas para ejecutar esta función en intervalos regulares. Por ejemplo, si usas AWS, puedes configurar Amazon CloudWatch Events para invocar la función cada minuto.
3. En la función, utiliza la API de la plataforma para obtener los mensajes nuevos desde la última revisión. Si hay mensajes nuevos, disparar el flujo automático correspondiente.

Este enfoque te permitirá procesar los mensajes nuevos sin tener que preguntar constantemente a la plataforma.