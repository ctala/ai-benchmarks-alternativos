# GPT-OSS 120B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.21 | quality: 8.5
- latency_total: 13.283s | tokens_per_second: 122.0
- input_tokens: 337 | output_tokens: 1621
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación exhaustiva de las ventajas y desventajas de ambas opciones de facturación para un cliente nuevo.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

### Facturar por adelantado vs. facturar contra entrega (al recibir la entrega)  
**Situación:** Cliente nuevo del que no tienes historial ni referencias.

---

## 1. Facturar **por adelantado** (pago anticipado)

| Ventajas | Desventajas |
|----------|--------------|
| **Liquidez inmediata**: el dinero llega antes de dedicar tiempo o recursos. | **Riesgo de rechazo**: el cliente puede decidir no comprar si le pides pago antes de ver el producto/servicio. |
| **Protección contra impagos**: eliminas el riesgo de que la factura quede en blanco. | **Falta de confianza percibida**: al no haber relación previa, puede parecer que no confías en él, lo que a veces aleja al prospecto. |
| **Facilita la planificación**: sabes con qué presupuesto cuentas para materiales, personal, etc. | **Posible fricción en negociaciones**: el cliente puede pedir descuentos o condiciones más flexibles. |
| **Menor carga administrativa**: no tendrás que hacer seguimiento de cobros tardíos o morosos. | **Coste de oportunidad**: si el cliente paga pero luego decide no continuar, habrás inmovilizado capital sin generar otra venta. |

**Cuándo usarlo:**  
- Cuando el proyecto implica **costos fijos elevados** (materia prima costosa, subcontratación, reserva de capacidad).  
- Cuando el cliente **solicita** explícitamente el pago anticipado.  
- Cuando puedes ofrecer **descuentos** atractivos a cambio del pago adelantado (por ejemplo, 5 % de descuento por pago al contado).  
- Cuando el **valor del pedido** es bajo y el riesgo de impago no justifica la complejidad de gestionar cobros posteriores.

---

## 2. Facturar **contra entrega** (pago a la vista o a plazo corto después de la entrega)

| Ventajas | Desventajas |
|----------|--------------|
| **Mayor facilidad de venta**: el cliente percibe menos riesgo y suele estar más dispuesto a comprar. | **Riesgo de impago**: puedes quedarte sin el dinero después de haber entregado el producto/servicio. |
| **Construye confianza**: demuestras que confías en la buena fe del cliente, lo que favorece la relación a largo plazo. | **Necesidad de gestión de cobros**: tendrás que dedicar tiempo a recordatorios, conciliaciones y, en el peor caso, a acciones de recuperación. |
| **Flexibilidad comercial**: puedes ofrecer condiciones de crédito (30 días, 60 días) que a veces son requisito del cliente. | **Impacto en el flujo de caja**: si el plazo es amplio y los márgenes son estrechos, la liquidez puede verse comprometida. |
| **Posibilidad de negociación**: al entregar primero, puedes usar la calidad del trabajo como argumento para negociar pagos rápidos o futuros. | **Mayor exposición a fraude** (especialmente en ventas online o internacionales). |

**Cuándo usarlo:**  
- Cuando el **valor del pedido** es bajo o medio y el riesgo financiero es aceptable.  
- Cuando el cliente indica que necesita **condiciones de pago** para poder cerrar la compra (p. ej., 30 días netos).  
- Cuando dispones de **políticas de crédito** (límites de exposición, análisis de riesgo) y puedes validar al cliente rápidamente (por ejemplo, mediante referencias, comprobantes bancarios, etc.).  
- Cuando el proyecto es **sencillo** y el coste de producción no requiere capital previo.

---

## 3. Estrategia intermedia (recomendación práctica)

1. **Solicita un depósito parcial (30‑40 % del total)** antes de iniciar o enviar la mercancía.  
   - Te da algo de liquidez y reduce el riesgo.  
   - El cliente sigue sintiendo que no está pagando todo de antemano.

2. **Define claramente los plazos de pago del resto**: 30 días desde la entrega, por ejemplo.  
   - Puedes incluir un **descuento por pronto pago** (ej. 2 % si paga en 10 días) y/o una **penalización** por retraso (ej. 1 % mensual).

3. **Utiliza mecanismos de garantía**:  
   - **Orden de compra con cláusula de crédito**,  
   - **Referencia comercial** de otro proveedor,  
   - **Cheque bancario** o **transferencia confirmada**.

4. **Comunica de forma transparente**: explica por qué pides el depósito (costes de materiales, reserva de tiempo, etc.). La mayoría de los clientes lo entiende cuando está justificado.

5. **Registra y monitorea**:  
   - En tu CRM, crea una ficha del cliente y marca la condición de “primer pedido – depósito”.  
   - Programa recordatorios automáticos (p.ej., 5 días antes del vencimiento del saldo) para evitar sorpresas.

---

## 4. Checklist rápido para decidir

| Pregunta | Sí → Considerar **adelantado/depósito** | No → Considerar **contra entrega** |
|----------|----------------------------------------|-----------------------------------|
| ¿El proyecto implica un **coste inicial alto** (material, subcontrato, reserva de capacidad)? | ✔ | |
| ¿Puedes ofrecer **descuento** atractivo a cambio del pago anticipado? | ✔ | |
| ¿El cliente **exige** condiciones de crédito? | | ✔ |
| ¿Tienes **referencias** o historial crediticio del cliente? | | ✔ |
| ¿El **valor del pedido** es bajo y el riesgo aceptable? | | ✔ |
| ¿Necesitas **liquidez inmediata** para cumplir con plazos internos? | ✔ | |
| ¿Puedes **absorber** un posible impago sin afectar tu operación? | | ✔ |

---

## 5. Conclusión

- **Para clientes totalmente desconocidos**, la opción más segura es **un depósito parcial** (o pago adelantado si el proyecto lo justifica).  
- **Si el cliente muestra resistencia** al pago anticipado, pasa a **condiciones de pago contra entrega** con plazos cortos y, si es posible, un pequeño incentivo por pago rápido.  
- La **clave está en la claridad contractual** y en establecer mecanismos de seguimiento (recordatorios, penalizaciones) desde el primer momento.

---

### Próximos pasos recomendados

1. **Prepara una cotización** que incluya:
   - Precio total.
   - Opciones de pago:  
     a) 40 % depósito + 60 % a 30 días.  
     b) 100 % a 30 días (con 2 % de descuento si paga en 10 días).  
2. **Adjunta una breve explicación** del porqué del depósito (costes de materia prima, reserva de agenda, etc.).  
3. **Solicita datos de referencia** (otro proveedor, historial bancario) para poder ofrecer la opción sin depósito si decides confiar en crédito.  
4. **Registra al cliente** en tu CRM con la etiqueta “primer pedido – condiciones de pago”.  

Con esa combinación tendrás mayor control del riesgo y, al mismo tiempo, darás al cliente la sensación de confianza que necesita para cerrar la venta. ¡Éxitos!