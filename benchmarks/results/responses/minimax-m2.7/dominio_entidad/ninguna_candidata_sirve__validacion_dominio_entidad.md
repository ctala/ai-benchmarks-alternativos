# MiniMax M2.7 — dominio_entidad/ninguna_candidata_sirve

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 9.03 | quality: 10.0
- latency_total: 6.2s | tokens_per_second: 31.6
- input_tokens: 246 | output_tokens: 196

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

{"dominio": null, "motivo": "Ninguna de las candidatas es el sitio web oficial: LinkedIn y Facebook son redes sociales, y el directorio es un sitio de terceros. Una empresa pequeña con poca presencia digital probablemente no tiene un sitio web propio detectable en esta búsqueda."}