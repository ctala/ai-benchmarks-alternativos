# Claude Opus 5 Fast — dominio_entidad/solo_articulos_de_prensa

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 3.027s | tokens_per_second: 30.1
- input_tokens: 428 | output_tokens: 91

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

EMPRESA: Kaltrix
CONTEXTO: Empresa de software de gestión mencionada en prensa sectorial.

CANDIDATAS:
- https://diarioeconomico.example/kaltrix-cierra-acuerdo-con-retail
- https://startupnews.example/tag/kaltrix
- https://medium.example/@analista/por-que-kaltrix-crece


## Respuesta completa

{"dominio": null, "motivo": "Todas las candidatas son artículos de prensa o páginas de etiquetas que hablan de Kaltrix, ninguna es su sitio oficial."}