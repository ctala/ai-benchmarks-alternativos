# Gemma 4 26B MoE (3.8B activos) — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.45 | quality: 7.0
- latency_total: 0.979s | tokens_per_second: 43.9
- input_tokens: 227 | output_tokens: 43

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
{"veredicto": "RESPALDADO", "motivo": "La fuente confirma una ronda de más de 4 millones de dólares, lo cual es equivalente al claim."}
```