# Claude Opus 5.5 — reasoning/business_analysis

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.83 | quality: 9.56
- latency_total: 44.251s | tokens_per_second: 103.8
- input_tokens: 256 | output_tokens: 4593
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

# Análisis de métricas SaaS: Enero–Marzo

## 1. Métricas clave

**Supuestos:**
- El churn rate se calcula sobre los usuarios al inicio del mes. Para enero uso 1,200 como base, porque no tengo datos de diciembre.
- No hay datos de expansión ni de upgrades, así que el NRR solo refleja la pérdida por churn.

### Métricas base

| Métrica | Enero | Febrero | Marzo | Tendencia |
|---|---|---|---|---|
| ARPU (MRR/usuarios) | $15.00 | $15.00 | $15.00 | ➖ Estancado |
| Churn rate mensual | 3.75% | 4.33% | **5.04%** | 🔴 Subiendo |
| Crecimiento usuarios/MRR | — | 12.5% | **9.6%** | 🔴 Desacelerando |
| Nuevos usuarios brutos | — | 202 | 198 | 🟡 Plano |
| MRR perdido por churn | $675 | $780 | **$1,020** | 🔴 +31% en marzo |
| LTV/CAC (reportado) | 4.94x | 4.51x | 5.23x | 🟢 Aparentemente sano |
| CAC payback | 5.7 meses | 6.1 meses | 5.2 meses | 🟢 Aceptable |
| NRR mensual | 96.3% | 95.7% | **95.0%** | 🔴 Bajando |
| NRR anualizado | ~63% | ~59% | **~54%** | 🔴 Muy bajo |
| Quick Ratio (MRR nuevo / perdido) | — | 3.9 | **2.9** | 🟡 Empeorando |

*Nuevos usuarios brutos = crecimiento neto + churns. Por ejemplo, en febrero: 150 + 52 = 202.*

### ⚠️ Hallazgo importante: tu LTV probablemente está sobreestimado

Con la fórmula estándar (LTV = ARPU ÷ churn rate, sin contar margen bruto):

| | Enero | Febrero | Marzo |
|---|---|---|---|
| LTV reportado | $420 | $415 | $408 |
| **LTV implícito** | $400 | $346 | **$298** |
| **LTV/CAC real** | 4.7x | 3.8x | **3.8x** |

El LTV reportado apenas baja (-3%), pero el churn subió un 34%. Parece que el cálculo de LTV no se está actualizando con el churn real. Si además aplicas el margen bruto (por ejemplo, 80%), el LTV/CAC de marzo bajaría a unos **3.1x**.

---

## 2. Tendencias preocupantes

**🔴 1. El churn se está acelerando, no solo creciendo.**
Los churns crecieron +15.6% en febrero y +30.8% en marzo. El churn rate sube unos 0.65 puntos porcentuales por mes. A este ritmo, superarás el 6% en mayo.

**🔴 2. El motor de adquisición está plano y el churn se come el crecimiento.**
Captas unos 200 usuarios brutos al mes, pero pierdes cada vez más. El crecimiento neto pasó de +150 a +130 usuarios.

Esto implica un techo matemático. Con 200 altas al mes y 5% de churn, tu base se estabilizaría en unos **4,000 usuarios ($60K MRR)**. Con 6% de churn, el techo baja a unos 3,300.

**🔴 3. Cero expansión de ingresos.**
El ARPU es exactamente $15 los tres meses. No hay upsells, upgrades ni subidas de precio. Por eso el NRR está muy por debajo del 100%: cada cohorte solo pierde valor. Los SaaS sanos B2B apuntan a un NRR anual de 100–120%.

**🟡 4. El CAC bajó en marzo, pero no trajo más usuarios.**
- Febrero: 202 usuarios × $92 = ~$18.6K de inversión.
- Marzo: 198 usuarios × $78 = ~$15.4K de inversión.

Gastaste menos y captaste casi lo mismo, lo cual es bueno. Pero conviene vigilar si los canales más baratos traen usuarios de menor calidad que harán churn más adelante.

---

## 3. Tres acciones concretas

### Acción 1: Diagnosticar y atacar el churn (prioridad máxima)
- **Análisis de cohortes:** ¿qué cohorte está generando los churns de marzo? ¿Se van en el mes 1–2 (problema de onboarding) o después (problema de valor o producto)?
- **Encuesta de salida obligatoria** al cancelar, más 5–10 llamadas con clientes perdidos.
- **Health score** basado en uso (logins, features clave) para detectar riesgo antes de la cancelación.
- **Meta:** volver a ≤4% en 60 días.
- **Impacto:** cada punto porcentual de churn evitado equivale a unos 15 usuarios y ~$220 de MRR al mes, y el efecto se acumula.

### Acción 2: Crear palancas de expansión de ingresos
- **Plan anual con descuento** (por ejemplo, 2 meses gratis). Reduce el churn mecánicamente y mejora el flujo de caja.
- **Estructura por niveles** (tiers por uso, asientos o features premium) para que el ARPU pueda crecer.
- **Meta:** ARPU de $16–17 en 3 meses y NRR mensual >97%.
- **Impacto:** un +$1 de ARPU sobre 1,500 usuarios suma ~$1,500 de MRR sin adquirir a nadie.

### Acción 3: Auditar la calidad de adquisición y corregir el LTV
- **Segmentar churn y LTV por canal de adquisición.** El CAC bajo de marzo solo es bueno si esos usuarios retienen.
- **Recalcular el LTV** con el churn real y el margen bruto. Tomar decisiones de inversión con un LTV inflado es peligroso.
- **No escalar inversión** en adquisición hasta estabilizar el churn. Hoy estás llenando un balde con un agujero que se agranda.

---

## 4. Proyección para abril (si las tendencias continúan)

**Supuestos del escenario base:**
- El churn sube a ~5.75%, siguiendo la tendencia de +0.7 pp al mes.
- Las altas brutas bajan a ~195, siguiendo la tendencia ligeramente descendente.
- El ARPU se mantiene en $15.

| Métrica | Optimista (churn estable) | **Base (tendencia)** | Pesimista (churn acelera) |
|---|---|---|---|
| Churn rate | 5.0% | **5.75%** | 6.5% |
| Churns | 74 | **85** | 96 |
| Nuevos brutos | 200 | **195** | 190 |
| Usuarios finales | 1,606 | **1,590** | 1,574 |
| MRR | $24,090 | **$23,850** | $23,610 |
| Crecimiento | 8.5% | **7.4%** | 6.4% |
| MRR perdido | $1,110 | **$1,275** | $1,440 |
| NRR mensual | 95.0% | **94.3%** | 93.5% |
| LTV implícito | $300 | **$261** | $231 |
| LTV/CAC (CAC ~$85) | 3.5x | **3.1x** | 2.7x |

### Conclusión

El negocio crece, pero la calidad del crecimiento se deteriora:
- El crecimiento se desacelera: 12.5% → 9.6% → ~7.4%.
- El churn ya consume casi el 45% de las altas nuevas en el escenario base (85 de 195).
- En el escenario pesimista, el LTV/CAC real caería por debajo de 3x, el umbral típico de salud.

La buena noticia es que el CAC está controlado y la adquisición funciona de forma estable. **El problema principal es la retención y la monetización, no la captación.** Enfoca abril en el churn antes de invertir más en marketing.

Si me compartes datos por cohorte, por canal o las razones de cancelación, puedo afinar el diagnóstico.