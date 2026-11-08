# Claude Sonnet 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 16.072s | tokens_per_second: 122.7
- input_tokens: 297 | output_tokens: 1972

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

# No le des todavía: con tus números, cada cliente nuevo apenas recupera lo que cuesta

## Dónde falla el cálculo

**1. El tiempo de vida está mal.** Con 8% de churn mensual, la vida media es 1 / 0,08 = **12,5 meses**, no 24. Para llegar a 24 meses necesitarías un churn de ~4,2%.

**2. El LTV debe ir sobre margen, no sobre ingresos.** Multiplicaste por el precio, pero lo que te queda es el 70%:

- Margen bruto mensual por cliente: 35 × 0,70 = **$24,50**
- LTV = 24,50 × 12,5 = **$306**

**3. El ratio real.** LTV/CAC = 306 / 290 = **1,06**. Y además 2,9 no está "por encima de 3": está por debajo. Pero el problema de fondo es que el ratio real es ~1, no 2,9.

## El payback es peor de lo que parece

Dividiendo 290 / 24,50 saldría un payback de ~12 meses. Pero con 8% de churn, solo el 37% de tus clientes sigue vivo al mes 12 (0,92¹² ≈ 0,37). Considerando el churn, recuperar los $290 de una cohorte tarda **unos 35 meses**, porque tienes que cobrar el 95% de todo el margen que un cliente generará en su vida.

## Qué pasaría con los $10.000

- Comprarías ~34 clientes.
- Generarían ~$10.500 de margen bruto en toda su vida, repartido en años.
- Recuperas tu inversión con suerte, sin ganancia, y con la caja inmovilizada durante ~3 años.
- Esto asume que el CAC no sube al escalar, y casi siempre sube.

Tu rentabilidad actual probablemente viene de clientes orgánicos o de referidos, que no pagan ese CAC. La publicidad no tiene los mismos números.

## Qué tendría que cambiar para llegar a LTV/CAC ≥ 3

Con CAC de $290 necesitas un LTV de ~$870. Opciones:

| Palanca | Resultado |
|---|---|
| Churn a 4% (25 meses) | LTV $612, ratio 2,1 |
| Churn a 3% (33 meses) | LTV $817, ratio 2,8 |
| CAC a ~$100 con churn actual | Ratio 3,0 |
| Churn 5% + precio $50 | LTV $700, ratio 2,4 |

Lo realista es combinar varias: reducir churn, subir precio o pasar a planes anuales (que cobran por adelantado y bajan el churn), y mejorar el CAC con mejores creativos o segmentación.

## Qué haría yo

1. **No invertir $10.000.** Si quieres probar, un test de $1.000–1.500 para medir CAC real y retención por canal.
2. **Atacar el churn primero.** Un 8% mensual es alto: revisa onboarding y en qué mes se van.
3. **Probar precio y planes anuales** antes de escalar.
4. **Escalar solo cuando** LTV/CAC (sobre margen) sea ≥ 3 y el payback realista sea menor a ~12 meses.

Si me pasas la curva de retención por cohortes, puedo afinar el cálculo, porque el churn suele ser mayor en los primeros meses y eso cambia el LTV real.