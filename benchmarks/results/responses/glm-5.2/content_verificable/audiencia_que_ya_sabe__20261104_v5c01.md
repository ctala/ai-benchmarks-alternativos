# GLM 5.2 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 19.137s | tokens_per_second: 72.6
- input_tokens: 107 | output_tokens: 1390

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Verde en todos los nodos, cero impacto en tu sistema. Si llevas tiempo en n8n, te habrá pasado: un workflow ejecuta con estado `success`, el log dice que todo fue genial, pero el registro en tu base de datos no se actualizó o el mensaje no se envió. ¿Por qué?

Porque n8n está orientado a datos. Si un nodo recibe un array vacío (`[]`) como input, simplemente lo salta y da por buena la ejecución. No hay error de sintaxis ni de conexión, simplemente no había nada que procesar. 

Esto suele ocurrir cuando una consulta SQL devuelve 0 filas, o cuando un nodo IF filtra todas las ramas porque el payload del webhook no traía el campo esperado. El flujo "termina" correctamente porque no rompió, pero no hizo su trabajo.

**Cómo detectarlo y blindarlo:**

1. **Validación explícita temprana:** Justo después de tu trigger o query inicial, inserta un nodo IF que verifique la longitud del array. Usa una expresión como `{{ $items().length > 0 }}`. Si es false, manda el payload original a una rama de alerta o lanza un error controlado.
2. **Configuración 'On No Items':** En nodos críticos (como HTTP Request o DB), ve a la pestaña *Settings*. Cambia el comportamiento cuando no hay items. En lugar de continuar silenciosamente, puedes forzar a que el nodo falle o redirija el flujo.
3. **Aserciones en el nodo final:** Antes de cerrar el workflow, añade un IF que compruebe que el output del último proceso crítico realmente tiene datos. Si el campo `id` de tu respuesta HTTP está undefined, corta la ejecución con un error.

No confíes en el check verde. Valida que el dato realmente cruzó el pipeline.