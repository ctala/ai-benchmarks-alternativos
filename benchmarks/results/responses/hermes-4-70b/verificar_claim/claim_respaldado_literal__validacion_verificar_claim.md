# Hermes 4 70B — verificar_claim/claim_respaldado_literal

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.049s | tokens_per_second: 52.4
- input_tokens: 286 | output_tokens: 55

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
Nordvia levantó una ronda semilla de 4,2 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 millones liderada por Aurora Ventures, con participación de dos fondos regionales. La compañía, fundada en 2024, opera en logística de última milla y planea abrir oficinas en Chile durante el primer trimestre de 2027.


## Respuesta completa

{"veredicto": "RESPALDADO", "motivo": "La fuente menciona que Nordvia anunció el cierre de una ronda semilla de US$ 4,2 millones, lo cual respalda el claim."}