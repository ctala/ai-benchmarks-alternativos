# Kimi K2.7 Code — extraer_claims/cifra_de_ejemplo_no_es_hecho

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 27.096s | tokens_per_second: 36.2
- input_tokens: 246 | output_tokens: 982

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

 ```json
{
  "claims": [
    {
      "texto": "Nordvia cerró una ronda semilla de US$ 4,2 millones.",
      "tipo": "evento"
    }
  ]
}
```