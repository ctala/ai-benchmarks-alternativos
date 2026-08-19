# Kimi K2.5 — translation/detect_language_issues

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 34.44s | tokens_per_second: 51.3
- input_tokens: 230 | output_tokens: 1767

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
      "correccion": "Especialmente en Latinoamérica (o \"En particular en América Latina\")"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando / están utilizando / hacen uso de"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios / para hacer crecer sus empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
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
      "correccion": "adoptan IA (Inteligencia Artificial)"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage",
      "correccion": "una ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "realizar un análisis profundo / profundizar / ahondar"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la mejor opción / la que mejor se ajuste / la mejor adaptación"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```