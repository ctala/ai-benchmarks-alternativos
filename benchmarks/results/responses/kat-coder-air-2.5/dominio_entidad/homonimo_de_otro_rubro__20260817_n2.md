# KAT Coder Air v2.5 — dominio_entidad/homonimo_de_otro_rubro

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.6 | quality: 7.0
- latency_total: 1.957s | tokens_per_second: 136.9
- input_tokens: 262 | output_tokens: 268

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



```json
{"dominio": "https://auroraventures.vc", "motivo": "El dominio .vc es el estándar para fondos de venture capital y corresponde al sitio oficial de Aurora Ventures, mientras que el .co.jp apunta a Japón (no coincide con su foco LATAM) y Crunchbase es solo un directorio."}
```