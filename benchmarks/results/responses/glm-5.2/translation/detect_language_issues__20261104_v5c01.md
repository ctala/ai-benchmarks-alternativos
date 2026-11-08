# GLM 5.2 — translation/detect_language_issues

- model_id: `z-ai/glm-5.2`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 3.999s | tokens_per_second: 107.8
- input_tokens: 202 | output_tokens: 431

## Entrada exacta (lo que recibió el modelo)

**system:**

Revisa el siguiente texto en espanol y reporta TODOS los problemas de idioma que encuentres. Responde en JSON.

**user:**

Revisa este texto generado por una IA para un blog en espanol:

"La inteligencia artificial ha revolucionado el mundo de las startups. En特别是在拉丁美洲, los emprendedores estan leveraging nuevas herramientas para scale their businesses. El machine learning permite optimize los procesos de manera unprecedented.

Las companies que adoptan AI tempranamente tienen un competitive advantage significativo. Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit para tu organización."

Devuelve un JSON con:
{"problemas": [{"tipo": "chino|spanglish|cliche|gramatical", "texto": "...", "correccion": "..."}], "score_idioma": 0-10, "veredicto": "publicable|necesita_edicion|inaceptable"}


## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在",
      "correccion": "En particular en"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize",
      "correccion": "El aprendizaje automático permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "que adoptan AI tempranamente",
      "correccion": "que adoptan la IA de forma temprana"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage significativo",
      "correccion": "tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "hacer un análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la mejor opción"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```