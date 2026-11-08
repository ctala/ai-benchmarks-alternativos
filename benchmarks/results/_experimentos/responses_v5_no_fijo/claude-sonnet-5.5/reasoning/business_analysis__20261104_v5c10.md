# Claude Sonnet 5.5 — reasoning/business_analysis

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.07 | quality: 9.76
- latency_total: 43.417s | tokens_per_second: 130.4
- input_tokens: 256 | output_tokens: 5663
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

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

# Análisis de métricas SaaS (Ene-Mar)

## 1. Métricas clave

**Supuestos:** el ARPU es exactamente $15 los tres meses (MRR ÷ usuarios), así que cada churn equivale a $15 de MRR perdido. No tengo datos de diciembre, así que el churn de enero usa los usuarios finales y es aproximado. No tengo datos de expansión ni margen bruto.

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| **Churn rate** (churns ÷ usuarios al inicio) | ~3.75%* | 4.33% | **5.04%** |
| **Crecimiento de usuarios y MRR** | n/d | +12.5% | **+9.6%** |
| **Altas brutas** (netos + churns) | n/d | 202 | 198 |
| **MRR perdido por churn** | $675* | $780 | $1,020 |
| **NRR** | n/d | 95.7% | **95.0%** |
| **LTV/CAC reportado** | 4.94 | 4.51 | 5.23 |
| **LTV real** (ARPU ÷ churn) | ~$400 | $346 | **$298** |
| **LTV/CAC real** | ~4.7 | 3.8 | **3.8** |
| **Payback de CAC** (CAC ÷ ARPU) | 5.7 meses | 6.1 meses | 5.2 meses |

**Cómo se calculó el NRR:** (MRR inicial − MRR perdido) ÷ MRR inicial, sin expansión. Por ejemplo, en marzo (20,250 − 1,020) ÷ 20,250 = 95.0%. Un NRR mensual de 95% equivale a conservar solo ~54% del MRR en 12 meses.

## 2. Tendencias preocupantes

1. **El churn se está acelerando.** Los churns absolutos subieron 31% en marzo (52 → 68), mientras la base creció solo 9.6%. La tasa pasó de ~3.75% a 5.04%.
2. **El LTV reportado está inflado.** Dice $408, pero con el churn actual de marzo el LTV real es ~$298, un 27% menos. El LTV/CAC "5.2" en realidad es ~3.8 y viene cayendo desde ~4.7.
3. **El crecimiento se desacelera.** Pasó de 12.5% a 9.6%. Las altas brutas están estancadas en ~200/mes, así que el crecimiento solo se frena a medida que el churn crece.
4. **El NRR está por debajo de 100% y el ARPU está plano en $15.** No hay expansión de ingresos que compense las bajas.
5. **Posible problema de calidad de adquisición.** En marzo el CAC bajó (92 → 78) y a la vez subió el churn. Es una hipótesis, no una conclusión, pero puede indicar que los nuevos canales traen usuarios de menor calidad.
6. **Hay un techo estructural.** Con ~200 altas/mes y 5% de churn, la base se estabilizaría en ~4,000 usuarios (200 ÷ 0.05), a menos que cambie algo.

## 3. Tres acciones concretas

**1. Diagnosticar y reducir el churn (prioridad máxima)**
- Segmenta los 68 churns de marzo por canal de adquisición, mes de alta, plan y nivel de uso. Haz una encuesta de salida corta.
- Revisa el onboarding: ¿cuántos churns ocurren en los primeros 30 días?
- Pon alertas de usuarios en riesgo (baja actividad) y contáctalos antes de que cancelen.
- **Meta:** bajar de 5.0% a ~3.5% en 2-3 meses. Cada punto de churn evitado son ~15 usuarios y ~$220 de MRR por mes.

**2. Crear expansión de ingresos**
- Introduce planes por niveles, add-ons o precios por uso, y ofrece plan anual con descuento (reduce churn y mejora caja).
- **Ejemplo:** si 10% de tus usuarios (148) pagan +$10, ganas $1,480 de MRR, más de lo que pierdes por churn en un mes.
- **Meta:** NRR > 100%.

**3. Optimizar adquisición por calidad, no por CAC bajo**
- Calcula LTV/CAC y retención a 30/60 días **por canal**. Mide el CAC con churn real, no solo con el costo por alta.
- Reasigna presupuesto hacia los canales con mejor retención aunque su CAC sea más alto.
- Mientras el churn no baje, no escales el gasto: cada usuario nuevo se queda menos tiempo.

## 4. Proyección de abril

Supuestos si la tendencia continúa: el churn sube otros ~0.7 pp (de 5.04% a ~5.7% sobre la base inicial de 1,480) y las altas brutas siguen bajando ligeramente (~194).

| Métrica | Abril (tendencia actual) | Abril (churn se estabiliza en 5.04%) |
|---|---|---|
| Churns | ~84 | ~75 |
| Altas brutas | ~194 | ~198 |
| **Usuarios** | **~1,590** | ~1,603 |
| **MRR** | **~$23,850** | ~$24,045 |
| Crecimiento | +7.4% | +8.3% |
| NRR | ~94.3% | ~95.0% |
| LTV real | ~$263 | ~$298 |
| LTV/CAC real (CAC ~$85) | **~3.1** | ~3.5 |

En el escenario de tendencia actual, el LTV/CAC se acerca al umbral de 3, y el crecimiento sigue desacelerándose.

**Limitaciones:** son solo tres meses, así que la extrapolación es frágil. Además asumí un solo plan de $15, sin margen bruto (con margen, el LTV real y el LTV/CAC serían menores). Si me das datos por canal o cohorte, puedo afinar el diagnóstico del churn.