# LongCat 2.0 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meituan/longcat-2.0`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 51.016s | tokens_per_second: 40.1
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

De hecho, si gastas esos $10,000 en publicidad con los números actuales, no vas a escalar; vas a cavar tu propia tumba financiera. Tu plan muere en la aritmética, tal como sospechas. 

El error está en cómo calculaste el LTV (Valor de Vida del Cliente). Cometiste dos errores clásicos pero fatales: ignorar la fórmula de churn y usar ingresos brutos en lugar de margen bruto.

Vamos a autopsiar tus números y a recalcular la realidad.

### Error 1: El Churn no es lineal, es exponencial
Dices que el cliente se queda "unos 2 años". Con un churn mensual del 8%, la realidad es muy distinta. En modelos de suscripción, la vida útil promedio de un cliente se calcula como **1 / Churn**.

*   Vida útil promedio = 1 / 0.08 = **12.5 meses** (No 24 meses).
*   Cada mes pierdes al 8% de tu base, y ese 8% se calcula sobre un número cada vez más pequeño. Es un decaimiento exponencial, no una línea recta.

### Error 2: El LTV se calcula con Margen Bruto, no con Ingresos
Tu precio es de $35, pero te cuesta $10.50 (30%) servir a ese cliente. El verdadero valor que te deja un cliente es tu margen bruto ($35 × 70% = **$24.50/mes**). El LTV debe calcularse sobre la ganancia que realmente puedes reinvertir, no sobre la facturación.

### La Recálculo Real (La Aritmética que Mata tu Plan)

1.  **LTV Real:** Margen mensual × Vida útil promedio
    *   $24.50 × 12.5 meses = **$306.25**
2.  **Ratio LTV/CAC Real:** LTV Real / CAC
    *   $306.25 / $290 = **1.05x**

### ¿Qué significa un LTV/CAC de 1.05x?
La regla de oro del SaaS es que el LTV/CAC debe ser **3x o superior**. 

¿Por qué? Porque el LTV solo cubre el costo de adquisición (CAC). Con un ratio de 1.05x, de cada cliente nuevo te sobran apenas **$16.25** ($306.25 - $290). Con esos $16.