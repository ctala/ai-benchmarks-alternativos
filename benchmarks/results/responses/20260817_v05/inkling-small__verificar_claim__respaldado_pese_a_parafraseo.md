# Inkling Small — verificar_claim/respaldado_pese_a_parafraseo

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 9.82 | quality: 10.0
- latency_total: 0.913s | tokens_per_second: 134.7
- input_tokens: 228 | output_tokens: 123

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

{"veredicto": "RESPALDADO", "motivo": "La fuente dice que el equipo suma 'medio centenar de empleados', equivalente a unas 50 personas."}