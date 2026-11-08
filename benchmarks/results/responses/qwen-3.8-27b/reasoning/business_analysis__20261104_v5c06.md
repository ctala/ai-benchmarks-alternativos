# Qwen 3.8 27B — reasoning/business_analysis

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 428.159s | tokens_per_second: 37.1
- input_tokens: 248 | output_tokens: 15866
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un análisis detallado y acciones concretas basadas en los datos.

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



## Resumen ejecutivo

Tu SaaS está creciendo de forma sólida, pero la **calidad del crecimiento se está deteriorando**: el churn sube, el crecimiento se desacelera y el LTV cae. El **LTV/CAC sigue siendo sano**, así que el problema principal no es adquisición cara, sino **retención/expansión**.

---

## 1) Métricas clave

### Supuestos de cálculo

Asumo que los usuarios y MRR reportados son **a fin de mes**. Por eso, para churn rate uso la base inicial del mes, es decir, los usuarios del mes anterior.

Fórmulas:

- **ARPU = MRR / Usuarios**
- **Churn rate = churns / usuarios de inicio del mes**
- **MRR churn = churns × ARPU**
- **Growth rate = usuarios finales - usuarios iniciales / usuarios iniciales**
- **LTV/CAC = LTV / CAC**
- **NRR estimado** = MRR de clientes existentes sin expansión ni contracción.  
  Como no tienes datos de expansión/contracción, lo estimo como:

\[
NRR \approx 1 - \text{churn rate de MRR}
\]

> Nota: si tus “usuarios” mensuales son de inicio de mes o promedio, el churn rate simple sería:  
> Enero 3.75%, Febrero 3.85%, Marzo 4.60%.  
> Con datos de fin de mes, el cálculo más correcto es el que muestro abajo.

### Tabla de métricas operativas

| Mes | Usuarios | MRR | ARPU | Churns | Churn rate | MRR churn | Growth usuarios | Growth MRR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Enero | 1,200 | $18,000 | $15.00 | 45 | 3.75%* | $675 | n/d | n/d |
| Febrero | 1,350 | $20,250 | $15.00 | 52 | 4.33% | $780 | +12.50% | +12.50% |
| Marzo | 1,480 | $22,200 | $15.00 | 68 | 5.04% | $1,020 | +9.63% | +9.63% |

\* Enero no tiene mes anterior, así que uso los 1,200 usuarios como proxy.

### Tabla de unit economics y retención estimada

| Mes | CAC | LTV | LTV/CAC | NRR estimado* |
|---|---:|---:|---:|---:|
| Enero | $85 | $420 | 4.94x | 96.25%* |
| Febrero | $92 | $415 | 4.51x | 95.67% |
| Marzo | $78 | $408 | 5.23x | 94.96% |

\* NRR estimado asumiendo que no hay expansión ni contracción de MRR. En la realidad necesitas saber cuánto MRR ganaste por upsell/expansión y cuánto perdiste por downsell/contracción.

---

## 2) Tendencias preocupantes

### 1. El churn está acelerándose

- Churn rate: de **4.33% en febrero** a **5.04% en marzo**.
- Churns absolutos: de **52** a **68**.
- MRR perdido por churn: de **$780** a **$1,020**.

Eso significa que estás perdiendo más ingresos cada mes. Con un churn mensual cercano al 5%, si no se corrige, el problema se vuelve estructural.

### 2. El crecimiento se está frenando

- Febrero: crecimiento de **+12.50%**.
- Marzo: crecimiento de **+9.63%**.

Aunque sigues creciendo, la tasa baja. Además, el ARPU sigue en **$15**, por lo que todo el crecimiento depende de meter usuarios nuevos. No estás generando crecimiento por expansión o aumento de precio.

### 3. El LTV está bajando

- Enero: $420
- Febrero: $415
- Marzo: $408

El LTV/CAC sigue siendo bueno, sobre todo en marzo con **5.23x**, pero la dirección del LTV no es buena. Si el churn sigue subiendo o el CAC vuelve a subir, esa métrica se puede deteriorar rápido.

### 4. NRR por debajo de 100%

Tu NRR estimado está entre **95% y 96%**. Eso indica que tu base de clientes existentes está contrayendo ingresos netos. En un SaaS sano, normalmente se busca NRR por encima de 100%, aunque depende mucho del modelo.

### 5. ARPU plano

El ARPU es **$15** en los tres meses. Eso sugiere que:

- No hay upsell relevante.
- No hay expansión de consumo.
- No hay cambios de precio visibles.
- La retención de valor por cliente no está mejorando.

---

## 3) Tres acciones concretas basadas en los datos

### Acción 1: Crear un plan urgente anti-churn

Prioridad: **reducir churn**.

Objetivo sugerido:

- Bajar el churn de **5.04% a 4.0% en 60 días**.
- Impacto aproximado: recuperar entre **$200 y $250 MRR mensual**, dependiendo del mes.

Acciones concretas:

1. Segmentar los 68 churns de marzo por:
   - Mes de vida del cliente.
   - Canal de adquisición.
   - Plan.
   - Uso del producto.
   - Motivo de cancelación.
   - Último evento antes del churn.

2. Lanzar 2 experimentos de retención:
   - Onboarding más fuerte para los primeros 14 días.
   - Alertas de riesgo para usuarios con caída de uso.
   - Win-back a clientes que cancelaron en los últimos 60 días.

3. KPIs:
   - Churn rate mensual.
   - MRR churn.
   - Tasa de recuperación de cancelados.
   - Churn de clientes de 30 a 90 días.

---

### Acción 2: Medir y activar expansión de ingresos

Hoy no ves expansión de ARPU. Necesitas crear al menos una vía de upsell.

Objetivo sugerido:

- Subir ARPU de **$15 a $16.50** en 90 días.
- Eso sería un **+10%** de ARPU.
- Con 1,480 usuarios, impactaría en:

\[
1,480 \times \$1.50 = \$2,220 \text{ MRR incremental}
\]

Acciones concretas:

1. Crear un plan superior o add-on.
2. Ofrecer límites mayores, usuarios adicionales, volumen, analítica, integraciones o soporte premium.
3. Medir expansión MRR y contracción MRR por separado.
4. Buscar NRR real >100%.

Sin expansión, tu crecimiento dependerá demasiado de vender usuarios nuevos.

---

### Acción 3: Optimizar adquisición hacia clientes con mayor LTV

Tu CAC bajó de $92 a $78, que es positivo. Pero el LTV también cayó. La meta no es solo gastar menos, sino comprar mejores clientes.

Objetivo sugerido:

- Mantener CAC cerca de **$75-$80**.
- Subir LTV a **$450** en 90 días.
- LTV/CAC objetivo: **5.5x o más**.

Acciones concretas:

1. Revisar canales de adquisición por:
   - CAC.
   - Churn a 60/90 días.
   - LTV inicial.
   - Activación.
   - NPS o riesgo de cancelación.

2. Reducir gasto en canales que traen churn alto.
3. Aumentar gasto en canales que traen clientes con mayor duración y menor churn.
4. Enfocar adquisición a segmentos con mejor fit.

---

## 4) Proyección de abril si las tendencias continúan

### Escenario base

Asumo:

- Crecimiento neto de abril igual al de marzo: **+9.63%**.
- Churn rate de abril igual al de marzo: **5.04%**.
- ARPU constante: **$15**.
- CAC último: **$78**.
- LTV último: **$408**.

### Proyección abril

| Indicador | Abril proyectado |
|---|---:|
| Usuarios | 1,623 |
| MRR | $24,338 |
| Growth neto | +9.63% |
| Churns | ~75 |
| MRR churn | ~$1,118 |
| LTV/CAC | 5.23x |
| NRR estimado | ~95.0% |

Cálculo:

\[
1,480 \times 1.0963 = 1,622.5 \approx 1,623
\]

\[
1,623 \times \$15 = \$24,345 \approx \$24,338
\]

\[
1,480 \times 5.04\% \approx 74.5 \approx 75 \text{ churns}
\]

\[
75 \times \$15 = \$1,125 \approx \$1,118
\]

### Escenario conservador

Si el churn sigue acelerándose y las altas nuevas se mantienen cerca de las 198 nuevas de marzo, abril podría ser más bajo:

| Indicador | Abril conservador |
|---|---:|
| Usuarios | 1,590-1,600 |
| MRR | $23,850-$24,000 |
| Churns | 80-85 |
| Churn rate | ~5.4%-5.7% |

---

## Conclusión

Tu negocio tiene una base unitaria decente porque el **LTV/CAC está sobre 4.5x**, pero tienes una señal clara de advertencia: **el churn sube y el NRR está por debajo de 100%**.

Prioridad de acciones:

1. **Reducir churn** de 5% a 4% en 60 días.
2. **Generar expansión** para subir ARPU y NRR.
3. **Mejorar calidad de adquisición** para subir LTV sin inflar CAC.