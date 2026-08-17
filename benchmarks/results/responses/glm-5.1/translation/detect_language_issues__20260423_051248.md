# GLM-5.1 — translation/detect_language_issues

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.91 | quality: 8.32
- latency_total: 41.34s | tokens_per_second: 57.4
- input_tokens: 201 | output_tokens: 2373
- judge_score: 5 | justificación: La respuesta identifica con precisión los problemas de idioma y ofrece correcciones adecuadas, es altamente relevante para la tarea dada, proporciona una profundidad razonable al explicar las razones detrás de cada corrección, está claramente organizada y fácil de entender, y es extremadamente útil para un emprendedor que busca mejorar el texto.

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是",
      "correccion": "En particular en"
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
      "texto": "AI",
      "correccion": "IA"
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
      "correccion": "la opción más adecuada"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```