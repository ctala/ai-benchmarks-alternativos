# Ling 3.0 Flash — translation/detect_language_issues

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.371s | tokens_per_second: 393.7
- input_tokens: 246 | output_tokens: 1327
- judge_score: 5 | justificación: La respuesta identifica con precisión los problemas de idioma, proporciona correcciones adecuadas y es altamente relevante y clara, ofreciendo utilidad práctica para los emprendedores.

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
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático"
    },
    {
      "tipo": "gramatical",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "unprecedented",
      "correccion": "sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "companies",
      "correccion": "empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "inteligencia artificial"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "profundización"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "la más adecuada"
    }
  ],
  "score_idioma": 2,
  "veredicto": "necesita_edicion"
}
```