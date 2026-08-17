# Claude Haiku 4.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 8.204s | tokens_per_second: 74.7
- input_tokens: 238 | output_tokens: 613
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y consejos prácticos para un emprendedor.

## Respuesta completa

# No. Tus números tienen dos problemas críticos.

## Problema 1: LTV mal calculado

Tu cliente **no se queda 2 años**. Con churn del 8% mensual, la vida útil real es mucho más corta.

**Cálculo correcto:**
- Vida útil promedio = 1 / churn = 1 / 0.08 = **12.5 meses** (no 24)
- LTV = $35 × 12.5 × 0.70 = **$306 en margen bruto**

(El margen del 70% es crítico aquí: solo puedes contar ingresos que efectivamente contribuyen a pagar el CAC)

## Problema 2: LTV/CAC está bajo, no alto

Con números reales:
- LTV/CAC = $306 / $290 = **1.05**

Eso es **peligroso**. Estás pagando casi tanto para adquirir un cliente como el margen que genera en su vida útil.

## Lo que eso significa en práctica:

Si gastas $10.000 en publicidad:
- Adquieres ~34 clientes ($10.000 / $290)
- Generan ~$10.404 en margen bruto total
- **Ganancia neta: ~$400** (si todo funciona perfecto)

Pero cualquier fricción te quiebra:
- Tasa de conversión 5% más baja → pierdes dinero
- CAC real sube a $310 → pierdes dinero
- Churn sube a 9% → pierdes dinero

## ¿Qué hacer?

Antes de escalar publicidad:

1. **Baja el churn** (es tu apalancador real). 8% es alto. ¿Qué hace que la gente se vaya?
2. **Sube el ticket o margen** - ¿hay un plan premium? ¿Puedes optimizar costos?
3. **Reduce CAC** - ¿hay canales más baratos? ¿Referrals? ¿Content?

Con churn al 5% y los demás números igual, tu LTV sería $490 y LTV/CAC = 1.69. Todavía bajo, pero movible.

**No gastes $10k. Gasta $1-2k en tests, mide bien, y enfócate en retención primero.**