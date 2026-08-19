# Gemini 3.6 Flash — dominio_entidad/ninguna_candidata_sirve

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 9.27 | quality: 10.0
- latency_total: 1.977s | tokens_per_second: 95.1
- input_tokens: 251 | output_tokens: 188

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

```json
{
  "dominio": null,
  "motivo": "Ninguna de las URLs candidatas corresponde a un sitio web oficial propio, son perfiles en redes sociales y directorios."
}
```