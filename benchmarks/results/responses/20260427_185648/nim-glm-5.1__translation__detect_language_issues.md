# GLM 5.1 (NIM) — translation/detect_language_issues

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.49 | quality: 7.13
- latency_total: 57.039s | tokens_per_second: 7.8
- input_tokens: 201 | output_tokens: 447
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是",
      "correccion": "En"
    },
    {
      "tipo": "chino",
      "texto": "特别是",
      "correccion": "especialmente"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "spanglish",
      "texto": "leverage",
      "correccion": "aprovechar"
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
      "correccion": "la mejor opción"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```