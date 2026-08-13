# Tencent Hy3 — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `tencent/hy3`
- success: True  | final: 7.74 | quality: 8.5
- latency_total: 28.748s | tokens_per_second: 41.8
- input_tokens: 621 | output_tokens: 1203
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para gestionar el riesgo de pago con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Esta es una excelente pregunta de gestión de riesgo comercial. Te respondo con criterio general y buenas prácticas, ya que no me has dado un cliente específico para consultar:

## Recomendación para clientes nuevos

**Lo más prudente es facturar por adelantado (o exigir un anticipo significativo)** cuando el cliente es nuevo y no tienes referencias de su comportamiento de pago. Razones:

- **Riesgo cero de impago:** No entregas producto/servicio sin haber cobrado.
- **Filtro de seriedad:** Los clientes ficticios o sin intención real de pagar suelen desertar ante el pago previo.
- **Flujo de caja sano:** Recibes el dinero antes de incurrir en costos de entrega.

## Opciones según tu modelo de negocio

| Modalidad | Cuándo sí conviene | Riesgo |
|-----------|-------------------|--------|
| **100% por adelantado** | Productos digitales, servicios pequeños, ventas online | Mínimo |
| **Anticipo + saldo contra entrega** (ej. 50/50) | Servicios medianos, proyectos con costos de materiales | Bajo |
| **Contra entrega** | Solo si la entrega es física y verificable en el acto (ej. mensajería con cobro) | Medio |
| **Crédito (facturar y cobrar después)** | Nunca para desconocidos sin aval o referencias | Alto |

## Cómo reducir el riesgo si debes facturar contra entrega

Si tu modelo te obliga a entregar primero, antes de emitir la factura puedes usar la herramienta **buscar_cliente** para verificar si, aunque sea "nuevo", ya tiene algún registro en el CRM (un contacto previo, un lead, un estado de cuenta inicial). Eso te da señales tempranas.

Si decides avanzar con un cliente nuevo, mi sugerencia operativa es:
1. Usa `buscar_cliente` para confirmar identidad y datos.
2. Emite la factura con `emitir_factura` solo por el **anticipo** (si aplica).
3. Una vez cobrado y entregado, facturas el saldo o cierras la operación.

---

**En resumen:** Para desconocidos, **por adelantado es la regla**. El crédito se gana con historial. Si me das el nombre o email de un cliente concreto, puedo verificar su situación en el CRM antes de que decidas qué hacer.

¿Quieres que consulte a algún cliente específico o necesitas ayuda para estructurar una factura de anticipo?