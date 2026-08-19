# LongCat 2.0 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meituan/longcat-2.0`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 47.82s | tokens_per_second: 42.8
- input_tokens: 221 | output_tokens: 2048

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

**No le doy luz verde.** 

Su plan muere en la aritmética, tal como temía. Usted ha cometido dos errores clásicos pero fatales al calcular el LTV (Valor de Vida del Cliente): **ignoró el churn en la esperanza de vida** e **ignoró el margen bruto**. 

Vamos a desarmar sus números y a poner los reales sobre la mesa.

### El error en su cálculo
Usted asumió que un cliente dura 24 meses (2 años). Con un churn mensual del 8%, la realidad es muy distinta. La fórmula para calcular la vida útil promedio de un cliente es `1 / Churn`. 

*   **Vida útil real:** 1 / 0.08 = **12.5 meses** (No 24).
*   **Ingreso real por cliente:** Usted cobra $35, pero su margen bruto es del 70%. El LTV debe calcularse sobre la ganancia, no sobre el ingreso, porque el 30% restante se lo come la infraestructura y los procesadores de pago. 
*   **Ganancia mensual real:** $35 × 0.70 = **$24.50**.

### La aritmética real
Ahora, recalculamos el LTV con los números correctos:

*   **LTV (Ganancia):** $24.50 (ganancia mensual) × 12.5 meses (vida útil) = **$306.25**
*   **CAC:** $290
*   **Ratio LTV/CAC real:** $306.25 / $290 = **1.05**

Usted tenía un ratio de 2.9; el realidad es de **1.05**. 

### ¿Por qué un ratio de 1.05 es una trampa mortal?
Un ratio de 1.05 significa que por cada dólar que invierte en publicidad, recupera $1.05 casi un año después. Pero el problema no es solo la rentabilidad, es el **flujo de caja (cash flow)**.

Calculemos el **Periodo de Recuperación del CAC (Payback Period)**:
*   CAC ($290) / Ganancia Mensual ($24.50) = **1