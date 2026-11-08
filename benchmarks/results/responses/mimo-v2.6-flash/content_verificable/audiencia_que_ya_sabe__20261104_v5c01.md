# MiMo V2.6 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 38.483s | tokens_per_second: 21.7
- input_tokens: 107 | output_tokens: 836

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El 'success' que no significa nada

Un workflow termina en verde. Cero errores. Y no ha hecho absolutamente nada.

Suena exagerado. Pero probablemente lo viestis esta semana sin saberlo.

**La causa más común: el flujo vacío.** Un nodo upstream devuelve `[]` — un filtro sin coincidencias, un HTTP Request que responde 200 con body vacío, un Code node que lanza un array de cero items. Los nodos aguas abajo ejecutan con cero items, saltan sin error y el workflow termina en success. Todo el sistema funciona "perfectamente"… procesando nada.

**La segunda: el error silenciado.** `continueOnError` activado en un nodo HTTP que devuelve 400. El flujo sigue, pero la acción real — el envío, la inserción — nunca ocurrió. Success en la ejecución, fallo silencioso en el negocio.

**La tercera: la respuesta anticipada.** Webhook en modo *Respond* responde al caller antes de que el resto del flujo acabe. El caller ve `{"status":"success"}` mientras el workflow explota tres nodos después.

---

## Cómo detectarlo sin leer todas las ejecuciones

**1. Assert en el output.** Tras cada nodo crítico, añade un IF que compruebe `items.length > 0` o que el body HTTP contiene el campo esperado. Si no, rama a un nodo que falle deliberadamente o envíe una alerta.

**2. Alerta en el else.** Un IF que nunca entra en la rama "else" porque no la creaste es exactamente el punto ciego. Crea la rama. Haz que avise.

**3. Auditoría de ejecuciones.** Un workflow aparte, con cron, que consulte la API de ejecuciones de n8n y compare: ejecuciones en success con cero items procesados en nodos marcados como críticos. Si sube, ya sabes dónde mirar.

El verde no es evidencia de que algo funcionó. Es evidencia de que nada falló *explícitamente*. Hay una diferencia enorme, y ahí es donde viven tus bugs silenciosos.