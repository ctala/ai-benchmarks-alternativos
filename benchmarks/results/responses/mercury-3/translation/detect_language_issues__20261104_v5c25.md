# Mercury 3 — translation/detect_language_issues

- model_id: `inception/mercury-3`
- success: True  | final: 7.52 | quality: 6.67
- latency_total: 0.777s | tokens_per_second: 535.5
- input_tokens: 231 | output_tokens: 416

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

{
  "problemas": [
    {
      "tipo": "spanglish",
      "texto": "En拉丁美洲",
      "correccion": "En América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas",
      "correccion": "están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
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
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan la IA"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "cliche",
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