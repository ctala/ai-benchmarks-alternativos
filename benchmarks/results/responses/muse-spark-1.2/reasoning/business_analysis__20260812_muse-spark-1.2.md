# Muse Spark 1.2 — reasoning/business_analysis

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.13 | quality: 9.44
- latency_total: 15.483s | tokens_per_second: 197.4
- input_tokens: 168 | output_tokens: 3056
- judge_score: 4.6 | justificación: 

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

Análisis de tu SaaS - Q1. Hay señales de alerta importantes.

Tu ARPU es de **$15 en los 3 meses** `MRR / Usuarios`. Eso significa que no estás haciendo upsell/expansión y todo tu crecimiento es por volumen.

### 1. Métricas Clave Calculadas

| Métrica | Enero | Febrero | Marzo | Fórmula |
| :--- | :--- | :--- | :--- | :--- |
| **Churn Rate** | **3.75%** | **3.85%** | **4.59%** | `Churns / Usuarios Totales del mes` |
| **Churn Rate Real*** | - | 4.33% | 5.04% | `Churns / Usuarios Inicio del mes` |
| **User Growth Rate** | - | 12.50% | 9.63% | `(Usuarios mes actual - mes anterior) / mes anterior` |
| **MRR Growth Rate** | - | 12.50% | 9.63% | `(MRR actual - MRR anterior) / MRR anterior` |
| **LTV / CAC Ratio** | **4.94x** | **4.51x** | **5.23x** | `LTV / CAC` |
| **Net Revenue Retention (NRR)**** | - | 95.67% | 94.96% | `(MRR inicial - MRR Churneado) / MRR inicial` |
| **MRR Churneado** | $675 | $780 | $1,020 | `Churns * $15 ARPU` |
| **Usuarios Nuevos Netos** | - | +150 | +130 |  |
| **Usuarios Nuevos Brutos** | - | 202 | 198 | `Netos + Churns` |

> *El Churn Rate Real es más preciso para SaaS. En ambos cálculos la tendencia es la misma: al alza.
> **Tu NRR es sin expansión porque tu ARPU es plano. Es esencialmente tu Gross Revenue Retention. Un NRR saludable en SaaS es >100%.

**Benchmark rápido:** LTV/CAC >3x es saludable, estás bien ahí. Pero Churn >4% mensual es PELIGROSO. Un churn >5% significa que pierdes más del 46% de tu base al año.

### 2. Tendencias Preocupantes

**1. El Churn se está acelerando:** No solo sube, sino que la aceleración es mayor cada mes. Pasaste de +7 churns de Ene-Feb a +16 churns de Feb-Mar. Tu churn rate creció un 22% en 60 días. Es tu mayor riesgo.

**2. Desaceleración del crecimiento a pesar de un CAC más barato:** En Marzo bajaste tu CAC de $92 a $78 (-15%), pero creciste MENOS `9.63% vs 12.5%`. Captaste menos usuarios brutos `198 vs 202` y menos MRR neto `$1,950 vs $2,250`. Estás trayendo usuarios más baratos pero de peor calidad que se van más rápido.

**3. LTV en caída libre y NRR por debajo de 95%:** Tu LTV bajó de $420 a $408 `-$12 en 3 meses`. Si tu ARPU es fijo en $15, la caída de LTV solo se explica porque los clientes se quedan menos tiempo. Tu NRR cayó de 95.67% a 94.96%. Sin expansión de ingresos, cada mes tienes que vender más solo para mantenerte en el mismo lugar.

**Conclusión:** Estás en un patrón clásico de "leaky bucket" - cubeta con fuga. Estás llenando la cubeta con más agua pero la fuga se hace más grande.

### 3. 3 Acciones Concretas Basadas en Datos

**ACCIÓN 1: Frenar el churn de Marzo de forma urgente - Ataca la cohorte de Febrero**
*   **Dato que la gatilla:** El salto de 5.04% de churn en Marzo coincide con los usuarios adquiridos en Febrero, cuando tu CAC fue el más alto `$92`.
*   **Qué hacer:** Esta semana haz 15 entrevistas de salida a los 68 churns de Marzo. Implementa un email de onboarding mejorado + un check-in humano en el día 14. Crea una oferta de rescate: plan anual con 20% descuento para usuarios que intenten cancelar.
*   **KPI a medir:** Bajar churn rate de Marzo de 5.04% a <4.0% en Abril.

**ACCIÓN 2: Auditar la calidad de adquisición, no solo el costo**
*   **Dato que la gatilla:** LTV/CAC subió a 5.23x en Marzo, parece bueno, pero es engañoso porque el LTV está cayendo.
*   **Qué hacer:** Pausa el canal/campaña que escalaste en Marzo por ser barato. Haz un análisis de cohortes: ¿Qué canal trajo a los 68 churns? Calcula el CAC y Churn por canal. Es preferible pagar $92 por un usuario que se queda 28 meses que $78 por uno que se queda 15.
*   **KPI a medir:** CAC por canal vs. Retención a 30 días por canal.

**ACCIÓN 3: Crear expansión de ingresos para subir LTV y NRR**
*   **Dato que la gatilla:** ARPU clavado en $15 por 3 meses y NRR <100%. Tu LTV solo puede subir si sube ARPU o baja churn.
*   **Qué hacer:** Lanza en los próximos 30 días un add-on o plan Pro de $29. Haz un upsell a tus 200 usuarios más activos. Ofrece pago anual por adelantado `anual = 10 meses`. Esto sube LTV y mejora tu flujo de caja inmediatamente.
*   **KPI a medir:** Pasar de ARPU $15 a $16.5 y llevar NRR de 94.96% a >100% en 60 días.

### 4. Proyección Abril si las tendencias continúan

Si no haces nada, esta es la proyección lineal:

| Métrica Proyectada Abril | Valor Estimado | Razonamiento |
| :--- | :--- | :--- |
| **Usuarios Totales** | **~1,590 - 1,610** | Crecimiento desacelerando: +110 a +130 netos vs +130 en Marzo |
| **MRR** | **~$23,850 - $24,150** | Crecimiento de +7.5% a +8.8% vs 9.63% anterior |
| **Churns** | **~78 - 93** | Churn rate sube a **5.1% - 5.5%** |
| **MRR Churneado** | **~$1,170 - $1,395** | Te comerá casi todo tu nuevo MRR |
| **LTV** | **~$400 - $402** | Sigue cayendo -$6/mes |
| **CAC** | **~$80 - $85** | Promedio volátil |
| **LTV/CAC** | **~4.7x - 5.0x** | Se mantiene "bien" pero ocultando el problema |

**Escenario pesimista:** Si la aceleración del churn continúa `+16 churns más que el mes anterior`, llegarás a **93 churns en Abril**. Tu crecimiento neto sería de solo +85 usuarios y tu MRR neto de apenas +$1,275. En 3 meses más estarías estancado.

> ¿Quieres que te arme el modelo de cohortes y el cálculo de cuántos meses te quedan hasta el estancamiento si el churn llega a 6%?