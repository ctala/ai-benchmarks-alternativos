# Gemini 2.5 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 4.308s | tokens_per_second: 111.6
- input_tokens: 93 | output_tokens: 481
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando consejos prácticos para detectar problemas en workflows de n8n.

## Respuesta completa

¡Hola, n8n-ers!

Hoy vamos a hablar de ese momento en que tu workflow te guiña un ojo, te dice "Success", pero en el fondo sabes que algo no cuadra. Sí, hablamos de los workflows que *parecen* funcionar, pero que en realidad están haciéndose los locos.

¿Por qué ocurre esto? La razón más común es una lógica condicional malentendida o una configuración de nodo que no maneja los casos de borde. Por ejemplo, un nodo `IF` que, al no encontrar una coincidencia, simplemente pasa el elemento de entrada al siguiente nodo sin modificarlo, o un nodo HTTP Request que devuelve un 200 OK, pero el cuerpo de la respuesta indica un error a nivel de aplicación (un `{"status": "error", "message": "Item not found"}`). n8n lo ve como un éxito HTTP, pero tu workflow no hizo lo que esperabas.

**¿Cómo lo detectamos?**

1.  **Registro de Nodos (Node Logging):** Es tu mejor amigo. Activa el registro detallado en los nodos críticos. Un `console.log()` en un nodo de código o ver el output de cada nodo te revelará qué datos fluyen (¡o no fluyen!) a través de tu sistema.
2.  **Validación de Salida:** No confíes ciegamente en el "Success". Añade nodos de validación. Después de un nodo que debería crear un registro, ¿por qué no añadir un nodo que lo busque o verifique su existencia? Si tu workflow crea un archivo, verifica que el archivo exista y no esté vacío.
3.  **Manejo de Errores Específico:** En lugar de un catch-all, implementa un manejo de errores más granular. Si esperas un JSON específico, usa un nodo `IF` para verificar la estructura o los valores clave. Si no se cumplen, considera eso un error, incluso si n8n no lo marca como tal.

Recuerda, "Success" en n8n a menudo significa que el nodo ejecutó su código sin lanzar una excepción. No siempre significa que tu lógica de negocio se cumplió. ¡Mantente atento y no dejes que tus workflows te engañen!

¡Hasta la próxima!