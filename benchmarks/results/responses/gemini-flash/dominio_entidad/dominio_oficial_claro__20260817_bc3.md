# Gemini 2.5 Flash — dominio_entidad/dominio_oficial_claro

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 1.625s | tokens_per_second: 34.5
- input_tokens: 257 | output_tokens: 56

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
{
  "dominio": "nordvia.com",
  "motivo": "Es el dominio principal que coincide con el nombre de la empresa y no es un subdominio de una plataforma ni un perfil de red social."
}
```