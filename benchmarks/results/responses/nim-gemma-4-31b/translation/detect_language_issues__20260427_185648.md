# Gemma 4 31B (NIM) — translation/detect_language_issues

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.25 | quality: 7.44
- latency_total: 5.756s | tokens_per_second: 78.0
- input_tokens: 217 | output_tokens: 449
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "特别是在",
      "correccion": "especialmente en"
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
      "correccion": "aprendizaje automático (o mantener como término técnico, pero el resto de la frase falla)"
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
      "texto": "companies",
      "correccion": "empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción / mejor ajuste"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```