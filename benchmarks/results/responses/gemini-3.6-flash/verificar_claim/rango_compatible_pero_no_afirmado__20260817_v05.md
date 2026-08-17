# Gemini 3.6 Flash — verificar_claim/rango_compatible_pero_no_afirmado

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 3.422s | tokens_per_second: 115.2
- input_tokens: 209 | output_tokens: 394

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
{
  "veredicto": "NO_RESPALDADO",
  "motivo": "La fuente menciona que la cifra fue de más de 4 millones de dólares, pero señala que no se confirmó el monto exacto ni especifica que hayan sido 4,2 millones."
}
```