# GLM-5.1 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 37.553s | tokens_per_second: 44.2
- input_tokens: 100 | output_tokens: 1658
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, abordando directamente el problema con soluciones prácticas y detalladas.

## Respuesta completa

¿Te ha pasado? El workflow termina en verde, el log dice "Success", pero el registro no se creó y el Slack nunca llegó. Te presento el éxito silencioso: tu automatización no hizo nada, pero n8n cree que todo fue perfecto.

Esto ocurre por tres motivos principales:

1. **Arrays vacíos:** Si el nodo anterior devuelve 0 items, los nodos posteriores simplemente no se ejecutan. El workflow termina con éxito porque no hubo errores, solo no había nada que procesar.
2. **Ramas IF sin salida:** Tu condición evaluó `false` y ese brazo no tenía nodos. El flujo muere ahí, en silencio y con un check verde.
3. **Continue On Fail:** Un nodo falla, pero como está configurado para continuar, inyecta un item vacío o con error en el siguiente nodo, que a su vez no ejecuta la acción esperada. 

¿Cómo cazar estos fantasmas? Deja de confiar en el estado de la ejecución y empieza a auditar los datos:

- **Añade un nodo de validación al final:** Usa un IF para comprobar que la salida del nodo crítico (el ID de la fila creada, el status 200 del HTTP Request, etc.) realmente existe. Si no, dispara una alerta.
- **Nunca dejes ramas vacías:** En lugar de dejar el brazo `false` del IF en el olvido, conéctalo a un nodo que registre un "No-op" en tu base de datos o mande un aviso.
- **Verifica el conteo de items:** Revisa que los nodos clave procesaron `>0` items.

Un "Success" sin items procesados es un error disfrazado. Vigila tus datos, no solo tus estados.