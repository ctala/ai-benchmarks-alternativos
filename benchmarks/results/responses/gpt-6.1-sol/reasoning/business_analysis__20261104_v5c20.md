# GPT-6.1 Sol — reasoning/business_analysis

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.15 | quality: 9.76
- latency_total: 25.488s | tokens_per_second: 67.6
- input_tokens: 168 | output_tokens: 1722
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

## 1. Métricas clave

**Supuesto:** los usuarios reportados son los activos al cierre de cada mes y los “churns” son usuarios perdidos durante ese mes. Si las cifras representan otra cosa —por ejemplo, usuarios registrados acumulados— habría que ajustar los cálculos.

| Métrica | Enero | Febrero | Marzo |
|---|---:|---:|---:|
| Usuarios activos | 1.200 | 1.350 | 1.480 |
| MRR | $18.000 | $20.250 | $22.200 |
| Crecimiento mensual de usuarios | — | 12,50% | 9,63% |
| Crecimiento mensual de MRR | — | 12,50% | 9,63% |
| Churn rate mensual¹ | No calculable | 4,33% | 5,04% |
| LTV/CAC | 4,94× | 4,51× | 5,23× |
| MRR por usuario | $15 | $15 | $15 |
| Net revenue retention —NRR—² | No calculable | No calculable | No calculable |

**Fórmulas y límites:**

- **Crecimiento mensual:** `(valor actual / valor anterior) − 1`.
- **Churn rate:** `usuarios perdidos / usuarios al inicio del mes`.  
  Febrero: `52 / 1.200 = 4,33%`. Marzo: `68 / 1.350 = 5,04%`. Para enero falta el cierre de diciembre. Dividir `45 / 1.200 = 3,75%` sería una aproximación con otra base, no el churn estándar.
- **LTV/CAC:** `LTV / CAC`.
- **NRR:** `(MRR inicial + expansión − contracción − MRR perdido) / MRR inicial`, considerando **solo clientes existentes al inicio del mes**. No incluye ingresos de nuevos clientes.

**La NRR real no puede calcularse con estos datos.** Si cada usuario generara exactamente $15 y no hubiera expansión ni contracción, su estimación sería **95,67% en febrero** y **94,96% en marzo**. El promedio constante de $15 por usuario, por sí solo, no demuestra esos supuestos.

## 2. Tendencias preocupantes

### El crecimiento se desacelera mientras aumenta el churn
El crecimiento mensual baja de **12,50% a 9,63%**, mientras el churn sube de **4,33% a 5,04%**: aproximadamente **0,70 puntos porcentuales**.

Además, las altas implícitas serían:

- **Febrero:** `1.350 − 1.200 + 52 = 202`.
- **Marzo:** `1.480 − 1.350 + 68 = 198`.

Suponiendo que no haya otros ajustes, **entran ligeramente menos usuarios y se pierden más**.

### El valor por cliente se deteriora
El LTV cae de **$420 a $408**, un **2,86%** en dos meses. Es compatible con problemas de retención, aunque habría que conocer cómo calculas el LTV para confirmar la relación.

### La mejora de adquisición puede ocultar la caída del LTV
El CAC de marzo mejora hasta **$78**, elevando LTV/CAC a **5,23×**. Es una señal positiva, pero la mejora del ratio viene del menor CAC, **no de un mayor valor del cliente**.

El MRR por usuario permanece en **$15**: no hay evidencia de crecimiento de monetización promedio que compense las bajas.

## 3. Tres acciones concretas

1. **Auditar las bajas y ejecutar un experimento de retención.**  
   Segmentar las 68 bajas de marzo por antigüedad, canal y uso; entrevistar una muestra y actuar sobre la causa principal. Si predominan bajas tempranas, probar onboarding asistido y mensajes ante inactividad. **Objetivo inicial:** volver al churn de febrero, aproximadamente **4,33%**.

2. **Redistribuir adquisición según calidad de cohorte, no solo CAC.**  
   Identificar qué canales explican el CAC de $78 y comparar su retención a 30/60/90 días. Aumentar inversión únicamente donde el menor CAC no venga acompañado de peor retención. **Medir:** CAC y LTV/CAC por canal.

3. **Instrumentar el desglose de MRR y probar una vía de expansión.**  
   Separar MRR nuevo, expansión, contracción y bajas para calcular NRR real. Después, probar un complemento o plan superior con clientes de uso elevado. **Medir:** MRR de expansión, NRR y cancelaciones asociadas al cambio.

## 4. Proyección de abril

Uso una **extrapolación lineal simple**: repetir el cambio mensual absoluto promedio entre enero y marzo. Con solo tres meses, es un escenario orientativo, no un pronóstico robusto.

| Indicador | Cambio mensual promedio | Abril proyectado |
|---|---:|---:|
| Usuarios | +140 | **1.620** |
| MRR | +$2.100 | **$24.300** |
| Usuarios perdidos | +11,5 | **≈80** |
| CAC | −$3,50 | **$74,50** |
| LTV | −$6 | **$402** |

De ahí se deriva:

- **Crecimiento de usuarios y MRR:** aproximadamente **9,46%**.
- **Churn rate:** aproximadamente **5,4%**, usando 1.480 usuarios iniciales.
- **LTV/CAC:** aproximadamente **5,40×**.
- **NRR real:** sigue sin poder proyectarse con estos datos; bajo los supuestos restrictivos anteriores, sería aproximadamente **94,6%**.

**Conclusión:** el SaaS sigue creciendo y la adquisición se abarata, pero la retención empeora. La prioridad es frenar las bajas antes de acelerar el gasto comercial.