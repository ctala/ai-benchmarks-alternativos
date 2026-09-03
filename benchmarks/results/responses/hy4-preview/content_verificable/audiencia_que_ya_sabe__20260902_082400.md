# Tencent Hy4 preview — content_verificable/audiencia_que_ya_sabe

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 98.99s | tokens_per_second: 67.7
- input_tokens: 117 | output_tokens: 6698

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Por qué tu workflow devuelve `success` y no hizo nada**

Que un workflow termine en `success` no significa que haya trabajado. En n8n, ese estado solo indica que el flujo llegó al final sin una excepción no controlada. El trabajo real se mide en **items procesados**, no en el color verde.

El caso más común es el temido **cero items**. Un `SELECT` sin filas, un `IF` que manda todo a `false`, un `Filter` que descarta todo, un `HTTP Request` que responde `200` con un array vacío, un `Code` que retorna `[]` o un `Merge` mal configurado hacen que los nodos siguientes no se ejecuten. Resultado: éxito absoluto y cero trabajo. Otro clásico es silenciar fallos con `On Error: Continue` (el viejo `Continue on Fail`) y no revisar la salida de error: el flujo sigue, pero quizás sin datos.

¿Cómo detectarlo?

1. **Mira los contadores, no el estado.** En la vista de ejecución, cada nodo muestra cuántos items emitió. Un `success` con `0 items` en el nodo donde esperabas datos —o en el último ejecutado— es una bandera roja.
2. **Añade asserts.** Tras pasos críticos, usa un `IF` o un `Code` que verifique `{{ $input.all().length === 0 }}` o que el campo clave exista. Si no, lanza un `Stop and Error` o dispara una alerta. Mejor un error visible que un silencio productivo.
3. **Audita los `200`.** Si respondes a un webhook, valida el body antes de devolver `200`; sin datos, responde `4xx` o notifica.
4. **Vigila `On Error: Continue`.** Comprueba explícitamente la rama de error (`{{ $json.error }}`) en lugar de ignorarla.

Un workflow robusto no es el que nunca falla, sino el que nunca miente.