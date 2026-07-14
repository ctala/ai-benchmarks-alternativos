# Nemotron 3 Ultra 550B — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 6.494s | tokens_per_second: 93.2
- input_tokens: 116 | output_tokens: 605
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Asunto: Tu workflow dice "Success". Miente.**

Ejecutas el workflow. Badge verde. 200 OK en el webhook. Cero errores en la pestaña *Executions*. Todo limpio.

Y sin embargo, la base de datos no se actualizó. El email no salió. El webhook de respuesta nunca llegó al cliente.

Bienvenido al **éxito silencioso**: n8n terminó *sin errores de sintaxis ni de red*, pero tu lógica de negocio no se ejecutó. Tres culpables clásicos:

1.  **El `IF` que siempre cae en *false* (y no tienes nodo en *false*).** n8n considera "éxito" terminar la rama ejecutada, aunque esa rama sea vacía. El workflow acaba en 0.3s y tú te enteras tres días después por un ticket de soporte.
2.  **El `Set` / `Edit Fields` que mapea `{{ $json.data.id }}` pero el upstream devolvió `{{ $json.data[0].id }}`**. Expresión resuelta a `undefined`. Nodo ejecutado, dato nulo escrito en BD. Sin error, dato basura.
3.  **HTTP Request con "Continue On Fail" activo + código 4xx/5xx manejado como "dato".** El nodo devuelve el JSON de error del proveedor como *output* exitoso. Tu siguiente nodo procesa basura feliz.

### Cómo cazarlos sin paranoia

*   **Assert Node (o `IF` + `Error Trigger`) al final de la ruta crítica.** Valida *contrato de salida*: `{{ $json.id }}` existe, `{{ $json.email }}` tiene `@`, `{{ $json.affectedRows }} > 0`. Si falla → lanza error real, alerta en Slack/Telegram, reintento automático.
*   **Pin "Execute Workflow" en pruebas unitarias.** Pasa *mocks* de edge cases (array vacío, null, 404 del proveedor). Verifica que el workflow *falla* cuando debe fallar.
*   **Metric: "Execution Time" + "Nodes Executed".** Un workflow que suele tardar 12s y 14 nodos, hoy tarda 0.4s y 3 nodos → alarma. No esperes al log.

**Regla de oro:** En producción, *success* solo significa "el motor no petó". Que tu negocio funcione es tu responsabilidad. Añade aserciones. Ahora.