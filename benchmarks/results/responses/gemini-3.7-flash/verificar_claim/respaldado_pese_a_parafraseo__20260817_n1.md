# Gemini 3.7 Flash — verificar_claim/respaldado_pese_a_parafraseo

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 3.084s | tokens_per_second: 68.7
- input_tokens: 216 | output_tokens: 212

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

```json
{"veredicto": "RESPALDADO", "motivo": "La fuente confirma que el equipo de Nordvia cuenta actualmente con medio centenar de empleados."}
```