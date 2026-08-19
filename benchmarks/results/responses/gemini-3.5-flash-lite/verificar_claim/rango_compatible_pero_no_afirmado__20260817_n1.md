# Gemini 3.5 Flash Lite — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.45 | quality: 7.0
- latency_total: 1.047s | tokens_per_second: 50.6
- input_tokens: 209 | output_tokens: 53

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
Nordvia levantó 4,2 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de más de US$ 4 millones, según fuentes cercanas a la operación. La compañía no confirmó el monto exacto.


## Respuesta completa

```json
{"veredicto": "RESPALDADO", "motivo": "La fuente afirma que la empresa cerró una ronda de más de 4 millones de dólares, lo cual respalda la cifra de 4,2 millones."}
```