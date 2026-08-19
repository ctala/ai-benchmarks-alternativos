# Step 3.5 Flash — dominio_entidad/dominio_oficial_claro

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 15.399s | tokens_per_second: 47.1
- input_tokens: 278 | output_tokens: 726

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

{
  "dominio": "nordvia.com",
  "motivo": "Dominio principal de la empresa, no es una plataforma externa ni un artículo de prensa."
}