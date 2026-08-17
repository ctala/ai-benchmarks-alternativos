# Claude Opus 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 21.78s | tokens_per_second: 55.2
- input_tokens: 159 | output_tokens: 1203

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## Un workflow verde no significa que haya pasado algo

El estado `success` en n8n solo dice que ningún nodo lanzó una excepción. No dice que hayas escrito una fila, enviado un email ni tocado una API. Y esa diferencia es la que te explota tres semanas después, cuando alguien pregunta por qué el reporte está vacío desde el día 12.

Los sospechosos habituales:

- **Cero ítems que se propagan en silencio.** Un Filter o un IF que se queda sin ítems no falla: simplemente los nodos siguientes no se ejecutan. Ejecución verde, cero trabajo.
- **`Always Output Data`** activado en un nodo que no devolvió nada: ahora tienes un ítem vacío recorriendo la rama y disimulando el problema.
- **`onError: continueRegularOutput`** puesto "por si acaso" hace meses. La API devuelve 500 y el flujo sigue como si nada.
- **HTTP 200 con error en el body.** Muchas APIs responden 200 y `{"status":"error"}`, o aceptan el batch y rechazan cada registro por separado.
- **Upserts que hacen match con 0 filas**, o queries con un `WHERE` que ya no coincide con nada.
- **Pinned data** que sobrevivió al paso a producción.

Cómo detectarlo:

1. **Asserts de cardinalidad.** Un Code node en los puntos críticos: `if (items.length === 0) throw new Error('0 ítems en <paso>')`. Si esperabas datos, cero es un fallo, no un caso normal.
2. **Log de ejecución propio**: workflow, timestamp, ítems entrantes, filas escritas. Alerta cuando `rows_written = 0` dos ciclos seguidos.
3. **Valida el body**, no el status code.
4. **Vigila duraciones anómalas.** Una ejecución que baja de 40s a 300ms no ha mejorado: se ha vaciado.

La regla: distingue explícitamente entre *"funcionó"* y *"no había nada que hacer"*. n8n no lo hará por ti.