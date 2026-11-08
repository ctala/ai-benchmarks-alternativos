# Gemma 4 26B MoE (3.8B activos) — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 9.751s | tokens_per_second: 49.0
- input_tokens: 112 | output_tokens: 478

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Aquí tienes una propuesta de texto con tono directo, técnico y sin rodeos, diseñada para retener a un perfil avanzado.

***

**Título: El falso positivo: Cuando tu workflow dice "Success" pero el mundo sigue igual**

Todos hemos estado ahí. Revisas la ejecución en n8n, ves el check verde de *Success* y asumes que la magia ha ocurrido. Sin embargo, al consultar la base de datos o el CRM, no hay rastro de los datos. El workflow terminó sin errores, pero el impacto es cero.

**¿Por qué sucede esto?**

El problema suele radicar en una desconexión entre la **ejecución técnica** y la **lógica de negocio**. n8n marca una ejecución como exitosa siempre que el nodo no lance una excepción. Si tu nodo HTTP Request recibe un `200 OK` de una API, pero el cuerpo de la respuesta es un `{"status": "error", "message": "invalid_token"}`, n8n lo considerará un éxito rotundo. El flujo no se detiene, pero tu proceso ha muerto en silencio.

Lo mismo ocurre con los nodos de filtrado o los *If nodes*. Si tu lógica de ramificación no está cubierta, los datos simplemente "caen por la rendija" hacia un final de flujo sin realizar ninguna acción, sin haber disparado un error.

**Cómo detectarlo (y evitarlo):**

1.  **Validación de esquema post-request:** No confíes en el código de estado HTTP. Implementa un nodo *Filter* o un *If* inmediatamente después de tus llamadas externas para validar que el payload contiene la estructura y los datos esperados.
2.  **Error Handling con "On Error -> Continue":** Si usas esta opción para evitar que el workflow se detenga, estás creando zonas ciegas. Si decides usarla, es obligatorio derivar ese camino hacia un nodo de notificación o un log de errores.
3.  **Monitorización de salidas vacías:** Si un nodo de transformación devuelve un array vacío, el flujo seguirá. Añade una validación de longitud (`$input.all().length > 0`) antes de los nodos críticos.

No confundas la ausencia de errores con la presencia de resultados.

***