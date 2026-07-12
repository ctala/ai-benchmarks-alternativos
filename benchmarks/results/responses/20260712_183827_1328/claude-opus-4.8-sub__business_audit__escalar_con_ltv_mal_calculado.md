# Claude Opus 4.8 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-opus-4-8`
- success: True  | final: 6.92 | quality: 8.4
- latency_total: 52.704s | tokens_per_second: 54.4
- input_tokens: 4 | output_tokens: 2868

## Respuesta completa

## No. Y no es cerca.

Hay tres errores en el cálculo, y cada uno empuja en la misma dirección: sobreestimar el LTV.

### Error 1: la vida del cliente no son 24 meses, son 12,5

Con churn mensual de 8%, la vida media es `1 / 0.08 = 12,5 meses`. No 24. Los 2 años los asumiste, no los mediste. Ese solo error infla el LTV al doble.

### Error 2: el LTV va sobre margen bruto, no sobre revenue

Un cliente no te deja $35 al mes, te deja $24,50 ($35 × 70%). El CAC se paga con margen, no con facturación.

### Error 3: 2,9 no está "por encima de 3"

Es menor a 3. Y ese 2,9 igual era el número inflado.

### El número real

| | Tu cálculo | Real |
|---|---|---|
| Vida del cliente | 24 meses | **12,5 meses** |
| Contribución/mes | $35 | **$24,50** |
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| **LTV/CAC** | **2,9** | **1,06** |

`LTV = 35 × 0,70 / 0,08 = $306`

**LTV/CAC = 1,06.** Estás en el límite de perder plata por cada cliente que compras.

### El dato que mata el plan: payback

`$290 / $24,50 = 11,8 meses` para recuperar el CAC.
Vida media del cliente: **12,5 meses**.

Recuperas la inversión 3 semanas antes de que el cliente se vaya. No hay ganancia, hay un préstamo que el cliente te devuelve justo antes de irse.

### Qué pasa con tus $10.000

- Compras ~34 clientes.
- Generan ~$10.500 de margen bruto... **repartidos en los próximos 12 meses**.
- Ganancia neta antes de costos fijos: **~$500**. Sobre $10.000, en un año.
- Y estás con $10.000 menos en caja desde el día 1.

Eso asumiendo que el CAC se mantiene en $290 al 10x-ear el gasto. No se mantiene. Si sube a $350 —completamente normal al escalar—, cada cliente te cuesta más de lo que te deja. Estarías pagando por perder plata, más rápido.

### Qué tendría que ser cierto para que este plan funcione

Para llegar a LTV/CAC = 3 necesitas **una** de estas:

- **CAC de $102** en vez de $290 (bajarlo 65%), o
- **Churn de 2,8%/mes** en vez de 8% (bajarlo 65%), o
- **Precio de $99/mes** en vez de $35 (subirlo 3x), o
- Alguna combinación. Ej: churn 5% + precio $50 → LTV $700 → ratio 2,4. Todavía corto.

El problema no es el canal de ads. El problema es que **8% de churn mensual no soporta adquisición pagada a $290**. Ningún canal lo arregla.

### Qué haría yo

1. **Congelar el escalamiento.** Deja el gasto donde está mientras el payback esté sobre 12 meses. La regla: no escalas paid hasta payback < 6 meses (idealmente < 3 si no tienes capital externo).
2. **Revisa el churn por cohorte, no el blended.** Si tu 8% es un promedio donde el mes 1 churnea 20% y el mes 6 en adelante churnea 3%, tu LTV real es mucho mejor y el diagnóstico cambia. Es lo único que puede salvar este cálculo. Mídelo antes de gastar un dólar más.
3. **Ataca el plan anual.** Cobrar 12 meses por adelantado hace dos cosas a la vez: te devuelve el CAC casi completo el día 1 y elimina 12 decisiones de cancelación. Es la palanca más rápida que tienes.
4. **Sube el precio o baja el CAC** — es la única forma de comprar crecimiento. Con el ratio actual, cada dólar de ads es un dólar que sale de tu rentabilidad para comprar un cliente que apenas se paga a sí mismo.

Eres rentable hoy. Ese plan de $10.000 convierte esa rentabilidad en una apuesta con retorno esperado cercano a cero y riesgo real de ser negativo. No le des.