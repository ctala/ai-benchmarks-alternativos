# MiniMax M3 — translation/detect_language_issues

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.98 | quality: 6.67
- latency_total: 3.414s | tokens_per_second: 149.4
- input_tokens: 350 | output_tokens: 510

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
      "correccion": "En特别, especialmente en América Latina" 
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas",
      "correccion": "están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize los procesos",
      "correccion": "El aprendizaje automático permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan IA"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage significativo",
      "correction": "tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones",
      "correccion": "profundizar en las opciones"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la opción más adecuada para tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "En特别是在拉丁美洲",
      "correccion": "Especialmente en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "los emprendedores estan leveraging",
      "correccion": "los emprendedores están aprovechando"
    },
    {
      "tipo": "gramatical",
      "texto": "El machine learning permite optimize",
      "correccion": "El aprendizaje automático permite optimizar"
    },
    {
      "tipo": "gramatical",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan IA"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}