# Qwen 3.8 Max 0902 — tool_calling_adversarial/abstencion_pregunta_conceptual

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.25 | quality: 8.5
- latency_total: 32.964s | tokens_per_second: 36.9
- input_tokens: 703 | output_tokens: 1217
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando una guía detallada y práctica sobre la gestión de pagos con clientes nuevos.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Me conviene facturar por adelantado o contra entrega cuando el cliente es nuevo y no lo conozco?


## Respuesta completa

Buena pregunta, y la respuesta corta es: **con un cliente nuevo, casi nunca conviene elegir entre los dos extremos — lo estándar es un híbrido.**

## El riesgo real de cada opción

**Contra entrega (crédito)**
- Pros: menos fricción comercial, cierras más rápido, es lo esperado en B2B.
- Contras: ya ejecutaste el costo (materiales, horas, envío) y quedas expuesto al impago. Cobrar después cuesta tiempo, relación y a veces dinero.
- Regla práctica: **no otorgues más crédito del que estarías dispuesto a perder** sin que te duela, ni más del costo variable del trabajo.

**Por adelantado (prepago)**
- Pros: riesgo de impago prácticamente cero, validas que el cliente es serio y tiene liquidez.
- Contras: puede enfriar la venta, y en muchos países **emitir la factura adelanta la obligación fiscal (IVA)** aunque no hayas cobrado todavía. Consúltalo según tu jurisdicción.

## Lo que recomiendo para cliente desconocido

1. **Anticipo del 30–50% + saldo contra entrega.** Cubre tu costo variable y deja el margen en riesgo compartido. Es lo más aceptado comercialmente.
2. **Escala el crédito con historial:** primera operación con anticipo → 2 o 3 pagos limpios → abres condiciones a 30 días → subes el monto progresivamente.
3. **Si el trabajo es a medida o irreversible** (producto personalizado, desarrollo específico, algo que no puedes revender): exige anticipo alto o prepago total. No fabriques sobre crédito sin conocer al pagador.
4. **Si el producto es estándar y reventas fácil:** puedes ser más flexible, porque el riesgo es menor.
5. **Documenta siempre:** condiciones de pago y recargos por mora escritos en la factura, orden de compra si es empresa, y datos fiscales verificados.
6. **Montos chicos:** a veces el costo de negociar un anticipo supera el beneficio. Ahí cobra por adelantado sin discutir, o simplemente absorbe el riesgo si el importe es marginal.

## Un apunte operativo de este sistema

Ten en cuenta que `emitir_factura` es **irreversible y tiene efecto contable**: no emitas la factura "para probar" o antes de tener el acuerdo de pago cerrado. Si el cliente se echa atrás, te queda un documento que anular. Para apurar un cobro ya facturado, lo correcto es `enviar_recordatorio_pago` (amable o firme), no volver a facturar.

---

Si me das el **nombre o email del cliente**, lo busco en el CRM y te digo su estado de cuenta — eso puede cambiar la recomendación (un cliente "nuevo" para ti puede ya tener historial registrado).