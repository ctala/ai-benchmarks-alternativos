# Nemotron 3 Super — translation/detect_language_issues

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.92 | quality: 6.67
- latency_total: 5.945s | tokens_per_second: 66.4
- input_tokens: 217 | output_tokens: 395

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
      "texto": "En特别是在拉丁美洲, los emprendedores estan leveraging nuevas herramientas para scale their businesses.",
      "correccion": "En especial en América Latina, los emprendedores están aprovechando nuevas herramientas para escalar sus negocios."
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize los procesos de manera unprecedented.",
      "correccion": "El machine learning permite optimizar los procesos de manera sin precedentes."
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente tienen un competitive advantage significativo.",
      "correccion": "Las empresas que adoptan la IA tempranamente tienen una ventaja competitiva significativa."
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit para tu organización.",
      "correccion": "Es importante analizar a fondo las opciones disponibles para encontrar la mejor opción para tu organización."
    },
    {
      "tipo": "gramatical",
      "texto": "los emprendedores estan leveraging",
      "correccion": "los emprendedores están aprovechando",
      "nota": "Falta acento en 'están' y uso incorrecto de verbo en inglés"
    },
    {
      "tipo": "gramatical",
      "texto": "tienen un competitive advantage",
      "correccion": "tienen una ventaja competitiva",
      "nota": "Error de género: 'ventaja' es femenino, requiere artículo 'una'"
    }
  ],
  "score_idioma": 4,
  "veredicto": "necesita_edicion"
}