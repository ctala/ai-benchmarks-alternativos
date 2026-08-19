# Nemotron 3 Nano 30B — verificar_claim/cifra_de_otra_magnitud

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.6 | quality: 7.0
- latency_total: 1.979s | tokens_per_second: 311.7
- input_tokens: 242 | output_tokens: 617

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
Nordvia alcanzó una valuación de 4,2 millones de dólares.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de US$ 4,2 millones liderada por Aurora Ventures. La compañía no reveló su valuación post-money.


## Respuesta completa


{
  "veredicto": "NO_RESPALDADO",
  "motivo": "La fuente menciona una ronda de financiación de US$4,2 millones, pero indica que la valuación post-money no fue revelada, por lo que no confirma que la valuación sea de 4,2 millones."
}