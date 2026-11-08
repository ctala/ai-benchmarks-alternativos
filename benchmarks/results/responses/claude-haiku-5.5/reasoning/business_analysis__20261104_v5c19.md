# Claude Haiku 5.5 — reasoning/business_analysis

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.52 | quality: 9.56
- latency_total: 26.625s | tokens_per_second: 207.7
- input_tokens: 256 | output_tokens: 5531
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

# Análisis de métricas SaaS: Enero a Marzo

## 1. Métricas clave

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| **ARPU** (MRR / usuarios) | $15.00 | $15.00 | $15.00 |
| **Churn mensual** (% de usuarios) | ~3.75%* | 4.33% | **5.04%** |
| **Crecimiento de usuarios** | — | +12.5% | +9.6% |
| **Crecimiento de MRR** | — | +12.5% | +9.6% |
| **Altas netas** | — | +150 | +130 |
| **Altas brutas estimadas**\*\* | — | ~202 | ~198 |
| **LTV / CAC** (reportado) | 4.94x | 4.51x | 5.23x |
| **LTV / CAC** (ajustado)\*\*\* | 4.7x | 3.8x | 3.8x |
| **Payback de CAC** (meses, sobre ingreso) | 5.7 | 6.1 | 5.2 |

\* Enero usa la base final de usuarios porque no hay datos de diciembre.
\*\* Altas netas + churn.
\*\*\* Usa el churn real de cada mes en lugar del implícito en el LTV reportado (ver punto 2 de tendencias).

**Net Revenue Retention (NRR):** no tienes datos de expansión (upgrades) ni contracción, así que solo puedo estimar la retención bruta de ingresos.
- Revenue retention mensual (solo churn): Feb 95.7%, Mar 95.0%
- Anualizada: ~59% en febrero y ~54% en marzo

Si tienes upgrades, el NRR real será mayor, pero el dato de churn ya es preocupante.

## 2. Tendencias preocupantes

**🔴 1. El churn se está acelerando (la más grave)**
- Churn mensual: 3.75% → 4.33% → 5.04%
- Usuarios perdidos: 45 → 52 → 68 (+51% en dos meses, mientras la base creció 23%)
- Un churn de 5% mensual equivale a perder aproximadamente el 46% de los clientes al año.

**🔴 2. El LTV reportado no cuadra con el churn actual**
- Con ARPU de $15 y churn de 5.04%, el LTV real sería ~$15 / 0.0504 ≈ **$298**, no $408.
- El LTV de $408 implica un churn de ~3.7%, que ya no refleja tu realidad.
- Probablemente estás usando un churn histórico o un modelo que no se actualizó. Esto sobrestima tu salud financiera.

**🟠 3. El crecimiento neto se está desacelerando**
- Altas netas: +150 → +130 (-13%)
- Las altas brutas se mantuvieron estables (~200), así que el churn está absorbiendo el crecimiento.
- En marzo, 34% de los nuevos usuarios se perdieron en el mismo mes (68 de ~198 altas brutas), frente a 26% en febrero.

**🟠 4. El CAC cayó en marzo, pero puede ser una señal engañosa**
- CAC: $85 → $92 → $78. La caída coincide con el aumento del churn.
- Hipótesis a validar: si el CAC bajó porque entraron canales baratos de baja intención, esos usuarios se van más rápido y el ahorro es ilusorio.

**🟡 5. No hay palanca de ingresos aparte de nuevos usuarios**
- El ARPU fijo en $15 y el crecimiento de MRR igual al de usuarios indican que no hay expansión, upgrades ni ajustes de precio. Todo el crecimiento depende de adquisición.

## 3. Tres acciones concretas

**Acción 1: Sprint de retención (prioridad máxima, próximas 4–6 semanas)**
- Activa encuestas de cancelación obligatorias y clasifica los motivos (precio, producto, uso, competencia).
- Revisa el churn involuntario: los pagos fallidos suelen representar entre 20 y 40% del churn en SaaS. Implementa reintentos de cobro y emails de recuperación.
- Mide el activation rate en los primeros 7–14 días, porque el churn temprano suele indicar onboarding deficiente.
- **Meta:** volver a un churn de 4.0–4.5% en dos meses.

**Acción 2: Segmentar churn y CAC por canal y cohorte**
- Calcula el churn a 60 y 90 días para cada canal de adquisición.
- Calcula el LTV real por canal, no el promedio global.
- Si un canal tiene CAC bajo pero churn alto, reduce su presupuesto y reasígnalo a los que retienen mejor, aunque cuesten más.
- **Meta:** que cada canal tenga LTV/CAC > 3 con churn real.

**Acción 3: Recalibrar el LTV y crear una palanca de ARPU**
- Recalcula el LTV con el churn actual (~$300). Así tomarás decisiones de inversión con números reales.
- Prueba un plan anual con descuento (10–20%): reduce el churn porque el cliente se compromete, y mejora el flujo de caja.
- Evalúa un ajuste de precio o un plan superior para nuevos clientes. Subir el ARPU de $15 a $17 daría +13% de MRR sin adquirir un solo usuario más.

## 4. Proyección de abril

Supuestos base: churn sube a ~5.7% (+0.7 pp, igual que de feb a mar) y altas brutas se mantienen en ~198.

| Escenario | Churn abril | Altas brutas | Usuarios fin de abril | MRR abril | Crec. MRR vs marzo |
|---|---|---|---|---|---|
| **Optimista** (churn se estabiliza) | 5.0% (~74) | 200 | ~1,606 | ~$24,100 | +8.6% |
| **Base** (tendencia continúa) | 5.7% (~84) | 198 | ~1,594 | ~$23,900 | +7.7% |
| **Pesimista** (churn sigue subiendo y adquisición cae) | 6.5% (~96) | 180 | ~1,564 | ~$23,500 | +5.9% |

**Lectura:** en el escenario base, el crecimiento neto seguiría cayendo (de +130 a ~+114) y el MRR crecería cerca de 8%. Pero si el churn sigue subiendo, las altas netas podrían llegar cerca de cero hacia junio. Con churn de ~6.5% o más, tu crecimiento se detendría sin importar cuántos usuarios captes, porque necesitarías adquirir más de 100 usuarios al mes solo para mantenerte.

## 5. Datos que necesitas para un análisis más preciso

- Usuarios de diciembre (para calcular el churn de enero correctamente).
- MRR de expansión, contracción y churn en dólares (para el NRR real).
- Churn involuntario frente a voluntario.
- Gasto en marketing y ventas por mes (para calcular el CAC de forma directa).
- Margen bruto (el payback y el LTV deberían usarlo, no solo el ingreso).
- Churn por cohorte y por canal de adquisición.

Si me compartes estos datos, puedo refinar el modelo y hacer una proyección más confiable.