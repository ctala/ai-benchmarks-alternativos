# GPT-OSS 20B (Groq) — translation/detect_language_issues

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.12 | quality: 9.06
- latency_total: 1.406s | tokens_per_second: 685.4
- input_tokens: 262 | output_tokens: 964
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara al identificar problemas de idioma e incluir correcciones adecuadas; ofrece insights útiles para emprendedores.

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "especialmente en Latinoamérica"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas para scale their businesses",
      "correccion": "están aprovechando nuevas herramientas para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning permite optimize los procesos de manera unprecedented",
      "correccion": "El aprendizaje automático permite optimizar los procesos de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI tempranamente tienen un competitive advantage significativo",
      "correccion": "Las empresas que adoptan IA tempranamente tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit para tu organización",
      "correccion": "Es importante realizar un análisis profundo de las opciones disponibles para encontrar la mejor opción para tu organización"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están"
    },
    {
      "tipo": "gramatical",
      "texto": "tempranamente",
      "correccion": "temprano"
    },
    {
      "tipo": "cliche",
      "texto": "revolucionado el mundo",
      "correccion": "transformado el mundo"
    },
    {
      "tipo": "cliche",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "cliche",
      "texto": "deep dive",
      "correccion": "análisis profundo"
    },
    {
      "tipo": "cliche",
      "texto": "best fit",
      "correccion": "la mejor opción"
    }
  ],
  "score_idioma": 3,
  "veredicto": "necesita_edicion"
}
```