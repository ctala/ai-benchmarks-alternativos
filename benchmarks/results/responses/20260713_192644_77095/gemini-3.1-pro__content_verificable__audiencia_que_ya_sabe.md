# Gemini 3.1 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.25 | quality: 10.0
- latency_total: 21.821s | tokens_per_second: 90.7
- input_tokens: 93 | output_tokens: 1980
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando el problema específico con soluciones prácticas.

## Respuesta completa

**El peligro del "Success" fantasma en n8n**

Ves el check verde de *Success* en tu historial de ejecuciones. Todo parece perfecto. Sin embargo, el cliente no recibió el correo o la base de datos no se actualizó. ¿Por qué n8n marca como exitoso un workflow que en realidad no hizo nada?

Los "falsos positivos" son uno de los mayores dolores de cabeza al escalar automatizaciones. Generalmente ocurren por tres motivos:

1. **La trampa de los 0 *Items*:** Es la causa número uno. Si un nodo devuelve un array vacío, n8n simplemente detiene la ejecución de esa rama. Como no hubo ningún error técnico (el nodo hizo su trabajo), el workflow termina y se marca como *Success*.
2. **APIs "mentirosas":** El endpoint remoto devuelve un HTTP 200 OK, por lo que el nodo *HTTP Request* lo da por bueno. Pero el payload JSON real contiene un `{"status": "error", "message": "Invalid payload"}`.
3. **Abuso del *Continue On Fail*:** Lo activaste en los *settings* del nodo para ignorar un timeout puntual, pero olvidaste manejar la salida de error, silenciando fallos críticos posteriores.

**Cómo blindar tus workflows para detectarlo:**

*   **Domina el *Always Output Data*:** Activa esta opción en los ajustes del nodo si necesitas forzar que la ejecución continúe (devolviendo un item vacío) para poder evaluarlo inmediatamente en un nodo *If* o *Switch*.
*   **Implementa el nodo *Stop and Error*:** No dejes que los flujos mueran en silencio. Si un paso crítico no devuelve los datos esperados, enrrútalo hacia un *Stop and Error*. Esto forzará un estado *Failed*, disparando tu *Error Trigger* global.
*   **Valida el payload:** Añade un nodo *If* tras llamadas a APIs inestables para validar que las propiedades clave existen realmente en la respuesta. 

No confíes ciegamente en el check verde; diseña tus flujos asumiendo que los datos te van a traicionar.