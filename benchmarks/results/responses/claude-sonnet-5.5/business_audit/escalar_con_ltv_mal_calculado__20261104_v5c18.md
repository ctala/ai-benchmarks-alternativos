# Claude Sonnet 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 16.838s | tokens_per_second: 122.6
- input_tokens: 297 | output_tokens: 2065

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

**No le des. Con tus números reales, la economía de ese gasto es casi cero.**

## Dónde está el error

**1. Vida del cliente.** Con churn mensual de 8%, la vida promedio es 1 / 0,08 = **12,5 meses**, no 24. Los 24 meses equivalen a un churn de ~4,2%.

**2. LTV sobre margen, no sobre ingresos.** Multiplicaste por el precio completo, pero lo que paga el CAC es el margen bruto.

| | Tu cálculo | Recalculado |
|---|---|---|
| Vida del cliente | 24 meses | 12,5 meses |
| Ganancia mensual por cliente | $35 | $24,50 (35 × 70%) |
| LTV | $840 | **$306** |
| LTV/CAC | 2,9 | **1,05** |

Además, 2,9 está por debajo de 3, no por encima.

## Lo que significa en la práctica

- **Payback simple:** 290 / 24,5 ≈ 11,8 meses. Es casi toda la vida promedio del cliente.
- **Payback real de la cohorte:** como los clientes se van, a los 12 meses solo has recuperado ~$194 de cada $290. Recuperas el CAC completo recién hacia el **mes 35**, y para entonces quedan pocos clientes activos.
- **Tus $10.000:** compran ~34 clientes que generarán ~$10.500 de margen en total, repartidos en varios años. Ganas ~$500 por inmovilizar $10.000, sin contar costos de soporte, y con el riesgo de que el CAC suba al escalar (suele subir).

## Matices que empeoran el panorama

- Si tu rentabilidad actual viene de clientes orgánicos o referidos, no prueba que el canal pagado funcione. Esos clientes suelen tener mejor churn y CAC casi nulo.
- Los clientes de publicidad suelen retener peor que los orgánicos, así que tu 8% podría ser optimista para esta cohorte.

## Qué tendría que cambiar para escalar (LTV/CAC ≥ 3, objetivo ~$870 de LTV)

Palancas, cada una por separado:
- **Churn:** bajarlo de 8% a ~2,8%. Muy difícil.
- **CAC:** bajarlo de $290 a ~$100.
- **Precio:** subir a ~$99/mes, si el producto lo aguanta.

Lo realista es combinar varias. Por ejemplo, churn 5% (vida 20 meses) con CAC ~$160 y precio $45 ya se acerca a 3.

## Qué haría yo

1. **No gastes los $10.000.** Si quieres seguir probando el canal, un presupuesto pequeño ($500–1.000) con un objetivo claro de CAC.
2. **Ataca el churn primero:** onboarding, planes anuales con descuento (mejoran caja y retención), y analiza por qué se van en los primeros 2–3 meses.
3. **Prueba subir precio** o crear un plan superior.
4. **Mide churn y margen por cohorte de publicidad**, separado del orgánico.
5. Escala cuando el CAC payback sea de menos de ~6 meses, o LTV/CAC (con margen y churn reales) supere 3.

Hoy, escalar con este CAC es pagar para crecer sin ganar dinero. Primero arregla la unidad, y después compra volumen.