# Claude Opus 5 — extraer_claims/negacion_no_se_invierte

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 5.783s | tokens_per_second: 58.8
- input_tokens: 310 | output_tokens: 340

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

{"claims": [{"texto": "Meridian Labs no cerró su ronda de financiamiento Serie A", "tipo": "evento"}, {"texto": "Meridian Labs había anunciado la ronda Serie A en junio", "tipo": "fecha"}, {"texto": "Meridian Labs confirmó que las negociaciones con Aurora Ventures se suspendieron", "tipo": "cita"}, {"texto": "Las negociaciones entre Meridian Labs y Aurora Ventures se suspendieron", "tipo": "evento"}]}