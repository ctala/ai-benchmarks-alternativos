# Ling 3.0 Flash VL — dominio_entidad/subdominio_de_plataforma

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 2.48s | tokens_per_second: 97.6
- input_tokens: 296 | output_tokens: 242

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

EMPRESA: Vertelia
CONTEXTO: Tienda de indumentaria sustentable, opera en Argentina.

CANDIDATAS:
- https://vertelia.squarespace.com
- https://www.instagram.com/vertelia
- https://emprendedores.example/vertelia-el-caso-de-la-moda-circular


## Respuesta completa

{"dominio": null, "motivo": "Ninguna de las URLs candidatas es el sitio web oficial: la primera es un subdominio de Squarespace, la segunda es un perfil de Instagram y la tercera es un artículo de prensa."}