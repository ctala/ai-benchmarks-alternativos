# Claude Opus 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.98 | quality: 10.0
- latency_total: 54.927s | tokens_per_second: 70.4
- input_tokens: 295 | output_tokens: 3868

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

## Veredicto

No. Con estos números, los $10.000 en publicidad convierten un negocio rentable en uno que quema caja. Tu cálculo tiene tres errores que se multiplican entre sí.

---

## Error 1: la vida del cliente

Con 8% de churn mensual, la vida promedio es **1 / 0,08 = 12,5 meses**, no 24.

Para que un cliente dure 24 meses necesitarías ~4% de churn. Tu 8% mensual equivale a perder **63% de la base cada año** (1 − 0,92¹² = 0,632). No estás en un negocio de retención de 2 años.

## Error 2: usaste ingreso, no margen

El LTV se calcula sobre margen bruto, porque los $290 de CAC se pagan con dólares de margen, no con dólares de facturación. Tu ingreso real por cliente-mes es 35 × 0,70 = **$24,50**.

## Error 3: 2,9 no está "por encima de 3"

Y más importante: el 3× es una regla de dedo, no un objetivo. Para un negocio bootstrapped que se autofinancia, la restricción que manda es el **período de repago en caja**, no el ratio.

---

## Los números corregidos

| Concepto | Tu cálculo | Real |
|---|---|---|
| Vida promedio | 24 meses | 12,5 meses |
| Ingreso mensual usado | $35 | $24,50 (margen) |
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| **LTV/CAC** | **2,9** | **1,06** |

Un LTV/CAC de 1,06 significa que por cada cliente que compras, ganas **$16 de margen bruto en toda su vida** — antes de soporte, tu sueldo, herramientas o cualquier gasto fijo. Después de eso, pierdes dinero por cliente.

**El repago es peor todavía.** Como la cohorte se va desangrando, hay que acumular margen sobre los clientes que sobreviven:

- Margen acumulado a 12 meses: $194 por cliente adquirido
- Margen acumulado a 24 meses: $270
- Punto de repago de los $290: **mes ~35**
- Techo teórico de recuperación: $306 (nunca llegas mucho más allá)

Estás poniendo $290 hoy para recuperarlos en tres años, en un negocio donde el cliente promedio se va en un año.

---

## Qué pasa concretamente con los $10.000

- Compras ~34 clientes
- Suman ~$845/mes de margen bruto el primer mes
- A los 12 meses quedan ~13 de esos 34 activos
- Margen bruto total recuperado en 12 meses: ~$6.700 de los $10.000
- Recuperación completa: mes 35, si el CAC no sube

Y el CAC **va a subir**. Los $290 los mediste con gasto bajo, en la audiencia más barata. Escalar a $10.000/mes normalmente empuja el CAC 20-50% arriba. Con CAC de $360, tu LTV/CAC baja a 0,85 y ya no hay repago posible: nunca recuperas el dinero.

---

## Qué tendría que ser cierto

Con CAC de $290, precio $35 y margen 70%, para llegar a LTV/CAC = 3 necesitas **churn de 2,8% mensual**. Es un cambio de escala, no un ajuste.

Alternativas, moviendo una variable a la vez:

| Palanca | Valor actual | Valor necesario |
|---|---|---|
| Churn (para 3× a CAC $290) | 8% | **2,8%** |
| Precio (para 3× a churn 8%) | $35 | **~$99** |
| CAC (para 3×, todo lo demás igual) | $290 | **≤ $102** |
| CAC (para repago de cohorte a 12 meses) | $290 | **≤ $194** |
| CAC (para repago a 6 meses) | $290 | **≤ $121** |

---

## Qué haría en tu lugar

1. **Congela los $10.000.** Deja $1.000–2.000/mes de prueba, solo para seguir midiendo CAC por canal. No es momento de escalar; es momento de arreglar el motor.

2. **Ataca el churn primero.** Es tu variable dominante: aparece en el denominador del LTV. Bajar churn de 8% a 4% duplica el LTV; bajar el CAC un 20% lo mueve mucho menos. Empieza por segmentar: casi seguro tienes cohortes con churn de 3-4% y otras con 15%. Averigua qué canal, plan o tamaño de cliente trae a los buenos.

3. **Después de segmentar, quizá el canal pago sí funcione — pero para un segmento.** Si un subconjunto retiene al 3,5% y lo puedes adquirir a $290, ahí sí hay negocio (LTV ≈ $700, ratio 2,4, repago ~15 meses). El error es escalar sobre el promedio.

4. **Revisa precio.** $35/mes con 8% de churn sugiere que el producto se percibe como opcional. Subir precio mejora LTV *y* filtra clientes que retienen mejor. Es la palanca de doble efecto.

5. **Fija un umbral antes de escalar, no después.** Sugerencia: repago de cohorte ≤ 12 meses (CAC ≤ $194 con tus números actuales) y LTV/CAC ≥ 3 medido sobre margen bruto. Si no se cumplen, el gasto no sube.

---

La buena noticia es que ya eres rentable, lo que significa que tienes un canal que funciona a un costo mucho menor que $290. Eso es un activo real. La publicidad pagada a estos números no lo amplifica: lo consume.