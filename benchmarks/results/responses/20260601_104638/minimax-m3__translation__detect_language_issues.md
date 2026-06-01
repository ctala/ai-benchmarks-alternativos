# MiniMax M3 — translation/detect_language_issues

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.32 | quality: 8.46
- latency_total: 28.818s | tokens_per_second: 38.1
- input_tokens: 350 | output_tokens: 1097
- judge_score: 5 | justificación: La respuesta es precisa al identificar y corregir problemas de idioma, relevante al ajustarse al contexto de un blog en español, y ofrece correcciones útiles y claras, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "En América Latina, especialmente"
    },
    {
      "tipo": "gramatical",
      "texto": "estan leveraging",
      "correccion": "están aprovechando"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging nuevas herramientas",
      "correccion": "aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "gramatical",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan inteligencia artificial"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage significativo",
      "correccion": "ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "hacer un análisis profundo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la mejor opción para tu organización"
    },
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "está transformando el ecosistema de las startups"
    },
    {
      "tipo": "cliche",
      "texto": "permiten optimize los procesos de manera unprecedented",
      "correccion": "permite optimizar los procesos de forma innovadora"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```