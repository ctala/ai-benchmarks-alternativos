# Nemotron 3 Nano 30B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.28 | quality: 8.5
- latency_total: 6.846s | tokens_per_second: 195.7
- input_tokens: 740 | output_tokens: 1340
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para manejar pagos con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Cuando trabajas con un cliente que es completamente nuevo y no tienes historial de pagos, lo más seguro suele ser **exigir alguna forma de garantía antes de entregar el producto o servicio**. Aquí tienes algunas opciones y consideraciones para decidir entre facturación por adelantado o contra‑entrega:

| Opción | Ventajas | Riesgos / Desventajas |
|--------|----------|----------------------|
| **Factura por adelantado (pago antes de la entrega)** | - Recibes el dinero antes de invertir tiempo o recursos.<br>- Reduce el riesgo de impago.<br>- Puedes usar ese efectivo para cubrir costos de producción. | - El cliente puede percibirlo como menos confianza o flexibilidad.<br>- Puede desistir si prefiere pagar después de ver el producto. |
| **Contra‑entrega (pago al recibir)** | - Pago inmediato al momento de la entrega, lo que garantiza el cobro.<br>- Es familiar para muchos compradores nuevos.<br>- Puedes combinarlo con un pequeño adelanto si el cliente lo solicita. | - Asumes el riesgo de que el cliente rechace el producto una vez recibido.<br>- Puede generar mayores costos de logística inversa si hay devoluciones. |
| **Deuda parcial + adelanto** (p.ej., 30 % al ordenar y 70 % a la entrega) | - Equilibrio entre riesgo y confianza.<br>- El cliente se siente parte del proceso y tiene “compromiso”. | - Necesita una gestión más cuidadosa de los cobros y los plazos. |

### Recomendación práctica

1. **Evalúa el tamaño y el tipo de pedido.**  
   - Pedidos pequeños o de bajo margen suelen manejarse mejor con pago al recibir.  
   - Pedidos grandes o con costos de producción significativos pueden justificar un adelanto o depósito.

2. **Establece términos claros desde el inicio.**  
   - Inclúyelos en el contrato o en la orden de compra: “30 % de anticipo, 70 % al recibir”.  
   - Señala las consecuencias de una posible cancelación o devolución.

3. **Verifica la identidad y la referencia del cliente.**  
   - Incluso si el cliente es nuevo, puedes comprobar datos básicos (email, nombre, historial de compras en tu base) usando la herramienta `buscar_cliente`. Si dispones del nombre o email, podemos buscar su registro y ver si ya tiene alguna facturación pendiente o historial de pagos.  
   - (Si decides hacerlo, compártenos el nombre o email y te ayudamos a obtener su perfil.)

4. **Empieza con una prueba piloto.**  
   - Para los primeros pedidos, propone un **pago parcial** (por ejemplo, 20 % al ordenar y el resto a la entrega). Esto te permite validar la relación sin asumir todo el riesgo.

### Herramientas a tu disposición

- **`buscar_cliente`**: Si te llegas a conocer el nombre o email del cliente nuevo, podemos buscar su registro en el CRM y confirmar si ya tiene alguna relación previa (por ejemplo, una cuenta activa, historial de impagos, etc.).  
- **`emitir_factura`** y **`enviar_recordatorio_pago`**: Una vez que la relación esté establecida y se acuerde el método de pago, podemos crear la factura o recordar al cliente los vencimientos de forma oportuna.

### Conclusión

Para **clientes totalmente desconocidos**, la práctica más recomendada es **exigir alguna garantía inicial**—ya sea un anticipo, un pago contra entrega, o una combinación de ambos—para proteger tu negocio. A medida que vayas construyendo confianza y conozcas más el historial de pagos del cliente, puedes flexibilizar esas condiciones.

Si te resulta útil, comparte el nombre o email de este nuevo cliente y te ayudo a buscar su información en el CRM antes de decidir los términos de facturación. ¡Estoy aquí para ayudarte en cada paso!