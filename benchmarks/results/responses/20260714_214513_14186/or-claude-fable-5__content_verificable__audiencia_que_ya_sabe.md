# Claude Fable 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 22.086s | tokens_per_second: 42.3
- input_tokens: 159 | output_tokens: 934
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**El "success" más peligroso es el que no hizo nada**

Todos hemos visto ese workflow verde, ejecutado a las 3 AM, que en realidad procesó cero registros. n8n marca éxito porque nada falló técnicamente. Pero "no fallar" y "funcionar" no son lo mismo.

**Los sospechosos habituales:**

1. **Items vacíos que se propagan en silencio.** Un HTTP Request devuelve 200 con un array vacío, el resto de nodos "se ejecutan" sin procesar nada, y la ejecución termina en verde. Cero errores, cero trabajo.

2. **Ramas de IF/Switch donde nadie entra.** Si ningún item cumple la condición y no hay rama de fallback, el flujo muere ahí. Éxito técnico, fracaso funcional.

3. **`Continue on Fail` activado y olvidado.** El error se traga, el output queda vacío o con el objeto de error, y los nodos siguientes trabajan sobre basura sin quejarse.

4. **APIs que devuelven 200 con errores en el body.** Si solo validas el status code, ese `{"status": "error"}` pasa de largo.

**Cómo cazarlo:**

- **Asserts explícitos.** Un nodo Code al final que lance excepción si `items.length === 0` cuando esperabas datos. Barato y brutal de efectivo.
- **Stop and Error como red de seguridad** en ramas que nunca deberían quedarse vacías.
- **Valida el payload, no solo el HTTP status.** Un IF que revise la estructura real de la respuesta.
- **Métricas de negocio, no de ejecución.** Loguea cuántos items procesaste en cada run (a una tabla, a Slack, donde sea). Un contador en cero grita más que cualquier error.

El Error Workflow no te salvará aquí: no hay error que capturar. Tienes que definir tú qué significa "éxito".