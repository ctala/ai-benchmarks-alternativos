# Qwen 3.8 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 16.555s | tokens_per_second: 117.9
- input_tokens: 148 | output_tokens: 1952

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Success no es negocio**

En n8n, un workflow devuelve *success* cuando la ejecución termina sin errores técnicos. No cuando el resultado esperado existe. Un flujo puede pasar “bien” y no hacer nada por varias razones: entra un webhook con payload vacío y el primer nodo lo ignora; un Filter deja cero items y el resto se ejecuta sobre un array vacío; un If envía a una rama que no hace nada; un Switch no coincide y termina; un Merge recibe solo una rama; un HTTP Request devuelve 204 o una respuesta que nadie valida; o un error queda oculto dentro de una rama opcional.

Para detectarlo, no mires solo el check verde. Añade checkpoints de negocio: un Set o Function que cuente items recibidos, procesados y enviados; un IF que falle si expected_output != real_output; un Stop and Error cuando el payload sea vacío, la clave no exista, la consulta no devuelva filas o el webhook no reciba el evento correcto. Activa Error Workflow y registra contexto: execution id, trigger, nodo, cantidad de items, ids afectados.

Incluye también métricas mínimas: ejecuciones con 0 outputs, ramas no alcanzadas, tiempos anómalos y payloads repetidos. Si un trigger se dispara pero el output esperado no aumenta, el problema suele estar entre el nodo inicial y el primero que transforma datos.

La regla es simple: *success* técnico es necesario, pero no suficiente. Si tu workflow puede terminar “bien” sin tocar la base de datos, sin crear el ticket o sin enviar el mensaje, no es exitoso: es un falso positivo.