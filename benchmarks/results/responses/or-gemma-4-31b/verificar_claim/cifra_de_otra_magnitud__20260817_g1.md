# Gemma 4 31B — verificar_claim/cifra_de_otra_magnitud

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 4.558s | tokens_per_second: 12.5
- input_tokens: 230 | output_tokens: 57

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

```json
{"veredicto": "CONTRADICE", "motivo": "La fuente indica que 4,2 millones de dólares fue el monto de la ronda semilla, no la valuación de la empresa, la cual no fue revelada."}
```