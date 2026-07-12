# MiniMax M3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.51 | quality: 8.14
- latency_total: 22.14s | tokens_per_second: 106.8
- input_tokens: 342 | output_tokens: 2364

## Respuesta completa

**No. No le dé. Con esos números, esos $10.000 se evaporan.**

Tu plan tiene tres errores aritméticos que se acumulan en tu contra. Vamos uno por uno.

## Error 1: La vida del cliente no es 24 meses, es 12,5

Con un churn mensual del 8%, cada mes pierdes el 8% de la base. La fórmula correcta de vida media esperada es:

$$\text{Lifetime} = \frac{1}{\text{churn}} = \frac{1}{0{,}08} = 12{,}5 \text{ meses}$$

De donde sacaste "2 años" es un misterio, pero con 8% mensual la mitad de tus clientes se van antes del mes 9. Dibuja la curva de supervivencia y verás que a los 24 meses ya casi no queda nadie.

## Error 2: El LTV se calcula sobre margen bruto, no sobre revenue

Estás comparando un outflow de CAC ($290, dinero real que sale) contra un inflow de revenue ($35, del cual solo $24,50 es contribution margin después de infra y procesador). Eso es comparar peras con manzanas.

$$\text{LTV} = \text{ARPU} \times \text{margen} \times \text{lifetime} = 35 \times 0{,}70 \times 12{,}5 = \$306{,}25$$

## Error 3: "Está por encima de 3 más o menos" — está por debajo de 1

Tu propio número decía 2,9, que ya está **por debajo** del 3 que mencionas como umbral. Pero con las correcciones:

$$\text{LTV/CAC} = \frac{306{,}25}{290} = \mathbf{1{,}06}$$

Estás en paridad. Cada dólar que entra en publicidad devuelve $1,06 a lo largo de toda la vida del cliente. Después de overhead, soporte, y los inevitables contratiempos, estás destruyendo valor.

## La tabla de la verdad

| Métrica | Tu cálculo | Realidad |
|---|---|---|
| Lifetime del cliente | 24 meses | 12,5 meses |
| LTV (base correcta) | $840 (revenue) | **$306 (gross profit)** |
| LTV/CAC | 2,9 | **1,06** |
| Payback period | — | **11,8 meses** |

El payback de casi 12 meses es la otra alerta roja: con un lifetime esperado de 12,5 meses, tu margen de seguridad es de **medio mes**. Si el churn sube al 10% o el CAC a $310, estás en negativo desde el día uno.

## Qué necesitas para que esto funcione

No te voy a decir "nunca escales con paid". Te voy a decir qué umbral tienes que pasar antes de meter esa plata. Cualquiera de estas correcciones te lleva a LTV/CAC ≥ 3:

- **Bajar churn a 3% mensual**: LTV sube a $816, ratio 2,8. Esto es lo más potente y lo más difícil.
- **Bajar CAC a $100**: con el LTV actual de $306, ratio = 3,06.
- **Subir precio a $70** (manteniendo todo lo demás): LTV = $612, ratio = 2,1. Insuficiente solo.

La combinación realista: atacar churn **y** optimizar CAC hasta estar en payback < 4 meses y ratio > 3.

## Veredicto

Esos $10.000 este mes te van a traer ~34 clientes que, en valor presente neto, generan ~$10.400 de gross profit durante toda su vida. Ganancia teórica: $400. Después de overhead, impuestos, y el hecho de que el cash flow es negativo los primeros 12 meses por cliente, es una operación que destruye capital.

**Acción concreta:** antes de abrir la billetera de ads, ponte una meta de payback < 4 meses y LTV/CAC > 3, y noEscales hasta llegar ahí. Si querés, te ayudo a modelar el plan de crecimiento con los números corregidos como input.