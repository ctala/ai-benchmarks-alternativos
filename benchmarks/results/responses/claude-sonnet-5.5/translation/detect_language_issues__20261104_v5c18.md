# Claude Sonnet 5.5 — translation/detect_language_issues

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.08 | quality: 6.67
- latency_total: 13.454s | tokens_per_second: 161.8
- input_tokens: 333 | output_tokens: 2177

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
      "correccion": "Especialmente en América Latina,"
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
      "correccion": "El aprendizaje automático (o «machine learning» en cursiva, si se mantiene el término técnico)"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes / de forma inédita"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas / Las compañías"
    },
    {
      "tipo": "spanglish",
      "texto": "adoptan AI",
      "correccion": "adoptan la IA (inteligencia artificial)"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa (además, corrige la concordancia de género: «ventaja» es femenino)"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "analizar en profundidad las opciones disponibles / profundizar en las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la mejor opción / la que mejor se ajuste a"
    },
    {
      "tipo": "spanglish",
      "texto": "startups",
      "correccion": "empresas emergentes (opcional: «startups» está muy extendido, pero conviene alternar)"
    },
    {
      "tipo": "cliche",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups.",
      "correccion": "Frase hueca y genérica. Sustituir por un dato o ejemplo concreto, p. ej.: «La inteligencia artificial está cambiando la forma en que las empresas emergentes automatizan tareas y toman decisiones.»"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive en las opciones disponibles",
      "correccion": "Muletilla de relleno típica de textos generados por IA. Reformular de forma directa: «Conviene comparar las opciones disponibles antes de decidir.»"
    },
    {
      "tipo": "gramatical",
      "texto": "para encontrar la best fit para tu organización",
      "correccion": "Cambio de registro: el texto usa tercera persona («los emprendedores», «las companies») y de pronto tutea («tu»). Unificar el registro, p. ej. «para encontrar la que mejor se ajuste a su organización»."
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```