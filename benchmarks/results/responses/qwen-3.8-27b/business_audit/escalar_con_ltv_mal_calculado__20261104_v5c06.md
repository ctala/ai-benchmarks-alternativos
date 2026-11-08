# Qwen 3.8 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.78 | quality: 10.0
- latency_total: 1406.578s | tokens_per_second: 16.5
- input_tokens: 255 | output_tokens: 23258

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



No. **Con esos números no le doy los $10,000.**

El problema no es que tengas 2,9 y no 3,0. Es que, con el churn que me das, ese LTV no existe. Tu cálculo mezcla cosas incompatibles:

1. **Churn mensual 8% vs. vida de cliente de 24 meses**
2. **LTV con precio ($35) en vez de con margen bruto ($24,50)**
3. **Sin descuento por tiempo, que mata mucha aritmética de SaaS**

---

## Recalculación

### 1. Margen real por cliente y mes

Precio: $35/mes  
Margen bruto: 70%

\[
35 \times 0,70 = 24,50 \text{ USD/mes de margen bruto}
\]

Ese es el número que deberías usar para LTV, no $35.

---

### 2. Si el churn es 8% mensual, la vida media no es 24 meses

Con churn constante:

\[
\text{Vida media} = \frac{1}{\text{churn}} = \frac{1}{0,08} = 12,5 \text{ meses}
\]

No 24.

Además, con 8% mensual, a los 24 meses queda:

\[
0,92^{24} \approx 13,5\%
\]

Es decir, **solo el 13,5% de la cohorte sigue viva a los 2 años**. No puedes asumir que todos se quedan 24 meses.

Si de verdad tus clientes se quedan 2 años en promedio, tu churn mensual no es 8%; estaría más cerca de **4,2% mensual**. Pero con el número que me diste, el LTV baja mucho.

---

### 3. LTV correcto con tus números

Usando margen bruto y churn mensual:

\[
LTV = \frac{\text{Margen mensual}}{\text{Churn mensual}}
\]

\[
LTV = \frac{24,50}{0,08} = 306,25
\]

También puedes verlo como:

\[
24,50 \times 12,5 = 306,25
\]

Así que tu LTV no es $840.

**Tu LTV real, sin descontar, es ~$306.**

Si aplico un descuento razonable, por ejemplo 10% anual, el LTV cae a aproximadamente:

\[
\sim 278
\]

Y ahí ya estás por debajo del CAC.

---

### 4. LTV/CAC real

Tu CAC: $290

\[
\frac{306,25}{290} \approx 1,06
\]

Con descuento de 10% anual:

\[
\frac{278}{290} \approx 0,96
\]

No tienes LTV/CAC de 2,9.

Tienes **LTV/CAC de ~1,06 sin descontar**, o incluso **negativo en valor presente** con un costo de capital normal.

Cada cliente nuevo te deja alrededor de:

\[
306,25 - 290 = 16,25
\]

de margen bruto esperado, antes de impuestos, soporte, equipo, costos fijos, descuento y cualquier costo variable adicional.

Eso no es crecimiento rentable. Es financiar clientes con tu caja durante mucho tiempo.

---

## El payback tampoco ayuda

Una regla simple dice:

\[
\frac{CAC}{\text{Margen mensual}} = \frac{290}{24,50} \approx 11,8 \text{ meses}
\]

Pero esa regla ignora el churn.

Con 8% mensual, la cohorte se va drenando. El cash acumulado por cliente tarda mucho más en recuperar el CAC.

Resolviendo con retención mensual:

\[
24,50 \times \frac{1 - 0,92^n}{0,08} = 290
\]

Da un payback aproximado de:

\[
\sim 35 \text{ meses}
\]

Sin descuento.

Con descuento razonable, el LTV está por debajo del CAC, así que **no recuperas ni en el infinito**.

---

## Qué pasa si metes $10,000 este mes

Con CAC de $290:

\[
\frac{10.000}{290} \approx 34,5 \text{ clientes nuevos}
\]

Caja hoy: **-$10,000**

Margen bruto del primer mes:

\[
34,5 \times 24,50 \approx 845
\]

Margen acumulado de esa cohorte:

| Tiempo | Margen acumulado aproximado |
|---:|---:|
| Mes 1 | ~$845 |
| Mes 3 | ~$2.340 |
| Mes 6 | ~$4.155 |
| Mes 12 | ~$6.680 |
| Mes 24 | ~$9.130 |
| ~Mes 35 | ~$10.000 |

Es decir:

- En 12 meses recuperas solo ~$6.700 de los $10.000.
- En 24 meses recuperas ~$9.100.
- Recién a los ~35 meses recuperas el gasto publicitario, **sin descontar** y antes de costos fijos, impuestos, soporte, equipo, etc.

No es un plan de escalar fuerte. Es atar caja por 2-3 años con un retorno marginal muy bajo.

---

## Tu supuesto de 2 años no encaja

Si dices “un cliente se queda unos 2 años”, entonces tu churn mensual no puede ser 8%.

Para que la vida media sea 24 meses con churn constante:

\[
\text{Churn mensual} = \frac{1}{24} \approx 4,17\%
\]

Con churn de 4,17% mensual y margen de $24,50:

\[
LTV = \frac{24,50}{0,0417} \approx 588
\]

Entonces:

\[
\frac{588}{290} \approx 2,03
\]

Mejor que 1,06, pero sigue sin ser 3x.

Y el payback con ese churn sería de ~16 meses.

Es un caso más razonable, pero todavía no es un plan de “meter fuerte” sin condiciones.

---

## Qué tendría que pasar para que yo le diera

### Opción 1: Bajar el CAC marginal

Con churn de 8% y LTV de $306:

Para LTV/CAC de 3x:

\[
CAC \leq \frac{306}{3} \approx 102
\]

Para LTV/CAC de 2x:

\[
CAC \leq 153
\]

Con CAC de $150, el payback con churn 8% es de ~8 meses.  
Con CAC de $100, el payback es de ~5 meses.

Así que para escalar con calma, yo querría ver:

- **CAC marginal ≤ $100** si quieres 3x, o
- **CAC marginal ≤ $150** si quieres un caso aceptable, no perfecto.

No $290.

---

### Opción 2: Mejorar el churn

Si mantienes CAC en $290 y quieres LTV/CAC de 3x:

\[
LTV requerido = 290 \times 3 = 870
\]

\[
Churn requerido = \frac{24,50}{870} \approx 2,8\%
\]

Necesitarías bajar de 8% mensual a ~2,8% mensual.

Eso es un cambio enorme. No se asume. Se demuestra con cohortes.

---

### Opción 3: Subir precio o margen

Para 3x con CAC $290 y churn 8%, necesitas:

\[
LTV = 870
\]

\[
\text{Margen mensual requerido} = 870 \times 0,08 = 69,60
\]

No tienes $24,50. Tienes que llegar a ~$69,60 de margen bruto mensual por cliente.

Con margen de 70%, eso implica:

\[
\frac{69,60}{0,70} \approx 99,40
\]

Precio mensual de ~$99, no $35.

Si no puedes subir precio o mejorar margen, la fórmula con CAC $290 y churn 8% no cierra.

---

## Veredicto

**No le doy los $10,000.**

Con tus números:

- LTV real: ~$306
- CAC: $290
- LTV/CAC: ~1,06
- Payback con churn: ~35 meses sin descuento
- Con descuento razonable: NPV negativo o casi cero

Eso no es escalar. Es comprar ingresos con caja propia y esperar a que la cola larga de clientes pague el gasto publicitario.

---

## Lo que sí aprobaría

Un test pequeño, no $10,000.

Yo aprobaría algo como **$1.000-$2.000** máximo, solo si puedes medir por cohorte:

1. **CAC marginal real**, no CAC promedio histórico.
2. **Retención por cohorte**: mes 1, mes 3, mes 6, mes 12.
3. **Margen bruto por cohorte**, no solo MRR.
4. **Costo de publicidad marginal**, porque al escalar normalmente el CAC sube.
5. **Calidad del lead/cliente**, porque más publicidad puede traer más churn.

Kill rules que pondría:

- CAC marginal > $150: frenar.
- Retención mensual < 92%: frenar.
- A 90 días, margen bruto acumulado < 35% del CAC: frenar.
- Si la cohorte paid confirma churn de 8% y CAC de $290: parar.

Si puedes demostrar que el CAC marginal baja a $100-$150, o que el churn real de los clientes de ads es mucho menor, entonces sí hay plan. Pero con 8% de churn mensual y CAC de $290, **no**.