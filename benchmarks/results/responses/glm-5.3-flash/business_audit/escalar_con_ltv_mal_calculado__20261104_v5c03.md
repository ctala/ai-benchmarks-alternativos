# GLM 5.3 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 74.396s | tokens_per_second: 77.0
- input_tokens: 206 | output_tokens: 5727

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

**Veredicto: no. El plan muere en la aritmética, y tiene dos errores que se multiplican entre sí.**

**Error 1: la vida media no es 24 meses.** Con churn del 8% mensual, la vida media es 1/0,08 = **12,5 meses**, no 24. A los 24 meses solo sobrevive ~13% de los clientes (0,92²⁴ ≈ 0,135). Que "se quedan 2 años" sería cierto con un churn de ~4% mensual. Tus dos datos se contradicen: o el churn es 8% o la permanencia es 24 meses. No pueden ser ambos, y no se gasta $10.000 sobre datos contradictorios.

**Error 2: el LTV se calcula sobre margen bruto, no sobre ingresos.** El CAC se paga con utilidad, no con facturación:

LTV = $35 × 0,70 ÷ 0,08 = **$306** (no $840).

Combinando ambos errores, te sobrestimaste el LTV ~2,7 veces.

**Los números reales:**

| Métrica | Tu cálculo | Recalculado |
|---|---|---|
| Vida media | 24 meses | 12,5 meses |
| LTV (sobre margen) | $840 | $306 |
| LTV/CAC | 2,9 | **1,05** |
| Payback del CAC | — | ~11,8 meses |

Y un detalle menor: 2,9 no está "más o menos por encima de 3". Está por debajo incluso con tu propia aritmética.

**Lo que compran realmente los $10.000:** ~34 clientes. Ese cohorte genera ~$830/mes de margen bruto. En 12 meses habrás recaudado ~$6.600; durante toda su vida, ~$10.400. Contra $10.000 invertidos: **+$400 repartidos en más de un año**, antes de overhead, tu tiempo y el costo de los creativos. El payback del CAC (11,8 meses) casi coincide con la vida del cliente (12,5): recuperas la inversión justo cuando se van. Eso no es escalar, es correr en una cinta que apenas se paga.

**Qué tendría que cambiar para llegar a LTV/CAC = 3 (LTV objetivo: $870):**

- CAC ≤ ~$100, con tus churn y precio actuales, o
- churn ≤ ~2,8% mensual, con CAC de $290, o
- precio ~$99/mes, con churn del 8% — o una combinación.

**Mi lectura:** tu rentabilidad actual probablemente viene de clientes con CAC ≈ 0 (orgánico, referidos). Eso valida que el producto vende, no que el canal pagado funcione. Y un churn del 8% mensual es una fuga enorme (~63% anual): antes de meter agua más rápido, tapa la fuga.

**Qué haría yo:** cero desembolsos grandes este mes. Un test de $1.000–1.500 para medir el CAC real de campaña —el estimado casi siempre sale optimista el primer mes— y el churn de los clientes que llegan por ads (suele ser peor que el orgánico). En paralelo: atacar churn con onboarding y planes anuales, que además mejoran tu caja. Cuando el LTV real supere ~$870 o el CAC baje de ~$100, el plan de $10.000 se aprueba solo. Hoy, con LTV/CAC ≈ 1, cada dólar de publicidad es un préstamo que te pagas a ti mismo en un año, sin intereses pero sin ganancia.