# GPT-6 Luna Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 15.497s | tokens_per_second: 107.0
- input_tokens: 2863 | output_tokens: 1658

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## «Success» no significa «hecho»

Un workflow puede terminar en verde sin haber producido ningún efecto útil. En n8n, *success* suele significar que la ejecución no terminó en un error no gestionado; no que se haya cumplido el objetivo de negocio.

Casos típicos: un `IF` manda los datos por una rama vacía; un nodo recibe cero items y no procesa nada; una expresión resuelve a `undefined` y el destino acepta el payload; o una API devuelve `200` aunque haya rechazado la operación en su respuesta. También ocurre cuando `Continue On Fail` convierte un fallo en datos que el flujo deja pasar.

La solución no es mirar el color de la ejecución, sino comprobar el resultado esperado.

Añade condiciones explícitas en puntos críticos: ¿llegaron items al nodo de escritura?, ¿se procesaron los N registros previstos?, ¿la respuesta confirma la operación y no solo el transporte? Si una condición de negocio no se cumple, lanza un error deliberado o envía la ejecución a una ruta de alerta. Un nodo `IF` que simplemente termina en una rama vacía no es una validación.

Cuando el impacto importa, verifica el efecto después de escribir: consulta el registro creado, comprueba su ID o confirma el cambio en el sistema destino. Y registra contadores útiles —items recibidos, descartados, escritos y fallidos— para distinguir «no había nada que hacer» de «algo se perdió».

La pregunta para cada workflow crítico no debería ser «¿terminó en success?», sino: **¿qué evidencia observable demuestra que hizo lo que debía?** Si no puedes responderla, tu estado verde es una hipótesis, no una garantía.