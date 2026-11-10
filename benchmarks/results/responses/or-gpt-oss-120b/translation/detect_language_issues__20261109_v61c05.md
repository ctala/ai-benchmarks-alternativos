# GPT-OSS 120B — translation/detect_language_issues

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 12.039s | tokens_per_second: 151.6
- input_tokens: 262 | output_tokens: 1825

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
      "texto": "En特别是在拉丁美洲",
      "correccion": "En especial, en Latinoamérica"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize",
      "correccion": "optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "unprecedented",
      "correccion": "sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "companies",
      "correccion": "empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA"
    },
    {
      "tipo": "gramatical",
      "texto": "temproramente",
      "correccion": "tempranamente"
    },
    {
      "tipo": "cliche",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "cliche",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    },
    {
      "tipo": "cliche",
      "texto": "best fit",
      "correccion": "mejor opción"
    }
  ],
  "score_idioma": 4,
  "veredicto": "necesita_edicion"
}
```