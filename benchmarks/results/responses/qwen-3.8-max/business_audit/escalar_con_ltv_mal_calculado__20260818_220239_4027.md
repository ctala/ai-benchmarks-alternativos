# Qwen 3.8 Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.86 | quality: 10.0
- latency_total: 278.771s | tokens_per_second: 49.6
- input_tokens: 255 | output_tokens: 13815

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

No. Con esos números, **todavía no le des**. El plan se ve bien con tu cálculo, pero la aritmética corregida dice otra cosa.

## 1) Tu LTV está mal calculado

Dices:  
“Como un cliente se queda unos 2 años, LTV = 35 × 24 = $840”.

Pero con **churn mensual del 8%**, la vida media esperada no es 24 meses.

Si el churn es 8% mensual:

\[
\text{Vida media} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Además, el LTV no debería compararse contra CAC usando ingresos completos, sino **contribución bruta**, porque el CAC se paga con dinero real y la infraestructura/pagos ya se comen parte del ingreso.

Tu contribución bruta mensual por cliente es:

\[
35 \times 70\% = 24.5
\]

Entonces:

\[
\text{LTV bruto} = \frac{24.5}{0.08} = 306.25
\]

Tu LTV realista, usando margen bruto, es aproximadamente **$306**, no $840.

---

## 2) El LTV/CAC real es mucho peor

Tu CAC:

\[
CAC = 290
\]

LTV bruto:

\[
LTV = 306.25
\]

Por tanto:

\[
\frac{LTV}{CAC} = \frac{306.25}{290} \approx 1.06
\]

No 2.9.

Incluso si usaras LTV de ingresos, que es menos conservador:

\[
\text{LTV ingresos} = \frac{35}{0.08} = 437.5
\]

\[
\frac{437.5}{290} \approx 1.51
\]

Tampoco da 2.9.

Y si usaras tu supuesto de 24 meses, pero corrigiendo por margen bruto:

\[
35 \times 24 \times 70\% = 588
\]

\[
\frac{588}{290} = 2.03
\]

Aun así estaría por debajo de 3, y además el supuesto de 24 meses no es consistente con un churn del 8% mensual.

---

## 3) El payback también es malo

Una forma rápida y engañosa de ver el payback sería:

\[
\frac{CAC}{\text{contribución mensual}} = \frac{290}{24.5} \approx 11.8 \text{ meses}
\]

Pero eso asume que el cliente se queda todo ese tiempo. Con churn del 8%, muchos clientes se van antes.

Si calculamos la contribución bruta esperada acumulada considerando churn:

- Después de 12 meses, un cliente deja aproximadamente **$194** de contribución bruta esperada.
- Tu CAC es **$290**.
- Es decir, después de un año todavía no recuperas el CAC en términos esperados.

El payback esperado está alrededor de **35 meses**.

Eso es demasiado largo, especialmente si estás financiando el crecimiento con caja.

---

## 4) ¿Qué pasa si metes $10.000 en publicidad este mes?

Con CAC de $290:

\[
\frac{10.000}{290} \approx 34.5 \text{ clientes}
\]

Esos clientes te dan aproximadamente:

\[
34.5 \times 306.25 \approx 10.560
\]

en contribución bruta futura durante toda su vida.

O sea: metes $10.000 hoy para recibir, con suerte y a lo largo de varios años, unos $10.560 de contribución bruta.

Te quedan apenas unos **$560** de margen bruto total, antes de:

- costos fijos,
- soporte,
- salarios,
- herramientas,
- impuestos,
- descuento por el tiempo del dinero,
- posibles desviaciones del CAC,
- posible aumento del churn en canales pagados.

Con cualquier ajuste realista, eso probablemente sea negativo.

---

## 5) Si repites $10.000 mensuales, el negocio queda flaco

Si gastas $10.000 al mes de forma continua y el CAC se mantiene en $290, adquirirías unos 34.5 clientes por mes.

Con churn del 8%, el estado estable sería aproximadamente:

\[
\frac{34.5}{0.08} \approx 431 \text{ clientes}
\]

MRR:

\[
431 \times 35 \approx 15.085
\]

Contribución bruta mensual:

\[
15.085 \times 70\% \approx 10.560
\]

Publicidad mensual:

\[
10.000
\]

Contribución después de publicidad:

\[
10.560 - 10.000 = 560
\]

Antes de costos fijos.

Eso no es escalar rentablemente. Es comprar ingresos casi al costo.

---

## 6) Los números que necesitarías para que sí tenga sentido

Para tener un LTV/CAC de 3 usando tu LTV bruto actual:

\[
CAC \text{ máximo} = \frac{306.25}{3} \approx 102
\]

Es decir, con tu precio y churn actuales, tu CAC debería ser cercano a **$100**, no $290.

Si quieres mantener CAC de $290 y buscar LTV/CAC de 3, necesitas una de estas tres cosas:

### Opción A: bajar el churn

Churn necesario:

\[
\frac{35 \times 70\%}{290 \times 3} = 2.8\% \text{ mensual}
\]

Hoy tienes 8%. Necesitarías bajarlo a aproximadamente **2.8% mensual**.

### Opción B: subir el precio

Precio necesario manteniendo churn de 8% y margen de 70%:

\[
\frac{290 \times 3 \times 0.08}{0.70} \approx 99.4
\]

Necesitarías cobrar alrededor de **$99/mes**, no $35.

### Opción C: bajar el CAC

Con precio de $35, churn de 8% y margen de 70%, para LTV/CAC de 3:

\[
CAC \leq 102
\]

Hoy estás en $290.

---

## 7) Señales de alerta adicionales

- Un churn mensual del 8% implica que después de 12 meses solo retienes aproximadamente:

\[
0.92^{12} \approx 37\%
\]

Es decir, pierdes cerca del 63% de los clientes en un año.

- Después de 24 meses solo queda:

\[
0.92^{24} \approx 13.5\%
\]

Por eso no puedes asumir vida media de 24 meses.

- Si el CAC de $290 es promedio, el CAC marginal al meter $10.000 en publicidad puede subir. En paid ads, muchas veces el primer dólar es barato y el siguiente es más caro.

- Si el churn de los clientes adquiridos con publicidad es mayor que el churn promedio, el LTV será todavía menor.

- Si el margen bruto del 70% no incluye soporte, éxito del cliente, fraude, reembolsos, herramientas o costos operativos, el LTV real también será menor.

---

## 8) Mi recomendación

No metas $10.000 este mes para escalar.

Con los números actuales, estás cerca del punto donde cada cliente adquirido apenas paga su CAC. Eso no da para cubrir costos fijos ni para financiar crecimiento.

Haz esto primero:

1. **No escales paid ads con fuerza.**
2. **Mide el CAC marginal real**, no el CAC promedio histórico.
3. **Mide churn específico de los clientes que vienen de publicidad.**
4. **Calcula payback por canal**, no solo LTV/CAC teórico.
5. **Mejora retención o precio antes de comprar tráfico.**
6. Si quieres probar el canal, hazlo con un presupuesto pequeño, por ejemplo $1.000-$2.000, con criterio de parada claro.

Yo aprobaría escalar solo si ves algo como:

- CAC marginal menor a $100-$120.
- Payback esperado menor a 12 meses.
- LTV/CAC de contribución mayor a 3.
- Churn mensual de la cohorte pagada menor a 3%-4%.
- Caja suficiente para aguantar el desfase entre pago de publicidad y recuperación.

## Respuesta corta

**No le des todavía.**  
Tu LTV real es aproximadamente **$306**, no $840.  
Tu LTV/CAC real es aproximadamente **1.06**, no 2.9.  
Con CAC de $290 y churn de 8%, estás comprando clientes casi sin margen. Primero arregla churn, precio o CAC.