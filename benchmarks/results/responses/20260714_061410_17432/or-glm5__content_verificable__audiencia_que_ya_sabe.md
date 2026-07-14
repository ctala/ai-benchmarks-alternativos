# GLM 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 20.853s | tokens_per_second: 75.7
- input_tokens: 100 | output_tokens: 1578
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Asunto: Cuando "verde" significa que no pasó nada**

Todos hemos estado ahí. Revisas el panel de ejecuciones, ves ese check verde satisfactorio, pero el Slack no llegó, el registro en Airtable no se creó y el cliente te pregunta qué pasó. El workflow dice "Success", pero la realidad dice "No-op".

¿Por qué ocurre esto? Porque para n8n, "éxito" simplemente significa que el flujo llegó al final del camino sin romperse en el intento. No juzga si hizo algo útil; solo constata que el recorrido terminó limpiamente.

Los culpables habituales son las ramas lógicas que terminan en el vacío. Piensa en un nodo `IF` donde la rama "True" ejecuta toda la lógica, pero la rama "False" no tiene conexión. Si los datos caen por "False", el workflow finaliza elegantemente, sin errores, pero sin procesar absolutamente nada. Lo mismo pasa con un `Split In Batches` que recibe un array vacío: itera cero veces y cierra el proceso con un "Success" técnico que es, funcionalmente, un fracaso.

La solución es dejar de diseñar para el "camino feliz" y empezar a diseñar para la detección de inacción.

1.  **Fuerza el error explícito:** No dejes ramas muertas. Usa un nodo `Stop` configurado como *Error* en las salidas no deseadas. Que el workflow explote si entra por donde no debe, así te enterarás de inmediato.
2.  **Valida la salida:** Añade un nodo al final que verifique que `items().length` es mayor que 0. Si es 0, lanza un error manual (`throw new Error('Sin datos procesadas')`) para forzar una notificación de fallo real.

Deja de confiar ciegamente en el color verde. Empieza a auditar tus ramas vacías.