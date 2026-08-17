# Qwen 3-Next 80B Instruct — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.328s | tokens_per_second: 50.4
- input_tokens: 239 | output_tokens: 67

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
Nordvia levantó 4,2 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de más de US$ 4 millones, según fuentes cercanas a la operación. La compañía no confirmó el monto exacto.


## Respuesta completa

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente menciona que Nordvia recaudó más de 4 millones de dólares, pero no confirma el monto exacto de 4,2 millones, por lo que no respalda el claim específico."}