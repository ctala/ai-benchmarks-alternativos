# Tencent Hy4 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy4`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 46.869s | tokens_per_second: 96.4
- input_tokens: 228 | output_tokens: 4520

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

**No. No le des.**

Tu plan no muere en la ambición, muere en tres líneas de aritmética.

| Concepto | Tu número | Recalculado |
|---|---|---|
| Vida esperada del cliente | 24 meses | **12,5 meses** |
| Valor mensual computable | $35 | **$24,50** |
| LTV | $840 | **$306,25** |
| LTV/CAC | 2,9 ("~3") | **1,06** |
| Payback | — | **11,8 meses** |

### Los tres errores, en orden de gravedad

**1. La vida del cliente.** Con churn mensual del 8%, la esperanza es `1 / 0,08 = 12,5 meses`, no 24. El 8% mensual equivale a **63% de churn anual** (0,92¹² = 36,8% de retención). Los 24 meses corresponden a un churn de ~4%, que no es el que reportas.

**2. Estás comparando ingresos contra costes.** El CAC se paga con **contribución**, no con facturación. Margen 70% → `35 × 0,70 = $24,50/mes`. LTV correcto: `24,50 / 0,08 = $306,25`.

**3. El redondeo.** 840/290 = 2,90, que es *por debajo* de 3, no "más o menos por encima". Y concediéndote incluso los 24 meses, con margen aplicado el LTV sería `24,50 × 24 = $588` → ratio **2,03**. Aun con tu supuesto más generoso, no llegas al umbral.

Ratio real: `306,25 / 290 = 1,06`. Estás recuperando el CAC con un 6% de colchón, antes de soporte, overhead, impuestos y coste de capital. Eso no es escalar, es empatar.

### Qué le pasa realmente a tus $10.000

- Clientes comprados: `10.000 / 290 = 34,5`
- Contribución mes 1: `34,5 × 24,50 ≈ $845`, decayendo 8% cada mes
- Contribución lifetime esperada de la cohorte: `34,5 × 306,25 ≈ $10.560`
- Resultado: **+$560 repartidos en más de un año**, un 5,6% nominal sin descontar

Aplica un coste de capital conservador del 1% mensual y el LTV cae a ~$275 → **ratio 0,95, VAN negativo**. Y eso asumiendo que el CAC se mantiene en $290 al escalar, que es el supuesto más frágil de todos: al subir puja y saturar audiencia, un CAC de $310 ya te deja en 0,99. Escalar "fuerte" es precisamente lo que empuja el CAC hacia arriba.

### El riesgo que no aparece en el ratio

Payback de **11,8 meses** contra una vida esperada de **12,5**. Recuperas el dinero justo cuando el cliente se está yendo: ~63% de la cohorte churnea antes de devolverte el CAC. Estás financiando el crecimiento con tu propia caja durante un año, con retorno casi nulo. Para un negocio rentable, ese es un trade-off pésimo: cambias rentabilidad presente por un crecimiento que no crea valor.

### La palanca que sí mueve el número

| Churn mensual | LTV | LTV/CAC |
|---|---|---|
| 8% (hoy) | $306 | 1,06 |
| 4% | $613 | 2,11 |
| 2,8% | $870 | **3,00** |

Bajar churn de 8% a ~2,8% te da el mismo efecto que reducir el CAC de $290 a **$102**. Arreglar retención es más barato que comprar tráfico, y además acorta el payback. Meter $10.000 en ads sobre un 8% de churn es echar agua en un cubo agujereado.

### Condición para volver a pedirme aprobación

1. LTV/CAC ≥ 3 **calculado sobre margen y con descuento**, no sobre revenue.
2. Payback < 6 meses.
3. CAC de $290 **verificado al volumen real de $10k/mes**, no el de la campaña de prueba.

Hasta entonces: $0 a escala. Un presupuesto pequeño de experimentación para atacar el churn, sí. Los $10.000, no.