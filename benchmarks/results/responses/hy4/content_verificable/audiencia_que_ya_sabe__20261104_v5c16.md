# Tencent Hy4 — content_verificable/audiencia_que_ya_sabe

- model_id: `tencent/hy4`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 34.327s | tokens_per_second: 93.6
- input_tokens: 117 | output_tokens: 3212

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El verde miente**

Tu dashboard está en verde, el `Respond to Webhook` devolvió 200 y la tabla de destino sigue intacta. No hubo crash, no hubo retry, no saltó el `Error Trigger`. Simplemente... no pasó nada.

El culpable casi siempre es el mismo: `items: []`. Un `HTTP Request` que devuelve array vacío, un `Postgres` con 0 rows, o un `{{ $json.payload?.id }}` que resolvió a `undefined`. Para n8n, propagar cero items no es una excepción: es un final limpio. El branch se apaga, los nodos downstream no entran al `runData` y el execution cierra con `finished: true`. Si además tienes un `Continue On Fail` aguas arriba sin verificar `$json.error`, el silencio es total.

El problema es que tus alertas están escuchando errores. Y aquí no hay stacktrace que parsear.

**Cómo cazarlo (sin agregar ruido):**

1. **Guard clause en el source.** Antes del primer `IF` de negocio, mete un `Stop and Error` condicionado a `{{ $items().length === 0 }}`. Convierte el silencio en un fallo explícito con mensaje propio (`"Upstream devolvió 0 rows"`). Ahora sí lo agarra el `Error Trigger`.

2. **Miente con datos, no con booleanos.** Cambia el `{"ok": true}` por `{{ { processed: $items().length, runId: $runId } }}`. Un `processed: 0` es trivial de alertar desde el caller, Datadog o tu TSDB. El 200 sigue siendo 200, pero deja de ser opaco.

3. **Watchdog de heartbeat.** Para crones, no basta con que el run exista: emite un contador incremental por cada item escrito. Si el disparo ocurrió pero el counter no se movió, tienes un falso positivo. (Alternativa sucia pero efectiva: query directa a `execution_entity` cruzando `finished` contra el tamaño de `data.resultData.runData`).

Regla de oro: en n8n, `success` significa *«no explotó»*, no *«hizo el trabajo»*. Audita volumen, no estado.