# Nemotron 3 Ultra 550B — translation/detect_language_issues

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 5.3 | quality: 4.88
- latency_total: 6.978s | tokens_per_second: 185.0
- input_tokens: 217 | output_tokens: 1291

## Respuesta completa

{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "En particular en Latinoamérica / Especialmente en Latinoamérica"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging",
      "correccion": "están aprovechando / están utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios / para hacer crecer sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático / El machine learning (si se usa como término técnico, mantener en cursiva)"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize",
      "correccion": "permite optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera inédita / sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas / Las compañías"
    },
    {
      "tipo": "spanglish",
      "texto": "adoptan AI",
      "correccion": "adoptan la IA / adoptan inteligencia artificial"
    },
    {
      "tipo": "spanglish",
      "texto": "competitive advantage",
      "correccion": "ventaja competitiva"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "hacer un análisis profundo / profundizar / realizar un estudio exhaustivo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la mejor opción / el mejor ajuste / la opción más adecuada"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta tilde en voz aguda terminada en -n)"
    },
    {
      "tipo": "gramatical",
      "texto": "permite optimize",
      "correccion": "permite optimizar (infinitivo tras 'permite')"
    },
    {
      "tipo": "cliche",
      "texto": "deep dive / best fit / competitive advantage / leverage / scale",
      "correccion": "Usar terminología española natural: análisis profundo, mejor opción, ventaja competitiva, aprovechar, escalar/crecer"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}