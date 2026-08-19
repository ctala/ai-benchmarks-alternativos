# KAT Coder Pro v2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 9.24s | tokens_per_second: 82.0
- input_tokens: 110 | output_tokens: 758

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



¿Tu workflow dice "success" pero no hizo nada? Es un clásico. Ocurre cuando un nodo intermedio —un IF, un Switch, un Merge con condición— no pasa datos al siguiente, pero la ejecución termina sin errores. Para n8n, eso es éxito: no hubo excepciones. El problema es que tú esperabas una acción concreta (un email, una fila en Airtable, un mensaje en Slack) y nunca llegó.

Los escenarios más comunes:

1. **Condiciones que silencian el flujo**: Un nodo IF con rama "false" que termina en un nodo vacío. La ejecución marca verde, pero no hay salida.
2. **Filtros en nodos de código**: Un nodo Function que retorna `[]` o `undefined` sin lanzar error. El siguiente nodo no recibe ítems y simplemente no hace nada.
3. **Webhooks que no disparan**: Un webhook configurado correctamente recibe una petición, pero el payload no coincide con lo esperado y el workflow termina en el primer nodo de validación.

¿Cómo detectarlo? No confíes en el estado "success" del panel de ejecuciones. Implementa validaciones explícitas:

- **Añade un nodo final de "Check"**: Un nodo de código que cuente los ítems procesados y lance un error si es cero. Así, el workflow fallará y podrás alertar.
- **Usa el nodo "Error Trigger"**: Configúralo para que te notifique cuando un workflow termine con error, pero también cuando no haya procesado ítems.
- **Logs de salida**: En nodos críticos, escribe en un log externo (un canal de Slack, una tabla de auditoría) cada vez que se ejecute la acción esperada. Si no hay registro, algo pasó.

La regla de oro: **nunca asumas que "success" significa "trabajo completado"**. Valida siempre el resultado, no solo el estado de la ejecución.