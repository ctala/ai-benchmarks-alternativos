# Qwen 3.8 Max 0902 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 370.084s | tokens_per_second: 42.2
- input_tokens: 255 | output_tokens: 15603

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

No. Con esos números, **no metas $10.000 en publicidad este mes**. El plan no aguanta la aritmética.

Tu cálculo tiene dos errores grandes:

1. **Estás usando ingresos, no margen bruto**, para el LTV.  
2. **Con churn mensual de 8%, la vida media no es 24 meses**; es mucho menor.

---

## 1. Recalculando la vida del cliente

Si el churn mensual es 8%, la retención mensual es 92%.

Vida esperada aproximada:

\[
\text{Vida media} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses.

Además:

- La mediana de permanencia es todavía peor: aproximadamente **8,3 meses**.
- La probabilidad de que un cliente llegue a 24 meses es:

\[
0.92^{24} \approx 13.5\%
\]

Es decir, solo cerca de 1 de cada 7 clientes llegaría a los 2 años. No puedes construir el LTV asumiendo 24 meses como caso base.

---

## 2. LTV correcto

Precio mensual: $35  
Margen bruto: 70%  
Margen bruto mensual por cliente:

\[
35 \times 0.70 = 24.5
\]

LTV bruto con churn mensual de 8%:

\[
\text{LTV bruto} = \frac{24.5}{0.08} = 306.25
\]

Tu LTV de $840 usa ingresos, no margen, y además usa una permanencia demasiado optimista.

Comparación:

| Concepto | Tu cálculo | Cálculo corregido |
|---|---:|---:|
| Vida media asumida | 24 meses | 12,5 meses |
| LTV ingresos | $840 | $437,5 |
| LTV bruto | No aplicado correctamente | $306,25 |
| CAC | $290 | $290 |
| LTV/CAC | 2,9 | **1,06** |

Incluso si usaras ingresos en vez de margen bruto, el ratio sería:

\[
\frac{437.5}{290} = 1.51
\]

Tampoco sirve.

Y si mantuvieras tu supuesto de 24 meses, pero aplicaras margen bruto:

\[
35 \times 24 \times 0.70 = 588
\]

\[
\frac{588}{290} = 2.03
\]

Seguiría por debajo de 3. Pero además ese supuesto de 24 meses no es consistente con 8% de churn mensual.

---

## 3. El problema real: estás comprando clientes casi a break-even

Con los números corregidos:

\[
\text{LTV bruto} = 306.25
\]

\[
\text{CAC} = 290
\]

Contribución bruta después de adquirir al cliente:

\[
306.25 - 290 = 16.25
\]

Es decir, por cada cliente adquirido, te quedan **$16,25** durante toda la vida del cliente, antes de:

- gastos fijos,
- soporte,
- impuestos,
- herramientas,
- equipo,
- devoluciones,
- costo financiero,
- errores de campaña,
- aumento de CAC al escalar.

Eso no es escalar rentablemente. Es comprar crecimiento casi sin margen.

---

## 4. ¿Qué pasa si metes $10.000?

Con CAC de $290:

\[
\frac{10,000}{290} \approx 34.5 \text{ clientes}
\]

LTV bruto total esperado:

\[
34.5 \times 306.25 \approx 10,560
\]

Beneficio bruto esperado después de publicidad:

\[
10,560 - 10,000 = 560
\]

O sea, metes $10.000 hoy para ganar aproximadamente **$560** de contribución bruta a lo largo de la vida de esos clientes.

Y eso antes de gastos fijos y antes de riesgo.

Además, el retorno no es inmediato. El payback simple da:

\[
\frac{290}{24.5} \approx 11.8 \text{ meses}
\]

Pero ese payback simple ignora que muchos clientes se van antes. Modelando la cohorte con churn de 8%, recuperar el CAC con el flujo esperado toma alrededor de **35 meses**, asumiendo primer cobro inmediato. Si el primer cobro no es inmediato, puede ser peor.

Para $10.000, aproximadamente:

- después de 12 meses recuperarías alrededor de $6.700,
- después de 24 meses alrededor de $9.100,
- recién cerca del mes 35 recuperarías los $10.000.

Estás dejando capital bloqueado casi 3 años por un margen mínimo.

---

## 5. El margen de error es peligrosamente pequeño

Con CAC de $290 y margen bruto mensual de $24,50, el churn de punto de equilibrio es:

\[
\frac{24.5}{290} = 8.45\%
\]

Tu churn actual es 8%. Es decir, estás a solo 0,45 puntos porcentuales de que el LTV bruto sea menor que el CAC.

Si el churn sube un poco, pierdes.  
Si el CAC sube 6%, pierdes.  
Si el CAC real incluye salarios, creative, herramientas, impuestos o fricción de pago, pierdes.  
Si el margen bruto real baja un poco, pierdes.

No hay colchón.

---

## 6. ¿Qué números necesitarías para que sí tenga sentido?

Para que paid acquisition sea sano, normalmente quieres algo como:

\[
\text{LTV bruto / CAC} \geq 3
\]

Con tu LTV bruto actual de $306,25, el CAC máximo sería:

\[
\frac{306.25}{3} = 102.08
\]

Es decir, tu CAC debería ser cercano a **$100**, no $290.

Otras combinaciones posibles:

| Palanca | Valor necesario aproximado |
|---|---:|
| Bajar CAC a | $102 |
| Bajar churn mensual a | 2,8% |
| Subir precio a | ~$99/mes |
| Combinación sana | CAC ~$150 + churn ~4% |

Por ejemplo, si bajaras churn a 4%:

\[
\text{LTV bruto} = \frac{24.5}{0.04} = 612.5
\]

Con CAC de $290:

\[
\frac{612.5}{290} = 2.11
\]

Todavía no llega a 3.

Si bajaras churn a 4% y CAC a $150:

\[
\frac{612.5}{150} = 4.08
\]

Ahí sí empieza a verse razonable.

---

## 7. Mi recomendación

**No le doy.**

No porque el negocio sea malo necesariamente, sino porque con estos unit economics no puedes escalar agresivamente con publicidad pagada.

Lo que haría:

1. **No meter $10.000 de golpe.**
2. Hacer una prueba pequeña, tipo $1.000-$2.000, solo para medir:
   - CAC marginal real,
   - activación,
   - retención a 30/60/90 días,
   - margen bruto real,
   - payback real.
3. Atacar primero una de estas tres variables:
   - bajar CAC a menos de $100-$150,
   - bajar churn mensual a menos de 3%-4%,
   - subir precio o añadir upsell que aumente el ingreso por cliente.
4. Solo escalar cuando tengas:
   - LTV bruto/CAC marginal mayor a 3,
   - payback razonable, idealmente menor a 6-9 meses,
   - evidencia de que el CAC no se dispara al aumentar presupuesto.

Si tus datos históricos realmente muestran una permanencia media de 24 meses, entonces tu churn mensual no es 8%. Hay una inconsistencia y hay que revisar cómo estás midiendo churn.

Pero con los números tal como los presentaste: **no. Primero arregla los unit economics.**