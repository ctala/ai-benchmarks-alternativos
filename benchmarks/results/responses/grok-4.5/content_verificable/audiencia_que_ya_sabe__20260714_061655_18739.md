# Grok 4.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.5`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 12.413s | tokens_per_second: 67.3
- input_tokens: 301 | output_tokens: 835
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Workflow en “success”… y no ha hecho nada**

Has cerrado la ejecución, verde. Todo “success”. Pero el CRM no se actualizó, el Slack no pitó y el Google Sheet sigue igual. No es un bug de n8n: es el diseño de ejecución.

Un workflow marca success cuando **ningún nodo lanza error no capturado**. No cuando produce side-effects. Escenarios clásicos:

- Trigger (webhook, cron, form…) llega con 0 items o con payload vacío. Los nodos siguientes reciben `[]`, hacen passthrough o se saltan la lógica y terminan limpio.
- IF / Switch / Filter: todas las ramas falsas. Nadie ejecuta la acción real. El grafo termina sin error.
- Loop o Merge que se alimenta de un array vacío. Las iteraciones son cero.
- Error Trigger o Continue On Fail que traga el fallo y deja que el resto del flujo “complete”.
- Nodo HTTP Request / Code / Function que devuelve `[]` o `null` sin throw. Success.

El panel de ejecución te miente si solo miras el semáforo. Mira el **número de items** en cada nodo (especialmente el último y los que hacen I/O). Si ves 0 items en el nodo crítico, no ha pasado nada aunque el status sea verde.

### Cómo detectarlo en producción (sin teatro)
1. **Último nodo de validación**: un Code o IF que falle (o envíe al error workflow) si `items.length === 0` o si falta el campo que debería haber escrito.
2. **Contadores explícitos**: al final, un Set o Code que escriba en un data store / Slack / log el `executionId` + `itemCount` del nodo de acción. Si el contador no sube, alarma.
3. **Revisión sistemática de ejecuciones**: filtra por success y abre las que tienen 0 items en el nodo de side-effect. En n8n Cloud/self-hosted el JSON de ejecución te lo dice en un segundo.
4. **No confíes en “Continue On Fail” sin un path de alerta**. Si lo usas, fuerza un branch que notifique cuando el fallo se tragó.

El success de n8n significa “no exploté”. No significa “hice el trabajo”. Añade la aserción de items y deja de confiar en el color verde.