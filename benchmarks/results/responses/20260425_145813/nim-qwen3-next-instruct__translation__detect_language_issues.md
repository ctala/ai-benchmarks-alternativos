# Qwen 3-Next 80B Instruct (NIM) — translation/detect_language_issues

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.21 | quality: 8.18
- latency_total: 6.98s | tokens_per_second: 55.7
- input_tokens: 213 | output_tokens: 389
- judge_score: 4.8 | justificación: 

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
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "permiten optimize",
      "correccion": "permiten optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente",
      "correccion": "Las empresas que adoptan la inteligencia artificial tempranamente"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage significativo",
      "correccion": "tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "realizar un análisis profundo de las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la mejor opción para tu organización"
    }
  ],
  "score_idioma": 3,
  "veredicto": "inaceptable"
}