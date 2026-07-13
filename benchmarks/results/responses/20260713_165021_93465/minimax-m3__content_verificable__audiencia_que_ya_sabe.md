# MiniMax M3 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.24 | quality: 8.14
- latency_total: 45.75s | tokens_per_second: 43.8
- input_tokens: 260 | output_tokens: 2004
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, abordando el problema específico con soluciones prácticas y detalladas.

## Respuesta completa

**Tu workflow dice "success" pero no hizo nada. De nuevo.**

Me ha pasado en producción más veces de las que me gustaría admitir. El check queda verde, n8n marca el run como exitoso, y sin embargo el log está vacío, el email nunca salió o el cliente recibió un 200 sin nada útil.

**Las causas reales que me he encontrado:**

- **HTTP nodes que devuelven 200 con body vacío** (típico de APIs internas mal diseñadas o respuestas condicionadas).
- **Filtros e IFs que descartan todos los items**: el siguiente nodo recibe 0 elementos y "termina" sin error.
- **`try/catch` mal planteado**: capturas el error y devuelves un objeto vacío "para no romper", y el flujo padre lo ve como éxito.
- **`Continue On Fail` activado por descuido** en un nodo crítico (upsert, update, delete).
- **Webhooks que responden 200 antes de procesar el trabajo asíncrono real**, y el cliente ya cerró la conexión.

**Cómo detectarlo sin volverte loco:**

1. **Guard al final del flujo**: un Code node que haga `if (!items.length) throw new Error('No se procesó nada')`. Falla en seco y te llega la alerta.
2. **Notificación final siempre**: un nodo de Slack o email con el `items.length` real, no solo "ejecutado".
3. **Inspecciona el execution history por nodo**, no te quedes en el check verde. Los items que entraron y salieron de cada nodo cuentan la historia real.
4. **Alerta por duración anómala**: si un workflow que tarda ~2s pasa a tardar 200ms, probablemente no hizo nada.

"Success" en n8n significa "no hubo excepción". Nada más. Trátalo como tal.