# Kimi K2.7 Code — verificar_claim/cifra_alterada

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 5.406s | tokens_per_second: 52.9
- input_tokens: 244 | output_tokens: 286

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
{"veredicto": "CONTRADICE", "motivo": "La fuente indica que la ronda semilla fue de US$ 4,2 millones, no de 42 millones."}
```