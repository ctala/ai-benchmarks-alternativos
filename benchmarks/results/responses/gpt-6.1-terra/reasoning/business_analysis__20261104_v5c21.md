# GPT-6.1 Terra — reasoning/business_analysis

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.31 | quality: 9.76
- latency_total: 19.481s | tokens_per_second: 77.8
- input_tokens: 168 | output_tokens: 1515
- judge_score: 5.0 | justificación: 

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

## 1. Métricas clave

Para calcular el churn, supongo que los usuarios reportados son la **base al cierre de cada mes** y que los churns son usuarios perdidos durante ese mes. Sin la base inicial de enero, no puede calcularse su tasa.

| Métrica | Enero | Febrero | Marzo |
|---|---:|---:|---:|
| Churn rate | No disponible | 4,33 % | 5,04 % |
| Crecimiento neto de usuarios | No disponible | 12,50 % | 9,63 % |
| Crecimiento de MRR | No disponible | 12,50 % | 9,63 % |
| LTV/CAC | 4,94 | 4,51 | 5,23 |
| MRR por usuario reportado | $15 | $15 | $15 |

**Cálculos:** churn de febrero = 52 / 1.200; churn de marzo = 68 / 1.350. El crecimiento compara cada cierre con el cierre anterior.

**Net Revenue Retention (NRR): no se puede calcular** con estos datos. Se necesita el MRR de una misma cohorte al inicio y al final del período, separando expansión, contracción y cancelaciones, sin incluir clientes nuevos:

\[
NRR = \frac{MRR\ inicial + expansión - contracción - MRR\ perdido}{MRR\ inicial}
\]

## 2. Tendencias preocupantes

- **El churn empeora:** pasa de 4,33 % en febrero a 5,04 % en marzo; las bajas suben de 52 a 68.
- **El crecimiento neto se desacelera:** de 12,50 % a 9,63 %, tanto en usuarios como en MRR. El aumento mensual de MRR baja de $2.250 a $1.950.
- **El LTV cae:** de $420 en enero a $408 en marzo, aproximadamente un **2,9 %**. El LTV/CAC mejora en marzo por la caída del CAC, pero eso no elimina el deterioro de retención.

## 3. Tres acciones concretas

1. **Investigar las bajas recientes.** Segmentar los 68 churns de marzo por antigüedad, plan y uso; entrevistar a una muestra para identificar las principales causas y priorizar una corrección.
2. **Reforzar la activación y retención.** Crear una secuencia de onboarding y alertas para usuarios inactivos en sus primeros 30 días. Medir su efecto por cohorte, con el objetivo inicial de volver a una tasa de churn cercana al 4,33 % de febrero.
3. **Medir adquisición y expansión por cohorte.** Desglosar CAC y LTV por canal, y registrar el MRR inicial, las ampliaciones, reducciones y cancelaciones de cada cohorte. Esto permitirá calcular NRR y orientar el presupuesto hacia canales que retengan mejor, no solo los más baratos.

## 4. Proyección para abril

Como escenario orientativo, aplico el **cambio mensual absoluto promedio** observado entre enero y marzo:

| Métrica | Proyección de abril |
|---|---:|
| Usuarios | 1.620 |
| MRR | $24.300 |
| Churns | Aproximadamente 80 |
| Churn rate | Aproximadamente 5,41 % |
| CAC | $74,50 |
| LTV | $402 |
| LTV/CAC | 5,40 |
| NRR | No proyectable con los datos disponibles |

Con esta proyección, el crecimiento neto seguiría siendo positivo, pero el churn continuaría aumentando. **Es una extrapolación, no un pronóstico sólido:** solo hay dos cambios mensuales y el CAC, en particular, ha sido volátil.