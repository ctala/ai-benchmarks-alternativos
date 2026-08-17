# Hermes 4 70B — extraer_claims/cifra_de_ejemplo_no_es_hecho

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.276s | tokens_per_second: 51.7
- input_tokens: 222 | output_tokens: 66

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

Nordvia cerró una ronda semilla de US$ 4,2 millones. Como referencia, una ronda semilla promedio en América Latina ronda los US$ 2 millones, según datos del sector.


## Respuesta completa

{"claims": [{"texto": "Nordvia cerró una ronda semilla de US$ 4,2 millones.", "tipo": "cifra"}, {"texto": "Una ronda semilla promedio en América Latina es de US$ 2 millones.", "tipo": "cifra"}]}