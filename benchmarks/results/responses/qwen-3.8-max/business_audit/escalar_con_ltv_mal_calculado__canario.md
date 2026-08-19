# Qwen 3.8 Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.88 | quality: 10.0
- latency_total: 265.038s | tokens_per_second: 48.2
- input_tokens: 255 | output_tokens: 12763

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

No. **No le doy con esos números.** Y menos $10.000 de golpe.

Tu conclusión de “LTV/CAC ~2,9, así que voy” tiene dos errores grandes:

1. **Estás usando ingresos, no margen**, para pagar el CAC.  
2. **Con 8% de churn mensual, la vida esperada no es 24 meses.**

Recalculando:

---

## 1. Vida esperada real con 8% de churn mensual

Si el churn mensual es 8%, la vida esperada aproximada de un cliente es:

\[
\text{Vida esperada} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Además, con 8% mensual, la probabilidad de que un cliente siga vivo después de 24 meses es:

\[
0.92^{24} \approx 13.5\%
\]

Es decir, después de 2 años solo queda vivo ~13% de la cohorte. Eso no es una base de clientes que “se queda 2 años” en promedio.

Si tus clientes de verdad se quedan 24 meses en promedio, tu churn mensual efectivo debería ser mucho más bajo, alrededor de 4,2%, no 8%.

---

## 2. LTV correcto: usa margen bruto, no ingresos

Precio mensual: $35  
Margen bruto: 70%  
Contribución bruta mensual por cliente:

\[
35 \times 0.70 = 24.5
\]

Con churn mensual de 8%, el LTV de contribución bruta es:

\[
LTV = \frac{24.5}{0.08} = 306.25
\]

Entonces:

\[
LTV/CAC = \frac{306.25}{290} = 1.06
\]

Eso no está cerca de 3. Está apenas por encima de 1.

Si lo haces sobre ingresos, que es menos correcto porque el CAC se paga con margen, el cálculo sería:

\[
LTV_{ingresos} = \frac{35}{0.08} = 437.5
\]

\[
LTV/CAC = \frac{437.5}{290} = 1.51
\]

Tampoco da.

---

## 3. Incluso tu supuesto de 2 años está mal usado

Si aceptáramos temporalmente que el cliente dura 24 meses, tu LTV de ingresos sería:

\[
35 \times 24 = 840
\]

Pero el LTV de margen sería:

\[
35 \times 0.70 \times 24 = 588
\]

Con CAC de $290:

\[
LTV/CAC = \frac{588}{290} = 2.03
\]

Seguiría por debajo de 3.

Y además, con churn del 8%, el LTV esperado en 24 meses no es $588 de margen, sino aproximadamente:

\[
24.5 \times \frac{1 - 0.92^{24}}{0.08}
\]

\[
\approx 24.5 \times 10.81 = 264.9
\]

Es decir, después de 24 meses, la contribución bruta esperada por cliente ni siquiera cubre completamente el CAC de $290.

---

## 4. ¿Qué pasa si metes $10.000 en publicidad?

Con CAC de $290:

\[
\frac{10.000}{290} \approx 34.5 \text{ clientes}
\]

MRR inicial aproximado:

\[
34.5 \times 35 = 1.207
\]

Contribución bruta mensual inicial:

\[
34.5 \times 24.5 = 845
\]

O sea, metes $10.000 hoy y recibes aproximadamente $845 de contribución bruta el primer mes.

El LTV total esperado de esa cohorte sería:

\[
34.5 \times 306.25 \approx 10.560
\]

Entonces, en el mejor caso teórico, la ganancia bruta después de recuperar el CAC sería:

\[
10.560 - 10.000 = 560
\]

Eso es ~5,6% de retorno sobre el gasto publicitario, antes de:

- costos fijos,
- soporte,
- devoluciones,
- impuestos,
- costo financiero,
- errores de atribución,
- aumento del CAC al escalar,
- cualquier costo variable adicional.

Es una economía demasiado frágil.

---

## 5. Payback: tardas demasiado en recuperar el dinero

Payback simple, ignorando churn:

\[
\frac{290}{24.5} = 11.8 \text{ meses}
\]

Eso ya es largo.

Pero con churn del 8%, la recuperación real de caja es peor, porque muchos clientes se van antes de pagar el CAC.

Aproximadamente, con esta cohorte:

| Periodo | Contribución bruta acumulada aproximada |
|---|---:|
| Mes 1 | $845 |
| Mes 3 | $2.300 |
| Mes 6 | $4.200 |
| Mes 12 | $6.700 |
| Mes 24 | $9.100 |
| LTV total esperado | $10.560 |

Es decir, después de 12 meses todavía no recuperaste ni el 70% del gasto. Después de 24 meses, aún no recuperaste todo.

Para escalar con publicidad pagada, necesitas recuperar el CAC mucho más rápido.

---

## 6. El problema no es crecer; es que la unidad económica no aguanta el CAC

Con los números actuales:

- Precio: $35/mes
- Margen bruto: 70%
- Contribución mensual: $24.50
- Churn: 8% mensual
- CAC: $290

El CAC máximo que podrías pagar para tener LTV/CAC de 3 sería:

\[
CAC_{max} = \frac{LTV}{3}
\]

\[
CAC_{max} = \frac{306.25}{3} = 102.08
\]

Es decir, para que estos números funcionen bien, tu CAC debería ser cercano a **$100**, no $290.

O, manteniendo CAC de $290, para tener LTV/CAC de 3 necesitarías:

### Opción A: bajar el churn

\[
\frac{24.5}{churn} \geq 3 \times 290
\]

\[
churn \leq \frac{24.5}{870} = 2.8\%
\]

Necesitarías churn mensual menor a 2,8%.

### Opción B: subir la contribución mensual

\[
\frac{contribución}{0.08} \geq 870
\]

\[
contribución \geq 69.6
\]

Con margen del 70%, eso implicaría un precio aproximado de:

\[
\frac{69.6}{0.70} \approx 99.4
\]

Es decir, necesitarías cobrar cerca de $100/mes, no $35/mes.

---

## 7. Si el negocio ya es rentable, cuidado con confundir rentabilidad actual con escalar rentablemente

Puedes ser rentable hoy por clientes orgánicos, por referidos, por un CAC bajo histórico o por una base antigua con mejor retención.

Pero si el CAC marginal pagado es $290 y el LTV marginal de contribución es $306, cada cliente nuevo adquirido con publicidad deja apenas ~$16 de contribución neta antes de todo lo demás.

Eso no es escalar rentablemente. Es comprar ingresos casi al costo.

---

## 8. Mi recomendación práctica

**No metas $10.000 este mes.**

Primero arregla una de estas tres palancas:

1. **Reducir churn**  
   Necesitas bajarlo de 8% a menos de 3% para justificar ese CAC con el precio actual.

2. **Reducir CAC**  
   Necesitas bajar el CAC pagado de $290 a alrededor de $100-$110.

3. **Subir precio o margen**  
   Con $35/mes y 70% de margen, el modelo no soporta $290 de CAC.

Si quieres hacer una prueba, no hagas una apuesta de $10.000. Haz una prueba pequeña, por ejemplo $1.000-$2.000, y mide:

- CAC real marginal, no mezclado con orgánico.
- Retención a 30, 60 y 90 días.
- Churn real por cohorte.
- Contribución bruta después de soporte, devoluciones y costos variables.
- Payback real.
- Si el CAC sube al aumentar gasto.

Yo aprobaría escalar solo si ves algo como:

- LTV/CAC ≥ 3 usando contribución bruta, no ingresos.
- Payback ≤ 6 meses.
- Churn mensual ≤ 3%-4%.
- CAC marginal estable o decreciente.
- Caja suficiente para financiar el payback.

Con tus números actuales, la respuesta es:

**No. No le des. Con churn de 8%, precio de $35 y CAC de $290, la unit economics no aguanta un escalado fuerte con publicidad pagada.**