# Kimi K2.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 35.886s | tokens_per_second: 56.6
- input_tokens: 119 | output_tokens: 2031
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

El peor bug es el que no parece bug. Ves la ejecución en verde, el webhook devolvió 200, pero la base de datos sigue igual, el Slack no pitó y el CSV sigue vacío. En n8n, "success" solo significa que no explotó nada. No garantiza que haya pasado algo.

Suele pasar en silencio en tres escenarios. Primero: un nodo Function o Set devuelve un array vacío y el siguiente nodo recibe cero items, pero sigue su curso sin error. Segundo: una condición IF filtró todo y nadie notificó que el flujo quedó en un callejón sin salida. Tercero: respondiste al webhook antes de que la rama asíncrona terminara, así que el cliente recibió "OK" mientras el backend moría tranquilamente en segundo plano.

n8n no falla por inactividad. Si no hay items, muchos nodos simplemente no operan y devuelven verde. Para detectarlo, olvídate del color del canvas. Implementa nodos de validación al final: si un Merge esperaba dos inputs y solo llegó uno, fuerza el error. Si un nodo de base de datos devuelve affectedRows = 0, dispara una alerta. Usa `$execution.customData` para trackear counts y lee siempre el execution log completo, no solo el HTTP response.

Mi regla de oro: añade un nodo dedicado al final que verifique "¿se procesó al menos un item?". Si el array está vacío, `throw new Error()`. Es mejor un falso rojo que un falso verde durmiendo en tu cuenta durante semanas.