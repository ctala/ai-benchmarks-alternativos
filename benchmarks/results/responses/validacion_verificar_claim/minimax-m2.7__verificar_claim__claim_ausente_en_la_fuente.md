# MiniMax M2.7 — verificar_claim/claim_ausente_en_la_fuente

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 4.425s | tokens_per_second: 38.0
- input_tokens: 218 | output_tokens: 168

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
Nordvia alcanzó la rentabilidad en 2026.

FUENTE:
TechFinance — 14 de agosto de 2026

La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 millones liderada por Aurora Ventures. La compañía opera en logística de última milla y planea abrir oficinas en Chile.


## Respuesta completa

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente menciona una ronda semilla y planes de expansión, pero no hace referencia alguna a que Nordvia haya alcanzado la rentabilidad."}