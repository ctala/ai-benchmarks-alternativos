# Kimi K3 — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 107.763s | tokens_per_second: 37.9
- input_tokens: 204 | output_tokens: 4081

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Tu workflow terminó en verde. No hizo nada.**

El status "success" solo certifica una cosa: que ningún nodo lanzó un error sin capturar. Nada más. Los falsos positivos habituales:

- **Input vacío.** Tu query o HTTP request devuelve cero filas; los nodos siguientes ni se ejecutan. Ejecución verde, cero items.
- **Un IF/Filter que lo descarta todo.** Una expresión resuelve a `undefined` o string vacío, la condición da false y la rama muere en silencio.
- **"Continue on Fail" olvidado** en algún nodo crítico. Falla, traga el error, sigue.
- **Un Error Workflow que captura todo y no avisa a nadie.** El workflow principal "funciona"; el error muere en un log que nadie lee.
- **Upserts y dedupe.** La API devuelve 200 porque no hubo error, no porque hubiera cambios.

La detección pasa por dejar de mirar el status y medir efectos:

1. **Cuenta items.** Escribe executionId + items procesados + timestamp en una sheet/DB desde el último nodo que ejecuta el efecto real. Si esperabas 50 filas y hay 0, ahí está tu problema.
2. **Assertions explícitas.** Si "cero resultados" es anómalo en tu caso, mételo en un IF → Stop and Error (o alerta a Slack). Convierte silencio en ruido.
3. **Dead man's switch.** Ping a healthchecks.io solo *después* de completar el trabajo. Sin ping = alerta. Es la única que cubre el caso "la rama nunca corrió".
4. **Audita desde fuera.** Un meta-workflow que consulte la API de n8n y compare items por nodo en las últimas N ejecuciones detecta degradaciones graduales que el verde esconde.

Regla rápida: si el éxito lo declara el propio workflow, no es éxito. Verifica el sistema de destino, no el color del nodo.

---

Si quieres, te preparo la versión extendida con el meta-workflow de auditoría paso a paso para el siguiente número.