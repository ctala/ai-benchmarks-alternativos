# Nemotron 3 Nano 30B — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.07 | quality: 8.5
- latency_total: 14.159s | tokens_per_second: 88.4
- input_tokens: 740 | output_tokens: 1251
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía completa y práctica para manejar pagos con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa


Cuando se trabaja con un cliente que **no conoces** y es la primera relación comercial, el riesgo de impago o de malentendidos suele ser mayor. Por eso, la práctica más segura suele ser **facturar por adelantado** (o al menos solicitar un depósito) hasta que se haya establecido confianza y se conozca el historial de pago del cliente.  

### Ventajas de facturar por adelantado  
1. **Reduce el riesgo de insolvencia**: el importe ya está en tu caja antes de iniciar el trabajo.  
2. **Mejora tu flujo de caja**: puedes planificar gastos e inversiones sin depender del pago futuro.  
3. **Facilita la evaluación del cliente**: al recibir el pago inicial, puedes validar que el cliente está dispuesto a cumplir con sus obligaciones.  

### Cuándo considerar **contra entrega** (pago al recibir el producto/servicio)  
- **Productos físicos de bajo valor o con bajo riesgo**: si entregas un bien tangible y el cliente lo recibe inmediatamente, el pago contra entrega puede ser aceptable.  
- **Clientes con reputación sólida o referidos**: si alguien de confianza los recomienda, el riesgo disminuye.  
- **Operaciones muy específicas** donde el cliente insiste en esta modalidad y tú estás cómodo con la gestión logística.  

### Buenas prácticas recomendadas para clientes nuevos  
| Paso | Qué hacer | Por qué |
|------|-----------|----------|
| 1. **Validar la información del cliente** | Usar la herramienta `buscar_cliente` (con nombre o email) para obtener su historial y estado de cuenta si dispones de datos. | Detectar posibles alertas o antecedentes antes de establecer condiciones. |
| 2. **Establecer un límite de crédito inicial bajo** | Ofrece un **pago parcial** (ej. 30‑50 % adelantado) o un **depósito** antes de iniciar el trabajo. | Garantiza compromiso y cubre costos iniciales. |
| 3. **Definir claramente los términos de pago** | Incluye en la propuesta: “Pago del 50 % al iniciar el proyecto y el resto a la entrega”. | Evita malentendidos y sirve como referencia contractual. |
| 4. **Utilizar facturación electrónica** | Con `emitir_factura` puedes crear y enviar la factura al cliente de forma automática. | Mantienes trazabilidad y profesionalismo. |
| 5. **Monitorear el pago** | Si el cliente se atrasa, podrías enviar un recordatorio con `enviar_recordatorio_pago`. | Refuerza la disciplina de pago sin necesidad de iniciar procedimientos de cobranza. |
| 6. **Revisar la relación después de la primera transacción** | Si el cliente cumple puntualmente, puedes considerar ampliar el crédito en futuras facturas. | Construye confianza para operaciones posteriores. |

### Resumen rápido  
- **Para un cliente desconocido**: factura por adelantado o exige un depósito inicial.  
- **Contra entrega**: solo es viable si el producto/servicio se entrega al momento y el riesgo de impago es bajo.  
- **Comunicación clara**: indica siempre los plazos y modalidades de pago en la propuesta y en la factura.  
- **Herramientas a tu disposición**: puedes buscar datos del cliente con `buscar_cliente`, emitir la factura con `emitir_factura` y, si fuese necesario, enviar recordatorios con `enviar_recordatorio_pago`.  

En conclusión, **facturar por adelantado** es la opción más segura al iniciar con un cliente nuevo y desconocido; la contra entrega puede explorarse más adelante, una vez que exista historial de pagos cumplidos y se haya construido confianza mutua. Si lo deseas, podemos buscar información del cliente antes de crear la primera factura—solo indícame el nombre o email para usar `buscar_cliente`.