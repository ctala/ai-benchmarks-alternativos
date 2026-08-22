# GLM 5.3 — dominio_entidad/ninguna_candidata_sirve

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 2.845s | tokens_per_second: 39.7
- input_tokens: 264 | output_tokens: 113

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

EMPRESA: Belmar Systems
CONTEXTO: Consultora tecnológica pequeña, poca presencia digital.

CANDIDATAS:
- https://www.linkedin.com/company/belmar-systems
- https://directorio-empresas.example/belmar-systems
- https://facebook.example/belmarsystems


## Respuesta completa

{"dominio": null, "motivo": "Todos los candidatos son perfiles de redes sociales o directorios, no un sitio web oficial."}