# GPT-OSS 120B — translation/detect_language_issues

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 6.54 | quality: 6.67
- latency_total: 27.533s | tokens_per_second: 26.2
- input_tokens: 259 | output_tokens: 721
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, identificando correctamente los problemas de idioma y ofreciendo correcciones adecuadas, con utilidad práctica para emprendedores.

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
      "tipo": "spanglish",
      "texto": "están leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "scale their businesses",
      "correccion": "escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize",
      "correccion": "El aprendizaje automático permite optimizar"
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
      "correccion": "mejor opción"
    },
    {
      "tipo": "gramatical",
      "texto": "los emprendedores estan leveraging",
      "correccion": "los emprendedores están aprovechando"
    },
    {
      "tipo": "gramatical",
      "texto": "El machine learning permite optimize los procesos",
      "correccion": "El aprendizaje automático permite optimizar los procesos"
    },
    {
      "tipo": "gramatical",
      "texto": "unprecedented",
      "correccion": "sin precedentes"
    },
    {
      "tipo": "gramatical",
      "texto": "adoptan AI tempranamente",
      "correccion": "adoptan IA tempranamente"
    },
    {
      "tipo": "gramatical",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa"
    },
    {
      "tipo": "gramatical",
      "texto": "para encontrar la best fit para tu organización",
      "correccion": "para encontrar la mejor opción para tu organización"
    },
    {
      "tipo": "cliche",
      "texto": "revolucionado el mundo de las startups",
      "correccion": "transformado el ecosistema de las startups"
    },
    {
      "tipo": "cliche",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}
```