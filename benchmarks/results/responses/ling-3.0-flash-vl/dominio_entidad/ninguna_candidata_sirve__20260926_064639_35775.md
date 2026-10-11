# Ling 3.0 Flash VL — dominio_entidad/ninguna_candidata_sirve

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.885s | tokens_per_second: 82.8
- input_tokens: 296 | output_tokens: 156

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

{"dominio": null, "motivo": "Ninguna de las URLs corresponde al sitio web oficial; son perfiles de redes sociales (LinkedIn, Facebook) y un directorio de empresas."}