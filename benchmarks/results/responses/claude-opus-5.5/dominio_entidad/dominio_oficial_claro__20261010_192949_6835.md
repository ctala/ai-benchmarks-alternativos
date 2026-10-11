# Claude Opus 5.5 — dominio_entidad/dominio_oficial_claro

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.38 | quality: 7.0
- latency_total: 6.693s | tokens_per_second: 71.6
- input_tokens: 408 | output_tokens: 479

## Entrada exacta (lo que recibió el modelo)

**system:**

Recibís el nombre de una empresa y una lista de URLs candidatas encontradas en una búsqueda. Elegí cuál es su SITIO WEB OFICIAL.

Respondé SOLO con un JSON:
{"dominio": "<dominio.com>" | null, "motivo": "<una frase>"}

Reglas duras:
- Un subdominio de una plataforma de sitios (squarespace, wixsite, myshopify, webflow.io, github.io) NO es el sitio oficial de la empresa.
- Un artículo de prensa QUE HABLA de la empresa no es su sitio.
- Un perfil en una red social o directorio no es su sitio.
- Si ninguno es claramente el sitio oficial, respondé null. Es preferible null a adivinar: una ficha con el dominio equivocado es peor que una sin dominio.

**user:**

EMPRESA: Nordvia
CONTEXTO: Startup uruguaya de logística de última milla, fundada en 2024.

CANDIDATAS:
- https://nordvia.com
- https://www.linkedin.com/company/nordvia
- https://techfinance.example/nordvia-levanta-ronda-semilla


## Respuesta completa

```json
{"dominio": null, "motivo": "LinkedIn es un perfil social y techfinance.example es un artículo de prensa; nordvia.com coincide con el nombre, pero nada confirma que pertenezca a esta startup uruguaya de logística y no a otra empresa con el mismo nombre."}
```