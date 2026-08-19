# KAT Coder Pro v2.5 — verificar_claim/plan_no_es_hecho

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 2.865s | tokens_per_second: 46.8
- input_tokens: 251 | output_tokens: 134

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
Nordvia abrirá oficinas en Chile en el primer trimestre de 2027.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de US$ 4,2 millones. La compañía **planea** abrir oficinas en Chile durante el primer trimestre de 2027, aunque la decisión final depende de la evolución del mercado.


## Respuesta completa



{"veredicto": "NO_RESPALDADO", "motivo": "La fuente dice que la compañía 'planea' abrir oficinas, condicionado a la evolución del mercado, no que lo hará con certeza."}