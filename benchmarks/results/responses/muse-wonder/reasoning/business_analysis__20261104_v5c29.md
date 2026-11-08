# Muse Wonder — reasoning/business_analysis

- model_id: `meta/muse-wonder`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 32.663s | tokens_per_second: 109.8
- input_tokens: 169 | output_tokens: 3587
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

Tu SaaS no tiene un problema de adquisición, tiene un problema de retención que está empezando a comerse el crecimiento.

Aquí está el desglose:

### 1. Métricas Clave Calculadas

Primero, un dato que lo explica todo: **ARPU = $15.00 exactos los 3 meses** ($18,000/1,200, $20,250/1,350, $22,200/1,480). Cero expansión de ingresos por cliente.

| Métrica | Enero | Febrero | Marzo | Fórmula |
| :--- | :--- | :--- | :--- | :--- |
| **Churn Rate mensual** | 3.75%* | **4.33%** | **5.04%** | Churns / Usuarios al inicio del mes |
| **Growth Rate (usuarios y MRR)** | - | 12.50% | 9.63% | (Mes actual - anterior) / anterior |
| **LTV / CAC** | 4.94 | 4.51 | 5.23 | LTV / CAC |
| **Net Revenue Retention (est.)** | - | 95.7% | 95.0% | (MRR inicio - MRR perdido por churn) / MRR inicio |
| **Payback Period** | 5.7 meses | 6.1 meses | 5.2 meses | CAC / ARPU |
| **Altas brutas (estimadas)** | - | 202 | 198 | Altas netas + Churns |

*\*Enero calculado sobre el total del mes al no tener diciembre.*

Detalle de la estimación de NRR: como tu ARPU es plano, no hay *expansion revenue*. Por tanto, NRR = Gross Retention. En marzo perdiste 68 x $15 = **$1,020 de MRR** solo por churn.

### 2. Tendencias Preocupantes

**1. El churn se está acelerando, no solo subiendo**
Pasó de 4.33% a 5.04% en un mes (+0.71 puntos). En términos absolutos: 45 → 52 (+15.6%) → 68 (+30.8%). Para un SaaS SMB, 5% mensual es la línea roja. Ya la cruzaste.

Esto implica que la vida media de un cliente cayó de ~23 meses a ~19.8 meses (1 / churn rate). Tu LTV reportado aún no refleja esto del todo (implica ~27 meses), así que **espera que el LTV caiga más rápido en abril/mayo** si no corriges.

**2. Te estás desacelerando pese a adquirir igual de bien**
Tus altas brutas son estables: ~200/mes en febrero y marzo. Pero tus altas netas cayeron de 150 a 130. No estás adquiriendo menos, estás perdiendo más. Es el clásico balde con fuga.

**3. LTV en caída constante y NRR < 100%**
LTV: $420 → $415 → $408. Y con NRR en 95%, tu base de clientes actual se encoge un 5% al mes sin ventas nuevas. Dependes 100% de adquisición nueva para crecer.

Lo positivo: LTV/CAC se mantiene sano (>4.5, benchmark es >3) y el payback es <7 meses. La economía unitaria aún funciona.

### 3. Tres Acciones Concretas

**Acción 1: Auditoría de churn de emergencia (esta semana)**
No intentes retener a todos, entiende a los 68 de marzo. Agrúpalos por antigüedad, plan y uso en los últimos 14 días antes de cancelar. Haz 10-15 entrevistas/surveys de salida.
*Meta:* Volver a <4.0% en 60 días. Solo bajar de 5.04% a 4.0% te ahorra ~15 clientes/mes = $225 MRR que se acumula mes a mes.
*Hipótesis a validar con tus datos:* si el churn subió justo cuando creciste 12.5% en febrero, probablemente es un problema de onboarding/calidad de cohorte, no de producto.

**Acción 2: Romper el ARPU de $15**
Tres meses planos significa cero upsell. Lanza una palanca de expansión simple: un add-on, límite de uso que empuje a un plan de $25-29, o funcionalidad premium.
*Impacto modelado:* Si solo el 10% de tus 1,480 clientes sube $10/mes, son **+$1,480 MRR sin adquirir a nadie**, y tu NRR se acerca al 100%. Esto ataca directamente tu métrica más débil.

**Acción 3: No escales adquisición, replica el CAC de marzo**
Tu CAC fue volátil: $85 → $92 → $78. Marzo fue tu mes más eficiente. Identifica qué canal/campaña bajó el CAC un 15.2% y concentra ahí el presupuesto. Pero no aumentes el gasto total hasta bajar el churn: a 5.04% de churn, de cada 200 clientes que compras, 85 se irán el mes que viene. Reasigna temporalmente un 15-20% del presupuesto de adquisición a retención/CS. Retener es hoy tu canal de crecimiento más barato.

### 4. Proyección para Abril (si nada cambia)

Asumiendo: altas brutas estables en ~200, churn rate sigue subiendo +0.7 pp, ARPU sigue en $15, LTV sigue su tendencia (-$5, -$7, -$9...).

| Métrica | Proyección Abril |
| :--- | :--- |
| Churn Rate | ~5.74% |
| Churns | ~85 clientes |
| Altas netas | ~115 |
| **Usuarios totales** | **~1,595** |
| **MRR** | **~$23,925** |
| Growth Rate | ~7.8% (vs 12.5% en feb) |
| LTV estimado | ~$399 |
| LTV/CAC (con CAC prom. $85) | ~4.7 |

**Conclusión:** Seguirás creciendo en abril, pero cada mes crecerás menos. Si esta trayectoria sigue, en junio tus altas netas caerán por debajo de 80 y tu crecimiento mensual será <5%. La palanca #1 ahora mismo no es vender más, es tapar la fuga de marzo.