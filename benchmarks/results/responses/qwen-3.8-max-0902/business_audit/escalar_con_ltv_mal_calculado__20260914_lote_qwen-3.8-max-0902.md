# Qwen 3.8 Max 0902 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 327.352s | tokens_per_second: 40.8
- input_tokens: 255 | output_tokens: 13368

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

No. **Todavía no.** Con esos números, meter $10.000 en publicidad no es escalar rentablemente; es comprar ingresos casi a precio de costo y asumir mucho riesgo de caja.

Tu cálculo tiene varios problemas.

---

## 1. Con 8% de churn mensual, la vida media no es 24 meses

Si el churn mensual es 8%, la vida esperada de un cliente, en un modelo simple, es:

\[
\text{Vida esperada} = \frac{1}{churn} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Además, con 8% mensual:

- Retención a 12 meses: \(0.92^{12} \approx 36.8\%\)
- Retención a 24 meses: \(0.92^{24} \approx 13.5\%\)

Entonces, asumir 24 meses de permanencia con 8% de churn mensual es demasiado optimista.

Si tu cliente realmente se queda 24 meses en promedio, entonces tu churn mensual no es 8%; sería más cercano a 4% mensual. Pero con los datos que diste, hay que usar 12.5 meses.

---

## 2. El LTV no se calcula con ingresos completos, sino con margen bruto

Tu precio es $35/mes, pero tu margen bruto es 70%.

Entonces, cada cliente deja:

\[
35 \times 0.70 = \$24.50/mes
\]

de ganancia bruta.

El LTV correcto, usando margen bruto y churn de 8%, es:

\[
LTV_{bruto} = \frac{24.50}{0.08} = \$306.25
\]

No $840.

---

## 3. Tu LTV/CAC real es mucho más bajo

Tu CAC es $290.

Entonces:

\[
LTV/CAC = \frac{306.25}{290} = 1.06
\]

Eso está muy lejos de 3.

Incluso si miráramos el LTV sobre ingresos, que no es lo correcto para decidir publicidad, sería:

\[
LTV_{ingresos} = \frac{35}{0.08} = \$437.50
\]

\[
LTV/CAC = \frac{437.50}{290} = 1.51
\]

Tampoco da.

Y si insistieras en usar 24 meses, que no es consistente con 8% de churn, el LTV bruto sería:

\[
35 \times 24 \times 0.70 = \$588
\]

\[
LTV/CAC = \frac{588}{290} = 2.03
\]

Seguiría por debajo de 3.

---

## 4. El problema de caja es serio

Con $10.000 de publicidad y CAC de $290, traerías aproximadamente:

\[
\frac{10.000}{290} \approx 34.5 \text{ clientes}
\]

El LTV bruto total esperado de esos clientes sería:

\[
34.5 \times 306.25 \approx \$10.560
\]

Después de recuperar el CAC, la ganancia bruta esperada sería:

\[
10.560 - 10.000 = \$560
\]

Sí: **$10.000 hoy para ganar aproximadamente $560 de utilidad bruta futura**, antes de gastos fijos, antes de impuestos, antes de errores, antes de aumentos de CAC y antes de descuento financiero.

Eso es demasiado delgado.

---

## 5. El payback es demasiado largo

El payback simple, sin considerar churn, sería:

\[
\frac{290}{24.50} \approx 11.8 \text{ meses}
\]

Pero eso ignora que cada mes se te va 8% de la base.

Con churn de 8%, la recuperación esperada por cohorte se estira mucho más.

La ganancia bruta acumulada esperada por cliente después de \(n\) meses es:

\[
24.50 \times \frac{1 - 0.92^n}{0.08}
\]

Para recuperar $290:

\[
24.50 \times \frac{1 - 0.92^n}{0.08} = 290
\]

Eso da aproximadamente:

\[
n \approx 35 \text{ meses}
\]

Es decir, con churn de 8%, tardarías alrededor de 3 años en recuperar el CAC de forma esperada.

A los 12 meses, apenas habrías recuperado aproximadamente:

\[
24.50 \times \frac{1 - 0.92^{12}}{0.08} \approx \$194
\]

o sea, 67% del CAC.

A los 24 meses:

\[
\approx \$265
\]

o sea, 91% del CAC.

Recién cerca del mes 35 recuperarías el CAC completo.

Eso no es aceptable para escalar publicidad pagada, especialmente si ya eres rentable y no necesitas quemar caja para comprar crecimiento.

---

## 6. El margen de seguridad es casi nulo

El punto de equilibrio económico sería:

\[
CAC = LTV_{bruto} = \$306.25
\]

Tu CAC actual es $290.

Es decir, si el CAC sube apenas 5.6%, ya pierdes dinero.

También puedes verlo desde el churn. Con precio de $35 y margen bruto de 70%, el churn máximo para que el LTV bruto cubra un CAC de $290 es:

\[
churn = \frac{24.50}{290} = 8.45\%
\]

Estás en 8%.

O sea, tienes menos de medio punto porcentual de margen antes de que el churn haga que la campaña pierda dinero.

Eso no es escalar; es caminar por la cornisa.

---

## 7. ¿Qué números necesitarías para que tenga sentido?

Para publicidad pagada, normalmente quieres algo como:

- LTV bruto / CAC ≥ 3
- Payback menor a 12 meses, idealmente menor a 6-9 meses
- Churn del canal pagado no peor que el orgánico
- CAC completamente cargado, incluyendo creativos, herramientas, tiempo, impuestos, etc.

Con tus números actuales, para tener LTV/CAC bruto de 3:

### Opción A: bajar CAC

Necesitarías:

\[
CAC \leq \frac{306.25}{3} = \$102
\]

Es decir, tu CAC tendría que bajar de $290 a aproximadamente $100.

---

### Opción B: bajar churn

Con precio de $35 y margen de 70%, para justificar un CAC de $290 con LTV/CAC de 3, necesitarías un churn mensual de aproximadamente:

\[
churn = \frac{24.50}{3 \times 290} = 2.82\%
\]

Es decir, tendrías que bajar churn de 8% mensual a menos de 3% mensual.

---

### Opción C: subir precio

Con churn de 8%, CAC de $290 y margen bruto de 70%, el precio necesario para tener LTV/CAC de 3 sería:

\[
Precio = \frac{3 \times 290 \times 0.08}{0.70} \approx \$99.4
\]

Es decir, necesitarías cobrar alrededor de $100/mes, no $35/mes, manteniendo el mismo margen.

---

### Opción D: combinación

Por ejemplo, si bajaras CAC a $150, necesitarías un churn máximo de:

\[
\frac{24.50}{3 \times 150} = 5.44\%
\]

Si bajaras CAC a $200, necesitarías churn de:

\[
\frac{24.50}{3 \times 200} = 4.08\%
\]

Si bajaras churn a 5%, necesitarías CAC máximo de:

\[
\frac{24.50 / 0.05}{3} = \$163
\]

La combinación tiene que ser realista y medible.

---

## 8. Mi recomendación

No metas $10.000 este mes.

Lo que haría en tu lugar:

1. **No escales todavía.**
2. Haz una prueba pequeña, por ejemplo $500-$1.000, en un solo canal.
3. Mide CAC marginal real, no CAC mezclado con clientes orgánicos.
4. Mide churn de los clientes que vienen de publicidad pagada.
5. Verifica si esos clientes activan, se quedan y pagan igual o mejor que los orgánicos.
6. Incluye todos los costos del canal: anuncios, creativos, software, agencia, tiempo, impuestos, etc.
7. Solo escala si el canal cumple algo como:
   - LTV bruto / CAC ≥ 3
   - Payback razonable, idealmente menor a 12 meses
   - Churn pagado no superior al orgánico
   - Margen de contribución positivo después de CAC

Con tus números actuales, la campaña apenas daría:

\[
LTV_{bruto} - CAC = 306.25 - 290 = \$16.25
\]

por cliente.

Eso no alcanza para cubrir gastos fijos, errores, cambios en publicidad, aumento de CAC, ni costo de capital.

---

## Conclusión

**No le des.**

Tu cuenta original usa 24 meses de vida cuando el churn de 8% implica aproximadamente 12.5 meses, y además usa ingresos en vez de margen bruto.

El número real es:

\[
LTV_{bruto} = \$306.25
\]

\[
LTV/CAC = 1.06
\]

Con eso, $10.000 en publicidad te generarían apenas unos $560 de utilidad bruta futura, recuperados a lo largo de varios años.

Primero arregla una de estas tres variables: **CAC, churn o precio**. Después escala.