# Qwen3-Coder-Next (OpenRouter FP8) — verificar_claim/anuncio_no_es_cierre

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.058s | tokens_per_second: 69.9
- input_tokens: 247 | output_tokens: 74

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente indica que la ronda se firmó «a comienzos del trimestre», sin especificar el 14 de agosto como fecha exacta de cierre, y el anuncio se hizo ese día, no necesariamente el cierre."}