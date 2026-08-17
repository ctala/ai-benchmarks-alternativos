# Qwen3-Coder-Next (OpenRouter FP8) — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 9.43 | quality: 10.0
- latency_total: 3.55s | tokens_per_second: 134.1
- input_tokens: 109 | output_tokens: 476
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para detectar 'éxitos falsos' en workflows de n8n.

## Respuesta completa

**Cuando tu workflow dice “success”… pero no hizo nada**  

¿Te ha pasado? Ejecutas un workflow, el estado es *success*, pero al revisar el resultado final (una tarea en Asana, un email enviado, un registro en la DB), *nada* ocurrió. ¿Cómo es posible?

Porque *success* solo significa que el workflow **se ejecutó sin errores críticos**, no que *todos los nodos hicieron su trabajo*. Algunos nodos pueden terminar sin efecto colateral, y n8n no los marca como fallos por diseño:  

- Un *HTTP Request* que devuelve 200 OK pero con un body vacío o vacío de datos relevantes.  
- Un *Filter* que descarta todos los items (¡y pasa un array vacío al siguiente nodo!).  
- Un *Set* que sobrescribe con valores por defecto *null*, y el siguiente nodo ignora el campo (pero no falla).  
- Un *Webhook* que recibe una petición, pero el payload no coincide con la lógica esperada → no dispara nada, pero sí completa el workflow.  

**Cómo detectarlo (sin volverte loco):**  

1. **Loguea explícitamente lo que esperas** en cada nodo clave (ej. `{{ $json }}` o `{{ $input.all() }}`), no solo al final.  
2. Usa *Assert* o *Function* nodes para validar que el output tiene la estructura y datos que necesitas. Si falla, lanza un error explícito.  
3. En nodos de integración (Slack, DB, APIs), revisa el campo `success` *dentro* del payload devuelto — no solo el código HTTP.  
4. Activa el *Debug Mode* en nodos problemáticos: te muestra el input/output real, no solo el estado final.  

El truco: *success* es una condición necesaria, pero no suficiente. Tu workflow debe no solo *ejecutarse*, sino *hacer lo que tú quieres*. ¿Qué truco usas tú para evitar estos “éxitos falsos”?