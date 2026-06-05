# Gemma 4 12B (Spark llama-server Q4_K_M) — translation/detect_language_issues

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.4 | quality: 8.16
- latency_total: 16.758s | tokens_per_second: 25.7
- input_tokens: 209 | output_tokens: 431
- judge_score: 4.8 | justificación: 

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在",
      "correccion": "En particular en"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
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
      "texto": "tienen un competitive advantage",
      "correccion": "tienen una ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "analizar a fondo"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit",
      "correccion": "encontrar la mejor opción"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```