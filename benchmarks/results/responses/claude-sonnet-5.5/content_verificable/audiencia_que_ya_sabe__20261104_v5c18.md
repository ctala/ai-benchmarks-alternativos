# Claude Sonnet 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 10.661s | tokens_per_second: 106.5
- input_tokens: 161 | output_tokens: 1135

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# Success en verde, cero trabajo hecho

El estado `success` de n8n significa solo que **ningún nodo lanzó error**. No dice nada sobre si pasó lo que esperabas. Los culpables habituales:

- **Cero items = rama muerta.** Un Filter, un IF o un Get Rows que devuelve vacío corta la rama en silencio. La ejecución termina en verde sin haber tocado nada.
- **200 con error en el body.** Slack (`ok: false`), GraphQL (`errors[]`) y varias APIs de pago responden 2xx y te dejan el fallo en el payload.
- **Continue On Fail / error output** sin nada conectado detrás: el error se traga y el flujo sigue.
- **Always Output Data** activado "para que no se rompa": lo que hace es esconder el vacío.

## Cómo detectarlo

**1. Guard clauses que fallen de verdad.** Tras cualquier fuente de datos crítica, un Code o un IF hacia **Stop and Error**:

```js
if ($input.all().length === 0) {
  throw new Error('Fuente vacía: 0 items');
}
```

Así el Error Trigger por fin tiene algo que capturar.

**2. Valida el body, no el status.** Un IF sobre `{{ $json.ok }}` o `{{ $json.errors }}` justo después del HTTP Request.

**3. Aserciones al final.** Compara items procesados con items esperados. Si entraron 120 y salieron 0, eso es un fallo.

**4. Heartbeat al final del camino feliz.** Un ping a Healthchecks.io o Uptime Kuma, solo en la rama donde el trabajo ocurrió. Si el ping no llega, alerta. Esto también atrapa los workflows que ni se dispararon.

**5. Registra métricas por ejecución** (items in/out) y alerta cuando el número sea 0 o se desvíe de la media.

Un workflow sin comprobaciones de resultado no está monitorizado: simplemente no se queja.