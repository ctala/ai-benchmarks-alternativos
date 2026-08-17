# Solar Pro 4 — extraer_claims/atribucion_es_parte_del_hecho

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 4.404s | tokens_per_second: 22.5
- input_tokens: 268 | output_tokens: 99

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

{
  "claims": [
    {
      "texto": "Según su CEO, Marta Iribarne, Nordvia abrirá oficinas en Chile en 2027.",
      "tipo": "evento"
    },
    {
      "texto": "La empresa cerró una ronda de US$ 4,2 millones en agosto de 2026.",
      "tipo": "cifra"
    }
  ]
}