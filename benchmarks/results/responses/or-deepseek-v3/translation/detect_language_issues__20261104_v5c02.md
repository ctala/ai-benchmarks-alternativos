# DeepSeek V3 — translation/detect_language_issues

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 6.77 | quality: 6.67
- latency_total: 9.446s | tokens_per_second: 38.9
- input_tokens: 213 | output_tokens: 367

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
            "tipo": "spanglish",
            "texto": "En特别是在拉丁美洲",
            "correccion": "Especialmente en América Latina"
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
            "texto": "optimize los procesos",
            "correccion": "optimizar los procesos"
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
    "score_idioma": 4,
    "veredicto": "necesita_edicion"
}
```