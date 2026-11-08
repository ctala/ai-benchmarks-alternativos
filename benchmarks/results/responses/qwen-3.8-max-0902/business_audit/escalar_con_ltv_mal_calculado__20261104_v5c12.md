# Qwen 3.8 Max 0902 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 303.594s | tokens_per_second: 44.4
- input_tokens: 255 | output_tokens: 13470

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

No. **Con esos números, no le des a meter $10.000 este mes para “escalar fuerte”.**

El problema no es que tu negocio sea necesariamente malo; el problema es que tu cálculo de LTV está demasiado optimista y el unit economics marginal queda casi en punto muerto.

---

## 1. Tu permanencia estimada no cuadra con 8% de churn mensual

Si tu churn mensual es 8%, la vida esperada de un cliente, bajo un modelo simple, es:

\[
\text{Vida esperada} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Con 8% mensual:

- Después de 12 meses, te queda aproximadamente **37%** de la cohorte.
- Después de 24 meses, te queda aproximadamente **13,5%**.
- La vida promedio es mucho más cercana a 12,5 meses que a 24 meses.

Si realmente tus clientes duran 24 meses, entonces tu churn mensual efectivo debería ser mucho menor, cercano a 4% mensual. Pero con 8% mensual, la matemática no da.

---

## 2. El LTV no se calcula con ingresos brutos, sino con margen bruto

Tu precio es $35/mes, pero no puedes usar $35 completos para pagar CAC. Tienes margen bruto de 70%.

Entonces:

\[
\text{Margen bruto mensual por cliente} = 35 \times 0.70 = \$24,50
\]

Tu LTV con churn de 8% sería:

\[
\text{LTV margen bruto} = \frac{24,50}{0.08} = \$306,25
\]

O equivalente:

\[
35 \times 12.5 \times 0.70 = \$306,25
\]

Tu CAC es $290.

Por tanto:

\[
\text{LTV margen bruto / CAC} = \frac{306,25}{290} = 1,06
\]

Eso no es 2,9. Es **1,06**.

Si usas ingresos brutos:

\[
\text{LTV ingresos} = 35 \times 12.5 = \$437,50
\]

\[
\text{LTV ingresos / CAC} = \frac{437,50}{290} = 1,51
\]

Tampoco da 2,9.

---

## 3. Incluso si tus clientes duraran 24 meses, el ratio sigue flojo

Supongamos que tu intuición de 24 meses fuera correcta.

LTV en ingresos:

\[
35 \times 24 = \$840
\]

LTV/CAC en ingresos:

\[
840 / 290 = 2,9
\]

Ese es el número que estás usando. Pero el negocio no paga publicidad con ingresos; paga con margen.

LTV en margen bruto:

\[
35 \times 24 \times 0.70 = \$588
\]

LTV margen bruto / CAC:

\[
588 / 290 = 2,03
\]

Es decir: incluso en el escenario optimista de 24 meses, tu ratio sobre margen bruto sería aproximadamente **2,0**, no 3,0.

No es catastrófico, pero tampoco es como para escalar agresivamente.

---

## 4. El payback también es peligroso

Tu margen bruto mensual por cliente es $24,50.

Payback simple:

\[
\text{Payback} = \frac{290}{24,50} = 11,8 \text{ meses}
\]

Eso ya es largo considerando que la vida esperada con 8% churn es 12,5 meses.

Pero el payback simple ignora que muchos clientes se van antes.

Con churn del 8%, el margen bruto acumulado esperado por cliente es aproximadamente:

| Horizonte | Margen bruto acumulado esperado |
|---|---:|
| 12 meses | ~$194 |
| 24 meses | ~$265 |
| Toda la vida | ~$306 |

Es decir, después de 12 meses todavía no recuperas el CAC de $290 en términos esperados. Después de 24 meses tampoco. Recién te acercas al break-even hacia el final de la vida del cliente.

Matemáticamente, recuperar $290 con este churn y este margen tomaría alrededor de **35 meses** en términos de flujo esperado. Pero el cliente promedio se va mucho antes.

Otro dato duro: con 8% churn mensual, la mediana de vida del cliente es aproximadamente:

\[
\frac{\ln(0.5)}{\ln(0.92)} \approx 8,3 \text{ meses}
\]

O sea, **la mitad de tus clientes se va antes de 8,3 meses**.

---

## 5. ¿Qué pasa si metes $10.000 en publicidad?

Si tu CAC es $290:

\[
10.000 / 290 \approx 34,5 \text{ clientes}
\]

Esos clientes traerían:

- MRR inicial:  
  \[
  34,5 \times 35 \approx \$1.207
  \]

- Margen bruto mensual inicial:  
  \[
  34,5 \times 24,50 \approx \$845
  \]

Pero el margen bruto total esperado durante la vida de esos clientes sería:

\[
34,5 \times 306,25 \approx \$10.560
\]

Como gastaste $10.000, la ganancia bruta esperada sería:

\[
10.560 - 10.000 = \$560
\]

Antes de:

- costos fijos,
- salarios,
- herramientas,
- soporte,
- impuestos,
- errores de atribución,
- aumento de CAC al escalar,
- descuento financiero,
- variabilidad del churn,
- devoluciones,
- fraude,
- cambios de precio,
- etc.

Estás escalando para ganar aproximadamente **$16 por cliente** en el mejor caso.

Eso es demasiado frágil.

---

## 6. Sensibilidad rápida: cualquier pequeño cambio te mata el plan

Con tus números actuales:

- LTV margen bruto: $306,25
- CAC: $290
- Beneficio bruto esperado por cliente: $16,25

Si el churn sube de 8% a 9%:

\[
LTV = \frac{24,50}{0.09} = \$272
\]

Ahora pierdes dinero contra un CAC de $290.

Si el CAC sube de $290 a $319:

\[
306,25 - 319 < 0
\]

También pierdes.

Si incluyes costo financiero, el LTV baja.

Si el margen real es menor que 70% porque faltan costos de soporte, onboarding, éxito del cliente, devoluciones, etc., también baja.

Si el CAC marginal aumenta al meter más presupuesto, también baja.

Es decir: el plan no aguanta ningún error.

---

## 7. Los números que necesitarías para que esto se vea sano

Para tener un LTV/CAC de 3 sobre margen bruto con tus números actuales:

\[
\text{CAC máximo} = \frac{306,25}{3} = \$102
\]

Tu CAC actual es $290.

Para mantener CAC de $290 y tener LTV/CAC de 3, necesitarías:

### Opción A: bajar churn

Necesitarías un churn mensual aproximado de:

\[
\frac{24,50}{3 \times 290} = 0.028
\]

Es decir, **2,8% mensual**, no 8%.

### Opción B: subir precio

Con churn de 8% y margen de 70%, para justificar CAC de $290 con ratio 3x, el precio debería ser aproximadamente:

\[
\frac{3 \times 290}{12.5 \times 0.70} \approx \$99,4/mes
\]

O sea, casi **$100/mes**, no $35.

### Opción C: combinación

Por ejemplo:

- menor churn,
- mayor precio,
- upsells,
- expansión,
- planes anuales,
- menor CAC,
- mejor segmentación de canales.

Pero con la combinación actual, no da.

---

## 8. Si igual quieres gastar, no metas $10.000 de golpe

Mi recomendación sería:

### No escales todavía.

Primero valida con un experimento pequeño, por ejemplo $1.000-$2.000, y mide:

1. **CAC marginal real**, no CAC histórico mezclado.
2. **Retención por cohorte** a 30, 60, 90 y 180 días.
3. **Churn real** de los clientes venidos de paid ads.
4. **Payback real**.
5. **Margen bruto real**, incluyendo soporte, devoluciones, fraude, procesamiento, infraestructura y cualquier costo variable adicional.
6. **Incrementalidad**: ¿esos clientes hubieran llegado igual sin publicidad?

Solo debería escalar si ves algo como:

- LTV margen bruto / CAC > 3,
- payback menor a 6-9 meses,
- churn estable o decreciente,
- CAC marginal no muy superior al CAC histórico,
- capacidad de caja para financiar el payback.

---

## 9. La frase clave

Una cosa es que tu empresa sea rentable hoy.

Otra cosa es que el próximo dólar invertido en publicidad sea rentable.

Tu rentabilidad actual puede venir de:

- clientes antiguos,
- canales orgánicos,
- CAC histórico más bajo,
- cohorts viejas con mejor retención,
- clientes que llegaron antes de aumentar precios o cambiar producto.

Pero el crecimiento pagado se evalúa con **unit economics marginales**.

Y tus números marginales actuales dicen:

\[
\text{LTV margen bruto} \approx \$306
\]

\[
\text{CAC} = \$290
\]

\[
\text{Margen esperado por cliente adquirido} \approx \$16
\]

Eso no es escalar con confianza. Es caminar por la cornisa.

---

## Conclusión

**No le des.**

Con churn de 8%, margen bruto de 70%, precio de $35 y CAC de $290, tu LTV/CAC real sobre margen bruto es aproximadamente **1,06**, no 2,9.

Incluso si los clientes duraran 24 meses, tu LTV/CAC sobre margen bruto sería aproximadamente **2,0**, todavía por debajo del estándar sano de 3x.

Antes de meter $10.000, deberías:

1. reducir churn a menos de 3-4% mensual,
2. subir precio o expansión,
3. bajar CAC a alrededor de $100-$150,
4. o validar que los clientes de paid ads tienen retención y LTV muy superiores.

Con los números actuales, escalar fuerte con publicidad pagada sería comprar crecimiento casi sin margen y con mucho riesgo de caja.