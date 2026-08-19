# Claude Haiku 4.5 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.31 | quality: 8.4
- latency_total: 30.726s | tokens_per_second: 64.7
- input_tokens: 10 | output_tokens: 1988

## Respuesta completa

# No. Acá se rompe tu aritmética.

Tu LTV está mal calculado. Estás ignorando el churn.

## El recálculo real

Con **8% churn mensual**, tu cliente promedio no dura 24 meses. Dura:

**1 ÷ 0.08 = 12.5 meses**

Eso significa:
- Ingresos por cliente: $35 × 12.5 = **$437.50**
- Después de margen 70%: $437.50 × 0.70 = **$306.25** ← este es tu LTV

Tu ratio real:
- LTV/CAC = $306.25 ÷ $290 = **1.05**

No 2.9. **1.05.**

## Por qué esto es un problema

Eso quiere decir que:
- Gastas $290 en un cliente
- Recuperas $306 de margen bruto en toda su vida útil
- Te sobran $16 de ganancia

Pero aún tienes **costos operativos** (infraestructura, soporte, contabilidad, tu tiempo). Con ese margen de $16, no llegas a nada.

La regla es: **LTV/CAC ≥ 3**. Tú estás en 1.05.

## Qué hacer antes de meter los $10K

1. **Audita el churn.** ¿Es real 8% o hay un cohort de clientes que se cae en mes 1-2 mientras otros se quedan más? Si el 60% se va en 3 meses, tu problema no es de escala — es de product-market fit.

2. **Reduce el churn primero.** 
   - 8% → 5%: LTV sube a $490, ratio = 1.69 (mejor, pero bajo)
   - 8% → 3%: LTV sube a $817, ratio = 2.82 (casi ahí)

3. **O aumenta precio.** $35 → $49: LTV = $430, ratio = 1.48 (más respirable)

4. **O baja CAC** optimizando la campaña.

## Línea de fondo

Con 1.05 LTV/CAC, escalar ads es quemar plata. Cada cliente nuevo te cuesta casi lo que vale. La publicidad es rentable **cuando tu LTV/CAC es ≥3 y tu churn ≤5% mensual**.

Hoy tienes ni lo uno ni lo otro.

Arregla el churn. Después hablamos de $10K en ads.