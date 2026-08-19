# Claude Opus 4.7 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 18.865s | tokens_per_second: 46.1
- input_tokens: 300 | output_tokens: 869
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y consejos prácticos para un emprendedor.

## Respuesta completa

No. Frena. Tu cálculo tiene tres errores que, corregidos, cambian la respuesta.

**Error 1: mal calculaste la vida del cliente.**
Con churn mensual del 8%, la vida promedio no es 24 meses, es 1/0,08 = **12,5 meses**. No dos años.

**Error 2: ignoraste el margen bruto.**
El LTV se calcula sobre el margen, no sobre el ingreso. Un cliente que paga $35 pero te cuesta 30% en infraestructura y pagos, te deja $24,50 de margen por mes.

**Error 3 (consecuencia): tu LTV real.**
LTV = (ARPU × margen) / churn = (35 × 0,70) / 0,08 = **$306**.

No $840. **$306.**

**Números corregidos:**
- LTV: $306
- CAC: $290
- LTV/CAC: **1,05**

Estás recuperando apenas el costo de adquirir el cliente durante toda su vida. Sin ganancia. Y encima:

- **Payback del CAC**: 290 / 24,50 = **11,8 meses**. Prácticamente toda la vida del cliente pagando el CAC. Cero flujo libre para reinvertir en el mes.
- **Financiación**: si metés $10.000 este mes, adquirís ~34 clientes que te devuelven ~$833/mes en margen. Vas a estar en rojo de caja muchos meses antes de recuperar, aunque en el papel "no pierdas".

**Qué haría antes de darle:**

1. **Atacar el churn.** Bajarlo de 8% a 4% duplica el LTV a $612 y LTV/CAC pasa a 2,1. Eso sí es escalable. Es la palanca más grande que tenés.
2. **Bajar el CAC** o segmentar campañas: ¿ese $290 es promedio o hay canales/segmentos con CAC de $150? Escalá esos primero.
3. **Subir precio o ARPU** (upsells, plan anual con descuento que mejora caja y reduce churn).
4. **Probar con $1.000–2.000, no $10.000.** Medí CAC real de la campaña (no el histórico) antes de escalar.

Regla simple: LTV/CAC < 3 y payback > 12 meses = no escalar con pauta. Optimizá la unidad económica primero, después metés combustible.

¿Querés que veamos cuál de las palancas (churn, CAC, precio) te da más upside con los datos que tenés?