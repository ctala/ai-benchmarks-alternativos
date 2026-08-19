# DeepSeek V3.2 — extraer_claims/cobertura_ocho_claims

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 8.11 | quality: 8.75
- latency_total: 8.134s | tokens_per_second: 38.0
- input_tokens: 273 | output_tokens: 309

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

Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, liderada por Aurora Ventures. La empresa, fundada en 2024 en Montevideo, emplea a 50 personas y opera en 3 países. Su facturación anual llegó a € 1,8 millones en 2025. Según su CEO, Marta Iribarne, la compañía abrirá oficinas en Chile durante el primer trimestre de 2027.


## Respuesta completa

```json
{
  "claims": [
    {
      "texto": "Nordvia cerró una ronda semilla de US$ 4,2 millones",
      "tipo": "cifra"
    },
    {
      "texto": "La ronda semilla fue el 14 de agosto de 2026",
      "tipo": "fecha"
    },
    {
      "texto": "La ronda fue liderada por Aurora Ventures",
      "tipo": "evento"
    },
    {
      "texto": "Nordvia fue fundada en 2024",
      "tipo": "fecha"
    },
    {
      "texto": "Nordvia fue fundada en Montevideo",
      "tipo": "evento"
    },
    {
      "texto": "Nordvia emplea a 50 personas",
      "tipo": "cifra"
    },
    {
      "texto": "Nordvia opera en 3 países",
      "tipo": "cifra"
    },
    {
      "texto": "Su facturación anual llegó a € 1,8 millones en 2025",
      "tipo": "cifra"
    },
    {
      "texto": "La compañía abrirá oficinas en Chile durante el primer trimestre de 2027",
      "tipo": "evento"
    }
  ]
}
```