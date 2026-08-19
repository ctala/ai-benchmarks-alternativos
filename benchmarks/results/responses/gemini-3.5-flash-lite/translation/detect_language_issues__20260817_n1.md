# Gemini 3.5 Flash Lite — translation/detect_language_issues

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 1.368s | tokens_per_second: 272.6
- input_tokens: 193 | output_tokens: 373

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
      "tipo": "spanglish",
      "texto": "En特别是在拉丁美洲",
      "correccion": "Especialmente en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "newvelles herramientas para scale their businesses",
      "correccion": "nuevas herramientas para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize los procesos de manera unprecedented",
      "correccion": "optimizar los procesos de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente",
      "correccion": "Las empresas que adoptan la IA tempranamente"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage significativo",
      "correccion": "ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "profundizar / hacer un análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción / ajuste ideal"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta tilde)"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```