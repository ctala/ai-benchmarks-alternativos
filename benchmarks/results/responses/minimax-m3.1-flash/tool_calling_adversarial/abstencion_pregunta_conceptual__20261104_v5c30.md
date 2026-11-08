# MiniMax M3.1 Flash — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.22 | quality: 8.5
- latency_total: 6.486s | tokens_per_second: 179.2
- input_tokens: 810 | output_tokens: 1162
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para manejar cobros con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Es una pregunta de política de cobros, y la respuesta corta es: **por defecto, cobra por adelantado**. Cuando no conoces al cliente, el riesgo de no cobrar pesa más que la fricción de pedirle un adelanto. Pero hay matices útiles.

## Por qué el adelanto es la opción por defecto

- **Te protege del impago**, que es el riesgo principal cuando no hay historial.
- **Te financia el costo** de preparation o envío de la mercancía antes de que recibas un centavo.
- **Es un filtro**: un cliente que se niega a pagar por adelantado es un cliente que probablemente te costará tiempo de cobranza.
- Casi nunca pierdes una venta por pedir adelanto; lo que pierdes esFacturas huérfanas.

## Cuándo sí conviene contra entrega

- El **monto es bajo** comparado con el costo de envío (si el flete vale más que la mercadería, cobrar contra entrega es lo razonable).
- La **entrega es inmediata** (servicio en el momento, producto digital que entregas al instante).
- El cliente **tiene identidad y reputation verificable**, aunque sea nuevo contigo (otra empresa, sector, referencias).
- El cliente es **un intermediario/revendedor** que necesita revender antes de pagar, y puedes fijar un volumen mínimo.

## La vía intermedia que uso en la práctica

Es la que mejor equilibra ambos extremos:

| Esquema | Cuándo |
|---|---|
| 100% anticipado | Cliente nuevo, monto alto, o entrega diferida |
| 50% anticipo + 50% contra entrega | Cliente nuevo con monto medio, y quieres no perderlo |
| 100% contra entrega | Monto bajo, entrega inmediata, cliente verificado |
| Hitos / milestones | Proyectos o servicios largos |

Other Alternativas de protección: **transferencia por adelantado con confirmación de pago antes de despachar**, **garantía de pago de plataforma** ( marketplaces con escrow ), **letra de crédito o factoring** para montos altos, y siempre un **documento firmado** (orden de compra, proforma o contrato) que deje por escrito las condiciones de pago, el plazo de vencimiento y el recargo por mora.

## Antes de decidir sobre este cliente en concreto

Verifica: identificación fiscal, antigüedad de la empresa, referencias de otros proveedores, y que los datos de facturación coincidan con los de entrega. En la práctica, muchas estafas empiezan con datos que no cuadran.

---

**Si me pasas el nombre o el email del cliente**, lo busco en el CRM y reviso si tiene historial de facturas, estado de cuenta yDelayed pagos anteriores — con eso te puedo decir con bastante más precisión qué esquema conviene. Y si decides avanzar, te emito la factura con el anticipo o el recordatorio de cobro que necesites.