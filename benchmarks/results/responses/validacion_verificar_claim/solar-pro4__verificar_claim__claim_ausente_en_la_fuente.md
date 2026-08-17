# Solar Pro 4 — verificar_claim/claim_ausente_en_la_fuente

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 7.347s | tokens_per_second: 8.2
- input_tokens: 296 | output_tokens: 60

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente no menciona nada sobre la rentabilidad de Nordvia en 2026, solo informa sobre el cierre de una ronda semilla y sus planes de expansión."}