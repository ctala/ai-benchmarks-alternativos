# Gemma 4 31B — extraer_claims/formatos_de_cifra_mezclados

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 3.027s | tokens_per_second: 40.3
- input_tokens: 208 | output_tokens: 122

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

```json
{
  "claims": [
    {
      "texto": "La operación combinó US$ 4,2 millones de capital nuevo",
      "tipo": "cifra"
    },
    {
      "texto": "La operación combinó € 1,8 M de deuda convertible",
      "tipo": "cifra"
    },
    {
      "texto": "El fondo administra 2 mil millones de dólares en activos",
      "tipo": "cifra"
    }
  ]
}
```