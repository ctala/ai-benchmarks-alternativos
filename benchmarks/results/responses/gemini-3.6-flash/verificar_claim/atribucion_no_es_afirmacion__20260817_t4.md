# Gemini 3.6 Flash — verificar_claim/atribucion_no_es_afirmacion

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 6.7 | quality: 7.0
- latency_total: 7.266s | tokens_per_second: 162.8
- input_tokens: 217 | output_tokens: 1183

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

```json
{"veredicto": "RESPALDADO", "motivo": "La fuente cita a la CEO de Nordvia afirmando que la empresa será rentable en 2027."}
```