# Qwen 3.8 27B — verificar_claim/inferencia_aritmetica_correcta

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.34 | quality: 7.0
- latency_total: 24.778s | tokens_per_second: 10.1
- input_tokens: 272 | output_tokens: 251

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



{"veredicto": "RESPALDADO", "motivo": "Si el equipo de 50 personas se duplicará, eso implica sumar otras 50 personas durante el próximo año."}