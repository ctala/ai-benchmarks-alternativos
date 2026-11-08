# Seed 2.0 Code — verificar_claim/cifra_de_otra_magnitud

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.23 | quality: 7.0
- latency_total: 71.752s | tokens_per_second: 73.2
- input_tokens: 258 | output_tokens: 5253

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
Nordvia alcanzó una valuación de 4,2 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de US$ 4,2 millones liderada por Aurora Ventures. La compañía no reveló su valuación post-money.


## Respuesta completa

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente indica que los US$4,2 millones corresponden a una ronda semilla de Nordvia, y que la compañía no reveló su valuación post-money, por lo que no respalda la afirmación."}