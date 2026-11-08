# GLM 5.3 — translation/detect_language_issues

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 67.133s | tokens_per_second: 91.4
- input_tokens: 208 | output_tokens: 6136

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
      "tipo": "chino",
      "texto": "En特别是拉丁美洲",
      "correccion": "Especialmente en América Latina (los caracteres chinos 特别是 significan 'especialmente' y fueron insertados en mitad de la frase)"
    },
    {
      "tipo": "gramatical",
      "texto": "estan",
      "correccion": "están (falta la tilde)"
    },
    {
      "tipo": "spanglish",
      "texto": "los emprendedores estan leveraging nuevas herramientas",
      "correccion": "los emprendedores están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos (verbo en inglés en lugar del infinitivo español)"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "sin precedentes / de forma sin precedentes"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies",
      "correccion": "Las empresas"
    },
    {
      "tipo": "spanglish",
      "texto": "adoptan AI",
      "correccion": "adoptan la IA (sigla en español, con artículo)"
    },
    {
      "tipo": "spanglish",
      "texto": "un competitive advantage significativo",
      "correccion": "una ventaja competitiva significativa (al traducir, hay que ajustar también el género del artículo y del adjetivo)"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive",
      "correccion": "hacer un análisis profundo / analizar a fondo"
    },
    {
      "tipo": "spanglish",
      "texto": "la best fit para tu organización",
      "correccion": "la opción más adecuada para tu organización"
    },
    {
      "tipo": "spanglish",
      "texto": "El machine learning",
      "correccion": "El aprendizaje automático (aunque 'machine learning' es habitual en textos técnicos, en un blog generalista se prefiere el término en español)"
    },
    {
      "tipo": "cliche",
      "texto": "ha revolucionado el mundo de las startups",
      "correccion": "Apertura muy gastada y propia de textos de IA; conviene concretar, p. ej.: 'está transformando la forma de crear y hacer crecer empresas'"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer...",
      "correccion": "Frase de relleno sin información; mejor ir directo al grano: 'Analiza a fondo las opciones disponibles...'"
    },
    {
      "tipo": "spanglish",
      "texto": "startups",
      "correccion": "Anglicismo aceptado en prensa tecnológica (la RAE registra la adaptación 'estartups'); en un blog de emprendimiento puede mantenerse, pero es el único anglicismo tolerable del texto"
    }
  ],
  "score_idioma": 2,
  "veredicto": "inaceptable"
}
```