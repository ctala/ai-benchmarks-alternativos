# Tencent Hy4 preview — verificar_claim/anuncio_no_es_cierre

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.35 | quality: 7.0
- latency_total: 48.951s | tokens_per_second: 68.9
- input_tokens: 255 | output_tokens: 3373

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

{"veredicto": "CONTRADICE", "motivo": "La fuente indica que la ronda se firmó a comienzos del trimestre y que el 14 de agosto de 2026 solo se anunció su finalización, no que se cerrara ese día."}