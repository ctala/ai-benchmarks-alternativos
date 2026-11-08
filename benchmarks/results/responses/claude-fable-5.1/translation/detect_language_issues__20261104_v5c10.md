# Claude Fable 5.1 — translation/detect_language_issues

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 5.69 | quality: 6.67
- latency_total: 15.232s | tokens_per_second: 98.9
- input_tokens: 333 | output_tokens: 1506

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
      "correccion": "Especialmente en Latinoamérica"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
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
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático (o 'machine learning' en cursiva si se opta por mantener el anglicismo)"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera inédita / sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan la IA"
    },
    {
      "tipo": "gramatical",
      "texto": "tempranamente",
      "correccion": "de forma temprana / desde el principio"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "analizar a fondo las opciones disponibles"
    },
    {
      "tipo": "cliche",
      "texto": "hacer un deep dive",
      "correccion": "analizar en profundidad (expresión corporativa trillada incluso en inglés)"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la opción que mejor se adapte a tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "la best fit",
      "correccion": "Además del anglicismo, hay discordancia de género/artículo con un sustantivo extranjero; usar 'la mejor opción'"
    },
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "está transformando el ecosistema emprendedor (evitar la fórmula 'X ha revolucionado el mundo de Y')"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```