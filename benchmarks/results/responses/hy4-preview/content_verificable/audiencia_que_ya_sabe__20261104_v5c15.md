# Tencent Hy4 preview — content_verificable/audiencia_que_ya_sabe

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 30.554s | tokens_per_second: 53.8
- input_tokens: 117 | output_tokens: 1645

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Asunto: El peligro del "Success" vacío en n8n (y cómo detectarlo)**

Todos hemos celebrado un "Workflow executed successfully" en el historial de ejecuciones, para luego descubrir que la automatización no procesó ni un solo registro. En n8n, un estado 200 OK no siempre significa que el trabajo en realidad se hizo.

¿Por qué pasa esto? Porque n8n asume que si el flujo llega al final sin lanzar una excepción de código, la ejecución fue un éxito. Si un nodo IF desvía todos los datos por una rama muerta, si un filtro descarta el 100% de los items, o si el webhook recibe un payload vacío, el workflow terminará en "success" sin haber insertado nada en tu base de datos ni haber enviado esa alerta crítica.

Para los que construimos sistemas críticos, esto es inaceptable. Aquí tienes tres tácticas directas para cazar estos falsos positivos:

1. **Nodo "Stop and Error" como centinela:** Colócalo en las ramas donde esperas acción obligatoria. Si no llega ningún item a esa parte del flujo, el nodo detiene la ejecución y fuerza un error a propósito para que te enteres.
2. **Chequeo de `$items().length`:** Antes de insertar datos o consumir APIs de terceros, añade un nodo IF que evalúe el volumen de items entrantes. Si es 0, desvía el flujo hacia una alerta en vez de continuar.
3. **Error Trigger global:** Enlaza un sub-workflow de manejo de errores a tus automatizaciones clave. Configúralo para que atrape cualquier fallo (incluidos los que fuercen con el Stop and Error) y te notifique en Slack o Telegram con el Execution ID.

No dejes que un "success" vacío te arruine el fin de semana. Haz que tus workflows te avisen a gritos cuando *NO* hacen nada.