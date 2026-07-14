# Gemma 4 26B MoE (3.8B activos) — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 10.339s | tokens_per_second: 48.9
- input_tokens: 112 | output_tokens: 506
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, abordando directamente el problema de los falsos positivos en workflows de n8n con soluciones prácticas.

## Respuesta completa

Aquí tienes una propuesta directa, técnica y sin relleno, diseñada para retener a usuarios avanzados.

***

**Título: El falso positivo: Cuando un "Success" es una mentira**

Has ejecutado el workflow, la ejecución aparece en verde y el nodo final marca `success`. Sin embargo, la base de datos sigue vacía o el CRM no se ha actualizado. No hubo error de sintaxis, no hubo timeout, no hubo fallo de conexión. Simplemente, el workflow "hizo nada".

Este es el problema de los **falsos positivos lógicos**. En n8n, un nodo devuelve éxito si la instrucción técnica se completó, no si la intención de negocio se cumplió.

**¿Por qué ocurre esto?**

1.  **Filtros silenciosos (If/Switch):** El error más común. Tu lógica de ramificación desvía el flujo por una ruta que no tiene nodos de acción. El workflow termina correctamente porque llegó al final de una rama, pero esa rama estaba vacía.
2.  **Data payloads vacíos:** Un nodo HTTP Request devuelve un `200 OK`, pero el cuerpo de la respuesta es un array vacío `[]`. Si tu siguiente nodo depende de iterar sobre esos datos, simplemente no hará nada, pero el proceso se considerará exitoso.
3.  **Manejo de errores mal configurado:** Tienes activado el *Continue on Fail* en un nodo crítico. El error ocurre, n8n lo ignora y pasa al siguiente paso, dando la ilusión de un flujo continuo.

**Cómo detectarlo (y dormir tranquilo):**

*   **Nodos de validación post-acción:** No confíes en el nodo que envía la data. Añade un nodo de consulta inmediatamente después para verificar si el cambio realmente ocurrió.
*   **Error Triggers con lógica de negocio:** No uses solo el *Error Workflow* para fallos de sistema. Crea una rama de "Validación de Integridad" que dispare una alerta si el conteo de registros procesados es cero tras una operación que debería haber devuelto datos.
*   **Check de longitud:** Antes de un nodo *Split In Batches*, usa un nodo *Code* para validar que `items.length > 0`. Si es cero, lanza un error manual con `throw new Error()`.

No busques errores de ejecución; busca errores de lógica.