# Mistral Large 4.0 — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 43.417s | tokens_per_second: 56.3
- input_tokens: 109 | output_tokens: 2446

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El "success" que no hizo nada**

Abres el historial de ejecuciones y ves el check verde: *success*. Pero si miras el output, no hay nada. Ni un item procesado, ni un email enviado, ni una fila actualizada. El workflow corrió, devolvió 200, y se quedó en nada.

Esto pasa constantemente. Un `IF` que evalúa falso sin rama `else`. Un `Split In Batches` que recibe un array vacío y pasa directo al final. Un HTTP Request que devuelve 200 con body vacío. Un loop que itera cero veces. n8n marca *success* porque ningún nodo lanzó error, no porque el trabajo se haya hecho.

El problema es que el estado global de la ejecución solo te dice "no explotó", no "produjo resultado". Y en producción, un workflow silenciosamente vacío es peor que uno que falla ruidosamente: no genera alertas, pero tampoco genera valor.

¿Cómo detectarlo? Deja de mirar solo el banner verde. Inspecciona el output de los nodos críticos: ¿ese nodo clave devolvió items o un array vacío? Añade validaciones explícitas con un nodo `Code` o `IF` justo después de los puntos donde los datos pueden perderse: si `items.length === 0`, lanza un error o envía una alerta. Usa contadores en tus logs estructurados ("procesados: 0" es una señal de alarma, no un dato más).

En resumen: trata el *success* de n8n como "la máquina no se rompió", no como "el trabajo terminó". La diferencia entre ambos es exactamente lo que separa un workflow robusto de uno que falla en silencio.