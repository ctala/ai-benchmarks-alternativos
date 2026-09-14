# Muse Spark 1.3 — dominio_entidad/sitio_que_anuncia_cierre

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 3.688s | tokens_per_second: 149.7
- input_tokens: 284 | output_tokens: 552

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

{"dominio": "trevian.com", "motivo": "Es el dominio propio que publica el aviso de cese de operaciones."}