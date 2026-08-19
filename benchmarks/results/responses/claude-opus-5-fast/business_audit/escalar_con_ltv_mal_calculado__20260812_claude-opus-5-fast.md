# Claude Opus 5 Fast — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 10.49s | tokens_per_second: 195.2
- input_tokens: 295 | output_tokens: 2048

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

## Respuesta corta: no. El error está en el primer paso.

Con 8% de churn mensual, un cliente **no** se queda 2 años. Se queda 12,5 meses.

Vida media = 1 / churn = 1 / 0,08 = **12,5 meses**

De ahí en adelante todo el cálculo se desmorona. Y hay un segundo error: no aplicaste el margen bruto. El LTV se mide en margen de contribución, no en ingresos brutos — de los $35 solo te quedan $24,50 para pagar el CAC.

## Los números corregidos

| Concepto | Tu cálculo | Real |
|---|---|---|
| Vida media | 24 meses | 12,5 meses |
| Base | $35 (ingreso) | $24,50 (margen) |
| LTV | $840 | **$306** |
| LTV/CAC | 2,9 | **1,06** |
| Payback del CAC | — | **11,8 meses** |

LTV = (35 × 0,70) / 0,08 = **$306,25**

Contra un CAC de $290, estás comprando un dólar por 95 centavos. El margen entero de un cliente promedio se va casi completo en adquirirlo.

(Aparte: 2,9 no está "por encima de