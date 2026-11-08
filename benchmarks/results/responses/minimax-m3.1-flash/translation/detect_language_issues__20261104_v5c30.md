# MiniMax M3.1 Flash — translation/detect_language_issues

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 6.52 | quality: 6.67
- latency_total: 55.01s | tokens_per_second: 66.0
- input_tokens: 376 | output_tokens: 3631

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
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "ha transformado el ecosistema de las startups"
    },
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "Especialmente en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando"
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
      "tipo": "gramatical",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de forma sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "adoptan AI",
      "correccion": "adoptan IA"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "examinar a fondo las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la mejor opción para tu organización"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}