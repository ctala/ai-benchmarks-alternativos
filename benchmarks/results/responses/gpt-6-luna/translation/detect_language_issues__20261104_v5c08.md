# GPT-6 Luna — translation/detect_language_issues

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 3.301s | tokens_per_second: 93.0
- input_tokens: 198 | output_tokens: 307

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
      "texto": "特别是在拉丁美洲",
      "correccion": "especialmente en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging nuevas herramientas para scale their businesses",
      "correccion": "aprovechando nuevas herramientas para hacer crecer sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize los procesos de manera unprecedented",
      "correccion": "El aprendizaje automático permite optimizar los procesos de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente tienen un competitive advantage significativo",
      "correccion": "Las empresas que adoptan la inteligencia artificial desde temprano tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles para encontrar la best fit",
      "correccion": "analizar a fondo las opciones disponibles para encontrar la más adecuada"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}