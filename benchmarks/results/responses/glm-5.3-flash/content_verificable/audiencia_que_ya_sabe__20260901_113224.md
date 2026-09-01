# GLM 5.3 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 88.158s | tokens_per_second: 30.4
- input_tokens: 107 | output_tokens: 2680

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El check verde miente: 'success' no significa 'lo hizo'**

En n8n, "success" significa una sola cosa: ningún nodo lanzó un error. No significa que se creara el registro, se enviara el mail ni se procesara una sola fila. Por eso existen ejecuciones verdes que no hicieron absolutamente nada.

Los sospechosos habituales:

- **Ramas vacías**: el IF evalúa false, o el Filter deja pasar cero items. Los nodos aguas abajo nunca llegan a ejecutarse, pero la ejecución termina en verde porque "cero items" es un estado válido, no un error.
- **Continue On Fail / onError: Continue**: el HTTP Request falla, escupe el error como item y los nodos siguientes lo tragan como si fuera data normal.
- **APIs que devuelven 200 con el error en el body**: n8n mira el status code, no tu contrato de negocio. Un `{"success": false}` pasa limpio. Igual con un 202 Accepted que el proveedor rechaza horas después.
- **try/catch en el Code node** que atrapa, loguea y devuelve `null`. Acabas de desactivar tu único detector.

Cómo detectarlo:

1. **Assert de items + Stop and Error**: cuenta items tras las operaciones críticas y lanza si el resultado está vacío. Convierte estados vacíos en rojo real.
2. **Valida el body, no el status**: un IF con `$json.success !== false` antes de dar el trabajo por hecho.
3. **Verificación post-acción**: tras el "create record", haz un GET de vuelta y aserte que existe.
4. **A nivel macro**: ejecuciones corridas vs. outcome de negocio. Si el cron corrió 30 veces y el CRM tiene cero records nuevos, la discordancia es tu alarma.

Regla: success es señal de transporte, no de negocio. Si no hay asserts, no hay creencia.