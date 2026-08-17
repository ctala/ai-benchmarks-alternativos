# Kimi K3 — verificar_claim/atribucion_no_es_afirmacion

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.0 | quality: 7.0
- latency_total: 25.557s | tokens_per_second: 27.2
- input_tokens: 334 | output_tokens: 696

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
Nordvia será rentable en 2027.

FUENTE:
TechFinance — 14 de agosto de 2026

«Vamos a ser rentables en 2027», afirmó Marta Iribarne, CEO de Nordvia, durante la presentación de la ronda. La compañía no publica sus estados financieros.


## Respuesta completa

{"veredicto": "RESPALDADO", "motivo": "La fuente cita a Marta Iribarne, CEO de Nordvia, afirmando que la compañía será rentable en 2027, aunque se trata de una declaración suya y no de un hecho verificado."}