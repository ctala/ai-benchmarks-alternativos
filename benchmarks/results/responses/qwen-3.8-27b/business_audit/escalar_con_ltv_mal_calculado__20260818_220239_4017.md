# Qwen 3.8 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 87.598s | tokens_per_second: 160.0
- input_tokens: 255 | output_tokens: 14012

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



No. Con esos números, **no le doy los $10.000**.

Tu plan muere en la aritmética. No es un tema de “más o menos 3x”. Es un error estructural.

## 1. Tu cálculo principal está mal

Dices:

> “Un cliente se queda unos 2 años, entonces LTV = 35 × 24 = $840.”

Pero también dices:

> “Churn mensual: 8%.”

Esas dos cosas no son compatibles.

Si el churn es **8% mensual**, la vida media de un cliente no es 24 meses. Es:

\[
\frac{1}{0.08} = 12,5 \text{ meses}
\]

No 24.

De hecho, con 8% de churn mensual, solo sobreviven hasta el mes 24:

\[
0,92^{24} \approx 13,5\%
\]

Es decir, **apenas 1 de cada 7 clientes** llega a 2 años.

---

## 2. Recalculemos tu LTV

Precio: **$35/mes**

Margen bruto: **70%**

Margen bruto mensual por cliente:

\[
35 \times 0,70 = 24,50
\]

Vida media con churn 8%:

\[
12,5 \text{ meses}
\]

### LTV de ingresos

\[
35 \times 12,5 = 437,50
\]

### LTV de margen bruto

\[
437,50 \times 0,70 = 306,25
\]

Ese es el LTV que importa para comparar contra CAC.

---

## 3. Tu LTV/CAC real

Tu CAC: **$290**

Tu LTV de margen bruto: **$306,25**

\[
\frac{306,25}{290} = 1,06
\]

No 2,9.

Si usas LTV de ingresos, que es peor:

\[
\frac{437,50}{290} = 1,51
\]

Tampoco 2,9.

Además, dijiste que 2,9 está “por encima de 3”. No está. Está por debajo. Pero eso da igual: el número correcto es mucho peor.

---

## 4. Incluso si te creo que el cliente se queda 24 meses

Aun así, tu cálculo falla porque usas ingresos, no margen.

Si un cliente se queda 24 meses:

LTV de ingresos:

\[
35 \times 24 = 840
\]

LTV de margen bruto:

\[
840 \times 0,70 = 588
\]

LTV/CAC con margen:

\[
\frac{588}{290} = 2,03
\]

No 2,9.

Y payback:

\[
\frac{290}{24,50} = 11,8 \text{ meses}
\]

Es decir, aunque el cliente se quede 2 años, tardas casi 12 meses en recuperar el CAC solo con margen bruto. Eso no es una máquina de crecimiento sano. Es un negocio de margen muy fino.

---

## 5. Qué pasa si metes $10.000 este mes

Con CAC de $290:

\[
\frac{10.000}{290} = 34,5 \text{ clientes nuevos}
\]

MRR nuevo aproximado:

\[
34,5 \times 35 = 1.207,50
\]

Margen bruto mensual nuevo:

\[
34,5 \times 24,50 = 845,25
\]

Gastas **$10.000** ahora.

Recuperas ese gasto en:

\[
\frac{10.000}{845,25} \approx 11,8 \text{ meses}
\]

El beneficio bruto de por vida de esa cohorte es:

\[
34,5 \times 306,25 \approx 10.560
\]

Menos los $10.000 de publicidad:

\[
10.560 - 10.000 = 560
\]

O sea: por cada $10.000 que metes en ads, generas aproximadamente **$560 de margen bruto extra**, antes de impuestos, antes de soporte, antes de ventas, antes de que el CAC suba.

Eso no es escalar. Es comprar clientes que apenas se pagan.

---

## 6. Si repites $10.000/mes a este CAC

Supongamos que mantienes CAC $290 y churn 8%.

Clientes nuevos al mes:

\[
34,5
\]

En estado estable, base total de clientes:

\[
\frac{34,5}{0,08} \approx 431 \text{ clientes}
\]

MRR en estado estable:

\[
431 \times 35 \approx 15.085
\]

Margen bruto mensual:

\[
431 \times 24,50 \approx 10.560
\]

Publicidad mensual:

\[
10.000
\]

Resultado incremental mensual:

\[
10.560 - 10.000 = 560
\]

Estás generando **$560 al mes** por meter $10.000 al mes en publicidad.

Y si el CAC sube un poco, te quedas en cero o en negativo.

Por ejemplo:

- Si CAC sube a $306,25, estás en break-even.
- Si CAC sube a $310, pierdes dinero en margen bruto.
- Si el churn sube de 8% a 8,5%, también pierdes.

Es extremadamente frágil.

---

## 7. Umbral para que esto sí tenga sentido

Con tus números actuales:

Margen bruto mensual por cliente: **$24,50**

Para tener un payback de 6 meses:

\[
24,50 \times 6 = 147
\]

Entonces tu CAC debería ser, como máximo, alrededor de:

\[
\$150
\]

Para tener 3x LTV/CAC usando margen bruto:

\[
\frac{306,25}{3} = 102,08
\]

Entonces, para un 3x sano, tu CAC debería ser:

\[
\leq \$102
\]

Con CAC de $290, no estás cerca.

---

## 8. ¿Qué necesitarías para que tu CAC de $290 funcionara?

Con churn 8%, precio $35 y margen 70%, para que CAC $290 diera 3x LTV/CAC, necesitarías:

### Opción A: bajar churn a 2,8%

\[
\frac{24,50}{0,028} \approx 875
\]

\[
\frac{875}{290} \approx 3
\]

Necesitarías churn de **2,8% mensual**, no 8%.

### Opción B: subir precio a ~$99/mes

Necesitarías margen bruto mensual de:

\[
3 \times 290 \times 0,08 = 69,60
\]

Con margen 70%:

\[
\frac{69,60}{0,70} = 99,43
\]

Es decir, precio de **~$99/mes**.

### Opción C: bajar CAC a ~$100

Ese es el camino más realista si no puedes subir precio ni mejorar churn drásticamente.

---

## 9. Mi veredicto

**No le doy los $10.000.**

Tu negocio actual puede ser rentable, pero eso no significa que la publicidad pagada sea una palanca sana a estos números.

La pregunta correcta no es:

> “¿Mi negocio ya es rentable?”

Sino:

> “¿Cada dólar de publicidad me devuelve más de un dólar en margen bruto, en un plazo razonable?”

Con tus números:

- LTV/CAC real con margen: **1,06**
- Payback: **11,8 meses**
- Beneficio bruto de por vida por $10.000 de ads: **~$560**
- Sensibilidad al CAC: **altísima**

No es un negocio de crecimiento acelerado. Es un negocio de margen delgado.

---

## 10. Si aún quieres probar, esta es la única forma aceptable

No $10.000.

**$1.000 a $2.000 máximo**, como test.

Y con reglas claras:

1. **CAC real** = gasto publicitario / clientes pagados activados.  
   No leads, no trials, no “clientes potenciales”.

2. Si CAC > **$150**, pausas.

3. Si payback > **6 meses**, pausas.

4. Si churn mensual de la cohorte > **5%**, pausas.

5. Si al escalar el CAC sube más de 10%, pausas.

Solo escalarías a $10.000 cuando tengas evidencia de:

- CAC ≤ **$150**, idealmente ≤ **$100**
- Churn ≤ **5%**, idealmente ≤ **3%**
- Payback ≤ **6 meses**
- LTV/CAC con margen ≥ **2x**, idealmente ≥ **3x**

Con CAC $290 y churn 8%, no.

**Decisión: no le doy.**