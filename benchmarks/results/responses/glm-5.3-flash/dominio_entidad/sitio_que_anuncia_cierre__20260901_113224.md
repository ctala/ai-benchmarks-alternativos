# GLM 5.3 Flash — dominio_entidad/sitio_que_anuncia_cierre

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 6.813s | tokens_per_second: 46.2
- input_tokens: 289 | output_tokens: 315

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

EMPRESA: Trevian
CONTEXTO: Empresa de movilidad. El contexto indica que cesó operaciones en 2026.

CANDIDATAS:
- https://trevian.com  (el sitio muestra: «Trevian cesó operaciones el 30 de junio de 2026. Gracias a nuestros usuarios.»)
- https://movilidadhoy.example/trevian-cierra-tras-cuatro-anos


## Respuesta completa

{"dominio": "trevian.com", "motivo": "El dominio de marca muestra un mensaje de la propia empresa anunciando su cese, coherente con el contexto; el artículo de prensa solo habla de ella."}