# MiniMax M2.7 (directo) — verificar_claim/anuncio_no_es_cierre

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.19 | quality: 7.0
- latency_total: 4.158s | tokens_per_second: 61.8
- input_tokens: 212 | output_tokens: 257

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
Nordvia cerró su ronda el 14 de agosto de 2026.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia anunció hoy que completó su ronda semilla de US$ 4,2 millones, operación que según la compañía se firmó «a comienzos del trimestre».


## Respuesta completa

{"veredicto": "RESPALDADO", "motivo": "La fuente está fechada el 14 de agosto de 2026 y dice que Nordvia anunció ese mismo día el cierre de su ronda semilla."}