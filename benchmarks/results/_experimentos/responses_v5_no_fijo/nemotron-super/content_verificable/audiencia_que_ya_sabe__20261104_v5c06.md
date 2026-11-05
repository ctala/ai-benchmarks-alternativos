# Nemotron 3 Super — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 10.512s | tokens_per_second: 94.6
- input_tokens: 116 | output_tokens: 994

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Cuando un workflow de n8n termina con el estado **success** pero, en realidad, no ha modificado nada, el motivo suele ser que ninguno de los nodos lanzó una excepción; n8n solo marca éxito cuando la ejecución no se interrumpe por un error. Por eso, un flujo puede pasar por nodos que reciben datos vacíos, que fallan silenciosamente (por ejemplo, una petición HTTP con código 200 pero cuerpo vacío) o que se saltan por condiciones nunca cumplidas, y aún así devolver *success*.

**Cómo detectarlo sin ralentizar el flujo**

1. **Validación explícita de datos**  
   - Después de cada nodo crítico (HTTP Request, Database, Function, etc.) inserta un **Set** que cree una bandera, p. ej. `{{ $json.length > 0 ? true : false }}`.  
   - Al final del flujo usa un **If** que revise esa bandera; si es falsa, deriva a un nodo de notificación o a un **Error Workflow** trigger.

2. **Continue On Fail + captura de errores**  
   - Activa *Continue On Fail* en los nodos que pueden fallar sin lanzar excepción (HTTP Request con *Response Code* handling).  
   - Conecta su salida **error** a un **Set** que registre el motivo y, opcionalmente, lance un error con un **Function**: `throw new Error('Nodo X no devolvió datos');`. Así el workflow pasa a *failed* y se activa tu flujo de alerta.

3. **Uso de nodos de control**  
   - **Merge** (mode: *Append*) después de un nodo que debería producir datos; si la salida está vacía, el merge no agrega nada y puedes detectarlo con un **Set** que cuente los ítems.  
   - **Execute Workflow** con *Wait Until Finish*: revisa el `executionData` del workflow hijo; si está vacío, marca el padre como fallido.

4. **Logs y métricas**  
   - Añade un **Set** que guarde `{{ $now }}` y el `{{ $json }}` antes y después de cada paso.  
   - En la vista de *Execution Data* busca campos que no cambian entre pasos; esa estabilidad indica que el nodo no hizo nada.

Implementar estas comprobaciones transforma un “success vacío” en una señal temprana de que algo no funcionó, permitiéndote actuar antes de que el dato perdido cause problemas mayores. No necesitas explicar qué es n8n; basta con que cada nodo deje constancia explícita de su efecto real.