# Kimi K2.7 Code — extraer_claims/atribucion_es_parte_del_hecho

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 15.476s | tokens_per_second: 67.5
- input_tokens: 243 | output_tokens: 1045

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

Según su CEO, Marta Iribarne, Nordvia abrirá oficinas en Chile en 2027. La empresa cerró una ronda de US$ 4,2 millones en agosto de 2026.


## Respuesta completa

 ```json
{
  "claims": [
    {"texto": "Marta Iribarne es la CEO de Nordvia.", "tipo": "evento"},
    {"texto": "Nordvia abrirá oficinas en Chile en 2027.", "tipo": "evento"},
    {"texto": "Nordvia cerró una ronda de US$ 4,2 millones.", "tipo": "cifra"},
    {"texto": "La ronda se cerró en agosto de 2026.", "tipo": "fecha"}
  ]
}
```