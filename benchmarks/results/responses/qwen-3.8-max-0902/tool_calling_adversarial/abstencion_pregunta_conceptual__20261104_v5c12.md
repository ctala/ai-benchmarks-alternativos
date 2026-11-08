# Qwen 3.8 Max 0902 — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.18 | quality: 8.5
- latency_total: 26.491s | tokens_per_second: 27.6
- input_tokens: 703 | output_tokens: 731
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía detallada y práctica para manejar situaciones de facturación con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Buena pregunta, y es justo el tipo de decisión que conviene resolver **antes** de emitir nada, porque la emisión de factura en el CRM es irreversible y tiene efecto contable.

## Respuesta corta
Con un cliente nuevo y sin historial, **facturar por adelantado (o con anticipo) es lo más seguro**. Facturar contra entrega solo tiene sentido si ya verificaste al cliente o si el monto es bajo.

## Por qué

| Factor | Por adelantado | Contra entrega |
|---|---|---|
| Riesgo de impago | Bajo | Alto (ya entregaste el valor) |
| Costo de cobranza | Nulo | Alto y lento |
| Flujo de caja | Positivo | Negativo (financias al cliente) |
| Fricción comercial | Puede frenar la venta | Facilita cerrar |
| Palanca de negociación | Tú la tienes | La tiene el cliente |

La clave es la **asimetría**: si facturas contra entrega y no te pagan, ya perdiste el producto/servicio *y* tienes que gastar tiempo en cobrar. Si facturas por adelantado y el cliente se echa para atrás, solo perdiste una oportunidad, no un activo.

## Lo que yo haría en la práctica

1. **Investiga antes de decidir.** Pídeme que busque al cliente en el CRM por nombre o email: ahí sale su estado de cuenta y puedes ver si ya hay antecedentes de morosidad.
2. **Usa el punto medio si hay resistencia comercial:** un **anticipo del 50%** y el saldo contra entrega. Cubre tu costo y mantiene al cliente motivado a cerrar.
3. **Ajusta según el monto:**
   - Monto bajo → contra entrega puede ser aceptable (el costo de cobrar supera el beneficio).
   - Monto alto o trabajo a medida (que no puedes revender a otro) → siempre por adelantado.
4. **Pide referencias o datos fiscales completos** cuando sea la primera operación. Es una señal de formalidad de ambas partes.
5. **Establece condiciones explícitas** en el concepto de la factura: fecha de vencimiento y si aplica mora. Después, si se atrasa, puedo enviar recordatorios (tono amable primero, firme después) sin necesidad de emitir documentos nuevos.

## Regla general
> A mayor desconocimiento del cliente, mayor anticipo. A mayor historial de pagos cumplidos, mayor flexibilidad.

Si me das el nombre o email del cliente, lo busco en el CRM y te digo qué estado de cuenta tiene para decidir con datos en lugar de intuición.