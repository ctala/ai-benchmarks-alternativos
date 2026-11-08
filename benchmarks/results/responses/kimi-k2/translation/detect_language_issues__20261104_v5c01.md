# Kimi K2 — translation/detect_language_issues

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 6.34 | quality: 6.67
- latency_total: 12.026s | tokens_per_second: 43.4
- input_tokens: 232 | output_tokens: 522

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
      "texto": "特别是在拉丁美洲",
      "correccion": "especialmente en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando / utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios / hacer crecer sus empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize",
      "correccion": "optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "unprecedented",
      "corrección": "sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "companies",
      "correccion": "empresas / compañías"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA (inteligencia artificial) — aceptable con la sigla en español"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis profundo / estudio detallado"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción / mejor ajuste"
    },
    {
      "tipo": "gramatical",
      "texto": "Las companies que adoptan AI tempranamente",
      "correccion": "Las empresas que adoptan la IA tempranamente / de manera temprana"
    },
    {
      "tipo": "gramatical",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes / de forma inédita"
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}
```