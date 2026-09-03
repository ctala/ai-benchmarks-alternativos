# Tencent Hy4 preview — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 17.97s | tokens_per_second: 69.6
- input_tokens: 249 | output_tokens: 1250

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente solo señala que Nordvia cerró una ronda de más de US$ 4 millones y que no confirmó el monto exacto, sin afirmar los 4,2 millones."}