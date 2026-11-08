# Qwen 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 131.17s | tokens_per_second: 114.1
- input_tokens: 255 | output_tokens: 14960

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

**No. No le doy el green light con estos números.**  
Tu plan se cae en la aritmética básica de unit economics.

## 1. El error principal

Estás usando:

- **Ingreso**, no **margen bruto**.
- Una vida de **24 meses**, pero tu churn mensual de **8%** implica una vida mucho más corta.

Con 8% de churn mensual, la retención es 92% cada mes. La vida media de un cliente es:

\[
\text{Vida media} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Además, la probabilidad de que un cliente llegue a 24 meses es:

\[
0.92^{24} \approx 13.4\%
\]

Es decir: con 8% de churn mensual, **solo ~13% de los clientes llega a vivir 2 años**.

---

## 2. LTV correcto

Tu margen bruto mensual por cliente es:

\[
35 \times 70\% = 24.5
\]

LTV con churn de 8%:

\[
\text{LTV} = \frac{24.5}{0.08} = 306.25
\]

LTV/CAC:

\[
\frac{306.25}{290} = 1.06
\]

No 2.9.

### Interpretación dura

Estás pagando **$290** por adquirir un cliente que, después de margen bruto y churn, te deja aproximadamente **$306** durante toda su vida.

Eso significa que el cliente apenas supera tu CAC.

Ganancia bruta de lifetime por cliente:

\[
306.25 - 290 = 16.25
\]

Con $10,000 en publicidad, si el CAC realmente es $290:

\[
\frac{10,000}{290} \approx 34.5 \text{ clientes}
\]

Beneficio bruto esperado de lifetime:

\[
34.5 \times 16.25 \approx 560
\]

Es decir: gastas $10,000, adquieres ~34 clientes y, en teoría, recuperas ~$10,560 de margen bruto durante toda la vida de esa cohorte.

Eso no es escalar fuerte. Es casi trabajar para el canal de publicidad.

---

## 3. El payback: el problema más grave

Tu cálculo ignora el efecto del churn sobre el flujo de caja.

Aporte bruto mensual por cliente: **$24.50**

Si no hubiera churn, el payback sería:

\[
\frac{290}{24.5} = 11.8 \text{ meses}
\]

Pero con 8% de churn mensual, el aporte mensual va cayendo.

Cumulative contribution after month \(m\):

\[
24.5 \times \frac{1 - 0.92^m}{0.08}
\]

Para recuperar $290:

\[
24.5 \times \frac{1 - 0.92^m}{0.08} = 290
\]

Resolviendo:

\[
m \approx 35 \text{ meses}
\]

### Payback con churn: ~35 meses

Y la vida media del cliente es ~12.5 meses.

Eso es una señal roja enorme.

A los 12 meses, cada cliente promedio te deja:

\[
24.5 \times \frac{1 - 0.92^{12}}{0.08} \approx 194
\]

No alcanza para cubrir un CAC de $290.

Con $10,000 en ads:

- Clientes adquiridos: ~34.5
- Margen bruto mes 1: ~$845
- Margen bruto acumulado a 12 meses: ~$6,680
- Sigue siendo negativo a 12 meses: ~-$3,320

Solo se vuelve marginalmente positivo después de muchos meses, porque el LTV total apenas supera al CAC.

---

## 4. Incluso usando tu supuesto de 24 meses, sigue mal

Digamos que aceptamos tu supuesto de que el cliente vive 24 meses.

Pero deberías usar margen bruto, no ingreso.

\[
\text{LTV} = 35 \times 0.70 \times 24 = 588
\]

\[
\text{LTV/CAC} = \frac{588}{290} = 2.03
\]

Sigue por debajo de 3.

Y si el churn real es 8% mensual, el supuesto de 24 meses es inconsistente.

Si realmente tus clientes viven 24 meses en promedio, tu churn mensual sería aproximadamente:

\[
\frac{1}{24} = 4.17\%
\]

No 8%.

---

## 5. Umbrales que necesitas para aprobar $10,000

Con tus números actuales:

- Precio: $35/mes
- Margen: 70%
- Aporte mensual: $24.50
- Churn: 8%
- CAC: $290

### Para un LTV/CAC de 3

Necesitas:

\[
\text{CAC} \leq \frac{306.25}{3} = 102.08
\]

Es decir, CAC de **$102 o menos**.

O bien, manteniendo CAC de $290, necesitas un LTV de al menos $870.

Con churn de 8%, eso exigiría un aporte mensual de:

\[
870 \times 0.08 = 69.6
\]

Eso implicaría un precio de:

\[
\frac{69.6}{0.70} = 99.4
\]

Es decir, precio cercano a **$100/mes**, no $35.

### Para payback de 12 meses con churn de 8%

A 12 meses, un cliente con churn 8% deja ~$194 de margen bruto.

Entonces el CAC máximo para payback de 12 meses sería:

\[
\text{CAC} \leq 194
\]

Con CAC de $290, el payback se va a ~35 meses.

---

## 6. Veredicto

**No metas $10,000 en publicidad con estos números.**

Tu negocio puede ser rentable hoy, pero la publicidad pagada no te da una economía unitaria suficiente para escalar fuerte.

El problema no es solo que LTV/CAC sea 2.9. El problema es que el número correcto, usando margen y churn, es ~1.06.

Y el payback real es ~35 meses.

Eso no escala con salud.

---

## 7. Qué haría yo antes de escalar

### A. Valida el churn por cohorte

No uses churn mezclado si vas a comprar clientes.

Necesitas saber:

- Retención mes 1
- Retención mes 3
- Retención mes 6
- Retención mes 12
- Churn de clientes adquiridos con ads vs orgánicos

Muchas veces los clientes pagados retienen peor.

---

### B. Define CAC totalmente cargado

¿Tu CAC de $290 incluye solo ad spend?

Debería incluir:

- Ads
- Creativos
- Agencia o copywriting
- Landing pages
- Test fallidos
- Descuentos
- Herramientas de conversión
- Tiempo de equipo si aplica

Si el CAC real es $350, el plan empeora.

---

### C. Arregla retention antes de escalar

Con $35/mes, 8% de churn mensual es alto para escalar con paid ads.

Necesitas llevar el churn a menos de ~3%–4% antes de meter volumen fuerte.

Con churn de 4%:

\[
\text{LTV} = \frac{24.5}{0.04} = 612.5
\]

\[
\text{LTV/CAC} = \frac{612.5}{290} = 2.11
\]

Mejor, pero sigue sin ser ideal.

Con churn de 3%:

\[
\text{LTV} = \frac{24.5}{0.03} = 816.7
\]

\[
\text{LTV/CAC} = \frac{816.7}{290} = 2.82
\]

Ya se acerca a 3, pero el payback sigue siendo largo con CAC de $290.

---

### D. Sube precio o margen

Si mantienes churn de 8% y CAC de $290, necesitas más aporte mensual.

Para payback de 12 meses con churn de 8%, necesitas:

\[
\text{Aporte mensual} \geq \frac{290}{7.904} \approx 36.7
\]

Con 70% de margen, eso implica un precio de:

\[
\frac{36.7}{0.70} \approx 52.4
\]

Es decir, precio de ~$52/mes solo para que el payback de 12 meses sea viable con churn de 8%.

Pero para LTV/CAC de 3, necesitas aporte mensual de ~$69.6, equivalente a precio de ~$99/mes con 70% de margen.

---

### E. Considera planes anuales

Si puedes vender anual, mejoras flujo de caja y reduces riesgo de churn.

Ejemplo:

- Mensual: $35/mes
- Anual: $350/año, con descuento

Eso no arregla automáticamente el LTV/CAC, pero mejora payback y reduce exposición mensual.

Eso sí, hay que ajustar churn, refunds, cancelaciones y descuento.

---

## 8. Cuándo sí le daría

Le daría a escalar con paid ads si se cumplen estas condiciones:

1. **LTV/CAC ≥ 3**, usando margen bruto y churn real.
2. **CAC payback ≤ 12 meses**, idealmente ≤ 6 meses si quieres escalar fuerte.
3. **CAC totalmente cargado**, no solo ad spend.
4. **Retención por cohorte estable**, no solo promedio histórico.
5. **Runway suficiente** para cubrir el periodo de payback.
6. **Margen bruto suficiente** para que la adquisición no se coma toda la ganancia.

Con tus números actuales:

\[
\text{LTV/CAC} \approx 1.06
\]

\[
\text{Payback} \approx 35 \text{ meses}
\]

No cumple.

---

## Conclusión

**No le doy.**

No porque tu negocio no sea rentable, sino porque con esos números la publicidad pagada no es un motor de crecimiento sano.

Estás pagando casi todo el LTV por cada cliente.

Antes de meter $10,000, necesitas:

- Bajar CAC a ~$100–$120, o
- Bajar churn a ~2%–3%, o
- Subir precio/margen, o
- Mejorar flujo de caja con planes anuales.

Si quieres escalar fuerte, primero arregla la aritmética.