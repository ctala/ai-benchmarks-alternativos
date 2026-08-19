# KAT Coder Air v2.5 — dominio_entidad/dominio_oficial_claro

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.406s | tokens_per_second: 118.8
- input_tokens: 267 | output_tokens: 167

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
{"dominio": "nordvia.com", "motivo": "Es el dominio corporativo directo de la empresa, mientras que LinkedIn es un perfil social y el otro enlace es un artículo de prensa sobre la startup."}
```