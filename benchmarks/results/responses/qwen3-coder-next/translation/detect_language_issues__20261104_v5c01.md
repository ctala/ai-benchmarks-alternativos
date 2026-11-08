# Qwen3-Coder-Next (OpenRouter FP8) — translation/detect_language_issues

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.83 | quality: 6.67
- latency_total: 6.774s | tokens_per_second: 56.1
- input_tokens: 213 | output_tokens: 380

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
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize",
      "correccion": "El aprendizaje automático permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "un unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente",
      "correccion": "Las empresas que adoptan la IA temprano"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "hacer un análisis exhaustivo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la opción más adecuada para su organización"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}