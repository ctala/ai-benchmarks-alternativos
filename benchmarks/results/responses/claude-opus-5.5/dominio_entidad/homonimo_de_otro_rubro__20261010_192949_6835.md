# Claude Opus 5.5 — dominio_entidad/homonimo_de_otro_rubro

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.42 | quality: 7.0
- latency_total: 5.668s | tokens_per_second: 66.3
- input_tokens: 405 | output_tokens: 376

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

EMPRESA: Aurora Ventures
CONTEXTO: Fondo de inversión de etapa temprana con foco en LATAM.

CANDIDATAS:
- https://auroraventures.co.jp
- https://auroraventures.vc
- https://www.crunchbase.example/organization/aurora-ventures


## Respuesta completa

{"dominio": null, "motivo": "El .co.jp apunta a una empresa japonesa homónima y Crunchbase es un directorio; auroraventures.vc es plausible para un fondo, pero nada lo vincula con el foco en LATAM y 'Aurora Ventures' es un nombre común, así que no es claramente el oficial."}