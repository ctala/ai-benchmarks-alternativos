# Claude Haiku 5.5 — translation/detect_language_issues

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.43 | quality: 10.0
- latency_total: 2.784s | tokens_per_second: 257.6
- input_tokens: 332 | output_tokens: 717

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
    {"tipo": "chino", "texto": "En特别是在拉丁美洲", "correccion": "Especialmente en Latinoamérica"},
    {"tipo": "spanglish", "texto": "leveraging", "correccion": "aprovechando"},
    {"tipo": "spanglish", "texto": "scale", "correccion": "escalar"},
    {"tipo": "spanglish", "texto": "their businesses", "correccion": "sus negocios"},
    {"tipo": "spanglish", "texto": "optimize", "correccion": "optimizar"},
    {"tipo": "spanglish", "texto": "unprecedented", "correccion": "sin precedentes"},
    {"tipo": "spanglish", "texto": "companies", "correccion": "empresas"},
    {"tipo": "spanglish", "texto": "competitive advantage", "correccion": "ventaja competitiva"},
    {"tipo": "spanglish", "texto": "deep dive", "correccion": "análisis profundo"},
    {"tipo": "spanglish", "texto": "best fit", "correccion": "la opción más adecuada"},
    {"tipo": "cliche", "texto": "ha revolucionado el mundo de las startups", "correccion": "ha transformado el ecosistema emprendedor (o reformular de forma más concreta)"},
    {"tipo": "gramatical", "texto": "estan", "correccion": "están (falta tilde)"},
    {"tipo": "gramatical", "texto": "Las companies que adoptan AI tempranamente", "correccion": "Las empresas que adoptan la IA tempranamente"},
    {"tipo": "gramatical", "texto": "los procesos de manera unprecedented", "correccion": "los procesos de forma sin precedentes"},
    {"tipo": "gramatical", "texto": "para encontrar la best fit para tu organización", "correccion": "para encontrar la opción más adecuada para tu organización"}
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```