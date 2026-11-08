# Claude Fable 5.1 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 19.742s | tokens_per_second: 59.5
- input_tokens: 161 | output_tokens: 1174

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**"Success" no significa nada. Significa que no explotó.**

Un workflow en verde solo te dice que ningún nodo lanzó un error sin capturar. No te dice que el correo salió, que la fila se escribió o que el pago se cobró. Y hay varias formas en que llega a verde sin haber hecho nada:

- **Cero items.** Un Filter o un IF deja pasar 0 items y todo lo que viene después simplemente no se ejecuta. Ni error, ni log, nada. Ocurre mucho cuando cambia el formato de la respuesta upstream y la condición deja de matchear.
- **Continue On Fail activado.** El HTTP Request falla, devuelve el item con `error` dentro del JSON, y el siguiente nodo lo procesa como si fuera un dato válido.
- **APIs que responden 200 con basura.** `{"status":"error","data":[]}` con código 200 es success para n8n. El nodo no lee el body.
- **Code node que devuelve `[]`.** Un `return` mal puesto y adiós.
- **Always Output Data.** Útil para debugging, letal en producción: te garantiza que la rama sigue aunque esté vacía.

**Cómo detectarlo**

1. **Afirma cantidades, no estados.** Si esperas N items, comprueba que llegaron N. Un IF con `{{ $items().length === 0 }}` conectado a un Stop and Error cubre el 80% de los casos.
2. **Valida el body, no el status code.** Mira `data.length`, `ok`, `id` del recurso creado. Lo que sea que demuestre que pasó algo.
3. **Compara entrada contra salida.** Leíste 47 filas, escribiste 47. Si no coincide, falla a propósito.
4. **Haz que el Error Workflow tenga algo que capturar.** Solo se dispara si tú lanzas el error. Un workflow silencioso jamás llegará ahí.

La regla: si no puedes señalar qué nodo fallaría si el resultado estuviera vacío, tu workflow no tiene verificación. Tiene esperanza.