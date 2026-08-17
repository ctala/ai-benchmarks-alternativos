# Nex-N2-Mini — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 41.208s | tokens_per_second: 194.5
- input_tokens: 216 | output_tokens: 8015

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

**No. No le daría $10.000 en publicidad con esos números.**

Tu cálculo tiene dos problemas grandes:

### 1. 8% de churn mensual no equivale a 2 años

Si el churn mensual es 8%, la vida media esperada es:

\[
1 / 0.08 = 12.5 \text{ meses}
\]

No 24 meses. En 24 meses, solo quedaría aproximadamente:

\[
0.92^{24} \approx 15\%
\]

de los clientes originales.

### 2. El LTV debe calcularse sobre margen bruto, no sobre ingresos

Tienes:

- ARPU: $35/mes
- Margen bruto: 70%
- Margen bruto por cliente/mes:

\[
35 \times 0.70 = 24.5
\]

Entonces:

\[
LTV = 24.5 \times 12.5 = 306.25
\]

Y contra un CAC de $290:

\[
LTV/CAC = 306.25 / 290 = 1.06
\]

Eso no es 3. Es casi punto y raya.

### CAC payback

\[
290 / 24.5 = 11.8 \text{ meses}
\]

Tu cliente tarda casi un año en recuperar el CAC. Pero su vida media esperada es solo 12.5 meses. Es decir: casi todo el valor del cliente se va en recuperar el CAC.

### Incluso usando tu supuesto de 24 meses

Si ignoras el churn y usas 24 meses:

\[
35 \times 0.70 \times 24 = 588
\]

\[
LTV/CAC = 588 / 290 = 2.03
\]

Aún así, no llega a 3.

---

## Qué tendría que cambiar

Para tener **LTV/CAC = 3** con CAC de $290, necesitas un LTV de:

\[
290 \times 3 = 870
\]

Con tu precio y margen actuales, eso requiere:

- Vida media de al menos **35.5 meses**
- O churn mensual de máximo **~2.8%**
- O CAC máximo de **~$102**
- O subir el precio a cerca de **$99/mes** si el churn no baja

---

## Decisión

**No apruebo $10.000 en publicidad pagada todavía.**

Si quieres hacer una prueba, haría un test pequeño y acotado, por ejemplo $1.000–$3.000, con criterios claros de salida:

- CAC marginal real
- Payback menor a 6–9 meses
- Retención D30/D60 saludable
- LTV/CAC proyectado mayor a 3
- Churn no deteriorándose

Pero con CAC de $290 y churn mensual de 8%, **escalar fuerte en paid sería aritméticamente peligroso**.