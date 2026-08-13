# Claude Sonnet 5 (suscripción) — reasoning/business_analysis

- model_id: `claude-sonnet-5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 123.331s | tokens_per_second: 84.3
- input_tokens: 2 | output_tokens: 10398
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

# Análisis SaaS — Enero a Marzo

## 1. Métricas clave

Antes de calcular: tu ARPU es **exactamente $15/usuario los tres meses** ($18,000/1,200 = $20,250/1,350 = $22,200/1,480 = 15.00). Esto importa porque significa que **no hay ingreso por expansión** — todo el crecimiento de MRR viene de logos nuevos, cero upsell. Lo uso más abajo.

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| Churn rate (churns / usuarios inicio mes) | 3.75% | 4.33% | 5.04% |
| Growth rate (usuarios y MRR, van iguales) | — | 12.50% | 9.63% |
| LTV/CAC (reportado) | 4.94 | 4.51 | 5.23 |
| Net Revenue Retention* | — | 95.67% | 94.96% |

*NRR calculado como `1 − churn rate` porque ARPU es plano (no hay expansión ni contracción por precio, solo pérdida de logos). Fórmula: `(MRR inicio − MRR perdido por churn) / MRR inicio`.

**Dato que no pediste pero necesitas ver:** tu LTV reportado (420→415→408) es una métrica *rezagada* — probablemente un promedio de cohorte histórico. Si calculo el LTV que implica el churn **actual** de cada mes (`ARPU / churn rate`), la foto es mucho peor:

| | Enero | Febrero | Marzo |
|---|---|---|---|
| LTV implícito (churn actual) | $400 | $346 | $298 |
| LTV/CAC implícito | 4.71 | **3.76** | **3.82** |

El LTV/CAC "oficial" dice que marzo mejoró (4.51→5.23) porque el CAC bajó a $78. El LTV/CAC real-time dice lo contrario: estás a un ajuste de churn de cruzar el piso de 3x que hace que el negocio deje de tener sentido unitario. La mejora de marzo es un espejismo de CAC barato tapando una economía de cliente que se deteriora.

## 2. Tendencias preocupantes (ordenadas por severidad)

1. **El churn se está acelerando, no solo subiendo.** 3.75% → 4.33% → 5.04% es +16% relativo cada mes, dos meses seguidos. Si esa pendiente sigue, en 3-4 meses estás en 7-8% mensual — churn anualizado de ahí es >60%. Esto es lo único que importa resolver primero.

2. **El crecimiento neto se desploma por churn, no por freno en adquisición.** El MRR nuevo bruto está estable (Feb $3,030 → Mar $2,970, -2%). El MRR perdido por churn está disparado (Feb $780 → Mar $1,020, **+31%**). Resultado: MRR neto nuevo cayó de $2,250 a $1,950 (-13% en un mes). Tu equipo de ventas/marketing está haciendo su trabajo; el problema es 100% retención.

3. **NRR por debajo de 100% y bajando, sin ningún motor de expansión.** 95.67% → 94.96%. Un SaaS sano vive con NRR 100-120%+ (la expansión de clientes existentes compensa el churn). Tú tienes ARPU perfectamente plano — cero upsell, cero cross-sell — así que cada punto de churn pega directo al NRR sin ningún colchón.

4. **CAC volátil sin patrón claro** ($85 → $92 → $78). No es una tendencia limpia, es ruido — pero la caída de marzo coincide exactamente con el salto de churn. Hipótesis a validar, no conclusión: ¿el canal más barato de marzo trajo usuarios de peor calidad/intención que cancelan más rápido? Correlación temporal, no until lo cruces por cohorte de adquisición.

## 3. Tres acciones concretas

**1. Cohort analysis de marzo por canal de adquisición — antes de mover un dólar más de presupuesto.** Cruza los 198 usuarios nuevos de marzo (CAC $78) contra los 202 de febrero (CAC $92) por canal y mide su churn a 30/60 días. Si el canal barato de marzo tiene 2x el churn del canal caro de febrero, ese CAC de $78 es una ilusión — estás comprando usuarios que se van antes de pagar de vuelta el CAC. Esto responde la pregunta #4 con datos, no con hipótesis.

**2. Exit survey obligatorio + intervención en el momento de cancelar, ya — no la próxima iteración de producto.** Con 68 churns en marzo y subiendo, necesitas la causa raíz esta semana, no en el próximo research sprint. Encuesta de 2 preguntas al cancelar (por qué te vas / qué te haría quedarte) + oferta de retención en el flujo de cancelación. Meta: bajar la tasa de marzo (5.04%) de vuelta a la de enero (3.75%) en 60 días — eso solo, sin tocar adquisición, mueve el MRR neto de $1,950 a algo cercano a $2,800/mes.

**3. Construir UN motor de expansión antes de fin de trimestre.** ARPU plano en $15 durante 3 meses seguidos significa que no tienes ningún mecanismo de upsell — ni plan superior, ni add-on, ni upgrade prompt. Es la palanca de crecimiento más barata que existe (no paga CAC) y hoy vale $0. Con NRR cayendo bajo el 95%, necesitas que la expansión empiece a compensar el churn, no solo la adquisición nueva.

## 4. Proyección abril (si las tendencias de marzo continúan sin intervención)

Metodología: extrapolo churn rate (+16% relativo mensual, patrón de los últimos 2 meses) y nuevos usuarios (~flat, -2% como feb→mar). CAC lo dejo como rango porque **no tiene tendencia limpia** — dos puntos no hacen una línea, y forzar una sería falsa precisión.

| Métrica | Marzo (real) | Abril (proyectado) |
|---|---|---|
| Usuarios | 1,480 | **~1,589** (+196 nuevos, -87 churn) |
| Churn rate | 5.04% | **~5.85%** |
| Growth rate | 9.63% | **~7.4%** |
| MRR (ARPU flat $15) | $22,200 | **~$23,835** |
| MRR nuevo neto | $1,950 | **~$1,635** (-16%) |
| LTV implícito (churn-based) | $298 | **~$256** |
| LTV/CAC implícito | 3.82 | **~3.2** (con CAC ~$80) |
| NRR | 94.96% | **~94.2%** |

**Lectura del número que importa:** si el churn sigue acelerando a este ritmo y nadie interviene, el MRR neto nuevo (que ya cayó 13% de feb a marzo) sigue cayendo ~15-16%/mes. Con esa pendiente, llegas a MRR neto nuevo ≈ $0 en 2-3 meses más — es decir, **crecimiento total plano para junio/julio, pase lo que pase con adquisición.** No es una certeza (es una línea recta sobre 2 puntos de dato), pero es la advertencia que estos números están dando: el problema no es de crecimiento, es de retención, y el reloj corre más rápido de lo que el LTV/CAC "oficial" te está mostrando.