# Gemini 3.5 Flash Lite — verificar_claim/cifra_alterada

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 0.63s | tokens_per_second: 73.0
- input_tokens: 210 | output_tokens: 46

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

```json
{"veredicto": "CONTRADICE", "motivo": "La fuente menciona que la ronda semilla fue de 4,2 millones de dólares y no de 42 millones."}
```