# Claude Haiku 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.38 | quality: 6.0
- latency_total: 7.432s | tokens_per_second: 174.4
- input_tokens: 161 | output_tokens: 1296

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# Tu workflow dice "success" y no hizo nada

Una ejecución verde solo significa que n8n no lanzó un error. No significa que el trabajo se hiciera. Estas son las trampas más comunes:

**Cómo ocurre**

- **Un nodo devuelve 0 items.** Los nodos siguientes no se ejecutan y la ejecución termina en éxito.
- **Un IF o Switch envía los items a una rama sin conectar,** o a una rama que no hace nada.
- **Un Filter elimina todos los items** por una condición que nadie revisó con datos reales.
- **"Continue On Fail" traga el error.** El nodo falla, el flujo sigue y el resultado es verde.
- **Una API responde 200 con un cuerpo vacío o con `{"error": ...}`.** El código HTTP engaña.
- **Una expresión resuelve a `undefined`.** El Set escribe campos vacíos y el destino acepta el registro sin quejarse.
- **Un Split In Batches recibe una lista vacía** y termina sin iterar.

**Cómo detectarlo**

- **Verifica cantidades, no solo estados.** Tras cada paso crítico, un IF que compruebe `$input.all().length > 0` y lleve a un Stop and Error si no se cumple.
- **Pon Stop and Error en las ramas vacías** en lugar de dejarlas sin salida.
- **Desactiva Continue On Fail** salvo que lo uses con intención, y conecta un Error Trigger a un workflow de alertas.
- **Valida el contenido de la respuesta,** no solo el status. Busca las claves que esperas.
- **Concilia efectos secundarios:** registros insertados, mensajes enviados y filas escritas frente a lo esperado.
- **Monitoriza el volumen.** Un workflow que procesaba 400 items al día y hoy procesa 0 necesita una alerta, aunque todas sus ejecuciones salgan en verde.

El éxito de n8n es un indicador de ejecución, no de resultado. Trata la ausencia de trabajo como un fallo y tu monitorización empezará a servir de algo.