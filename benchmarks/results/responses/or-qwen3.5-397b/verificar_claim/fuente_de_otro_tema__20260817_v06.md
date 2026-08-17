# Qwen 3.5 397B — verificar_claim/fuente_de_otro_tema

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 34.897s | tokens_per_second: 38.2
- input_tokens: 234 | output_tokens: 1332

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
Nordvia levantó una ronda semilla de 4,2 millones de dólares.

FUENTE:
TechFinance — 9 de agosto de 2026

El Banco Central de Uruguay mantuvo la tasa de política monetaria en 8,5% en su reunión de agosto, en línea con lo esperado por el mercado.


## Respuesta completa



{"veredicto": "NO_RESPALDADO", "motivo": "La fuente trata sobre el Banco Central de Uruguay y no menciona a Nordvia ni rondas de inversión."}