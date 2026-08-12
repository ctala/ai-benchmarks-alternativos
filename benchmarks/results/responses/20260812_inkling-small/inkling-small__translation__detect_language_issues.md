# Inkling Small — translation/detect_language_issues

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 31.576s | tokens_per_second: 113.8
- input_tokens: 206 | output_tokens: 3593

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
    {"tipo": "chino", "texto": "En特别是在拉丁美洲", "correccion": "Especialmente en América Latina"},
    {"tipo": "gramatical", "texto": "estan", "correccion": "están"},
    {"tipo": "spanglish", "texto": "leveraging", "correccion": "aprovechando"},
    {"tipo": "spanglish", "texto": "scale their businesses", "correccion": "escalar sus negocios"},
    {"tipo": "spanglish", "texto": "machine learning", "correccion": "aprendizaje automático"},
    {"tipo": "spanglish", "texto": "optimize", "correccion": "optimizar"},
    {"tipo": "spanglish", "texto": "unprecedented", "correccion": "sin precedentes"},
    {"tipo": "spanglish", "texto": "Las companies", "correccion": "Las empresas"},
    {"tipo": "spanglish", "texto": "AI", "correccion": "IA"},
    {"tipo": "spanglish", "texto": "competitive advantage", "correccion": "ventaja competitiva"},
    {"tipo": "gramatical", "texto": "significativo", "correccion": "significativa"},
    {"tipo": "spanglish", "texto": "deep dive", "correccion": "análisis profundo"},
    {"tipo": "spanglish", "texto": "best fit", "correccion": "mejor opción / ajuste más adecuado"}
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}