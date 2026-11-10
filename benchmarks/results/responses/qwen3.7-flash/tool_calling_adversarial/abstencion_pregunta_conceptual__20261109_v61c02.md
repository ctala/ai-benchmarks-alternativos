# Qwen 3.7 Flash — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 8.12 | quality: 8.5
- latency_total: 20.753s | tokens_per_second: 62.3
- input_tokens: 656 | output_tokens: 1293
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una estrategia bien estructurada y práctica para manejar pagos con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Para un cliente nuevo con el que no hay historial de confianza, **lo más recomendable es un modelo mixto**: pedir un anticipo (30%–50%) y dejar el saldo contra entrega o contra realización del servicio. Esto equilibra protección financiera y competitividad comercial.

Aquí te dejo un resumen práctico para decidir:

| Enfoque | Ventajas | Riesgos | Cuándo usarlo |
|--------|----------|---------|---------------|
| **Pago por adelantado** | Garantizas cobro, mejor flujo de caja, reduces morosidad | Puede frenar la venta o generar recelo si el cliente no te conoce | Servicios personalizados, productos hechos a medida, alta competencia por tiempo o recursos |
| **Contra entrega** | Menor fricción comercial, atrae más leads, construye confianza inicial | Riesgo real de impago o disputas, afecta tu liquidez hasta que pague | Productos estándar, valor bajo/medio, o si puedes validar previamente la solvencia del cliente |

### 🔹 Recomendación estratégica
1. **Factura sí o sí antes de entregar** (la factura es un comprobante fiscal, no define la fecha de pago). Elige un régimen de pago claro en el contrato: *“Factura emitida a fecha XX. Pago: 40% al emitir, 60% contra entrega/recepción”*.
2. **Solicita mínimo un anticipo**. Cubre costos iniciales y filtra compradores serios.
3. **Incluye cláusulas de protección**: 
   - Penalización por mora o rescisión unilateral.
   - Límites de responsabilidad mientras no se haya pagado el total.
   - Medio de pago trazable (transferencia, tarjeta, plataforma con retención).
4. **Valida brevemente al cliente** si vas a trabajar todo contra entrega: solicitud de RFC/cédula, referencia comercial simple, o uso de pasarelas de pago con confirmación inmediata.

### ⚠️ Nota operativa
Tus herramientas de sistema (`emitir_factura`, `buscar_factura`, etc.) sirven para gestionar documentos una vez decididas las condiciones comerciales. Si me indicas nombre/email del cliente o monto, puedo ayudarte a registrarlo o emitir la factura con los términos que acuerdes.

¿En qué sector operas y qué tipo de producto/servicio ofreces? Con eso afinamos la estrategia de cobro exacta para tu caso.