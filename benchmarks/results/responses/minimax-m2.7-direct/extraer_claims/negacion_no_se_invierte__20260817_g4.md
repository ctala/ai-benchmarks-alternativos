# MiniMax M2.7 (directo) — extraer_claims/negacion_no_se_invierte

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 7.084s | tokens_per_second: 46.7
- input_tokens: 186 | output_tokens: 331

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

```json
{"claims": [
  {"texto": "Meridian Labs no cerró la ronda Serie A que había anunciado en junio", "tipo": "evento"},
  {"texto": "Las negociaciones con Aurora Ventures se suspendieron", "tipo": "evento"}
]}
```