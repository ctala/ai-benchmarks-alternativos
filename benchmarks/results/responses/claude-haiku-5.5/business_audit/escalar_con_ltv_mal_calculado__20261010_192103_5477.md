# Claude Haiku 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 11.29s | tokens_per_second: 184.9
- input_tokens: 297 | output_tokens: 2088

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**No, no le daría todavía.** El cálculo tiene dos errores que cambian la conclusión.

**1. El LTV usa ingreso, no margen.** Con margen de 70%, cada cliente aporta $24,50 al mes de contribución, no $35.

**2. La vida útil no es 24 meses.** Con churn de 8% mensual, la vida promedio es 1/0,08 = **12,5 meses**, no 24. Un 8% mensual implica que el 60% de los clientes se van en el primer año.

**Recalculado:**

| Métrica | Tu cálculo | Corregido |
|---|---|---|
| Vida promedio | 24 meses | 12,5 meses |
| LTV (ingreso) | $840 | $437 |
| LTV (margen bruto) | — | **$306** |
| LTV / CAC | 2,9 | **1,06** |
| Payback del CAC | — | ~12 meses sin churn, **~35 meses con churn** |

Un LTV/CAC de 1,06 significa que, en promedio, cada cliente te devuelve apenas un poco más de lo que te costó. Antes de costos fijos, equipo, soporte y tu propio sueldo, prácticamente no generas valor por cliente.

**Qué pasa con los $10.000:**
- Compras unos 34 clientes.
- Esos clientes aportan unos $10.500 de margen en total, a lo largo de su vida.
- Ganas unos $500 en el horizonte completo, pero el dinero tarda hasta 3 años en volver. Mientras tanto, el flujo de caja queda comprometido.
- Si el CAC sube al escalar (es lo habitual, porque las primeras audiencias son las mejores), el resultado es negativo.

**Para llegar a 3x con este CAC**, necesitarías una de estas cosas:
- Churn cercano a 2,8% mensual (no 8%).
- Margen por cliente de ~$870 de vida útil, por ejemplo, subiendo precio o pasando a planes anuales.
- CAC cercano a $100.

**Lo que yo haría antes de escalar:**
1. **Atacar el churn primero.** Es la palanca más grande. Pasar de 8% a 4% duplica la vida útil y cambia todo el modelo. Revisa por qué se van (encuestas de cancelación, activación en la primera semana, onboarding).
2. **Probar precio y plan anual.** Un plan anual con descuento moderado (15–20%) reduce el churn efectivo y mejora el payback.
3. **Validar el CAC a escala pequeña.** Con $1.000–1.500 en publicidad, mide CAC real y retención por cohorte durante 2–3 meses antes de subir inversión.
4. **Regla de decisión:** escala solo cuando el payback sea menor a 12 meses ajustado por churn y LTV/CAC (con margen) sea de al menos 3.

Si me compartes cómo se distribuye el churn (¿se van en el mes 1, o después de 6 meses?) y el CAC por canal, puedo ayudarte a identificar dónde está el problema.