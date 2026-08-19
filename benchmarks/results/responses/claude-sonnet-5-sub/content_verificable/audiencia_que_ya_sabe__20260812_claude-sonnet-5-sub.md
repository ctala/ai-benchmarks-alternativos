# Claude Sonnet 5 (suscripción) — content_verificable/audiencia_que_ya_sabe

- model_id: `claude-sonnet-5`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 28.011s | tokens_per_second: 43.0
- input_tokens: 2 | output_tokens: 1204

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Cuando "success" miente**

n8n te dice que el workflow corrió bien. Verde, sin errores, ejecución completa. Y sin embargo no pasó nada: el mensaje no llegó a Slack, el registro no se creó en la base, el email nunca salió.

El problema no es que n8n falle. Es que **el último nodo falló en silencio** y el workflow entero heredó su status "exitoso" porque, técnicamente, terminó de ejecutarse sin lanzar una excepción.

Las tres causas que más veo:

1. **Credenciales rotas o expiradas** en un nodo intermedio que devuelve una respuesta vacía en vez de un error 401 explícito. El nodo "corre", solo que no hace nada útil.
2. **Dos workflows con el mismo nombre.** Editaste uno, probaste, funcionó — pero el trigger real seguía apuntando a la versión vieja.
3. **Sub-workflows que fallan puertas adentro.** El workflow padre solo ve que el sub-workflow "terminó", no qué hizo dentro. Si el sub-workflow tiene su propio try/catch mal configurado, el error nunca sube.

**Cómo detectarlo, no después de que un cliente te avise:**

- No confíes en el status del workflow. Verifica el output del **último nodo real** (el que hace el trabajo, no un Set decorativo al final).
- Agrega un nodo de validación explícito: si el payload de salida está vacío o no tiene la forma esperada, que falle de verdad (throw), no que pase de largo.
- Si usas sub-workflows, propaga el error hacia arriba en vez de capturarlo y devolver `{success: true}` por costumbre.

La regla de fondo: un workflow que puede fallar en silencio, tarde o temprano lo hace. Y lo peor es que nadie se entera hasta que alguien pregunta por qué no llegó algo que "el sistema dice que se envió".