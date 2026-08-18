# Grok 4.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 18.127s | tokens_per_second: 84.4
- input_tokens: 394 | output_tokens: 1530

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

**No. No apruebes los $10k.** El plan muere en la aritmética.

El fundador cometió dos errores graves y uno de magnitud:

- La vida media no es 24 meses. Con churn mensual constante del 8 %, la vida media es \(1 / 0{,}08 = 12{,}5\) meses (no “unos 2 años”).
- El LTV se calcula con el margen de contribución, no con el precio. Contribución mensual = \(35 \times 0{,}70 = 24{,}50\).
- LTV real = \(24{,}50 / 0{,}08 = 306{,}25\).

LTV/CAC = \(306 / 290 \approx 1{,}05\). Payback ≈ 11,8 meses. Eso no es “cerca de 3”; es prácticamente 1. Con ese ratio no hay colchón para costes de soporte, impuestos, incrementos de CAC al escalar, ni para el riesgo de que el churn no sea perfectamente constante. Estás comprando clientes que apenas devuelven el CAC.

Los $10k comprarían ~34 clientes. El valor esperado neto es casi cero (o negativo una vez entran costes no incluidos en el 70 %). No es un motor de crecimiento; es un reciclador de caja.

Antes de meter publicidad a escala hay que mejorar al menos uno de estos tres: bajar CAC de forma demostrable, bajar churn o subir precio/margen. Con los números actuales el plan no pasa. Recalcula con datos reales de cohortes (no con la media teórica) y vuelve.