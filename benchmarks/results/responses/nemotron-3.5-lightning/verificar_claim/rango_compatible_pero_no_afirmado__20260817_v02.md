# Nemotron 3.5 Lightning — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.2 | quality: 10.0
- latency_total: 6.841s | tokens_per_second: 330.1
- input_tokens: 239 | output_tokens: 2258

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente indica 'más de US$ 4 millones' y señala que la compañía no confirmó el monto exacto, sin afirmar los 4,2 millones específicamente."}