# Claude Sonnet 5.5 — reasoning/business_analysis

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.09 | quality: 9.76
- latency_total: 38.896s | tokens_per_second: 132.0
- input_tokens: 256 | output_tokens: 5136
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

# Análisis SaaS: Q1

## 1. Métricas clave

**Supuestos:** el churn se calcula sobre usuarios al cierre del mes (no tengo los usuarios de inicio de enero). El ARPU es constante en $15 (MRR ÷ usuarios), así que no hay expansión de ingresos. No incluyo margen bruto.

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| **Churn rate mensual** | 3.75% | 3.85% | **4.59%** |
| Churn sobre usuarios de inicio de mes | n/d | 4.33% | 5.04% |
| **Crecimiento de usuarios/MRR** | n/d | 12.5% | **9.6%** |
| Altas brutas (nuevos usuarios) | n/d | 202 | 198 |
| **LTV/CAC (reportado)** | 4.94 | 4.51 | 5.23 |
| **LTV implícito** (ARPU ÷ churn) | $400 | $390 | **$327** |
| **LTV/CAC con LTV implícito** | 4.7 | 4.2 | **4.2** |
| Payback del CAC | 5.7 meses | 6.1 meses | 5.2 meses |
| **NRR mensual** | n/d | 95.7% | **95.0%** |
| NRR anualizado | n/d | ~59% | ~54% |

*NRR = (MRR inicial − MRR perdido por churn + expansión) ÷ MRR inicial. Como el ARPU es plano, asumo expansión = 0 y que cada churn pierde $15.*

## 2. Tendencias preocupantes

1. **El churn se acelera.** Los churns absolutos suben 31% de febrero a marzo (52 → 68), mientras la base solo crece 9.6%.
2. **El crecimiento se desacelera.** Pasó de 12.5% a 9.6%. Las altas brutas están estancadas (~200/mes), así que el churn se come una porción cada vez mayor: 26% de las altas en febrero y 34% en marzo.
3. **Tu LTV reportado probablemente está inflado.** Baja solo de $420 a $408, pero con el churn real de marzo el LTV implícito es ~$327 (o ~$297 con churn sobre base inicial). El LTV/CAC "5.2" en realidad es ~4.2, o ~3.8 con la base inicial. Sigue siendo sano, pero la dirección es mala.
4. **El CAC bajó a $78 justo cuando subió el churn.** Puede ser coincidencia, pero también puede indicar que estás captando usuarios más baratos y de menor calidad. Conviene validarlo.
5. **NRR por debajo de 100% y sin expansión.** El ARPU es exactamente $15 los tres meses. Todo el crecimiento depende de adquirir clientes nuevos, y el NRR anualizado de ~54% implica perder casi la mitad del MRR en un año sin reposición.
6. **Techo estructural de crecimiento.** Usuarios en equilibrio ≈ altas mensuales ÷ churn rate. Con ~195 altas y 5% de churn, el techo es ~3,900 usuarios (~$58k MRR). A 3% sería ~6,500.

## 3. Tres acciones concretas

**1. Diagnosticar y atacar el churn de marzo (prioridad máxima)**
- Haz un análisis de cohortes: ¿los 68 churns vienen de usuarios de enero, febrero o marzo? ¿De qué canal?
- Lanza una encuesta de salida y llama a los 10-15 últimos churns.
- Revisa el onboarding: mide qué % activa el producto en los primeros 7 días y refuerza esa etapa.
- **Meta:** bajar el churn a <3.75% en 60 días. Equivale a ~20 clientes menos perdidos por mes, unos $300 de MRR retenido por cada mes, acumulativo.

**2. Crear expansión de ingresos y reducir churn con planes anuales**
- Tu ARPU lleva 3 meses clavado en $15. Introduce tiers, add-ons o precios por uso.
- Ofrece plan anual con 15-20% de descuento. Reduce churn y mejora el cash flow.
- **Meta:** llevar el NRR a ≥100%.

**3. Medir calidad por canal, no solo CAC**
- Calcula CAC, retención a 30/60 días y LTV por canal de adquisición.
- Si los canales baratos de marzo retienen peor, reasigna presupuesto aunque el CAC suba un poco.
- Recalcula el LTV con tu churn real, y mejor aún con margen bruto, y úsalo como métrica oficial.

## 4. Proyección de abril

**Supuestos del caso base:** altas brutas ~195 (tendencia ligeramente a la baja), churns ~81 (la tasa sube ~0.5 pp más), ARPU $15, CAC ~$85.

| Escenario | Altas | Churns | Usuarios | MRR | Crecimiento |
|---|---|---|---|---|---|
| Optimista (churn se estabiliza) | 200 | 68 | 1,612 | $24,180 | 8.9% |
| **Base (tendencia continúa)** | 195 | 81 | **1,594** | **$23,910** | 7.7% |
| Pesimista (churn sigue acelerando) | 190 | 90 | 1,580 | $23,700 | 6.8% |

**Métricas proyectadas del caso base:**
- Churn rate: ~5.1% (sobre usuarios al cierre)
- NRR mensual: ~94.5%
- LTV implícito: ~$295, frente a ~$401 si sigues la tendencia del LTV reportado
- LTV/CAC: ~3.5 con el LTV implícito, 4.7 con el reportado

Si el churn sigue subiendo y las altas no crecen, el crecimiento neto se desacelera cada mes. Marzo-abril es el momento de actuar, antes de que el churn se consolide como nivel "normal".

## Datos que me ayudarían a afinar el análisis
- Usuarios al inicio de enero, para calcular el churn de enero con precisión.
- Churn por cohorte y canal.
- Margen bruto, para un LTV real.
- Si hay expansión o contracción de MRR que el ARPU plano esté ocultando.
- Cómo calculas el LTV hoy, porque no coincide con ARPU ÷ churn.