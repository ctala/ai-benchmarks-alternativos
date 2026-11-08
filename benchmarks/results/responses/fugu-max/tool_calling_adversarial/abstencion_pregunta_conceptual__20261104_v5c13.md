# Fugu Max — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `sakana/fugu-max`
- success: True  | final: 7.63 | quality: 8.5
- latency_total: 6.861s | tokens_per_second: 170.2
- input_tokens: 770 | output_tokens: 1168
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para manejar la facturación con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

**Corto: por adelantado (o con anticipo parcial).** Con un cliente del que no sabes nada, el riesgo no es "cuándo facturo" sino **quién asume el impago**. Y con un desconocido, no deberías ser tú.

Ojo con una trampa de vocabulario: "contra entrega" puede significar dos cosas muy distintas:

| Escenario | Riesgo real | Veredicto |
|---|---|---|
| **Facturar y cobrar antes de entregar** | Casi nulo (si entra el dinero, entregas) | ✅ Ideal para primer pedido |
| **Contra entrega con cobro simultáneo** (efectivo/transferencia al recibir) | Bajo, pero asumes logística y posible rechazo | ✅ Aceptable |
| **Facturar contra entrega y cobrar a 15/30/60 días** | Alto: es crédito puro a un desconocido | ❌ Evítalo |

Ese tercer caso es el que suele llamarse "contra entrega" en la práctica y es donde la gente se quema.

**Cómo decidir, en orden:**
1. **Tamaño del pedido vs. tu margen.** Si el monto es menor que tu margen unitario, arriesgar crédito es matemáticamente absurdo: pide 100% adelantado sin drama.
2. **¿Puedes verificar al cliente?** Referencias comerciales, NIF/RUC verificable, domicilio comprobable, historial en buró de crédito. Si no hay nada verificable → anticipo.
3. **Costo de capital.** Cobrar a 30 días es financiar gratis. Ponle número: si tu margen es 20% y financias 30 días, una tasa de descuento razonable se come una parte real de la ganancia.
4. **Potencial de recurrencia.** Un cliente nuevo con pinta de comprador habitual justifica flexibilizar *en el segundo pedido*, no en el primero.

**Esquema híbrido que funciona bien con desconocidos:**
- Pedido pequeño o de bajo margen → **100% anticipado**.
- Pedido mediano/grande → **50% anticipo, 50% contra entrega con cobro simultáneo** (no a plazo).
- Crédito a 30 días → solo tras 2–3 operaciones pagadas puntualmente, o con garantía (cláusula de reserva de propiedad, aval, seguro de crédito).

**Dos advertencias:**
- Facturar **antes** de entregar puede adelantar obligaciones fiscales (IVA/IGV devengado por emisión, no por cobro) según tu jurisdicción. Si vas a facturar por adelantado en volumen, confírmalo con tu contador: a veces conviene *cobrar* el anticipo y emitir la factura al despachar.
- Si el anticipo no entra, no entregues. Suena obvio; es la causa #1 de pérdidas con clientes nuevos.

Si me das el nombre o email del cliente, lo busco en el CRM y te digo si ya tiene historial o estado de cuenta — eso convertiría esto en una decisión con datos en vez de una regla general.