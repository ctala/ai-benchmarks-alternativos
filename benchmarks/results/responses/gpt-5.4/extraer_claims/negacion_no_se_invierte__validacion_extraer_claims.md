# GPT-5.4 — extraer_claims/negacion_no_se_invierte

- model_id: `gpt-5.4`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 1.781s | tokens_per_second: 48.3
- input_tokens: 187 | output_tokens: 86

## Entrada exacta (lo que recibió el modelo)

**system:**

Extraé de la nota TODOS los datos verificables: cifras, fechas, nombres de empresas con su acción, y afirmaciones factuales que un verificador podría contrastar contra una fuente.

Devolvé SOLO un JSON:
{"claims": [{"texto": "<el dato, en una frase>", "tipo": "cifra|fecha|evento|cita"}]}

Reglas:
- NO extraigas opiniones, adjetivos ni proyecciones sin cifra.
- NO inventes: si no está en el texto, no va.
- Una cifra usada como EJEMPLO o comparación general no es un hecho de la nota.
- Respetá las negaciones: «no cerró» no es «cerró».

**user:**

Meridian Labs no cerró la ronda Serie A que había anunciado en junio. La compañía confirmó que las negociaciones con Aurora Ventures se suspendieron.


## Respuesta completa

{"claims":[{"texto":"Meridian Labs no cerró la ronda Serie A que había anunciado en junio.","tipo":"evento"},{"texto":"La ronda Serie A había sido anunciada en junio.","tipo":"fecha"},{"texto":"La compañía confirmó que las negociaciones con Aurora Ventures se suspendieron.","tipo":"evento"},{"texto":"Aurora Ventures participaba en negociaciones con Meridian Labs.","tipo":"evento"}]}