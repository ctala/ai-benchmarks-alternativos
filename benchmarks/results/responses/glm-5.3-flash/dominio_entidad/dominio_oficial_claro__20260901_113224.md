# GLM 5.3 Flash — dominio_entidad/dominio_oficial_claro

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 15.946s | tokens_per_second: 16.2
- input_tokens: 269 | output_tokens: 258

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

{"dominio": "nordvia.com", "motivo": "El dominio coincide exactamente con el nombre de la empresa y es el único candidato que no es un perfil social, un artículo de prensa ni un subdominio de plataforma."}