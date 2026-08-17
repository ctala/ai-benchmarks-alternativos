# Claude Sonnet 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 27.1s | tokens_per_second: 68.4
- input_tokens: 295 | output_tokens: 1855

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

# Antes de que actives esos $10K, revisemos la aritmética — porque tiene dos errores que cambian todo.

## Error #1: El lifetime no es 24 meses

Con churn mensual del 8%, la vida promedio de un cliente es:

$$\text{Lifetime} = \frac{1}{\text{churn}} = \frac{1}{0.08} = 12.5 \text{ meses}$$

No 24 meses. Para que la vida promedio fuera 2 años, tu churn mensual tendría que ser ~4.17%, no 8%. Estás sobreestimando la duración del cliente casi al doble.

## Error #2: El LTV no se calcula sobre revenue bruto, sino sobre margen

El cliente no te deja $35/mes de valor — te deja $35 × 70% = $24.50/mes después de costos.

$$LTV = \frac{ARPU \times \text{Margen bruto}}{\text{Churn}} = \frac{35 \times 0.70}{0.08} = \frac{24.50}{0.08} = \$306.25$$

## El LTV/CAC real

$$\frac{LTV}{CAC} = \frac{306.25}{290} = 1.06$$

No 2.9. **1.06**, prácticamente en el punto de equilibrio. La regla de "3x mínimo" existe justamente para dar margen de error ante variaciones en churn, CAC creciente, o costos operativos no capturados. Tú estás en el límite de romper.

## El dato que más debería preocuparte: payback period

$$\text{Payback} = \frac{CAC}{ARPU \times \text{Margen}} = \frac{290}{24.50} = 11.8 \text{ meses}$$

Tu cliente promedio dura **12.5 meses** y tarda **11.8 meses** en pagar su propio CAC. Le queda menos de un mes de margen neto positivo antes de irse. Cualquier variación negativa (CAC sube con más volumen de ads, churn empeora en cohortes nuevas y menos cualificadas) te pone en rojo.

## ¿Le doy a los $10K?

**No, todavía no.** Con estos números, escalar significa multiplicar una operación que apenas empata, no que gana. Además, el CAC tiende a subir cuando aumentas presupuesto (agotas la audiencia más barata primero), así que los próximos clientes probablemente sean *peores* que el promedio actual.

### Qué haría antes de meter el dinero:

1. **Ataca el churn primero.** Bajar de 8% a 5% mensual sube tu LTV a $490 (con el mismo CAC, LTV/CAC = 1.69). Bajar a 4% te da LTV=$612 (LTV/CAC = 2.1). El churn es tu palanca más poderosa, no el CAC.
2. **O ataca el CAC.** Si lo bajas a $150, LTV/CAC = 2.04. Sigue sin ser 3x, pero ya es otra conversación.
3. **Prueba con $1,000–2,000, no $10,000.** Mide el CAC real a ese volumen (probablemente suba) y el churn de esa cohorte específica de ads (suele ser peor que el churn de clientes orgánicos/referidos).
4. **Verifica si "rentable" incluye estos CAC.** Si tu rentabilidad actual viene de canales orgánicos con CAC bajo, meter pauta cara puede convertir un negocio sano en uno que quema caja aunque "crezca".

¿Tienes el desglose del churn por cohorte (orgánico vs. pagado) o el CAC blended actual sin el ads nuevo? Con eso afinamos si el problema es de fondo o solo de este canal.