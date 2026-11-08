# Inkling Small — reasoning/business_analysis

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 27.302s | tokens_per_second: 234.0
- input_tokens: 176 | output_tokens: 6389
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

Aquí tienes el análisis completo con cálculos, alertas y plan de acción.

---

## 1. Métricas clave (calculadas)

| Métrica | Ene | Feb | Mar | Cálculo / Nota |
|---|---|---|---|---|
| **Usuarios (fin mes)** | 1,200 | 1,350 | 1,480 | — |
| **MRR** | $18,000 | $20,250 | $22,200 | — |
| **ARPU** | **$15.00** | **$15.00** | **$15.00** | MRR / Usuarios (constante, sin expansión) |
| **Churn absoluto** | 45 | 52 | 68 | — |
| **Churn rate (mensual)**¹ | **~3.8%**² | **4.33%** | **5.04%** | Churn / Usuarios inicio mes (mes anterior) |
| **Growth usuarios** | — | **+12.5%** | **+9.6%** | (Actual - Ant) / Ant |
| **Growth MRR** | — | **+12.5%** | **+9.6%** | Igual que usuarios (ARPU fija) |
| **CAC** | $85 | $92 | $78 | — |
| **LTV** | $420 | $415 | $408 | — |
| **LTV / CAC** | **4.94x** | **4.51x** | **5.23x** | LTV / CAC |
| **NRR (estimado)**³ | — | **~95.7%** | **~95.0%** | (MRR existente retenido / MRR inicio) |
| **MRR perdido por churn** | ~$675 | ~$780 | **~$1,020** | Churn × $15 |

¹ *Churn rate estándar: bajas del mes / base de usuarios al inicio del mes (tomando el mes anterior como inicio).*
² *Enero estimado sobre base aproximada (1,200) porque no hay mes previo.*
³ *NRR estimado sin datos de upsell/downsell: asumiendo que todo el crecimiento es por nuevos usuarios y el resto es retención de base existente.*

**Puntos clave de los números:**
- **ARPU congelado en $15**: todo tu crecimiento es por volumen, no por valor por cliente.
- **Churn acelerado**: +15.5% (45→52) y luego +30.8% (52→68). Crece más rápido que tu base.
- **LTV en caída libre**: -$12 en 2 meses (-2.9%). La vida útil del cliente se acorta.
- **NRR < 100%**: tu base existente pierde valor cada mes; sin nuevos usuarios, el MRR caería.

---

## 2. Tendencias preocupantes

1. **Churn fuera de control relativo**  
   Tu base creció +23% (1,200→1,480) pero las bajas crecieron **+51%** (45→68). El churn rate pasó de ~3.8% a **5.04%**. Si se mantiene, pierdes ~6% mensual.

2. **Crecimiento desacelerado**  
   De +12.5% a +9.6%. Cada mes sumas menos usuarios netos (150, luego 130). El "motor" de nuevos clientes se está enfriando.

3. **LTV baja + ARPU estática = sin expansión**  
   Los clientes no te pagan más ni se quedan más tiempo. El 100% del crecimiento es por adquisición pura, lo que es insostenible si el CAC sube o el churn sigue así.

4. **CAC volátil y riesgo de eficiencia**  
   Subió a $92 en febrero (peor mes de LTV: $415, ratio 4.5x) y bajó a $78 en marzo. Esto sugiere que estás cambiando canales o campañas, pero la tendencia de LTV es más peligrosa que la mejora de CAC.

5. **MRR perdido por churn crece exponencialmente**  
   Perdías $675/mes (ene), luego $780 (feb), ahora **$1,020/mes** (mar). Eso es un 51% más de "fuga" de ingreso recurrente en 2 meses.

---

## 3. 3 acciones concretas basadas en los datos

### Acción 1: Detener la fuga inmediatamente (churn)
**Dato que la respalda:** Churn pasó de 4.33% a 5.04% y los churns absolutos subieron 51% en 2 meses; estás perdiendo $1,020 MRR mensual solo por bajas.

**Qué hacer:** Lanza un protocolo de retención de 3 pasos:
- **Día 1-3:** Email/WhatsApp automático si no hay login (intervención temprana).
- **Día 7:** Llamada o video de "check-in" a todos los usuarios nuevos (la cohorte que entra hoy es la que se va mañana).
- **Día 30:** Oferta de "pause" o descuento de retención antes de que cancelen.

**Meta:** Bajar churn a **<4%** antes de abril (de 68 a ~60 bajas).

### Acción 2: Romper el estancamiento de ARPU/LTV
**Dato que la respalda:** ARPU = $15 fijo; LTV cayó de $420 a $408; NRR ~95%. No hay expansión.

**Qué hacer:** Lanza un **add-on/plan premium** ($5-$8/mes) para el 20% más activo de tu base (en marzo ~296 usuarios = ~$1,480-$2,370 MRR extra). También introduce una "feature de pago" que resuelva un problema específico.

**Meta:** Subir ARPU a **$16-17** y detener la caída de LTV (objetivo: recuperar $420 en 2 meses).

### Acción 3: Reasignar presupuesto de adquisición por eficiencia
**Dato que la respalda:** CAC osciló $85 → $92 → $78; LTV/CAC cayó a 4.5x en febrero y subió a 5.2x en marzo por el CAC bajo, pero LTV sigue bajando.

**Qué hacer:** 
- **Congela** los canales que te dieron CAC $92 (o más) hasta que LTV vuelva a $420.
- **Doble** inversión en los canales que generaron $78 en marzo.
- **Prioriza retención sobre adquisición pura:** con NRR ~95%, cada nuevo usuario que traes "compensa" la fuga de la base, pero es más barato retener que reemplazar.

---

## 4. Proyección de abril (si las tendencias continúan)

Asumiendo **continuación lineal de las tendencias** observadas (crecimiento desacelerado, churn acelerado, LTV cayendo, CAC estable/optimizado):

| Métrica | Proyección Abril | Lógica |
|---|---|---|
| **Usuarios (fin mes)** | **~1,580 - 1,590** | Crecimiento absoluto: +150 → +130 → **+110** (desaceleración); o 7-7.5% sobre 1,480 |
| **Churn absoluto** | **~88 - 93** | Incremento: +7 → +16 → **+25** (aceleración); ~6.2% sobre base de marzo |
| **MRR** | **~$23,700 - $23,850** | 1,590 usuarios × $15 ARPU |
| **Churn rate** | **~6.0 - 6.3%** | 93 bajas / 1,480 inicio |
| **Growth MRR** | **~7.4%** | De 12.5% a 9.6% a ~7% |
| **CAC** | **~$75** | Tendencia a la baja de -$7 en marzo; optimización de canales |
| **LTV** | **~$400 - $402** | Tendencia: -5, -7 → **-6** (408 - 6) |
| **LTV/CAC** | **~5.3x** | Se mantiene por CAC bajo, pero LTV baja es riesgo |
| **NRR (estimado)** | **~94%** | Si no lanzas upsell, la base sigue perdiendo ~6% de valor |
| **MRR perdido por churn** | **~$1,350** | ~90 bajas × $15 |

### ¿Qué significa esta proyección?
- **No es sostenible:** Si en abril tienes ~90 bajas y solo ~110 usuarios netos nuevos, el "motor" de crecimiento se debilita mucho. En 2-3 meses podrías entrar en estancamiento o contracción si el churn sigue subiendo.
- **El LTV/CAC de 5.3x parece "bien"**, pero es engañoso: estás gastando menos en adquirir (CAC $75) y los clientes se van más rápido (LTV $400). El **payback** empeora porque recuperas menos por cliente.
- **La única variable que salva la proyección** es que **rompas la tendencia de ARPU y churn**; si no, abril será tu último mes de crecimiento "fácil".

---

### Resumen ejecutivo para ti
> **Tu SaaS tiene un problema de retención, no de adquisición.** El CAC está bajo control ($78), el crecimiento es positivo (+9.6%), pero el churn está acelerando (5% y subiendo) y tu LTV se erosiona ($408 y bajando). **No necesitas más usuarios; necesitas que los actuales paguen más ($16-17 ARPU) y no se vayan (bajar churn a <4%).** Si no actúas en abril, proyectas ~1,590 usuarios con ~90 bajas mensuales, es decir, casi estás creciendo por pura "reposiciones" de clientes perdidos.

¿Quieres que te arme un plan de acción de 30 días con métricas semanales para seguimiento?