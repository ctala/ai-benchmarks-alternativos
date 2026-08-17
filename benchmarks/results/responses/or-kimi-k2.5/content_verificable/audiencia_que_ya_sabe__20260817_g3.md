# Kimi K2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 18.156s | tokens_per_second: 79.0
- input_tokens: 120 | output_tokens: 1434

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿147 ejecuciones verdes? Revisa antes de celebrar.

El peor bug en n8n no es el que falla: es el que devuelve **success** sin haber tocado un solo registro. El webhook recibió el payload, el IF evaluó false, la búsqueda en Postgres volvió vacía... y el workflow terminó feliz, pintando tu dashboard de verde mientras tu base de datos se pudre.

n8n no sabe si tu lógica tuvo sentido. Solo sabe que no explotó.

Aquí cómo detectar el silencio antes de que cueste caro:

**Trata los "empty runs" como errores.** Después de cualquier nodo que filtre (IF, Switch, Code node con `.filter()`), verifica explícitamente si el output tiene items. Si `length === 0` y no es un caso válido de negocio, dispara un notify o forza un error con un Function node. Mejor una alerta falsa que un día de datos perdidos.

**Abandona el "execution count" como métrica.** Monitoriza *business value*: registros creados, emails enviados, filas actualizadas. Un workflow que procesa 0 items pero responde 200 OK es técnicamente perfecto y operativamente inútil.

**Implementa "dead man's switches".** Si un workflow debe actualizar al menos 10 registros diarios y un día actualiza 0, que falle. Los success silenciosos son más difíciles de debuggear que los errores explícitos.

Confía en los datos, no en el color del badge.