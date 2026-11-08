# MiniMax M3 — translation/detect_language_issues

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.9 | quality: 6.67
- latency_total: 4.106s | tokens_per_second: 84.3
- input_tokens: 337 | output_tokens: 346

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
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "En particular, en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "ampliar sus negocios"
    },
    {
      "tipo": "gramatical",
      "texto": "El machine learning permite optimize los procesos de manera unprecedented",
      "correccion": "El aprendizaje automático permite optimizar los procesos de forma sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage significativo",
      "correccion": "ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones",
      "correccion": "profundizar en las opciones"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la opción más adecuada para tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}