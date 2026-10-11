# Bonsai 2 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 471.753s | tokens_per_second: 38.1
- input_tokens: 255 | output_tokens: 17964

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



No. **No le doy $10,000 a escala con esos números.**  
Con tu aritmética actual no estás escalando; estás comprando clientes casi a breakeven, con payback largo y mucho riesgo.

## 1. El error principal: 8% churn mensual no es 2 años

Si el churn es **8% mensual**, la retención mensual es **92%**.

Vida media aproximada:

\[
\text{Vida media} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No son 24 meses.  
24 meses implicarían un churn mensual de aproximadamente **4.2%**, no 8%.

---

## 2. Tu LTV no es $840 de margen

Tu LTV de $840 es **LTV de ingresos**, no de beneficio.

Ingresos mensuales por cliente:

\[
\$35
\]

Margen bruto:

\[
70\%
\]

Beneficio bruto mensual por cliente:

\[
35 \times 0.70 = \$24.50
\]

LTV bruto con churn real:

\[
24.50 \times 12.5 = \$306.25
\]

Si cobras al final del mes, sería todavía menos, aproximadamente:

\[
24.50 \times 11.5 \approx \$282
\]

Entonces tu LTV bruto real es más bien:

\[
\textbf{~\$280 a \$310}
\]

No $840.

---

## 3. Tu LTV/CAC real no es 2.9

Con tu cálculo:

\[
840 / 290 = 2.9
\]

Pero eso usa LTV de ingresos, no de margen.

Con LTV bruto correcto:

\[
306.25 / 290 = 1.06
\]

Es decir:

\[
\textbf{LTV/CAC ≈ 1.06}
\]

Si cobras al final del mes:

\[
282 / 290 ≈ 0.97
\]

O sea: **apepado o negativo**.

Incluso si usas tu vida incorrecta de 24 meses pero aplicas el margen:

\[
35 \times 24 \times 0.70 = 588
\]

\[
588 / 290 = 2.03
\]

Aun así, no estás en 3x. Estás en ~2x.

---

## 4. El payback es el problema serio

Tu CAC es $290.  
Tu beneficio bruto mensual por cliente es $24.50.

Si no hubiera churn:

\[
290 / 24.50 = 11.8 \text{ meses}
\]

Pero con 8% churn mensual, el beneficio bruto acumulado por cliente cae:

| Meses | Beneficio bruto acumulado por cliente |
|---:|---:|
| 12 | ~$194 |
| 24 | ~$265 |
| 36 | ~$291 |

Es decir: **recuperarías el CAC alrededor de los 35 meses**, no en 12.

Eso es una señal muy mala para crecimiento.

---

## 5. ¿Qué pasa con meter $10,000 en publicidad?

Con CAC de $290:

\[
10,000 / 290 = 34.5 \text{ clientes}
\]

Beneficio bruto esperado por cliente:

\[
\$306
\]

Beneficio bruto total esperado:

\[
34.5 \times 306 \approx \$10,560
\]

Antes de descontar el tiempo, el riesgo y otros costos, te quedas con:

\[
10,560 - 10,000 = \$560
\]

O sea: **$560 de margen bruto esperado por $10,000 invertidos**.

Y eso asumiendo:

- que el CAC se mantenga a $290 al escalar,
- que el churn sea exactamente 8%,
- que no haya costo de capital,
- que no haya errores de atribución,
- que no haya saturación de publicidad,
- que no haya costos adicionales de ventas, soporte, infraestructura, etc.

Si descontas el valor del dinero en el tiempo, el resultado se vuelve negativo.

Por ejemplo:

| Tasa de descuento mensual | LTV aproximado | LTV/CAC |
|---:|---:|---:|
| 0% | $306 | 1.06 |
| 1% | $275 | 0.95 |
| 5% | $198 | 0.68 |
| 10% | $150 | 0.52 |

Con una tasa de descuento modesta de **1% mensual**, ya pierdes dinero.

---

## 6. Veredicto

No apruebo $10,000 a escala con estos números.

Tu plan actual tiene:

- **LTV bruto real ≈ $306**
- **CAC = $290**
- **LTV/CAC ≈ 1.06**
- **Payback ≈ 35 meses**
- **Margen esperado con $10k ≈ $560 antes de descuentos y riesgos**

Eso no es escala. Eso es comprar clientes casi a breakeven.

---

## 7. Para que yo le dé el $10,000, necesitaría una de estas condiciones

### Opción A: Bajar CAC

Con precio $35, margen 70% y churn 8%:

| Objetivo | CAC máximo aproximado |
|---|---:|
| Breakeven sin descuento | ~$306 |
| Payback en 12 meses | ~$194 |
| LTV/CAC = 3x | ~$102 |

Si quieres escalar fuerte, no debería estar a $290.  
Debería estar mucho más cerca de **$100 o menos**.

---

### Opción B: Bajar churn

Para tener LTV/CAC = 3x con CAC de $290, precio $35 y margen 70%, necesitarías:

\[
\text{churn mensual} \leq 2.8\%
\]

No 8%.

Eso es una mejora enorme.

---

### Opción C: Subir precio o margen

Con churn de 8% y CAC de $290:

| Objetivo | Precio mensual aproximado con 70% margen |
|---|---:|
| Payback en 12 meses | ~$53 |
| LTV/CAC = 3x | ~$99 |

Si puedes subir el precio a ~$100/mes o mejorar el margen, cambia la historia.

---

## 8. Recomendación

No metas $10,000 a escala.

Haz un test pequeño:

- $1,000 a $2,000
- 5 a 10 clientes
- midiendo CAC real
- churn a 3, 6 y 12 meses
- payback por cohorte

Kill criteria:

- Si CAC > $100, no es escala.
- Si el beneficio bruto acumulado a 12 meses < CAC, no es escala.
- Si churn > 8%, no es escala.
- Si payback > 12 meses, no es escala.

Si con el test demuestras que puedes bajar CAC a ~$100, o subir churn a ~3%, o subir precio a ~$100, entonces sí podemos hablar de escalar.

**Con los números que diste: no le doy.**