# Tencent Hy4 preview — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `tencent/hy4-preview`
- success: True  | final: 7.63 | quality: 8.5
- latency_total: 16.395s | tokens_per_second: 55.1
- input_tokens: 580 | output_tokens: 903
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando estrategias detalladas y consideraciones prácticas para manejar la facturación con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Como regla general: con clientes nuevos y sin historial, **factura por adelantado (total o parcial)**. El riesgo de crédito lo asumes tú si entregas primero, y sin historial no tienes forma de estimar si te van a pagar.

**Cómo escalonarlo según el caso:**

| Situación | Recomendación |
|---|---|
| Ticket pequeño / trabajo estándar | 100% por adelantado |
| Proyecto mediano | 30–50% de anticipo, resto contra entrega |
| Proyecto grande o largo | Facturación por hitos, con el primer pago antes de empezar |
| Cliente que exige crédito | Primer pedido por adelantado; condiciones abiertas recién a partir del segundo |

**Si de todos modos quieres ir contra entrega**, reduce la exposición:
- Limita el monto del primer pedido (que sea una prueba, no tu factura más grande).
- Pide referencias comerciales de otros proveedores y verifícalas.
- Deja por escrito plazo de pago, intereses de mora y quién asume gastos de cobranza.
- No encadenes entregas: no embarques el segundo pedido si el primero está impago.

**Como cliente ya conocido:** una vez que tengas 2–3 facturas pagadas puntualmente, ya tienes datos reales para decidir en lugar de una corazonada.

Dos notas prácticas de mi lado:
- Si me das el nombre o email, puedo buscarlo en el CRM: aunque sea "nuevo" para ti, a veces ya existe con historial de cuenta, y eso cambia la recomendación.
- Si decides facturar por adelantado, avísame con el cliente y el monto: la emisión de facturas tiene efecto contable y **no se puede revertir**, así que conviene confirmar los datos antes de ejecutarla.