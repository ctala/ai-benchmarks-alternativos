# GLM-5.1 — translation/detect_language_issues

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 31.193s | tokens_per_second: 82.5
- input_tokens: 201 | output_tokens: 2575
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, identificando correctamente los problemas de idioma y ofreciendo correcciones adecuadas, lo que la hace muy útil para un emprendedor.

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
      "tipo": "gramatical",
      "texto": "significativo",
      "correccion": "significativa (debe concordar en femenino con 'ventaja')"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "analizar en profundidad"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "la mejor opción"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```