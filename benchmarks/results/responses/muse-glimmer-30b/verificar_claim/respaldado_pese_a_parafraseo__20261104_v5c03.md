# Muse Glimmer 30B — verificar_claim/respaldado_pese_a_parafraseo

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 9.58 | quality: 10.0
- latency_total: 1.583s | tokens_per_second: 137.7
- input_tokens: 231 | output_tokens: 218

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
Nordvia emplea a unas 50 personas.

FUENTE:
TechFinance — 14 de agosto de 2026

Nordvia cerró una ronda semilla de US$ 4,2 millones. Su equipo, que hoy suma medio centenar de empleados entre Montevideo y Buenos Aires, se duplicará durante el próximo año.


## Respuesta completa

{"veredicto": "RESPALDADO", "motivo": "La fuente indica que su equipo hoy suma medio centenar de empleados, equivalente a unas 50 personas."}