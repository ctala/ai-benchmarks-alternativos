# GPT-OSS 20B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.73 | quality: 7.94
- latency_total: 10.514s | tokens_per_second: 88.9
- input_tokens: 337 | output_tokens: 935
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

### Facturar por adelantado vs. contra entrega cuando el cliente es nuevo

| Critério | Facturar por adelantado | Facturar contra entrega |
|----------|------------------------|------------------------|
| **Control de flujo de caja** | Mejor: recibes el pago antes de entregar el producto o servicio. <br> *Ventaja*: mitigación de riesgo de no pago. | Peor: pagas a proveedor/servicio antes de generar ingresos. <br> *Desventaja*: riesgo de quedar sin liquidez. |
| **Riesgo de impago** | Menor: el cliente ya ha sacado dinero. <br> *Riesgo residual*: cancelación en último momento, pero ya tienes el cobro. | Mayor: el cliente debe pagar una vez que reciba el bien. <br> *Riesgo*: cobranza post entrega. |
| **Confianza del cliente** | Alta: el cliente paga antes, lo cual demuestra confianza de su parte. | Baja: el cliente paga solo cuando lo ve, lo que puede generar incertidumbre. |
| **Credibilidad del proveedor** | Alta: indica profesionalismo y preparación. | Variable: si el cliente duda de la calidad, puede retrasar el pago. |
| **Gestión de inventario** | Necesitas primero el pago para moverte con pedidos alpino. | Derecho de hacer pedido según despacho, útil si tu inventario es preexistente. |
| **Relación a largo plazo** | Positivos: fortalece la relación al generar confianza. | Negativos: puede frenar la fidelización si el cliente percibe falta de compromiso. |
| **Costos administrativos** | Algunas empresas cobran un anticipo más alto, pero suele ser mayor beneficio. | Menos costo interno, pero con mayor tiempo de recuperación de fondos. |

### Recomendación general

1. **Para un cliente *completamente nuevo* (sin historial de pagos con tu empresa):**
   - **Factura adelantada** suele ser la opción más segura.  
   - Puedes agregar una pequeña **bonificación** o descuento por pagar antes para incentivar la respuesta (ejemplo: 2 % de descuento al pagar en el primer día).
   - Si el producto tiene stock limitado o tratamiento personalizado, exigir el adelanto reduce el riesgo de inventario vacío.

2. **Si tienes algún dato de su solvencia vía antes de emitir la factura:**
   - Pide un **anticipo de 50–30 %**.  
   - Emite la factura con el saldo restante una vez entregado el producto.  
   - Este modelo mezcla los beneficios de ambas estrategias.

3. **Situaciones de alta confianza o contratos de valor elevado:**
   - Puedes optar por **contra entrega** si el cliente muestra disposición a pagar a crédito y se dispone de garantías (garantía de seguro, aval…).

4. **Consideraciones operativas:**
   - Si tu cadena de suministro depende de pagos anticipados (proveedores que exigen factoraje), factura adelantado es práctico.
   - Si la logística es rápida y el inventario es estable, contra entrega arriesgará menos en términos de flujo de caja.

### Pasos concretos si decides facturar por adelantado

1. Analiza la *solvencia* (si es posible, obtén datos del cliente antes de la facturación).  
2. Emite la factura con un **plazo corto** (ej. 3 días hábiles).  
3. Envia recordatorios tal y como se recomienda (amable; si no pagara, firme).  
4. Al recibir el pago, verifica la cuenta antes de lanzar la entrega.  
5. Una vez entregado el producto/servicio, confirma la entrega y mantén al cliente informado sobre la factura pagada.

---

> **Resumen**  
> Con clientes nuevos, el riesgo de impago suele ser mayor. Facturar por adelantado te protege, fortalece la relación y asegura flujo de caja. Si consideras que la operación lo permite, un anticipo parcial también es una opción intermedia que combina los beneficios de ambas políticas.