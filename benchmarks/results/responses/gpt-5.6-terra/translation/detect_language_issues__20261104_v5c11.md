# GPT-5.6 Terra — translation/detect_language_issues

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 3.651s | tokens_per_second: 142.4
- input_tokens: 198 | output_tokens: 520

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
      "correccion": "Especialmente en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging nuevas herramientas",
      "correccion": "aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "hacer crecer sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize los procesos",
      "correccion": "optimizar los procesos"
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
      "tipo": "spanglish",
      "texto": "tempranamente",
      "correccion": "de forma temprana"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis exhaustivo"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "opción más adecuada"
    },
    {
      "tipo": "cliche",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups.",
      "correccion": "La inteligencia artificial está transformando la forma en que operan las empresas emergentes."
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}