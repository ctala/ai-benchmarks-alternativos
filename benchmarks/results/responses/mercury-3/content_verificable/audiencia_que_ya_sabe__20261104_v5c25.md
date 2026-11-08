# Mercury 3 — content_verificable/audiencia_que_ya_sabe

- model_id: `inception/mercury-3`
- success: True  | final: 6.52 | quality: 6.0
- latency_total: 4.666s | tokens_per_second: 429.1
- input_tokens: 114 | output_tokens: 2002

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Tu workflow terminó en verde. Y, sin embargo, el pedido no se registró, el email no salió, el lead no llegó al CRM. El estado `success` en n8n es una mentira piadosa: significa que ningún nodo lanzó una excepción, no que la lógica cumplió su objetivo.

Esto pasa más de lo que crees. Un `IF` manda todos los datos a una rama vacía. Un `Filter` elimina los items y los nodos siguientes procesan cero. Un `Merge` con la clave equivocada devuelve 0 filas. Un nodo con *Continue on Fail* activado traga el error y sigue. O una API externa responde 200 con un error dentro del body.

¿Cómo detectarlo? No mires solo el estado global. Abre la ejecución y revisa el contador de items en cada nodo. Si un nodo crítico muestra 0 de input, ya sabes dónde se perdió el trabajo. También puedes hacer clic en el último nodo y ver si existe output real.

Mejor aún: haz que el workflow se queje. Después de cada paso crítico, añade un nodo `IF` que compruebe `items.length > 0`; si no, lanza un `Stop and Error`. Conecta ese error a un *Error Workflow* que te envíe una alerta. Así, un success falso se convierte en un fallo ruidoso.

En resumen: valida resultados, no estados. El verde es solo el principio.