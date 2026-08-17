# Nemotron 3 Nano 30B — verificar_claim/fuente_de_otro_tema

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 9.85 | quality: 10.0
- latency_total: 0.822s | tokens_per_second: 199.5
- input_tokens: 242 | output_tokens: 164

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
Nordvia levantó una ronda semilla de 4,2 millones de dólares.

FUENTE:
TechFinance — 9 de agosto de 2026

El Banco Central de Uruguay mantuvo la tasa de política monetaria en 8,5% en su reunión de agosto, en línea con lo esperado por el mercado.


## Respuesta completa

{
  "veredicto": "NO_RESPALDADO",
  "motivo": "La fuente solo menciona la tasa de política monetaria del Banco Central de Uruguay y no menciona ninguna ronda de financiación de Nordvia."
}