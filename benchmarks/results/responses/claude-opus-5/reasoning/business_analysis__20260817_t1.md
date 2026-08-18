# Claude Opus 5 — reasoning/business_analysis

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 68.69s | tokens_per_second: 69.5
- input_tokens: 254 | output_tokens: 4773
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y acciones concretas basadas en los datos.

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

# Análisis SaaS — Q1

## Nota metodológica previa

Antes de los números, dos aclaraciones importantes sobre lo que **sí** y **no** se puede calcular con estos datos:

- **ARPU es constante en $15.00** los tres meses (18,000/1,200 = 20,250/1,350 = 22,200/1,480). Esto es sospechosamente exacto: sugiere un solo plan de precio o datos redondeados. Lo asumo como real, pero conviene verificarlo.
- **Net Revenue Retention no se puede calcular correctamente** con estos datos. NRR requiere separar el MRR de la cohorte inicial en: expansión, contracción y churn de revenue. Aquí solo tenemos MRR total y conteo de churns. Más abajo doy una aproximación explícita con sus supuestos, pero no la trates como NRR real.
- **Los churns son "usuarios perdidos" absolutos.** No sé si son cancelaciones voluntarias, impagos o downgrades a free. Esa distinción cambia radicalmente el diagnóstico.

---

## 1. Métricas clave

### Churn rate (mensual, sobre base inicial)

| Mes | Usuarios inicio | Churns | Churn rate |
|---|---|---|---|
| Enero | 1,200 | 45 | **3.75%** |
| Febrero | 1,350 | 52 | **3.85%** |
| Marzo | 1,480 | 68 | **4.59%** |

*Nota: uso el conteo de usuarios de cada mes como base. Si esos números son cierres de mes y no aperturas, el churn real es ~0.3-0.5 pp más alto. Aclarar.*

**Churn anualizado (Marzo):** 1 − (1 − 0.0459)¹² = **43.0%** anual. Para B2B SaaS es alto; para B2C self-serve es tolerable.

### Growth rate

| Período | Usuarios | MRR |
|---|---|---|
| Ene→Feb | +12.5% | +12.5% |
| Feb→Mar | +9.6% | +9.6% |
| **CMGR (Ene→Mar)** | **+11.06%** | **+11.06%** |

Crecimiento neto sano, pero **desacelerando**: −2.9 pp entre períodos.

### Usuarios nuevos (derivado)

Esto es lo más revelador del dataset:

| Mes | Neto | Churns | **Nuevos (neto + churns)** |
|---|---|---|---|
| Ene→Feb | +150 | 52 | **202** |
| Feb→Mar | +130 | 68 | **198** |

**La adquisición está plana (~200/mes). Todo el crecimiento neto perdido viene de churn creciente, no de menos ventas.** Esto es un diagnóstico clave: no tienes un problema de marketing, tienes un problema de retención.

### LTV/CAC ratio

| Mes | LTV | CAC | Ratio |
|---|---|---|---|
| Enero | $420 | $85 | **4.94x** |
| Febrero | $415 | $92 | **4.51x** |
| Marzo | $408 | $78 | **5.23x** |

Los tres por encima del benchmark de 3x. **Pero hay una inconsistencia que hay que señalar:** con ARPU de $15 y churn de 4.59%, el LTV implícito sería ARPU/churn = $327 (sin margen bruto) o ~$262 asumiendo 80% de margen. El LTV reportado de $408 implica un churn de ~3.7% o márgenes/expansión no visibles en los datos.

→ **Tu LTV reportado parece estar rezagado respecto al churn real.** Recalcularlo con datos de Marzo probablemente baje el ratio a ~3.4x (o ~2.8x si se ajusta por margen bruto). Sigue siendo viable, pero el colchón es mucho menor de lo que parece.

### CAC Payback

CAC / (ARPU × margen bruto), asumiendo 80%:
- Enero: 85 / 12 = **7.1 meses**
- Marzo: 78 / 12 = **6.5 meses**

Bueno (<12 meses). El CAC bajando 8% mientras el volumen se mantiene es la mejor señal del trimestre.

### Net Revenue Retention (aproximación, no NRR real)

Asumiendo ARPU uniforme de $15 y **cero expansión** (que es lo que los datos sugieren, dado que ARPU no se mueve):

| Mes | MRR inicial | MRR perdido | NRR aprox. |
|---|---|---|---|
| Febrero | $20,250 | 52 × $15 = $780 | **96.2%** |
| Marzo | $22,200 | 68 × $15 = $1,020 | **95.4%** |

**El hallazgo real aquí no es el número, es que ARPU no crece.** Un ARPU perfectamente plano durante tres meses significa que no hay upsells, no hay cross-sells, no hay expansión de asientos. Los mejores SaaS tienen NRR >110% porque las cuentas existentes crecen. Tú estás en ~95% y bajando, lo que significa que **cada mes tienes que vender más solo para quedarte igual.**

---

## 2. Tendencias preocupantes

**🔴 Churn acelerando de forma no lineal.** +0.10 pp de Ene a Feb, pero **+0.74 pp** de Feb a Mar. No es una tendencia lineal, es una curva que se está inclinando. Esto es lo más urgente del análisis.

**🔴 Adquisición estancada en ~200/mes.** Dos meses consecutivos casi idénticos. Tu motor de crecimiento no está escalando; el crecimiento neto que ves es una ilusión que el churn está erosionando.

**🔴 Cero expansión de revenue.** ARPU clavado en $15.00. Sin NRR >100%, el crecimiento depende 100% de adquisición nueva, que es la palanca más cara.

**🟡 El LTV reportado no cuadra con el churn observado.** O el LTV está calculado con datos históricos, o hay segmentos con retención muy distinta. En cualquier caso, tus dashboards probablemente están mostrando una economía unitaria más optimista que la real.

**🟡 Deceleración del growth rate.** De 12.5% a 9.6%. Si sigue, el crecimiento se aplana en Q2.

**Aritmética preocupante:** a este ritmo de aceleración del churn, en ~4-5 meses las cancelaciones (~200/mes) igualarán las altas (~200/mes) y el crecimiento neto será **cero** — sin que hayas vendido ni un cliente menos.

---

## 3. Tres acciones concretas

### Acción 1 — Cohort analysis de urgencia sobre los churns de Marzo (esta semana)

**Por qué:** El salto de 52→68 no es ruido, es una señal. Necesitas saber si son clientes nuevos (problema de onboarding/expectativas), clientes viejos (problema de valor a largo plazo), o de un canal específico (problema de calidad de leads).

**Cómo:**
- Segmenta los 68 churns por: antigüedad al cancelar, canal de adquisición, plan, y nivel de uso en los últimos 30 días.
- Hipótesis a testear primero: **los 202 usuarios que entraron en Febrero fueron de peor calidad.** Ojo al dato — el CAC de Febrero fue el más alto ($92) y el churn de Marzo el más alto. Si en Febrero se abrió un canal nuevo o se hizo una promo agresiva, ahí está tu respuesta.
- Llama por teléfono a 15-20 de los que cancelaron. No encuesta: llamada.

**Métrica de éxito:** identificar la causa raíz que explique >50% de los 68 churns.

### Acción 2 — Instalar un sistema de expansión de revenue (30-60 días)

**Por qué:** Es la palanca con mayor ROI que tienes sin usar. Pasar de NRR 95% a 105% equivale a añadir ~$2,200/mes de MRR sin gastar $1 en CAC. Con 1,480 usuarios ya pagando, es dinero sobre la mesa.

**Cómo:**
- Define 2-3 triggers de upsell basados en uso (límite de asientos al 80%, feature premium tocada 3 veces, volumen de uso en top quintil).
- Lanza un tier superior si solo tienes uno. Un ARPU plano de $15.00 exacto sugiere un único plan — eso es dejar valor sin capturar en tus mejores cuentas.
- Meta concreta: **ARPU de $15.00 → $15.75 en 60 días** (+5%). Eso son ~$1,100/mes adicionales.

**Métrica de éxito:** ARPU creciendo mes a mes por primera vez.

### Acción 3 — Reasignar presupuesto al canal de CAC $78 y activar early-warning de churn

**Por qué:** Dos cosas a la vez, ambas basadas en datos que ya tienes. El CAC bajó a $78 en Marzo (el mejor del trimestre) mientras el volumen se mantuvo — algo está funcionando y hay que identificarlo y escalarlo. Y necesitas dejar de reaccionar al churn después de que ocurre.

**Cómo:**
- Desglosa el CAC de $78 por canal. Identifica qué canal específico bajó y si tiene capacidad de absorber más presupuesto sin degradar la calidad del lead (cuidado: escalar un canal casi siempre sube su CAC).
- **Antes de escalar, valida la retención por canal.** No repitas el patrón de Febrero: CAC alto → churn alto un mes después. Vale más un canal de CAC $92 con 2% de churn que uno de $78 con 6%.
- En paralelo: define un health score simple (login en 14 días + acción core completada) y dispara intervención automática a los que caen en zona roja.

**Métrica de éxito:** Abril con >220 usuarios nuevos **y** churn <4.5%. Ambas condiciones, no una.

---

## 4. Proyección de Abril

Presento tres escenarios porque la extrapolación depende críticamente de cómo modeles el churn — y ese es exactamente el punto de decisión.

### Escenario A — Base (tendencia lineal del churn)

Churn +0.42 pp/mes promedio → **5.01%**. Nuevos usuarios: 200.

| Métrica | Valor |
|---|---|
| Churns | 1,480 × 5.01% = **74** |
| Usuarios | 1,480 + 200 − 74 = **1,606** |
| MRR | 1,606 × $15 = **$24,090** |
| Growth | **+8.5%** |
| Ratio LTV/CAC | ~4.1x (con LTV ajustado) |

### Escenario B — Pesimista (el churn sigue acelerando)

Si Marzo (+0.74 pp) marca la nueva pendiente → churn **5.33%**.

| Métrica | Valor |
|---|---|
| Churns | **79** |
| Usuarios | **1,601** |
| MRR | **$24,015** |
| Growth | **+8.2%** |

### Escenario C — Con intervención (Acciones 1-3 funcionando)

Churn contenido en 4.2%, nuevos 220, ARPU $15.30.

| Métrica | Valor |
|---|---|
| Churns | **62** |
| Usuarios | **1,638** |
| MRR | **$25,061** |
| Growth | **+12.9%** |

### La proyección que realmente importa

A 6 meses vista, con el churn acelerando y la adquisición plana:

| Mes | Escenario base | Con intervención |
|---|---|---|
| Abril | 1,606 | 1,638 |
| Mayo | 1,719 | 1,802 |
| Junio | 1,821 | 1,973 |
| Julio | 1,908 | 2,152 |
| Agosto | 1,977 | 2,340 |
| **Septiembre** | **2,026** | **2,536** |

**La brecha en Septiembre es de 510 usuarios (~$7,800 de MRR).** Y nota la forma de la curva base: el crecimiento mensual cae de 8.5% en Abril a **2.5% en Septiembre**. No es una recesión, es la matemática del churn compuesto contra una adquisición plana.

---

## Resumen ejecutivo

Tu trimestre luce bien en la superficie: MRR +23%, LTV/CAC de 5.2x, CAC bajando. Pero **los números buenos son de adquisición y los números malos son de retención** — y en SaaS la retención es la que compone.

Tres cosas que vale la pena repetir:

1. **La adquisición no es el problema** (~200 nuevos/mes constantes). El churn se está comiendo el crecimiento.
2. **Tu LTV reportado probablemente está inflado** respecto al churn actual. Recalcúlalo con datos de Marzo antes de tomar decisiones de inversión en adquisición.
3. **ARPU plano en $15.00 exacto es tu mayor oportunidad no explotada.** Cero expansión con 1,480 clientes pagando.

**Datos que te faltan para decidir bien:** churn segmentado por cohorte y canal, ARPU por plan, margen bruto real, y la distinción entre churn voluntario e involuntario (los impagos son el churn más fácil de arreglar — a veces es solo lógica de reintento de cobro).

Si me compartes esos datos, el análisis pasa de descriptivo a prescriptivo.