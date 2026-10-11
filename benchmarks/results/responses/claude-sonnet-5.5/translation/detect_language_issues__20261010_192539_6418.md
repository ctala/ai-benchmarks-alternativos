# Claude Sonnet 5.5 — translation/detect_language_issues

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 14.12s | tokens_per_second: 159.1
- input_tokens: 333 | output_tokens: 2247

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
      "correccion": "En especial en América Latina (o: Especialmente en Latinoamérica). El fragmento chino significa 'especialmente en América Latina' y sobra además el 'En' inicial."
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
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático (o 'machine learning' en cursiva si se prefiere el término técnico)"
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
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA (inteligencia artificial)"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa (además se corrige la concordancia de género)"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "analizar a fondo las opciones disponibles / profundizar en las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la opción que mejor se ajuste / la opción más adecuada"
    },
    {
      "tipo": "spanglish",
      "texto": "startups",
      "correccion": "empresas emergentes (o 'startups' en cursiva, anglicismo muy extendido pero evitable)"
    },
    {
      "tipo": "cliche",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups.",
      "correccion": "Frase genérica y muy repetida. Mejor ser específico, por ejemplo: 'La inteligencia artificial está cambiando la forma en que las empresas emergentes automatizan tareas y toman decisiones.'"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit",
      "correccion": "Relleno típico de texto generado por IA. Por ejemplo: 'Conviene comparar las opciones disponibles y elegir la que mejor se adapte a tu organización.'"
    },
    {
      "tipo": "gramatical",
      "texto": "para tu organización",
      "correccion": "Cambio de registro: el texto es impersonal y de pronto usa 'tú'. Unificar, por ejemplo: 'para su organización' o 'para tu organización' en todo el texto."
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```