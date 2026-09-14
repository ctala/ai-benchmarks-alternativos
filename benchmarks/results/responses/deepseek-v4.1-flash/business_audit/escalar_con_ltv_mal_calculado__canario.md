# DeepSeek V4.1 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 29.099s | tokens_per_second: 169.6
- input_tokens: 228 | output_tokens: 4934

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

No. Con esos números, no le daría $10.000 a publicidad pagada. Tu cálculo tiene dos errores que cambian la decisión.

| Concepto | Tu cálculo | Correcto |
|---|---:|---:|
| Churn mensual | 8% | 8% |
| Vida media del cliente | ~24 meses | 1 / 0,08 = **12,5 meses** |
| LTV ingresos | $35 × 24 = $840 | $35 × 12,5 = **$437,50** |
| Margen bruto | 70% | 70% |
| LTV bruto | No lo usaste | $437,50 × 70% = **$306,25** |
| CAC | $290 | $290 |
| LTV bruto / CAC | 2,9 | 306,25 / 290 = **1,06** |
| Payback | No lo calculaste | 290 / (35 × 70%) = **11,8 meses** |

El error principal: con churn mensual de 8%, el cliente promedio no se queda 2 años, se queda **12,5 meses**. Además, para comparar contra CAC no uses LTV de ingresos, usa **LTV de margen bruto**, porque el CAC se paga con margen, no con facturación.

Con $10.000 en ads compras aproximadamente:

$10.000 / $290 = **34,5 clientes**

LTV bruto total del cohorte:

34,5 × $306,25 = **$10.565**

Después de CAC:

$10.565 − $10.000 = **+$565 en toda la vida del cohorte**

Eso es antes de costos fijos, equipo, herramientas, refunds, impuestos, etc. Es básicamente ruido. Y ese dinero no llega rápido: a los 12 meses habrías recuperado unos $6.677 de esos $10.000. O sea, todavía estarías abajo.

Peor aún: con 8% de churn, solo sobrevive aproximadamente:

0,92^11,8 ≈ **37%**

Solo ~37% de los clientes siguen activos cuando terminas de pagar el CAC.

Para escalar fuerte con publicidad pagada, yo exigiría al menos:

- LTV bruto / CAC ≥ 3
- Payback < 6–12 meses, idealmente < 6
- Churn mucho menor o prepago anual

Con tus números actuales:

- Para LTV/CAC = 3 con CAC $290, necesitarías churn mensual ≈ **2,8%**, no 8%.
- O con tu churn actual, tu CAC máximo para LTV/CAC = 3 sería ≈ **$102**, no $290.
- O necesitarías subir mucho el ARPU: con 8% churn y 70% margen, necesitarías cobrar ≈ **$99/mes** para justificar CAC $290 con ratio 3.

Mi recomendación: **no metas $10.000 de golpe**. Si quieres testear, haz un piloto capado de $500–$2.000, mide CAC real por canal, y trabaja primero churn, pricing, plan anual, upsells y activación. Escala publicidad solo cuando el cohorte pagado tenga LTV bruto/CAC > 3 y un payback que tu caja aguante. Hoy cada cliente pagado deja ~$16 de contribución total antes de costos fijos. No hay colchón para escalar fuerte.