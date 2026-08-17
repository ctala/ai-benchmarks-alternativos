# Nex-N2-Mini — verificar_claim/titular_contradice_cuerpo

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 7.6 | quality: 7.0
- latency_total: 0.644s | tokens_per_second: 65.3
- input_tokens: 279 | output_tokens: 42

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
Meridian Labs fue adquirida por Grupo Antares.

FUENTE:
MERIDIAN LABS SERÍA ADQUIRIDA POR GRUPO ANTARES
Diario Económico — 12 de agosto de 2026

Según tres fuentes cercanas a la operación, Grupo Antares habría iniciado conversaciones para adquirir Meridian Labs. Consultada por este medio, la compañía **desmintió la operación**: «no existe ningún acuerdo de compra ni negociaciones en curso», señaló su directora de comunicaciones. Grupo Antares declinó comentar.


## Respuesta completa

{"veredicto":"NO_RESPALDADO","motivo":"La fuente indica que la operación fue desmentida por Meridian Labs y no que ya haya sido adquirida."}