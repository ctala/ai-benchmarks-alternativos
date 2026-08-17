# Gemini 2.5 Flash — dominio_entidad/solo_articulos_de_prensa

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 1.183s | tokens_per_second: 44.8
- input_tokens: 268 | output_tokens: 53

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

```json
{
  "dominio": null,
  "motivo": "Ninguna de las URLs candidatas es el sitio web oficial de Kaltrix. Todas son artículos de prensa o perfiles en plataformas de contenido."
}
```