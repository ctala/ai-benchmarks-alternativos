# Qwen 3.8 27B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 406.708s | tokens_per_second: 56.0
- input_tokens: 255 | output_tokens: 22781

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



No. **No le doy.**

Con los números que me diste, el plan no sobrevive a la aritmética. No estás en “2,9 casi 3”; estás en un caso donde el margen por cliente es apenas positivo sin descuento y probablemente negativo con descuento.

Aquí está el recálculo.

---

## 1. Si tu churn mensual es 8%, un cliente no se queda 2 años

Con churn mensual constante:

```text
Vida promedio = 1 / churn
Vida promedio = 1 / 0.08
Vida promedio = 12.5 meses
```

No 24 meses.

De hecho, con 8% mensual:

```text
Retención a 12 meses = 0.92^12 ≈ 36.8%
Retención a 24 meses = 0.92^24 ≈ 13.5%
```

Es decir, si tu churn real es 8% mensual, la gran mayoría de tu base se va antes de 1 año.

Si tú observas que “un cliente se queda unos 2 años”, entonces tu churn no es 8% mensual. Sería más bien:

```text
Churn mensual aproximado = 1 / 24 ≈ 4.2%
```

Eso cambia el caso, pero con el churn que declaraste, el lifetime no es 24 meses.

---

## 2. Tu LTV no es $840. Tu LTV debe calcularse con margen, no con revenue

Tú calculaste:

```text
LTV = $35 × 24 = $840
```

Eso es revenue bruto, no LTV de margen.

Tu margen bruto mensual por cliente es:

```text
$35 × 70% = $24.50 por mes
```

Entonces, con churn del 8%:

```text
LTV = Margen mensual / churn
LTV = $24.50 / 0.08
LTV = $306.25
```

Tu LTV/CAC real sería:

```text
LTV/CAC = $306.25 / $290
LTV/CAC ≈ 1.06
```

No 2.9.

Incluso si asumimos tu supuesto de 24 meses:

```text
LTV de margen = $24.50 × 24 = $588
LTV/CAC = $588 / $290 ≈ 2.03
```

Todavía no llegas a 3x. Y ese 2.03 sería sobre un lifetime que no cuadra con tu churn declarado.

---

## 3. Con descuento, el caso empeora

El LTV de $306.25 es sin descuento. Pero estás metiendo dinero en publicidad hoy para recibir margen durante muchos meses. Hay que descontar.

Con un descuento mensual del 1%, equivalente a una tasa anual de dos dígitos, el valor presente de ese margen es aproximadamente:

```text
LTV descontado ≈ $275
```

Tu CAC es $290.

Entonces:

```text
NPV por cliente ≈ $275 - $290 = -$15
```

Con estos números, cada cliente nuevo comprado con publicidad destruye valor en presente.

El punto de equilibrio de descuento para que ese cliente sea apenas positivo está alrededor de un 6% anual. Para crecimiento con riesgo, costo de capital y ejecución, eso es demasiado bajo. Con 10%-12% anual, estás en negativo.

---

## 4. ¿Qué pasa si metes $10,000 este mes?

Si tu CAC es $290:

```text
Clientes nuevos = $10,000 / $290 ≈ 34.5 clientes
```

Margen bruto mensual esperado de esa cohorte:

```text
34.5 × $24.50 ≈ $845 por mes
```

Entonces el flujo de caja aproximado sería:

| Tiempo | Flujo esperado de la cohorte |
|---|---:|
| Mes 0 | -$10,000 |
| Mes 1 | +$845 |
| Acumulado a 12 meses | +$6,678 aprox. |
| Acumulado a 24 meses | +$9,132 aprox. |
| Lifetime esperado | +$10,560 aprox. |

El margen total esperado de esa cohorte sería:

```text
$10,560 - $10,000 = +$560
```

O sea: **$560 de margen total antes de descuento, riesgo, inflación de CAC, costos adicionales o fuga extra.**

Y eso asumiendo que tu CAC se mantiene en $290 al escalar. En publicidad pagada, normalmente el CAC marginal sube cuando metes más presupuesto. Si el CAC real al escalar es $320 o $350, el caso ya no es marginal: es negativo.

Además, si modelas el cash flow esperado mes a mes con churn del 8%, recuperar el CAC por cliente lleva mucho más tiempo que la simple regla de:

```text
CAC / margen mensual = $290 / $24.50 ≈ 11.8 meses
```

Esa regla simple asume que el cliente no se va. Con churn del 8%, la recuperación depende de la cola de clientes que sobreviven. En expectativa, el payback por cliente se acerca a ~35 meses. Con descuento, no se recupera con tasas razonables.

---

## 5. Tu ratio 2.9 está mal por dos razones

Primero: 2.9 no está “por encima de 3”. Está por debajo.

Segundo: está calculado sobre revenue, no sobre margen.

Tu comparación correcta con los números que diste es:

| Concepto | Tu cálculo | Cálculo correcto |
|---|---:|---:|
| Lifetime | 24 meses | 12.5 meses |
| LTV | $840 revenue | $306 margen |
| LTV/CAC | 2.9 | 1.06 |

Eso no es un plan escalable. Es un plan que compra clientes con margen casi cero.

---

## 6. ¿Qué tendría que pasar para que sí le diera?

Depende de qué quieras lograr.

### Para ser apenas positivo sin descuento

Necesitas:

```text
CAC < LTV
CAC < $306
```

Tu CAC de $290 cumple eso, pero apenas.

### Para ser positivo con descuento de 10%-12% anual

Necesitarías un CAC más bien alrededor de:

```text
CAC ≈ $275-$280
```

O un churn ligeramente menor, o un precio/margen mayor.

Con margen de $24.50 y churn 8%, para que el LTV descontado cubra $290 necesitarías subir el precio a algo como:

```text
Precio ≈ $37-$38 con 70% de margen
```

Es decir, un aumento pequeño de precio ya cambia el caso. Pero no lo salva a 3x.

### Para LTV/CAC = 2 usando margen

Necesitas:

```text
CAC ≤ $153
```

O, con CAC $290:

```text
Churn ≤ 4.2%
```

O margen mensual:

```text
$46.40 por mes
```

Con 70% de margen, eso implica precio de:

```text
$46.40 / 0.70 ≈ $66 por mes
```

### Para LTV/CAC = 3 usando margen

Necesitas:

```text
CAC ≤ $102
```

O, con CAC $290:

```text
Churn ≤ 2.8%
```

O margen mensual:

```text
$69.60 por mes
```

Con 70% de margen, eso implica precio de:

```text
$69.60 / 0.70 ≈ $99 por mes
```

Eso es muy distinto a tu precio actual de $35.

---

## 7. Mi veredicto

**No metas $10,000 este mes con esos números.**

Con churn 8%, precio $35, margen 70% y CAC $290, tu LTV/CAC real es ~1.06. No es un caso de crecimiento fuerte; es un caso de margen casi nulo y payback largo.

Si ya eres rentable, probablemente tu base actual tiene CAC histórico bajo, canales orgánicos, referrals, ventas salientes o churn mejor. Eso no significa que puedas comprar clientes nuevos a $290 y esperar que la publicidad sea rentable.

---

## 8. Lo que sí aprobaría

Aprobaría un experimento pequeño, no $10,000.

Por ejemplo:

```text
$1,000-$2,000 de test
```

Con cohortes medidos por semana o mes, y kill criteria claros:

- CAC total ≤ $150, idealmente ≤ $100.
- Churn de la cohorte ≤ 4%, idealmente ≤ 3%.
- Retención a 3 meses ≥ 75%.
- Retención a 6 meses ≥ 70%.
- Payback esperado ≤ 6 meses.
- LTV/CAC con margen ≥ 2x, idealmente ≥ 3x.
- CAC estable al escalar, no inflado.

Si puedes demostrar que tu churn real es ~4% y no 8%, el caso cambia. Pero aun así no estarías en 2.9x; estarías cerca de 2x con margen. Y para escalar fuerte, querrías más margen de seguridad.

---

## Resumen ejecutivo

Tu plan dice:

```text
LTV = $840
CAC = $290
LTV/CAC = 2.9
```

La realidad con tus números es:

```text
Lifetime = 12.5 meses
LTV de margen = $306
LTV/CAC = 1.06
LTV descontado < CAC
```

**No le doy.** Primero arregla churn, precio, margen o CAC. Luego escala.