# Nemotron 3.5 Lightning — translation/detect_language_issues

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.37 | quality: 6.67
- latency_total: 1.315s | tokens_per_second: 248.0
- input_tokens: 217 | output_tokens: 326

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
      "texto": "En particularmente en latinoamérica, los emprendedores estan leveraging nuevas herramientas para scale their businesses.",
      "correccion": "En particular, en Latinoamérica, los emprendedores están aprovechando nuevas herramientas para escalar sus negocios."
    },
    {
      "tipo": "gramatical",
      "texto": "El machine learning permite optimize los procesos de manera unprecedented.",
      "correccion": "El aprendizaje automático permite optimizar los procesos de manera unprecedented." (Nota: "unprecedented" es adjetivo en inglés; en español sería "sin precedentes" o "sin precedentes históricos").
    },
    {
      "tipo": "gramatical",
      "texto": "Las companies que adoptan AI tempranamente tienen un competitive advantage significativo.",
      "correccion": "Las empresas que adoptan IA tempranamente tienen una ventaja competitiva significativa."
    },
    {
      "tipo": "cliche",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "realizar un análisis profundo de las opciones disponibles"
    },
    {
      "tipo": "cliche",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la mejor opción o adaptación para tu organización"
    }
  ],
  "score_idioma": 4,
  "veredicto": "necesita_edicion"
}