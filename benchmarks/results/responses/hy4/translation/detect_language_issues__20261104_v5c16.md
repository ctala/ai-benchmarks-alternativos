# Tencent Hy4 — translation/detect_language_issues

- model_id: `tencent/hy4`
- success: True  | final: 6.77 | quality: 6.67
- latency_total: 6.789s | tokens_per_second: 103.3
- input_tokens: 232 | output_tokens: 701

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
      "correccion": "En particular en Latinoamérica"
    },
    {
      "tipo": "gramatical",
      "texto": "emprendedores estan leveraging",
      "correccion": "emprendedores están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando / utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize",
      "correccion": "optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "unprecedented",
      "correccion": "sin precedentes"
    },
    {
      "tipo": "gramatical",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes / como nunca antes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis en profundidad"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "la mejor opción / el mejor ajuste"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "ha transformado el ecosistema de las startups"
    },
    {
      "tipo": "cliche",
      "texto": "tienen un competitive advantage significativo",
      "correccion": "obtienen una ventaja competitiva medible"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive en las opciones disponibles",
      "correccion": "Conviene evaluar con detalle las opciones disponibles"
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}