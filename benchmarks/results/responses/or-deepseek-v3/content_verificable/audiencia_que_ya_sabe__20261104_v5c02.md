# DeepSeek V3 — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 14.766s | tokens_per_second: 30.9
- input_tokens: 100 | output_tokens: 456

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Tu workflow dice 'success'... pero mintió.**

Lo has visto: la ejecución aparece en verde, todo parece correcto, pero el cliente nunca recibió el email, la base de datos no se actualizó o el mensaje no se envió a Slack. La lógica interna funcionó, no hubo errores técnicos, pero el resultado real es nulo. Es frustrante y peligroso.

Esto suele pasar por tres caminos:

1.  **Condiciones demasiado estrictas (o erróneas).** Un nodo 'IF' filtra todos los ítems y no pasa nada a los siguientes nodos. El flujo se ejecuta "correctamente" sobre... nada.
2.  **Conexiones fantasmas.** Eliminaste un nodo, pero su conexión lógica (esa línea gris) sigue apuntando a la nada. n8n procesa un camino que no conduce a ninguna acción.
3.  **Errores silenciosos en nodos clave.** Algunos nodos, por configuración, no fallan aunque no puedan cumplir su misión (ej., un 'HTTP Request' con manejo de errores muy permisivo).

**La solución: Deja de confiar en el color verde.**

Activa **"Execution Progress"** en tu workflow. Esta opción te mostrará, nodo a nodo, qué datos pasan y cuáles no. Verás el momento exacto en el que tu flujo de trabajo comienza a operar sobre un array vacío.

Implementa **nodos de verificación final.** Antes de terminar, añade un nodo simple (como un 'Function' o 'Set') que compruebe si existe un resultado tangible (ej., un ID de registro, un código de estado). Si no lo hay, que falle **intencionadamente** y te alerte.

No es un bug del software; es un fallo en la lógica de supervisión. Construye workflows que no solo funcionen, sino que también demuestren que han **hecho** lo que esperabas.