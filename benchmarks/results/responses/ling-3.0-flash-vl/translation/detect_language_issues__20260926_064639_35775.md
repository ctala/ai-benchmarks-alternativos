# Ling 3.0 Flash VL — translation/detect_language_issues

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 11.163s | tokens_per_second: 145.9
- input_tokens: 246 | output_tokens: 1629

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

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "En especial en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas para scale their businesses",
      "correccion": "están aprovechando nuevas herramientas para escalar sus negocios"
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
      "texto": "Las companies que adoptan AI tempranamente tienen un competitive advantage significativo",
      "correccion": "Las empresas que adoptan la inteligencia artificial de manera temprana tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta la tilde en el pronombre verbal)"
    },
    {
      "tipo": "gramatical",
      "texto": "permite optimize",
      "correccion": "permite optimizar (el verbo después de un verbo modal debe ir en infinitivo en español)"
    },
    {
      "tipo": "cliche",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "analizar a fondo las opciones disponibles"
    },
    {
      "tipo": "cliche",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la opción más adecuada para tu organización"
    }
  ],
  "score_idioma": 2,
  "veredicto": "necesita_edicion"
}
```