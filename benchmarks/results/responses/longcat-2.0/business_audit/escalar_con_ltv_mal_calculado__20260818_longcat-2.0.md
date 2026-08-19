# LongCat 2.0 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meituan/longcat-2.0`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 47.885s | tokens_per_second: 42.8
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

**Respuesta corta: No le doy. Ni un centavo.**

Tu plan muere en la aritmética. Has cometido dos errores clásicos y fatales al calcular tu unit economics: has ignorado la fórmula real del churn y has calculado el LTV sobre ingresos brutos en lugar de sobre margen bruto. 

Vamos a desglosar por qué tu crecimiento te llevaría a la quiebra.

### Error 1: La ilusión de los "2 años de vida"
Dices que el cliente se queda 2 años porque asumes que el churn es lineal. El churn mensual **nunca** es lineal; es exponencial. Si pierdes el 8% de tus clientes cada mes, la vida útil promedio de tu cliente no es de 24 meses.

La fórmula real de la vida útil (Lifetime) es: **1 / Churn mensual**.
*   Tu churn: 8% (0.08)
*   Vida útil real: 1 / 0.08 = **12.5 meses**.

Cada mes que pasa, el 8% de los que quedan se va. Al año, te quedas con el 36% de tus clientes iniciales. A los 2 años, apenas te queda un 13%. Asumir 24 meses es una fantasía.

### Error 2: LTV sobre ingresos vs. LTV sobre margen
El LTV (Valor de Vida del Cliente) debe calcularse sobre la ganancia que realmente te queda después de pagar la infraestructura y el procesador de pagos, no sobre el precio de venta.

*   Ingreso por mes: $35
*   Margen bruto: 70%
*   **Ganancia real por mes: $35 × 0.70 = $24.50**

---

### La realidad de tus números (La autopsia)

Ahora, recalculamos con las matemáticas correctas:

1.  **LTV real:** Ganancia mensual × Vida útil
    *   $24.50 × 12.5 meses = **$306.25**
2.  **Ratio LTV/CAC:** LTV real / CAC
    *  