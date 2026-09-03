# Tencent Hy4 preview — extraer_claims/atribucion_es_parte_del_hecho

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 143.005s | tokens_per_second: 73.1
- input_tokens: 237 | output_tokens: 10451

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
      "tipo": "cita"
    },
    {
      "texto": "El año previsto para que Nordvia abra oficinas en Chile es 2027.",
      "tipo": "fecha"
    },
    {
      "texto": "Nordvia cerró una ronda de US$ 4,2 millones.",
      "tipo": "evento"
    },
    {
      "texto": "El monto de la ronda que cerró Nordvia fue de US$ 4,2 millones.",
      "tipo": "cifra"
    },
    {
      "texto": "Nordvia cerró una ronda en agosto de 2026.",
      "tipo": "fecha"
    }
  ]
}