# GPT-OSS 20B — verificar_claim/anuncio_no_es_cierre

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.45 | quality: 7.0
- latency_total: 2.386s | tokens_per_second: 112.3
- input_tokens: 270 | output_tokens: 268

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

{"veredicto": "RESPALDADO", "motivo": "El artículo de TechFinance fechado el 14 de agosto de 2026 indica que Nordvia completó su ronda el mismo día."}