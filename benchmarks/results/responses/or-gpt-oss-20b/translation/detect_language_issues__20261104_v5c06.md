# GPT-OSS 20B — translation/detect_language_issues

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.84 | quality: 6.67
- latency_total: 23.756s | tokens_per_second: 136.0
- input_tokens: 249 | output_tokens: 3232

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
      "correccion": "En especial en"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "El machine learning permite optimize los procesos",
      "correccion": "El aprendizaje automático permite optimizar los procesos"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las compañías que adoptan IA"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    },
    {
      "tipo": "spanglish|gramatical",
      "texto": "best fit",
      "correccion": "ajuste ideal"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}
```