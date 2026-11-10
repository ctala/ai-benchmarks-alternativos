# Claude Fable 5.2 — translation/detect_language_issues

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.17 | quality: 10.0
- latency_total: 17.752s | tokens_per_second: 110.6
- input_tokens: 333 | output_tokens: 1963

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
      "texto": "En特别是在拉丁美洲,",
      "correccion": "Especialmente en América Latina, (los caracteres chinos significan «especialmente en América Latina»; el «En» inicial queda redundante)"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta la tilde)"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas",
      "correccion": "están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios / hacer crecer sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de una manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático (anglicismo extendido en el sector, pero existe equivalente en español)"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas / Las compañías"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA (sigla en español, coherente con «inteligencia artificial» usada al inicio)"
    },
    {
      "tipo": "gramatical",
      "texto": "adoptan AI tempranamente",
      "correccion": "adoptan la IA de forma temprana (falta el artículo; «tempranamente» es un calco forzado de «early»)"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones",
      "correccion": "analizar a fondo las opciones"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la opción más adecuada / la que mejor se adapte"
    },
    {
      "tipo": "cliche",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups",
      "correccion": "Sustituir la apertura genérica por un dato o afirmación concreta (p. ej., un caso o una cifra de adopción de IA en empresas emergentes)"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive",
      "correccion": "Conviene evaluar con detalle... (evitar la fórmula vacía «es importante» junto con la jerga corporativa)"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```