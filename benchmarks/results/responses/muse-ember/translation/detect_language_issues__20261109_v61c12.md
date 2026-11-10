# Muse Ember — translation/detect_language_issues

- model_id: `meta/muse-ember`
- success: True  | final: 9.18 | quality: 10.0
- latency_total: 4.381s | tokens_per_second: 639.1
- input_tokens: 213 | output_tokens: 2800

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

{"problemas": [{"tipo": "cliche", "texto": "ha revolucionado el mundo", "correccion": "ha transformado el panorama empresarial"}, {"tipo": "spanglish", "texto": "startups", "correccion": "empresas emergentes"}, {"tipo": "chino", "texto": "特别是在拉丁美洲", "correccion": "especialmente en Latinoamérica"}, {"tipo": "gramatical", "texto": "estan", "correccion": "están"}, {"tipo": "spanglish", "texto": "leveraging", "correccion": "aprovechando"}, {"tipo": "spanglish", "texto": "scale their businesses", "correccion": "hacer crecer sus negocios"}, {"tipo": "spanglish", "texto": "machine learning", "correccion": "aprendizaje automático"}, {"tipo": "spanglish", "texto": "optimize", "correccion": "optimizar"}, {"tipo": "spanglish", "texto": "de manera unprecedented", "correccion": "de una manera sin precedentes"}, {"tipo": "spanglish", "texto": "companies", "correccion": "empresas"}, {"tipo": "spanglish", "texto": "AI", "correccion": "IA"}, {"tipo": "spanglish", "texto": "competitive advantage", "correccion": "ventaja competitiva"}, {"tipo": "spanglish", "texto": "deep dive", "correccion": "análisis profundo"}, {"tipo": "spanglish", "texto": "best fit", "correccion": "la opción más adecuada"}], "score_idioma": 3, "veredicto": "inaceptable"}