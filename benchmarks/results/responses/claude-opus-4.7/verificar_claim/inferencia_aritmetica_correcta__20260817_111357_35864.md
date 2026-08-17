# Claude Opus 4.7 — verificar_claim/inferencia_aritmetica_correcta

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 6.54 | quality: 7.0
- latency_total: 3.178s | tokens_per_second: 37.4
- input_tokens: 364 | output_tokens: 119

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

{"veredicto": "CONTRADICE", "motivo": "La fuente indica que el equipo de 50 personas se duplicará, es decir, sumarán unas 50 más para llegar a 100, no que contratarán solo 50 en total desde cero; además el claim omite que ya tienen 50 y sugiere una cifra final distinta."}