# Claude Fable 5.1 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 30.914s | tokens_per_second: 69.4
- input_tokens: 297 | output_tokens: 2145

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

No. El plan muere en la aritmética, y en dos sitios distintos.

**Error 1: la vida del cliente no son 2 años**

Con churn mensual del 8%, la vida media esperada es 1 / 0,08 = **12,5 meses**, no 24. Los "2 años" no salen de ningún número que me hayas dado; salen de una sensación. Un churn del 8% significa que de cada 100 clientes que entran hoy, a los 12 meses te quedan ~37. A los 24 meses, ~13.

**Error 2: el LTV se calcula sobre margen, no sobre ingreso**

De cada $35 que cobras, $10,50 se van en infraestructura y pagos antes de que puedas usar un centavo para recuperar el CAC. Lo que de verdad te queda por cliente al mes es 35 × 0,70 = **$24,50**.

**El LTV real**

$24,50 × 12,5 meses = **$306**

**La ratio real**

306 / 290 = **1,06**

No 2,9. Por cada dólar que metes en publicidad, recuperas $1,06 a lo largo de más de un año. Eso es antes de salarios, soporte, herramientas, tu tiempo. En la práctica, pierdes dinero.

(Detalle menor pero revelador: 2,9 tampoco está "por encima de 3". Cuando uno redondea hacia la respuesta que quiere, suele haber más cosas redondeadas.)

**Payback**

290 / 24,50 = **11,8 meses** para recuperar el CAC. Tu cliente promedio dura 12,5. Estás recuperando la inversión justo cuando el cliente se va.

**Qué pasa con los $10.000**

- Compras ~34 clientes.
- En los primeros 12 meses, con el churn comiéndose la cohorte, recuperas unos **$6.600** en margen.
- El total acumulado en el horizonte completo roza los $10.400. Es decir, tardas más de dos años en recuperar la caja, sin contar valor del dinero ni nada más.

Y hay un riesgo adicional: $290 es tu CAC *al volumen actual*. Al escalar publicidad el CAC casi siempre sube (agotas la audiencia barata primero), y los clientes que vienen de ads suelen churnear más que los que llegaron orgánicos. Ambos efectos empujan la ratio por debajo de 1.

**Qué haría yo**

1. **No meter los $10.000.** Esto no es escalar un motor que funciona; es amplificar un motor que apenas llega al punto de equilibrio.
2. **Atacar el churn antes que nada.** Es la palanca más potente que tienes:
   - Churn 8% → 5%: vida 20 meses, LTV $490, ratio 1,7.
   - Churn 8% → 4%: vida 25 meses, LTV $612, ratio 2,1.
   - Churn 8% → 3%: vida 33 meses, LTV $817, ratio 2,8.
3. **Subir precio o bajar CAC** como palancas secundarias. A $45/mes con el mismo churn, LTV $394, ratio 1,4. Mejor, pero el churn sigue siendo lo que mata.
4. **Si quieres validar el canal igualmente**, mete $1.000–$1.500, no $10.000. Mide el CAC real a ese gasto y, sobre todo, mide el churn de *esa* cohorte a 2–3 meses. Es el dato que no tienes y el que decide todo.

El umbral para darle en serio: LTV/CAC ≥ 3 calculado con margen y con churn real, y payback < 12 meses. Hoy estás en 1,06 y 11,8. Tienes un negocio rentable con clientes baratos; no lo conviertas en un negocio que pierde dinero con clientes caros.