# Nemotron 3 Super — translation/detect_language_issues

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.067s | tokens_per_second: 393.5
- input_tokens: 217 | output_tokens: 420

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
      "correccion": "En especial en Latinoamérica"
    },
    {
      "tipo": "spanglish",
      "texto": "están leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
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
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción"
    },
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "está transformando el ecosistema de las startups"
    },
    {
      "tipo": "gramatical",
      "texto": "los emprendedores estan",
      "correccion": "los emprendedores están"
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}