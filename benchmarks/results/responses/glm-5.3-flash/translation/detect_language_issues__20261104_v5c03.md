# GLM 5.3 Flash — translation/detect_language_issues

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 58.805s | tokens_per_second: 82.8
- input_tokens: 208 | output_tokens: 4871

## Entrada exacta (lo que recibió el modelo)

**system:**

Revisa el siguiente texto en espanol y reporta TODOS los problemas de idioma que encuentres. Responde en JSON.

**user:**

Revisa este texto generado por una IA para un blog en espanol:

"La inteligencia artificial ha revolucionado el mundo de las startups. En特别是在拉丁美洲, los emprendedores estan leveraging nuevas herramientas para scale their businesses. El machine learning permite optimize los procesos de manera unprecedented.

Las companies que adoptan AI tempranamente tienen un competitive advantage significativo. Es importante hacer un deep dive en las opciones disponibles para encontrar la best fit para tu organización."

Devuelve un JSON con:
{"problemas": [{"tipo": "chino|spanglish|cliche|gramatical", "texto": "...", "correccion": "..."}], "score_idioma": 0-10, "veredicto": "publicable|necesita_edicion|inaceptable"}


## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "está transformando el ecosistema de startups (apertura genérica muy típica de IA; conviene una frase más concreta)"
    },
    {
      "tipo": "chino",
      "texto": "特别是在拉丁美洲",
      "correccion": "especialmente en América Latina"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta la tilde)"
    },
    {
      "tipo": "spanglish",
      "texto": "leveraging",
      "correccion": "aprovechando / utilizando"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "machine learning",
      "correccion": "aprendizaje automático (anglicismo habitual en textos técnicos; si se conserva, escribirlo en cursiva)"
    },
    {
      "tipo": "spanglish",
      "texto": "optimize",
      "correccion": "optimizar"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera inédita / sin precedentes"
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
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa (además, \"ventaja\" es femenino)"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en",
      "correccion": "analizar a fondo / hacer un análisis profundo de"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit",
      "correccion": "la mejor opción / la que mejor se adapte"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```

Nota: el texto contiene un fragmento en chino incrustado y más de diez frases en inglés sin traducir, por lo que no es publicable sin una reescritura completa, no solo una corrección puntual.