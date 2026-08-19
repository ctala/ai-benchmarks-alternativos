# Muse Glimmer 30B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 52.067s | tokens_per_second: 40.8
- input_tokens: 204 | output_tokens: 2125
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y práctica de la situación del emprendedor.

## Respuesta completa

No. Con esos números escalar con $10k en ads te va a quemar caja.

Tu cálculo tiene 2 errores graves que matan la unidad económica:

**1. Estás usando ingresos y no margen, y asumiendo 24 meses de vida.**
Con 8% de churn mensual la vida media no es 2 años.

Vida media = 1 / churn mensual = 1 / 0,08 = 12,5 meses
Retención a 24 meses = 0,92^24 = 13,8%. El 86% ya se fue.

**2. El LTV hay que calcularlo sobre margen bruto, no sobre precio.**

LTV correcto = Precio x Margen Bruto / Churn mensual
LTV = $35 x 0,70 / 0,08 = $24,5 / 0,08 = **$306 por cliente**

Con tu CAC de $290:
LTV / CAC = 306 / 290 = **1,05**
Payback = CAC / (Precio x Margen) = 290 / 24,5 = **11,8 meses**

Incluso si te aferras a tu LTV de ingresos $840, con margen es $840 x 0,70 = $588. LTV/CAC = 2,03 < 3.

### Qué significa eso con $10.000

Clientes que compras: $10.000 / $290 = ~34 clientes
Margen bruto mensual que generan: 34 x $24,5 = $833
Primer mes pierdes $9.167 y necesitas casi 12 meses para recuperar el CAC.

Con 8% de churn mensual, de esos 34 clientes en 12 meses solo te quedan ~13. Nunca recuperas el CAC de los que se fueron antes del payback.

Regla de oro: LTV/CAC >= 3 y payback < 12 meses. Tú estás en 1,05 y 11,8 meses.

**No escales hasta que arregles la unidad económica.** Opciones:

* **Bajar churn:** Para llegar a LTV/CAC = 3 con CAC $290 necesitas churn ~2,8% mensual. De 8% a ~3% es donde está el dinero.
* **Bajar CAC:** Con churn 8% y margen 70% tu CAC máximo para 3:1 es $102.
* **Subir margen/precio:** $35 x margen 70% = $24,5 de contribución mensual. Necesitas más.

Haz un test pequeño para validar CAC y retención antes de meter $10k. Hoy la publicidad pagada te da un ROI de vida de ~5% y flujo de caja negativo durante un año.