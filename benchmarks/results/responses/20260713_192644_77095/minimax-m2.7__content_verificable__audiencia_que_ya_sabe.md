# MiniMax M2.7 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 15.576s | tokens_per_second: 39.7
- input_tokens: 104 | output_tokens: 618
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

# Tu workflow dice "success". No te confíes.

Aquí va una situación que todos hemos vivido: el workflow termina en verde, el log dice "success", pero lo que se suponía que debía pasar... no pasó.

**El problema no es n8n. Es cómo diseñamos para detectar el fracaso.**

Un nodo que no se ejecuta por una condición IF devuelve success. Un HTTP Request que recibe un 404 pero tiene "Ignore Response Errors" activado devuelve success. Un Code Node que lanza un error pero está dentro de un Try-Catch que solo hace log... adivina qué devuelve.

El workflow no miente: técnicamente sí completó. El problema es que "completar" no es lo mismo que "funcionar".

**Cómo detectarlo de verdad:**

1. **Verifica el output real**, no solo el estado. ¿El nodo que te interesa realmente se ejecutó? Revisa los tokens de ejecución en el historial.

2. **Configura un nodo Error Trigger** separado. No en el mismo workflow, sino uno global que capture fallos de todos. Sí, todos.

3. **Checkpoints de datos.** Después de cada paso crítico, guarda en una hoja de cálculo o documento qué se procesó, con qué resultado. Si mañana ves un registro sin su "completado", ahí murió la automatización.

4. **Usa expresiones que comparen** el resultado esperado contra el real. Por ejemplo, verifica que `{{ $json.body.id }}` existe antes de continuar. No asumas que el API respondió como esperabas.

5. **Alerts sobre silencio.** Si un cron que debería ejecutarse cada hora no registra nada nuevo en 3 horas, que te llegue un mensaje. El silencio también es un error.

El verde no significa verde. Significa "llegué al final". Que el final sea lo que querías... eso ya depende de ti.