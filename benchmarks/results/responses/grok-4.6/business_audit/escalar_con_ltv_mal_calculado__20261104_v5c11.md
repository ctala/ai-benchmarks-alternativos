# Grok 4.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 36.691s | tokens_per_second: 57.2
- input_tokens: 394 | output_tokens: 2098

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

**No. No apruebes el gasto de $10k.**

El cálculo del fundador está mal en dos puntos críticos (vida útil y margen). Con los números reales el LTV/CAC es ~1,0-1,1, el payback casi coincide con la vida del cliente y no hay margen de error. Escalar publicidad pagada ahora quema caja.

### Recálculo correcto
- **Vida útil**: churn mensual 8 % → vida media = 1 / 0,08 = **12,5 meses**, no 24. (La serie 1 + 0,92 + 0,92² + … suma exactamente 12,5 pagos esperados.)
- **Contribución mensual**: $35 × 70 % = **$24,50**. Hay que usar margen bruto, no revenue. El CAC se recupera con el dinero que queda después de infra y procesador.
- **LTV (contribución)**: $24,50 × 12,5 = **$306**.
- **LTV/CAC**: 306 / 290 ≈ **1,05**. Muy por debajo del umbral típico de 3× (incluso 2,9 ya era insuficiente y además estaba mal calculado).
- **Payback**: 290 / 24,50 ≈ **11,8 meses**. Con una vida de 12,5 meses recuperas el CAC casi al final y apenas queda beneficio. Cualquier descuento por valor temporal del dinero, estacionalidad, aumento de CAC o subida de churn lo deja en negativo.

$10.000 / $290 ≈ 34 clientes. El valor presente de su contribución apenas cubre el desembolso; el resto de costes (soporte, equipo, impuestos, etc.) no está incluido.

### Qué tendría que cambiar para que el plan sobreviviera a la aritmética
Necesitas al menos una de estas (mejor varias):
- CAC sustancialmente más bajo (objetivo < $100-120 para estos números).
- Churn claramente inferior (4-5 % mensual ya cambia el cuadro).
- Precio o margen más altos.
- Payback < 6-8 meses y LTV/CAC ≥ 3 con el LTV descontado.

Hasta que los unit economics den, el $10k en ads es un mal uso de caja. Primero arregla retención, pricing o canal de adquisición; después escala.