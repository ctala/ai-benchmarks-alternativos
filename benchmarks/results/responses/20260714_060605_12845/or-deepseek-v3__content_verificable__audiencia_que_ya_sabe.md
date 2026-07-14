# DeepSeek V3 — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 20.338s | tokens_per_second: 24.9
- input_tokens: 91 | output_tokens: 507
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando el problema específico con soluciones prácticas.

## Respuesta completa

**Éxito Fantasma: Cuando tu Workflow Miente**

Tu workflow ejecuta sin errores, devuelve ese satisfactorio estado 'success'... pero nada ha cambiado. La base de datos sigue igual, no hay correo en tu bandeja y el Slack está en silencio. ¿Qué demonios pasó?

No es un bug de n8n. Es, casi siempre, una de estas tres trampas lógicas:

1. **El Nodo Silencioso:** Un nodo crítico (como una consulta de base de datos con un filtro muy estricto) no encuentra datos con los que operar. No hay error, simplemente no hay *output*. El flujo continúa vacío hacia el siguiente paso, que no tiene nada sobre lo que actuar.

2. **La Condición Invisible:** Tu nodo IF o Switch tiene una condición que no se cumple, desviando el flujo por una rama que, en el mejor de los casos, termina en un nodo sin operaciones y, en el peor, simplemente se pierde sin nodos de salida definidos.

3. **El Webhook Efímero:** Recibiste el payload, lo procesaste correctamente y devolviste un 200 OK... pero los datos no se encaminaron a ningún nodo posterior. El éxito fue solo en la recepción, no en la acción.

**Cómo Cazar el Fantasma:**

*   **Habilita el Log de Ejecución:** Es tu primera herramienta. Revisa la pestaña "Execution" de la corrida sospechosa y expande cada nodo. ¿Ves datos de entrada y salida en TODOS los nodos clave? Si un nodo muestra entrada pero salida vacía, ahí está el problema.
*   **Punto de Control con un "Code" o "Function":** Inserta un nodo simple de código (console.log) o una Function node temporal solo para hacer un *log* de los datos recibidos. Te confirmará si la información llega como esperas.
*   **Nunca dejes ramas sueltas:** Asegúrate de que cada ruta de tu lógica (especialmente las de "else" o "default") termina en un nodo explícito, aunque sea uno de "Send Alert" para decirte: "Por aquí pasó, pero no hizo lo principal".

Un 'success' sin acción es una falla silenciosa. Desconfía de él y verifica siempre el flujo real de datos, no solo el estado final.