# Granite 4.2 8B — content_verificable/audiencia_que_ya_sabe

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 9.23 | quality: 10.0
- latency_total: 13.704s | tokens_per_second: 100.2
- input_tokens: 114 | output_tokens: 1373

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

*(~248 palabras)*

¿Alguna vez ves un workflow marcado como **"success"** en la lista de ejecuciones… pero *realmente no hizo nada*? No es un error de n8n, ni un glitch. Es un caso común y sencillo de detectar si sabes dónde mirar. No te explico qué es un webhook ni qué es un cron: tú ya los usas todos los días, así que saltamos directo al punto.

Por qué ocurre: n8n marca como *success* por defecto **si NO hubo error explícito** en ninguna etapa. Pero "hacer nada" no siempre significa "error". Ejemplos reales que ves frecuentemente:  
→ Un nodo `IF` con condición que nunca se cumple (ej.: `data.id` es `null` o vacío), así que el brazo "success" se ejecuta pero no envía datos a ningún otro nodo.  
→ Un nodo que depende de salida de otro (ej.: `Function` que devuelve un array vacío o `undefined`), y el workflow termina antes de que el siguiente nodo tenga oportunidad de ejecutarse.  
→ En workflows con nodos asíncronos (ej.: llamada a API externa), el *success* del workflow se reporta al final de la ejecución n8n, mientras que la respuesta real de la API llega minutos después; el workflow termina "éxito" pero el efecto (ej.: crear recurso) aún no ocurrió en el momento de la ejecución.

**Cómo detectarlo, rápido y sin debug innecesario:**  
1. **Revisa la pestaña "Execution details"** de la ejecución en cuestión (no solo el resumen "success"). Allí verás exactamente qué nodos se ejecutaron y cuáles fueron *skipped* (ej.: "IF – Condition false", o "Function – Output: []"). Si ves nodos clave marcados como "skipped" o con salida vacía, ahí está la causa.  
2. **Añade temporalmente un nodo `Set` al inicio del brazo que debería ejecutarse** (antes del `IF` o `Function`). Ponle un campo único, como `debug_id: "wf-test-{{randomUUID}}"`. Luego, en la salida final o en un `Log` mínimo, incluye ese `debug_id`. Si en *Execution details* el `Set` aparece ejecutado pero el `IF`/`Function` se salta, verás el `debug_id` en el `Set` pero no en los nodos posteriores → confirma que "no hizo nada" por condición/flujo, no por fallo.  
3. **Verifica la salida real del nodo crítico**: no asumas que "devolvió éxito" significa "envió datos". Abre la salida del último nodo ejecutado (ej.: `Function` o `HTTP Request`) en *Execution details*; busca si es `[]`, `{}` vacío o `null`. Si es así, el workflow terminó sin pasar datos al siguiente paso esperado.

No necesitas cambiar configuraciones complejas. Solo abre *Execution details*, busca "skipped" o verifica la salida del último nodo ejecutado. En 2 minutos sabrás si fue una condición que no se cumplió, un flujo que se cerró temprano o si el efecto async aún está pendiente. Evita revisar logs generales; usa siempre la vista de ejecución detallada.  

> *Ejemplo práctico en 30 segundos:* Añade `Set` → `debug_id: "test-123"`, ejecuta. En *Execution details*, si ves `Set` ejecutado pero el `IF` no se ejecutó (mostrando "Condition false"), sabes que la causa es la condición, no un error. Elimina el `Set` después; no afecta tu workflow.

Detectar es solo mirar dónde se ejecutó y dónde se saltó. No hay magia: n8n es claro en la traza. Usa *Execution details*, revisa la salida del último nodo ejecutado y busca "skipped". Ahora sabes exactamente qué verificar. ¿Algún workflow reciente te dio este "success" sin acción? Comparte el nombre del nodo clave en comentarios; te ayudo a revisar la traza en 5 min. (Sin teorías, solo la vista de ejecución.) — *Tu newsletter breve, útil y sin repeticiones.*