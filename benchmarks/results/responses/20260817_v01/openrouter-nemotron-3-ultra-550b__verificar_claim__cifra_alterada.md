# Nemotron 3 Ultra 550B — verificar_claim/cifra_alterada

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 9.33 | quality: 10.0
- latency_total: 1.648s | tokens_per_second: 87.4
- input_tokens: 238 | output_tokens: 144

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
Nordvia levantó una ronda semilla de 42 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 millones liderada por Aurora Ventures.


## Respuesta completa

{"veredicto": "CONTRADICE", "motivo": "La fuente indica US$ 4,2 millones, no US$ 42 millones."}