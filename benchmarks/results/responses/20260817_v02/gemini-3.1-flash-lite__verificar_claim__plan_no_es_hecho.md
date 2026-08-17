# Gemini 3.1 Flash Lite — verificar_claim/plan_no_es_hecho

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.6 | quality: 7.0
- latency_total: 0.678s | tokens_per_second: 56.1
- input_tokens: 233 | output_tokens: 38

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

{"veredicto": "RESPALDADO", "motivo": "La fuente confirma explícitamente los planes de la empresa para abrir oficinas en Chile en el periodo mencionado."}