# Solar Pro 4 — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.273s | tokens_per_second: 54.2
- input_tokens: 282 | output_tokens: 69

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



{"veredicto": "NO_RESPALDADO", "motivo": "La fuente indica que el monto es 'más de US$ 4 millones' y que no se confirmó el número exacto, por lo que no respalda específicamente los 4,2 millones mencionados en el claim."}