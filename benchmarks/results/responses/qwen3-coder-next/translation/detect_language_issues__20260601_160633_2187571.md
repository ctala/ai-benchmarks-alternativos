# Qwen3-Coder-Next (OpenRouter FP8) — translation/detect_language_issues

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.73 | quality: 8.34
- latency_total: 3.579s | tokens_per_second: 140.8
- input_tokens: 213 | output_tokens: 504
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, identificando correctamente los problemas de idioma y proporcionando correcciones adecuadas, lo que la hace muy útil para un emprendedor.

## Respuesta completa

{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "特别是在拉丁美洲",
      "correccion": "especialmente en América Latina"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando / están utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios / expandir sus empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize",
      "correccion": "El aprendizaje automático permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "un unprecedented",
      "correccion": "una manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "AI",
      "correccion": "la inteligencia artificial" (o "IA", pero debe estar introducida antes; aquí se usa en mayúscula inglesa y sin artículo)
    },
    {
      "tipo": "spanglish",
      "texto": "tempranamente",
      "correccion": "a tiempo" o "de forma temprana" (aunque "tempranamente" es correcto, suena forzado; lo natural es "a tiempo" o "de manera anticipada")
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "deep dive",
      "correccion": "análisis profundo / evaluación detallada"
    },
    {
      "tipo": "spanglish",
      "texto": "best fit",
      "correccion": "mejor opción / mejor ajuste"
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}