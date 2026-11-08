# MiniMax M2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 5.397s | tokens_per_second: 103.6
- input_tokens: 106 | output_tokens: 559

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El workflow dijo "success" pero no hizo nada.

Te ha pasado: ejecutas, todo verde, y nada cambia. Sin errores. Sin logs. Sin explicación.

**Por qué pasa esto**

n8n marca un workflow como exitoso cuando llega al final sin explotar. No cuando hace lo que esperabas. El flujo puede llegar al nodo final porque:

- Un nodo anterior no devolvió datos (IF sin matches, HTTP sin resultados)
- Un nodo se saltó por condiciones
- Manejaste el error con un nodo Error Workflow que silenció todo
- Los datos vinieron vacíos desde el inicio

El resultado: un execution log limpio y un sistema que parece funcionar pero no actúa.

**Cómo detectarlo**

1. **Verifica el output de cada nodo** en el log de ejecución. Si un nodo muestra "No data returned" o "Items: 0", lo tienes.

2. **Usa el nodo Stop Workflow** en modo "error" cuando no haya datos. Así fuerzas un fallo visible en lugar de un success silencioso.

3. **Añade un nodo Slack/Email al final** que te notifique solo si el workflow realmente procesó algo. No al revés.

4. **Revisa el campo "items"** en cada nodo. Si baja a 0 en algún punto, ahí se cortó la cadena.

El éxito de n8n no es que no falle. Es que sepas cuándo no hizo nada.

Revisa tus executions de esta semana. Apuesto a que hay al menos uno verde que no movió nada.