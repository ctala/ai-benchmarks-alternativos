# Qwen 3.7 Flash — dominio_entidad/homonimo_de_otro_rubro

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 12.287s | tokens_per_second: 130.3
- input_tokens: 262 | output_tokens: 1601

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

{"dominio": "auroraventures.vc", "motivo": "Coincide con el perfil de un fondo VC y utiliza la extensión .vc, descartando el dominio japonés por la región foco y el enlace de Crunchbase por ser un directorio."}