# Qwen 3.7 Flash — verificar_claim/claim_ausente_en_la_fuente

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 6.6 | quality: 6.0
- latency_total: 7.797s | tokens_per_second: 139.0
- input_tokens: 244 | output_tokens: 1084

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

{"veredicto": "NO_RESPALDADO", "motivo": "La fuente no menciona ningún dato sobre la rentabilidad de Nordvia, solo informa sobre una ronda de inversión y planes de expansión."}