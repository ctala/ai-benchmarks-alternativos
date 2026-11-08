# Mistral Large 3 675B — translation/detect_language_issues

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 5.289s | tokens_per_second: 87.4
- input_tokens: 206 | output_tokens: 462

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
      "tipo": "spanglish",
      "texto": "En especialmente en拉丁美洲",
      "correccion": "Especialmente en Latinoamérica"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "nuevas herramientas para scale their businesses",
      "correccion": "nuevas herramientas para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning permite optimize",
      "correccion": "el aprendizaje automático permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "adoptan AI tempranamente",
      "correccion": "adoptan la IA tempranamente"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "realizar un análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "corrección": "mejor opción o ajuste ideal"
    },
    {
      "tipo": "gramatical",
      "texto": "En especialmente en拉丁美洲",
      "corrección": "Especialmente en Latinoamérica (eliminar 'En' redundante y corregir caracteres)"
    }
  ],
  "score_idioma": 4,
  "veredicto": "necesita_edicion"
}
```