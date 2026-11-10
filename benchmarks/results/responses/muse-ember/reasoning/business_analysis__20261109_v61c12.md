# Muse Ember — reasoning/business_analysis

- model_id: `meta/muse-ember`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 11.049s | tokens_per_second: 439.0
- input_tokens: 169 | output_tokens: 4850
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

Creces, pero cada vez a un coste mayor de reposición. El problema no es adquisición, es retención.

### 1. Métricas clave calculadas

ARPU es constante: **$15/mes** en los 3 meses ($18,000/1,200 = $20,250/1,350 = $22,200/1,480). Todo el crecimiento viene de nuevos usuarios, no de expansión.

| Métrica | Enero | Febrero | Marzo | Tendencia |
| :--- | :--- | :--- | :--- | :--- |
| **Usuarios** | 1,200 | 1,350 | 1,480 | |
| **MRR** | $18,000 | $20,250 | $22,200 | |
| **Growth Rate usuarios/MRR** | - | **+12.5%** | **+9.6%** | Desacelerando |
| **Altas netas** | - | +150 | +130 | -20 |
| **Altas brutas** (netas + churns) | - | 202 | 198 | Estancadas |
| **Churns** | 45 | 52 | 68 | **+51% en 2 meses** |
| **Churn Rate mensual** * | 3.75% | 4.33% | **5.04%** | Acelerando |
| **Vida media del cliente** (1/churn) | 26.7 meses | 23.1 meses | **19.8 meses** | Cayendo |
| **CAC** | $85 | $92 | $78 | Volátil |
| **Payback CAC** (CAC/ARPU) | 5.7 meses | 6.1 meses | 5.2 meses | |
| **LTV reportado** | $420 | $415 | $408 | -2.9% |
| **LTV/CAC reportado** | 4.94x | 4.51x | 5.23x | Mejora en marzo solo por CAC |
| **NRR estimado** ** | ~96.3% | ~95.7% | **~95.0%** | <100% siempre |

\* Churn Rate = churns / usuarios a inicio de mes. Para enero es aproximado.
\** NRR exacto no se puede calcular sin datos de upsell/expansión. Como el ARPU es plano en $15, no hay expansión. NRR proxy = 100% - churn. Un SaaS sano está >100%, los mejores >110%.

**Alerta importante:** Tu LTV reportado de $408 en marzo no cuadra con tu churn actual. Con churn de 5.04%, la vida futura esperada es 19.8 meses x $15 = **$297 de LTV forward**, no $408. El LTV que reportas es histórico, el real hacia adelante ya está cayendo mucho más rápido. Eso pone tu LTV/CAC forward en 3.8x, no en 5.23x.

### 2. Tendencias preocupantes

**1. Churn descontrolado:** Pasaste de perder $675 de MRR en enero a **$1,020 de MRR en marzo** (68 x $15). El salto de febrero a marzo fue el mayor: +16 churns. Si no se frena, te comes el crecimiento.

**2. Growth que se desacelera:** +12.5% a +9.6%. Las altas brutas están planas (202 -> 198), pero las bajas suben. Cada mes necesitas adquirir más para crecer lo mismo.

**3. LTV erosionándose:** $420 -> $415 -> $408. Es la consecuencia directa del churn. Tu cliente vive 7 meses menos que en enero.

**4. CAC volátil y poco fiable:** Subió +8.2% en febrero a $92 y bajó -15.2% en marzo a $78. Esa bajada de marzo mejora el ratio en el papel, pero si ese canal barato trae usuarios de baja calidad, explica el salto de churn de marzo. Hay que sospechar de la cohorte de febrero/marzo.

**5. NRR <100% y ARPU plano:** No estás monetizando a los que se quedan. Depende 100% de conseguir logos nuevos, que es lo más caro.

### 3. Tres acciones concretas basadas en tus datos

**1. Plan de rescate de churn en 14 días - Prioridad #1**
No adquieras más hasta entender marzo. Haz exit interviews a los 68 churns de marzo y clasifica por antigüedad, plan y canal de adquisición. Implementa un play de salvamento para usuarios con 30-60 días (donde probablemente está la fuga): check-in, onboarding 1:1, descuento por cambio a anual.

*Objetivo medible:* Bajar churns de 68 a <55 en abril. Cada churn evitado = $15 MRR recurrente + $297 de LTV forward salvado. Evitar 13 churns = $195 MRR/mes que no tienes que recomprar a $78 CAC.

**2. Subir NRR de 95% a >100% en 60 días**
Con ARPU clavado en $15, tienes una sola palanca. Lanza una expansión simple: un add-on o un plan Pro ($29) con una feature que hoy piden los usuarios que se quedan. O migración forzada a pago anual con 2 meses gratis para bajar churn mensual.

*Impacto:* Un aumento de ARPU de solo $2 sobre tu base actual = **+$2,960 MRR sin adquirir un solo usuario**. Eso compensaría 3 meses de churn actual.

**3. Congelar y auditar adquisición**
Analiza CAC y churn por cohorte/canal de febrero. Si el CAC de $92 vino de un canal que luego tuvo churn alto en marzo, paúsalo aunque ahora parezca barato. No persigas el CAC de $78 de marzo si trae clientes de 10 meses de vida en vez de 24.

*Objetivo:* Mantener Payback <6 meses, pero con LTV/CAC forward >3.5x. Calidad sobre volumen: 198 altas brutas malas son peores que 170 buenas.

### 4. Proyección para Abril si nada cambia

Supuestos: altas brutas siguen bajando -4/mes (198 -> 194), churn rate sube +0.71pp como en marzo (5.04% -> 5.75%), ARPU se mantiene en $15, CAC vuelve a su media de $85.

| Proyección Abril | Valor |
| :--- | :--- |
| **Churns** | ~85 (5.75% sobre 1,480) |
| **Altas brutas** | ~194 |
| **Usuarios finales** | **~1,589** (+7.4%) |
| **MRR** | **~$23,835** (+7.4%) |
| **LTV reportado (tendencia)** | ~$400 |
| **LTV forward real (1/churn x ARPU)** | **~$261** |
| **CAC estimado** | ~$85 |
| **LTV/CAC forward** | ~3.1x |

En resumen: seguirías creciendo en absoluto, pero a ritmo decreciente. En 2-3 meses más con churn al 6% mensual, tu vida media bajará de 16 meses y necesitarás >200 altas brutas mensuales solo para mantenerte en 1,600 usuarios.

**Conclusión:** Deja de optimizar CAC por un mes. Tu ratio reportado de 5.23x te da una falsa sensación de seguridad. Con churn al 5% y NRR al 95%, estás en una cubeta agujereada: entra agua (198 altas), pero se sale más rápido cada mes (68 bajas).