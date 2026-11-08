# GLM-5.1 — translation/detect_language_issues

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.52 | quality: 6.67
- latency_total: 7.889s | tokens_per_second: 62.0
- input_tokens: 202 | output_tokens: 489

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
      "texto": "En特别是",
      "correccion": "Especialmente en"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático (o 'machine learning' en cursiva si el público es técnico)"
    },
    {
      "tipo": "gramatical",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
    },
    {
      "tipo": "gramatical",
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
      "texto": "adoptan AI",
      "correccion": "adoptan IA"
    },
    {
      "tipo": "spanglish",
      "texto": "tempranamente",
      "correccion": "de forma temprana"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage",
      "correccion": "una ventaja competitiva"
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
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```