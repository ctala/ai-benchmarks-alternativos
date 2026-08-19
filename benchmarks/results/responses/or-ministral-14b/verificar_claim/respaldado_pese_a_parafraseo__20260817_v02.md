# Ministral 14B — verificar_claim/respaldado_pese_a_parafraseo

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 1.454s | tokens_per_second: 36.4
- input_tokens: 235 | output_tokens: 53

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
{
  "veredicto": "RESPALDADO",
  "motivo": "La fuente afirma que Nordvia tiene 'medio centenar de empleados' (50 personas) en el momento de la noticia."
}
```