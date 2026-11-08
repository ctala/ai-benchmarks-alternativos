# DeepSeek V4 Flash (OpenRouter) — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 15.067s | tokens_per_second: 46.6
- input_tokens: 100 | output_tokens: 702

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Asunto: Cuando “Success” es una mentira**

Sabes que tu workflow terminó con un check verde, pero el destinatario no recibió el correo, la base de datos no se actualizó, o el archivo no se movió. ¿Te ha pasado?

El problema no es n8n: es que el estado `success` solo confirma que el flujo **se ejecutó sin errores lanzados**, no que hiciera lo que esperabas. Las causas más comunes:

- **Filtros silenciosos**: un `IF` o `Filter` devolvió 0 items, y el resto del workflow operó sobre un array vacío. Todo OK para n8n, nada para ti.
- **Nodos que fallan sin error**: un `HTTP Request` con `responseCode: 200` pero cuerpo vacío o con error lógico. Tu nodo siguiente procesa `undefined` y no se queja.
- **Actualizaciones condicionales**: un `Set` o `Function` que modifica datos solo si se cumple una condición que nunca se activó.
- **Timeouts parciales**: un `Wait` o `Execute Workflow` que expira pero no lanza excepción (depende de configuración).

**Cómo detectarlo (sin volverte loco):**

1. **Siempre valida el output clave**. Después del nodo que debería producir el resultado esperado (ej. `Send Email`, `Update Row`), añade un `IF` que compruebe el `response` o el número de items. Si no coincide, lanza un error deliberado (`Throw Error`).
2. **Log estructurado**: usa un nodo `Function` para escribir a un archivo o servicio externo (o simplemente a `console.log` si tienes logs de ejecución) los IDs o resúmenes de lo que se procesó.
3. **Monitoreo externo**: un webhook de salud que recibe un ping solo si el workflow completa una acción real. Si no llega, sabes que algo falló.

No confíes en el check verde. Ponle un cinturón de seguridad a tu workflow.