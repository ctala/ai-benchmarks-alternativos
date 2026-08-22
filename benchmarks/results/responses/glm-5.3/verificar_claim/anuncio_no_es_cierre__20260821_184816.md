# GLM 5.3 — verificar_claim/anuncio_no_es_cierre

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.94 | quality: 7.0
- latency_total: 3.5s | tokens_per_second: 68.6
- input_tokens: 229 | output_tokens: 240

## Entrada exacta (lo que recibió el modelo)

**system:**

Sos el verificador de datos de una redacción. Recibís un CLAIM y la FUENTE de la que supuestamente sale. Tu única tarea es decidir si la fuente respalda el claim.

Respondé SOLO con un JSON:
{"veredicto": "RESPALDADO" | "NO_RESPALDADO" | "CONTRADICE", "motivo": "<una frase>"}

RESPALDADO: la fuente afirma el claim, o algo equivalente.
NO_RESPALDADO: la fuente no dice nada sobre eso.
CONTRADICE: la fuente dice algo incompatible con el claim.

No uses conocimiento propio: solo lo que está en la fuente.

**user:**

CLAIM:
Nordvia cerró su ronda el 14 de agosto de 2026.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia anunció hoy que completó su ronda semilla de US$ 4,2 millones, operación que según la compañía se firmó «a comienzos del trimestre».


## Respuesta completa

{"veredicto": "CONTRADICE", "motivo": "La fuente indica que el 14 de agosto fue solo la fecha del anuncio, y que la ronda se firmó «a comienzos del trimestre», no ese día."}