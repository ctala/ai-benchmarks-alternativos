# Ling 3.0 Flash — translation/detect_language_issues

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 5.973s | tokens_per_second: 104.0
- input_tokens: 247 | output_tokens: 621

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
      "correccion": "En particular en América Latina / Sobre todo en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas para scale their businesses",
      "correccion": "están aprovechando nuevas herramientas para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize los procesos",
      "correccion": "El aprendizaje automático permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "manera unprecedented",
      "correccion": "manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente",
      "correccion": "Las empresas que adoptan IA de manera temprana / temprano"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage significativo",
      "correccion": "ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "realizar un análisis profundo / un estudio detallado de las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la opción más adecuada / el mejor ajuste para tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta tilde en 'están')"
    },
    {
      "tipo": "gramatical",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups",
      "correccion": "La inteligencia artificial ha revolucionado el mundo de las startups. (falta punto al final de la oración)"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}
```