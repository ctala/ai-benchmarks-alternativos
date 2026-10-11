# GPT-6 Luna — extraer_claims/formatos_de_cifra_mezclados

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 2.291s | tokens_per_second: 63.7
- input_tokens: 194 | output_tokens: 146

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

La operación combinó US$ 4,2 millones de capital nuevo con € 1,8 M de deuda convertible. El fondo administra 2 mil millones de dólares en activos.


## Respuesta completa

{"claims":[{"texto":"La operación combinó US$ 4,2 millones de capital nuevo con € 1,8 millones de deuda convertible.","tipo":"evento"},{"texto":"El fondo administra 2 mil millones de dólares en activos.","tipo":"cifra"}]}