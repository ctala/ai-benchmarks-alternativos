# Gemma 4 12B (Spark llama-server, reasoning) — translation/detect_language_issues

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.14 | quality: 8.04
- latency_total: 82.316s | tokens_per_second: 25.6
- input_tokens: 207 | output_tokens: 2109
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "problemas": [
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
      "correccion": "mejor opción"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```