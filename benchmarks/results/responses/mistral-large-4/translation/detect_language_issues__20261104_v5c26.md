# Mistral Large 4.0 — translation/detect_language_issues

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 23.675s | tokens_per_second: 165.5
- input_tokens: 203 | output_tokens: 3917

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
      "texto": "特别是在",
      "correccion": "Especialmente (o 'En particular')"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando (o 'utilizando')"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios (o 'hacer crecer sus empresas')"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize",
      "correccion": "optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "unprecedented",
      "correccion": "sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "startups",
      "correccion": "empresas emergentes (aunque la RAE acepta 'startup', en contexto formal español es preferible la traducción)"
    },
    {
      "tipo": "spanglish",
      "texto": "companies",
      "correccion": "empresas (o 'compañías')"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "IA (Inteligencia Artificial)"
    },
    {
      "tipo": "gramatical",
      "texto": "tempranamente",
      "correccion": "temprano (o 'de forma temprana' / 'con antelación')"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis en profundidad (o 'inmersión profunda')"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción (o 'la que mejor se adapta')"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}
```