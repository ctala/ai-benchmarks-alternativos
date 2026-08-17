# DeepSeek V4 Pro (0813) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 27.581s | tokens_per_second: 92.8
- input_tokens: 202 | output_tokens: 2559

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

No le doy. Tus números, recalculados, muestran que escalar con publicidad pagada en estas condiciones destruiría valor. Aquí está el detalle:

---

### 1. Tu error principal: la vida media del cliente

Con **churn mensual del 8%**, la vida media de un cliente no es 2 años.  
La fórmula correcta es:

\[
\text{Vida media (meses)} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

Eso es **1 año y medio, no 2 años**. Y como el churn es compuesto, a los 12 meses solo queda el 36.8% de los clientes.

---

### 2. El LTV debe calcularse con margen bruto, no con ingreso total

Tu margen bruto es 70%, así que la contribución mensual real por cliente es:

\[
\$35 \times 70\% = \$24.5 \text{ por mes}
\]

El LTV correcto (sin descontar flujos futuros) es:

\[
\text{LTV} = \frac{\$24.5}{0.08} = \$306.25
\]

No \$840.

---

### 3. LTV/CAC real

\[
\text{LTV/CAC} = \frac{\$306.25}{\$290} = 1.06
\]

Está **muy por debajo de 3**. Apenas cubre el CAC, dejando solo \$16.25 de valor neto por cliente. Eso no es escalable.

---

### 4. Payback period (tiempo para recuperar el CAC)

\[
\text{Payback} = \frac{\$290}{\$24.5} = 11.8 \text{ meses}
\]

Casi un año para recuperar la inversión. Con un churn mensual del 8%, muchos clientes se van antes de que recuperes el CAC. De hecho, a 12 meses el ingreso acumulado esperado por cliente es:

\[
\$24.5 \times \sum_{t=0}^{11} 0.92^t = \$193.55
\]

Eso es **menor que el CAC de \$290**. Es decir, en el primer año pierdes dinero con cada cliente.

---

### 5. El churn es insostenible

Un churn mensual del 8% equivale a un churn anual de:

\[
1 - (0.92)^{12} = 63.2\%
\]

Pierdes más de la mitad de tus clientes cada año. Antes de escalar, debes reducir ese churn a al menos 3–4% mensual.

---

### 6. ¿Qué pasaría con \$10,000 en publicidad?

Con CAC de \$290, adquirirías ~34 clientes.  
Valor neto total esperado: \(34 \times (\$306.25 - \$290) = \$552.5\).  
Pero el flujo de caja sería negativo durante meses, y el retorno es mínimo.

---

### Recomendación

**No escales con publicidad pagada todavía.** Primero arregla las unit economics:

- **Reduce el churn** a <4% mensual (idealmente 2–3%).
- **Aumenta el precio** o el margen bruto.
- **Optimiza el CAC** (mejora anuncios, landing, prueba orgánico/referidos).
- Apunta a un **LTV/CAC > 3** y un **payback < 6–12 meses**.

Una vez que logres eso, escalar con publicidad tendrá sentido. Hoy, meter \$10,000 en ads es quemar dinero.