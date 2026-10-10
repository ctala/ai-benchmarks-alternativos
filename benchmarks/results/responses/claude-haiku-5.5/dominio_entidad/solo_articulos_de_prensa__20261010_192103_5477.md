# Claude Haiku 5.5 — dominio_entidad/solo_articulos_de_prensa

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.533s | tokens_per_second: 79.6
- input_tokens: 430 | output_tokens: 122

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

{"dominio": null, "motivo": "Ninguna candidata es el sitio oficial: son un artículo de prensa, una página de etiqueta de un medio y un post de blog de un analista."}