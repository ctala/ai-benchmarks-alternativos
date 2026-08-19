# Nemotron 3.5 Lightning — verificar_claim/inferencia_aritmetica_correcta

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.4 | quality: 7.0
- latency_total: 3.39s | tokens_per_second: 307.4
- input_tokens: 244 | output_tokens: 1042

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
Nordvia contratará 50 personas durante el próximo año.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de US$ 4,2 millones. Su equipo, de 50 personas, se duplicará durante el próximo año según su CEO.


## Respuesta completa

{"veredicto": "RESPALDADO", "motivo": "La fuente indica que el equipo de 50 personas se duplicará, lo que equivale a contratar 50 personas adicionales durante el próximo año."}