# Sakana Namazu — dominio_entidad/homonimo_de_otro_rubro

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 7.937s | tokens_per_second: 204.7
- input_tokens: 285 | output_tokens: 1625

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

{"dominio": "auroraventures.vc", "motivo": "El dominio .vc es propio e identifica a una firma de venture capital, coherente con el contexto del fondo; el .co.jp parece corresponder a otra empresa y el crunchbase es un directorio."}