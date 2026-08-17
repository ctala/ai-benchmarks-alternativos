# Qwen 3-Next 80B Instruct — verificar_claim/inferencia_aritmetica_correcta

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 2.162s | tokens_per_second: 31.9
- input_tokens: 239 | output_tokens: 69

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente dice que el equipo de 50 personas se duplicará, lo que implica que actualmente tiene 50 y llegará a 100, no que contratará 50 nuevas personas en total."}