# Solar Pro 4 — content_verificable/audiencia_que_ya_sabe

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 10.037s | tokens_per_second: 48.4
- input_tokens: 149 | output_tokens: 486

## Respuesta completa



El `true` enganoso: cuando tu workflow dice "todo bien" y no hizo nada

Es el bug que más tiempo de depuración consume en n8n. Tu ejecución finaliza con estado `Success` (verde), los logs no lanzan errores, pero la acción real nunca se ejecutó. ¿Por qué?

Generalmente, la máquina de flujos está diseñada para ser resistente. Si tienes un `IF` que filtra el 100% de las iteraciones, o un nodo de búsqueda que devuelve un array vacío sin un manejo explícito, el workflow no "falla". Simplemente se queda sin nodos por procesar y finaliza limpiamente. Para la plataforma, es un éxito. Para tu lógica, es un silencio peligroso.

El riesgo es acumulación de deuda técnica invisible. Pierdes datos, triggers se ignoran y no te das cuenta hasta que un cliente pregunta por un reporte que nunca se generó.

¿Cómo detectarlo sin mirar logs cada hora?

1.  **Mide el throughput, no solo el estado:** En lugar de monitorear solo si el workflow terminó, monitorea cuántas operaciones *reales* se completaron. Si esperas 500 registros y el payload final dice 0, eso es una anomalía, aunque el estado sea `Success`.
2.  **Validación al final del pipeline:** Añade un último paso de validación que compare el resultado esperado vs. el obtenido. Si la diferencia supera un umbral, dispara una alerta (a Slack, email o un ticket) incluso si el workflow no lanzó excepciones.
3.  **Manejo explícito de vacíos:** No confíes en que un array vacío sea "normal". Usa condiciones para detectar cuando un origen de datos devuelve nada y trata eso como un caso que requiere atención, no como un camino feliz.

En n8n, un workflow verde no garantiza que tu negocio funcionó. Asegúrate de que el "éxito" incluya la verificación de que se hizo el trabajo.