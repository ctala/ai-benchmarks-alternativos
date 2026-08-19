# MiniMax M2.7 (directo) — translation/detect_language_issues

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 9.752s | tokens_per_second: 72.1
- input_tokens: 194 | output_tokens: 703

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
      "correccion": "Especialmente en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "los emprendedores estan leveraging nuevas herramientas",
      "correccion": "los emprendedores están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "to scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning permite optimize los procesos de manera unprecedented",
      "correccion": "el aprendizaje automático permite optimizar los procesos de manera nunca vista"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage significativo",
      "correccion": "tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "Es importante hacer un deep dive",
      "correccion": "Es importante analizar a fondo"
    },
    {
      "tipo": "spanglish",
      "texto": "para encontrar la best fit",
      "correccion": "para encontrar la mejor opción"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```