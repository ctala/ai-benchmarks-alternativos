# North Mini Code — reasoning/business_analysis

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 8.15 | quality: 8.54
- latency_total: 23.168s | tokens_per_second: 88.3
- input_tokens: 157 | output_tokens: 2046

## Respuesta completa

**1. Cálculo de las métricas clave**

| Mes | Usuarios (inicio) | MRR (total) | Churns | **Tasa de churn** | ΔUsuarios (vs mes anterior) | **Tasa de crecimiento** | CAC | LTV | **LTV / CAC** | **Retención de ingresos netos (NRR)** |
|-------|----------------|-----------|---------|----------------|------------------------|----------------|-----|-----|--------------|------------------------------|
| **Enero** | 1,200 | $18,000 | 45 | **45 ÷ 1,200 = 3.75 %** | – | – | $85 | $420 | **4.94** | – |
| **Febrero** | 1,350 | $20,250 | 52 | **52 ÷ 1,350 = 3.85 %** | +150 | **12.5 %** | $92 | $415 | **4.51** | $20,250 ÷ $18,000 = **112.5 %** |
| **Marzo** | 1,480 | $22,200 | 68 | **68 ÷ 1,480 = 4.59 %** | +130 | **9.63 %** | $78 | $408 | **5.23** | $22,200 ÷ $20,250 = **109.75 %** |

*Notas sobre los cálculos*

* **Tasa de churn** = Churns ÷ Usuarios (inicio de mes). Cuanto más alto sea el número de usuarios, más precisa será la tasa.
* **Tasa de crecimiento** = (Usuarios mes actual – Usuarios mes anterior) ÷ Usuarios mes anterior × 100 %.
* **LTV / CAC** = Valor de por vida ÷ Costo de adquisición.
* **NRR** (en este caso simplificado) = MRR del mes en curso ÷ MRR del mes anterior. Un NRR > 100 % significa que la empresa está generando ingresos netos a partir de la cartera existente (aumento neto tras la pérdida de clientes).

---

**2. Tendencias preocupantes**

| Tendencia | Lo que muestra la tabla | Por qué es importante |
|-------|--------------------------|----------------|
| **Aumento del churn** | 3.75 % → 3.85 % → **4.59 %** (un salto de ≈ 0.7 p.p.) | Una mayor pérdida de clientes reduce el crecimiento de los usuarios y el MRR. |
| **Disminución de la tasa de crecimiento** | 12.5 % → **9.63 %** | El crecimiento de los usuarios se está desacelerando, lo que pone en riesgo el objetivo de expansión. |
| **LTV decreciente** | $420 → $415 → $408 (≈ 3 % de reducción en 3 meses) | Cada cliente vale menos con el tiempo, lo que reduce el potencial de ingresos. |
| **NRR en disminución** | 112.5 % → **109.75 %** | La efectividad de los ingresos generados por la cartera existente está disminuyendo, lo que indica una posible pérdida de clientes o una menor adopción de funciones de mayor valor. |

*Conclusión:* Aunque el crecimiento de los usuarios sigue siendo positivo, el **churn está aumentando más rápido que el crecimiento**, y el **valor de los clientes está disminuyendo**. Esto es una señal de alerta clásica de que el producto o el servicio de atención al cliente puede estar perdiendo terreno.

---

**3. Tres acciones concretas basadas en los datos**

| # | Acción | Cómo se aborda el problema | Métrica clave a seguir |
|---|--------|------------------------|-----------------------|
| **1** | **Implementar un programa de incorporación con "momentos de activación"** (por ejemplo, una llamada de éxito inicial, un taller de introducción al producto, un plan de adopción de 30 días). | Reduce el abandono temprano (la causa principal del aumento del churn) y aumenta el LTV al que los usuarios descubren funciones de mayor valor. | **Tasa de churn** (especialmente en los primeros 30 días), **LTV** |
| **2** | **Lanzar un programa de expansión/upsell** (actualización de planes, módulos adicionales, precios basados en el uso). | Mejora la retención de ingresos netos (NRR) y detiene la disminución del LTV al aumentar el ARPU sin necesidad de nuevos clientes. | **NRR**, **ARPU**, **LTV/CAC** |
| **3** | **Optimizar la adquisición de clientes** – realizar pruebas A/B en los canales de generación de leads y ajustar el mensaje para atraer a usuarios de mayor valor; considerar un aumento estratégico de precios si la elasticidad lo permite. | Estabiliza o reduce el CAC (actualmente volátil: $85 → $92 → $78) y mejora el ratio LTV/CAC (ideal > 3–4). | **CAC**, **LTV/CAC**, **Tasa de crecimiento** |

*Por qué estas tres?* Abordan directamente las tres señales de alerta: el **programa de incorporación** aborda el churn, el **programa de expansión** mejora el NRR y el LTV, y la **optimización de la adquisición** estabiliza el CAC y mejora la relación LTV/CAC.

---

**4. Proyección para abril (asumiendo que las tendencias continúan)**

* Supuestos:
  * La