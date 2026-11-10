# Claude Fable 5.2 — reasoning/business_analysis

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.85 | quality: 9.76
- latency_total: 42.178s | tokens_per_second: 103.1
- input_tokens: 256 | output_tokens: 4349
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

## Entrada exacta (lo que recibió el modelo)

**user:**

Analiza estos datos de mi SaaS:

Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC $78, LTV $408

Necesito:
1. Calcula las metricas clave (churn rate, growth rate, LTV/CAC ratio, net revenue retention)
2. Identifica tendencias preocupantes
3. Sugiere 3 acciones concretas basadas en los datos
4. Proyecta abril si las tendencias continuan


## Respuesta completa

# Análisis de tu SaaS (enero-marzo)

## 1. Métricas clave

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| Crecimiento de usuarios y MRR | n/d | +12.5% | +9.6% |
| Churn rate mensual | ≈3.8%* | 4.3% | 5.0% |
| LTV/CAC | 4.9x | 4.5x | 5.2x |
| NRR (estimado) | n/d | 95.7% | 95.0% |
| ARPU | $15 | $15 | $15 |
| Altas brutas | n/d | 202 | 198 |
| Quick ratio (altas/bajas) | n/d | 3.9 | 2.9 |

Supuestos:
- **Churn rate:** está calculado sobre los usuarios al inicio del mes. *Para enero no tengo el dato de diciembre, así que usé los usuarios de enero como aproximación.
- **NRR:** no tengo datos de expansión ni contracción. Como el ARPU es exactamente $15 los tres meses, asumí expansión cero, así que NRR = 100% − churn.

## 2. Tendencias preocupantes

- **El churn se acelera más rápido que el crecimiento.** Las bajas crecieron 16% en febrero y 31% en marzo, mientras la base creció 12.5% y 9.6%. Un churn mensual de 5% equivale a perder cerca del 46% de los clientes al año.

- **El crecimiento se frena aunque la adquisición sigue estable.** Las altas brutas están planas (alrededor de 200 al mes), pero las altas netas bajaron de 150 a 130. El quick ratio cayó de 3.9 a 2.9, y lo saludable es estar por encima de 4.

- **Tu LTV probablemente está sobreestimado.** Con ARPU de $15 y churn de 5%, el LTV implícito es $15 / 0.05 ≈ $300, no $408. Tu LTV/CAC real sería entonces cerca de 3.8x en lugar de 5.2x: sigue siendo sano, pero con mucho menos margen del que parece.

- **No hay ingresos por expansión.** Con el ARPU fijo en $15, el NRR está por debajo de 100% y cayendo, así que todo el crecimiento depende de adquirir clientes nuevos.

- **El CAC más bajo coincide con el churn más alto.** En marzo el CAC bajó a $78 y las bajas subieron a 68. Puede que estés atrayendo clientes más baratos pero de peor calidad. Los datos no lo confirman, pero conviene revisarlo.

## 3. Tres acciones concretas

1. **Diagnosticar las 68 bajas de marzo.** Segméntalas por antigüedad, canal de adquisición y plan, y contacta a 15-20 de esos clientes. Si se concentran en usuarios de menos de 60 días, el problema es de onboarding o de calidad del canal; si son antiguos, es de producto o competencia. Volver a 45 bajas al mes te ahorraría unos $1,800 mensuales en CAC de reposición (23 clientes × $78).

2. **Crear una vía de expansión de ingresos.** Las opciones más directas son un plan anual con descuento (por ejemplo, 2 meses gratis), que además reduce el churn, y un tier superior o add-ons. Un objetivo razonable es llevar el NRR por encima de 100% en 6 meses.

3. **Medir los canales por retención, no solo por CAC.** Calcula el churn a 30, 60 y 90 días por canal y mueve presupuesto hacia los que traen clientes que se quedan, aunque cuesten más. No aumentes el gasto en adquisición hasta estabilizar el churn.

## 4. Proyección de abril (si todo sigue igual)

| Métrica | Abril (proyectado) | Lógica |
|---|---|---|
| Altas brutas | ~200 | Estables en feb-mar |
| Bajas | ~85 | Churn sube a ~5.7% (+0.7 pp por mes) |
| Usuarios | ~1,595 | 1,480 + 200 − 85 |
| MRR | ~$23,900 | 1,595 × $15 |
| Crecimiento | ~7.8% | Tercer mes de desaceleración |
| NRR | ~94.3% | Sin expansión |
| LTV reportado | ~$400 | Caída de $5-7 por mes |
| CAC | ~$85 | Sin tendencia clara; promedio de los 3 meses |
| LTV/CAC reportado | ~4.7x | Con LTV implícito (~$260) sería ~3.1x |

Es una extrapolación con solo tres meses de datos, así que tómala como orden de magnitud. En términos absolutos seguirías creciendo, pero el LTV/CAC implícito quedaría en el umbral mínimo de 3x. Si el churn sigue subiendo a este ritmo y las altas se mantienen en 200, el crecimiento neto llegaría a cero en unos 12 meses.