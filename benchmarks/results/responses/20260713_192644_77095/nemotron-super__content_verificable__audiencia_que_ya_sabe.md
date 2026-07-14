# Nemotron 3 Super — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 77.689s | tokens_per_second: 11.7
- input_tokens: 116 | output_tokens: 912
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, proporcionando soluciones prácticas y detalladas para detectar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa



Los workflows de n8n devuelven **success** cuando el grafo termina sin lanzar una excepción, aunque ninguno de sus nodos haya producido el efecto esperado. Esto ocurre con frecuencia cuando:

* Un nodo recibe un arreglo vacío y su salida es un objeto sin datos (por ejemplo, un **HTTP Request** que devuelve `{}` o un **MySQL** que no encuentra filas).  
* Un **Set** o **Function** sobrescribe `$json` con un valor que luego se descarta porque el nodo siguiente no lo consume (p. ej. un **Merge** en modo *Append* que no encuentra coincidencias).  
* Un nodo está configurado para *Continue On Fail* y su error se silencia, dejando que el flujo siga como si todo hubiera ido bien.  
* Un **IF** evalúa una condición que siempre resulta falsa y la rama *true* nunca se ejecuta, pero el workflow sigue por la rama *false* sin hacer nada útil.

### Cómo detectarlo antes de que pase desapercibido

1. **Inspecciona la salida de cada nodo** en la vista de ejecución. Si el `$json` está vacío o contiene solo placeholders, marca el nodo con un **Set** que añada un campo `_ok: true` solo cuando haya datos reales.  
2. **Usa un nodo IF inmediatamente después** de cualquier paso crítico (HTTP Request, Base de datos, etc.) con la expresión `{{ $json.length > 0 }}` o `{{ Object.keys($json).length > 0 }}`. Conecta la salida *false* a un nodo de notificación (Slack, Email, Webhook) o a un **Throw Error** para forzar un fallo visible.  
3. **Aprovecha la opción “Continue On Fail” con cautela**. Si la activas, coloca un **Error Workflow** que capture el nodo fallido y registre su mensaje; de lo contrario, el éxito aparente es engañoso.  
4. **Registra métricas de datos**: un **Function** que haga `return { itemsReceived: $json.length }` y lo envíe a un nodo de monitoring (Prometheus, Grafana, o incluso a una hoja de Google) te permite crear alertas cuando el contador cae a cero.  
5. **Revisa los nodos de tipo “No Operation”** (por ejemplo, un **Set** que solo copia campos sin transformación). Si su única función es pasar datos, verifica que el nodo siguiente realmente los consuma; de lo contrario, elimínalo o reemplázalo por un **IF** que valide la presencia de datos antes de continuar.

Con estas prácticas pasas de confiar en el estado “success” a validar realmente que el workflow haya realizado la acción que esperabas, evitando silencios peligrosos en tus automatizaciones.