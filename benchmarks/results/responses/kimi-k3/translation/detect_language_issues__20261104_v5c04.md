# Kimi K3 — translation/detect_language_issues

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 5.84 | quality: 6.67
- latency_total: 24.362s | tokens_per_second: 21.5
- input_tokens: 248 | output_tokens: 524

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
      "correccion": "El aprendizaje automático"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
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
      "texto": "que adoptan AI tempranamente",
      "correccion": "que adoptan inteligencia artificial tempranamente"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage",
      "correccion": "tienen una ventaja competitiva"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive",
      "correccion": "Es importante analizar a fondo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la mejor opción para tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```