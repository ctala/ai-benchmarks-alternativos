# DeepSeek V4.1 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 124.23s | tokens_per_second: 37.0
- input_tokens: 228 | output_tokens: 4599

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

No. Con esos números, escalar fuerte con publicidad pagada es una forma cara de comprar ingresos, no de comprar beneficio.

Tu error principal: usaste 24 meses de vida y no descontaste el margen bruto.

| Métrica | Cálculo correcto | Resultado |
|---|---:|---:|
| Vida media del cliente | 1 / 0,08 | **12,5 meses** |
| Margen bruto mensual por cliente | $35 × 70% | **$24,50** |
| LTV bruto real | $24,50 / 0,08 | **$306,25** |
| LTV/CAC | $306,25 / $290 | **1,06** |
| Payback de CAC | $290 / $24,50 | **11,8 meses** |
| Contribución por cliente antes de costos fijos | $306,25 − $290 | **$16,25** |
| Probabilidad de seguir tras 24 meses | 0,92^24 | **~13,5%** |

Un churn mensual del 8% no da clientes de 2 años. Da una vida media de 12,5 meses, y la mediana es aún menor: ~8,3 meses. Es decir, muchos clientes se van antes de que recuperes el CAC.

Además, tu LTV/CAC de 2,9 estaba mal calculado. Incluso ese 2,9 no está “por encima de 3”; está por debajo. Y el correcto es **1,06**, no 2,9.

Si usas LTV sobre ingresos, sin margen:  
$35 / 0,08 = $437,50  
$437,50 / $290 = **1,51**. Sigue siendo malo.

Con $10.000 en publicidad:
- Compras ~34,5 clientes.
- Margen bruto total de esa cohorte: ~$10.560.
- Después de pagar los $10.000, quedan ~$560 **antes de costos fijos, soporte, herramientas, refunds, impuestos, etc.**
- El payback tarda casi 12 meses.

O sea: si escalas fuerte, aumentas el hoyo de caja durante casi un año para terminar casi en cero.

Para que este canal tenga sentido, necesitas algo así:
- LTV/CAC > 3, con LTV calculado sobre margen bruto.
- Payback idealmente < 6–9 meses.
- Con tu ARPU, margen y CAC actuales, necesitarías bajar el churn mensual a **≤ 2,8%** para llegar a LTV/CAC = 3.
- O bajar el CAC a **≤ $102** para LTV/CAC = 3.
- O bajar el CAC a **≤ $147** para payback de 6 meses.

Mi recomendación: **no metas $10.000 este mes**. Haz una prueba pequeña, mide CAC real por cohorte, trabaja retención/onboarding, considera prepago anual, sube precio o mejora margen, y reduce CAC. Cuando LTV/CAC esté claramente arriba de 3 y el payback sea menor a 9–12 meses, entonces sí escalas. Antes de eso, la publicidad pagada te va a crecer la caja negativa, no el negocio.