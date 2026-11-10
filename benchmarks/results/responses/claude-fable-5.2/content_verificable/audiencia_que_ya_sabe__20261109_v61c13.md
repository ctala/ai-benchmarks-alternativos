# Claude Fable 5.2 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 18.819s | tokens_per_second: 96.9
- input_tokens: 161 | output_tokens: 1823

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# "Success" no significa que haya pasado algo

En n8n, "success" solo quiere decir que ningún nodo lanzó un error. No dice nada sobre si el workflow hizo su trabajo.

Hay tres causas habituales:

- **Cero items.** Si un nodo devuelve cero items, los siguientes no se ejecutan y la ejecución termina en verde. Una query sin resultados o un Filter que lo descarta todo se ven igual que un día normal.
- **Errores tragados.** Con "On Error: Continue" o "Never Error" en HTTP Request, el fallo existe pero nadie lo ve.
- **APIs que mienten.** Un 200 con `{"error": "rate limit"}` en el body, o con un array vacío porque caducó el token, pasa como éxito.

## Cómo detectarlo

1. **Convierte el vacío en error.** Activa "Always Output Data" en el nodo crítico, comprueba con un IF si llegó algo real y, si no, termina en un Stop and Error. Así salta tu Error Workflow.

2. **Valida el body, no el status.** Tras cada HTTP Request importante, pon un IF sobre el campo que realmente necesitas.

3. **Pon un heartbeat al final.** Haz que el último nodo envíe un ping a Healthchecks.io o similar solo cuando se procesó algo. Si el ping no llega en la ventana esperada, recibes el aviso. Esto cubre también el caso en que el trigger ni siquiera se dispara.

4. **Registra el conteo.** Guarda cuántos items procesó cada ejecución. Un cero donde suele haber 200 es una alerta, aunque todo esté en verde.

La regla de fondo: define qué significa "hizo su trabajo" y haz que el workflow falle cuando no se cumpla.