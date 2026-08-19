# Gemini 3.1 Flash Lite — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 4.266s | tokens_per_second: 96.3
- input_tokens: 95 | output_tokens: 411
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y técnicas para detectar y manejar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

### El falso positivo: cuando tu workflow dice "OK" pero el resultado es un espejismo

Todos hemos caído en la trampa: revisas el historial de ejecuciones en n8n, ves una fila de puntos verdes brillantes, y asumes que el trabajo está hecho. Pero, al abrir el dashboard destino, no hay rastro de los datos. El workflow terminó, devolvió un `200 OK`, pero no hizo nada.

¿Por qué ocurre esto? Generalmente, el culpable es una **gestión optimista de los errores** o una lógica de filtrado demasiado estricta.

#### El problema: El "éxito" del nodo vacío
n8n considera que un nodo se ejecutó con éxito simplemente si no lanzó una excepción. Si tienes un nodo *Filter* o un *If* que descarta todos los ítems de entrada, el workflow continúa su flujo hacia el siguiente nodo con un array vacío. Si los nodos posteriores no tienen configurado el "Continue On Empty", simplemente se saltan la ejecución. Como no hubo error, el workflow finaliza exitosamente. Resultado: flujo verde, cero impacto real.

#### La solución: La técnica del "Canario"
Para dejar de confiar ciegamente en el color verde, implementa estas dos estrategias:

1.  **Validación de salida:** Añade un nodo *If* al final de tu flujo que verifique si el array de salida tiene una longitud mayor a cero. Si es 0, dispara un *Error Trigger* o un webhook de alerta a Slack/Discord.
2.  **Manejo de errores explícito:** Configura la opción "Continue On Fail" solo donde sea estrictamente necesario. En el resto, utiliza un nodo *Error Trigger* global para capturar ejecuciones que, aunque "exitosas" técnicamente, no procesaron ningún ítem.

No te fíes del historial: **si no hay datos procesados, no hay éxito.**