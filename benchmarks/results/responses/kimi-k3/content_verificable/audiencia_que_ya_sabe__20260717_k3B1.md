# Kimi K3 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 83.586s | tokens_per_second: 38.7
- input_tokens: 204 | output_tokens: 3237
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**El check verde que miente**

En n8n, "success" significa exactamente una cosa: ningún nodo lanzó una excepción. No significa que haya pasado trabajo por tu workflow. En esa brecha viven los peores bugs.

Los culpables habituales:

- **`continueOnFail`**: la API falla, el nodo devuelve el error *como data*, y los nodos siguientes procesan basura o nada. Todo verde.
- **Cero items**: una expresión que devuelve `undefined`, un IF que manda todo a una rama vacía, un Filter mal calibrado. Un nodo que recibe 0 items se ejecuta 0 veces — y eso no es un error, es un pase limpio.
- **Respond to Webhook inmediato**: el caller recibe su 200 antes de que corra la lógica, que luego hace no-op en silencio.

Cómo cazarlo:

1. **Mira items por nodo, no el status.** En la vista de ejecución, un nodo verde con 0 items procesados es la prueba del delito.
2. **Falla a propósito.** Añade asserts: un IF que dispare Stop and Error (o un `throw` en Code) cuando `items.length === 0` y no debería. Convierte el silencio en ruido.
3. **Audita tu config de guardado.** Si desactivaste "Save Data Success Execution" en producción para ahorrar espacio, estás ciego justo donde duele.
4. **Marker externo.** Tu Error Workflow no atrapa no-ops (no hubo error). Escribe un marker de "trabajo real hecho" —fila en DB, métrica— y un cron que verifique que existe. Si el workflow corre cada hora y el marker no aparece, alerta.

El status es una mentira útil. Los items no mienten.