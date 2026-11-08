# Muse Spark 1.3 — content_verificable/audiencia_que_ya_sabe

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 16.481s | tokens_per_second: 118.2
- input_tokens: 117 | output_tokens: 1948

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El check verde miente.

En n8n, `success` solo significa: ningún nodo lanzó una excepción. No significa que transformaste, enviaste o actualizaste algo.

Los no-ops que más veo en producción:

**1. Filtro silencioso.**
Un IF, Filter, Remove Duplicates o Split Out deja 0 items y todo lo de abajo simplemente no se ejecuta. Todo en verde. Es el caso #1, por goleada.

**2. Code que retorna vacío.**
Un `return []`, un `.map` sin `return`, o devolver un objeto en vez de array de objetos. Propaga nada y nadie se queja.

**3. HTTP 200 falso.**
Muchas APIs devuelven 200 con `{ success: false }`, `{ affectedRows: 0 }`, `{ inserted: 0 }` o el error dentro del body. Si solo chequeas que el nodo no falló, lo das por bueno.

**4. Rama muerta.**
Un Switch que nunca matchea, un Merge en modo que espera input que nunca llega, un Loop Over Items que itera sobre vacío, un Respond to Webhook temprano con `respondWhen` mal puesto.

¿Cómo detectarlo? No mires executions, audita resultados.

Añade guardias explícitos: después de cualquier Filter / Code / HTTP crítico, mete un IF con `$input.all().length === 0` -> `throw new Error('NO_OP: filtro dejó 0 items')`. Obliga al workflow a fallar fuerte en vez de terminar en silencio.

Valida contrato, no status: comprueba `$json.data`, `affectedRows`, `upsertedIds`. Si esperabas 1 y llega 0, es error.

Y cierra con nodo auditor: guarda en Postgres/Sheets/Better Stack `execution.id`, items in vs items out y acción real hecha. Alerta si `out === 0` dos veces seguidas.

Separa éxito técnico de éxito de negocio. Deja de confiar en el verde. Confía en el conteo.
