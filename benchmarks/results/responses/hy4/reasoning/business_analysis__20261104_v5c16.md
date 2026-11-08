# Tencent Hy4 — reasoning/business_analysis

- model_id: `tencent/hy4`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 53.634s | tokens_per_second: 98.7
- input_tokens: 193 | output_tokens: 5293
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

Este es un dataset muy limpio y revelador. Antes de entrar en los cálculos, hay un **insight estructural** que explica todo tu trimestre: tu **ARPU es exactamente $15 en los 3 meses** ($18k/1.2k, $20.25k/1.35k, $22.2k/1.48k). 

Eso significa que **no ha habido ni upsell ni downgrade**. Todo tu crecimiento (y todo tu deterioro) viene exclusivamente de *volumen de usuarios* y *retención*. Aquí el análisis:

---

### 1. Métricas Clave

*Nota metodológica: Para Churn y NRR uso la base del mes anterior (estándar SaaS). Enero se calcula como proxy sobre su propia base.*

| Métrica | Enero | Febrero | Marzo | Fórmula / Nota |
| :--- | :--- | :--- | :--- | :--- |
| **ARPU** | $15.00 | $15.00 | $15.00 | MRR / Usuarios (Plano) |
| **Churn Rate (Logo)** | ~3.75% | **4.33%** | **5.04%** | Bajas / Base inicial |
| **Growth (MRR / Users)** | - | **+12.50%** | **+9.63%** | (Mes actual - Anterior) / Anterior |
| **Altas Brutas** | - | **202** | **198** | Netos + Churns *(¡Clave!)* |
| **LTV / CAC** | **4.94x** | **4.51x** | **5.23x** | LTV / CAC |
| **NRR** (= GRR) | ~96.25% | **95.67%** | **94.96%** | (MRR ini - Churn$) / MRR ini |

> **Sobre el NRR:** Al ser el ARPU constante, no hay expansión. Por tanto, tu `NRR = GRR (Gross Revenue Retention)`. Estás perdiendo ~$780 en Feb y ~$1,020 en Mar de ingresos recurrentes que ya habías ganado.

---

### 2. Tendencias preocupantes 🚨

1. **El "Falso Crecimiento" (Treadmill Effect):** Tus altas brutas están **estancadas o cayendo levemente** (202 ➔ 198), pero las bajas saltaron de 45 a 68 (**+51% en 2 meses**). El crecimiento neto se desaceleró de 12.5% a 9.6% *no* porque marketing falle, sino porque el churn se está comiendo la adquisición.
2. **El LTV cae por mortalidad, no por precio:** Baja $420 ➔ $415 ➔ $408. Como el ARPU no cambia, la única variable que se mueve es la **vida útil del cliente** (de ~28 a ~27.2 meses). Es una confirmación matemática del churn acelerado.
3. **Espejismo del LTV/CAC de Marzo:** El ratio rebotó a 5.23x y parece una buena noticia, **pero es un falso positivo**. Mejoró solo porque el CAC bajó de $92 a $78, mientras el activo subyacente (LTV) siguió degradándose. Si el CAC vuelve a $92 en Abril, el ratio cae a 4.43x.
4. **Sospecha de calidad del tráfico barato:** Justo en el mes que optimizaste el CAC un -15% ($92 ➔ $78), el churn se disparó un +16% (4.33% ➔ 5.04%). Hipótesis fuerte: **estás comprando leads de menor *fit* más baratos** que se activan mal y se van rápido.
5. **NRR < 95% y bajando:** Sin expansión, necesitas vender ~200 clientes nuevos *todos los meses* solo para mantenerte en el sitio. Es un negocio que corre en una cinta de correr.

---

### 3. Tres acciones concretas (Data-Driven)

**Acción 1: Auditar la cohorte de Marzo antes de escalar el CAC barato**
*   *Dato:* CAC -15% coincidió con Churn +16% y LTV -$7.
*   *Qué hacer:* Segmenta los 68 churns de Marzo por mes de alta. Compara la tasa de activación día-7 de los captados a $92 (Feb) vs. los de $78 (Mar). Si los de $78 mueren antes, **sube el CAC de vuelta a ~$85-$88** ajustando el targeting (no el budget). Perder $7 de LTV por ahorrar $14 de CAC sale a penas si el cliente no pasa del mes 2.

**Acción 2: Exprimir la cohorte de Enero para arreglar el NRR (sin vender nada nuevo)**
*   *Dato:* ARPU congelado en $15, pero tienes ~1,110 usuarios de Enero que ya sobrevivieron 3 meses (tu segmento más sano).
*   *Qué hacer:* Lanza un add-on o tier "Pro" a ese segmento maduro. Subir el ARPU solo **$0.75** (5%) en esos 1,110 usuarios genera **~$830 de MRR de expansión pura**. Eso solo empuja el NRR de 94.9% a ~99% sin gastar un solo dólar en ads.

**Acción 3: Reasignar el "ahorro" de Marzo a un Save-Flow**
*   *Dato:* Ahorraste $14 x 198 altas ≈ **$2,770** en Marzo, pero dejaste ir $1,020 de MRR.
*   *Qué hacer:* Usa ese presupuesto para un flujo de cancelación (descuento temporal, pausa de cuenta, o llamada de CS) en lugar de más ads. Recuperar **solo 4 de los 68 churns** devuelve $60 MRR inmediato y ~$1,680 de LTV agregado. El ROI de retención ahora mismo es superior al de adquisición.

---

### 4. Proyección: Abril (si no intervienes)

Extrapolando la aceleración de las tasas (Churn +~0.65pp/mes, Altas brutas -2%/mes, LTV -$6/mes, CAC estable en $78):

| Métrica | Proyección Abril | Δ vs. Marzo |
| :--- | :--- | :--- |
| **Churn Rate** | **~5.70%** | +0.66 pp |
| **Bajas (Churns)** | **~85** | +17 |
| **Altas Brutas** | **~194** | -4 |
| **Usuarios Netos** | **1,589** | **+7.4%** *(sigue frenando)* |
| **MRR** | **$23,835** | +$1,635 |
| **LTV** | **~$402** | -$6 |
| **LTV / CAC** | **5.15x** | -0.08x *(sigue engañando)* |
| **NRR** | **~94.25%** | -0.71 pp |

⚠️ **Alerta estratégica (El punto de inflexión):** Si esta inercia continúa, la base sigue creciendo y el % de churn también. Alrededor de **Julio/Agosto** (base ~1,800, churn ~11%), tus ~190 altas mensuales igualarán a tus ~190 bajas. **El MRR se aplanará en ~$27k** aunque sigas invirtiendo ~$15k/mes en adquisición. 

*El trimestre no se arregla comprando más barato; se arregla cerrando la fuga de los que ya entraron.* ¿Quieres que modelemos el impacto de la Acción 2 (el upsell) sobre el NRR de Abril?