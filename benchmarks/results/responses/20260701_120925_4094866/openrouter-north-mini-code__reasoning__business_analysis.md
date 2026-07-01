# North Mini Code — reasoning/business_analysis

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 8.15 | quality: 8.54
- latency_total: 28.802s | tokens_per_second: 71.0
- input_tokens: 157 | output_tokens: 2046

## Respuesta completa

A continuación, encontrarás un análisis conciso y basado en datos de tus tres meses de actividad, junto con las métricas clave solicitadas, las señales de alerta, tres acciones prácticas y una proyección para abril (si las tendencias actuales continúan).

---

## 1️⃣ Cálculo de las métricas clave

| Mes | Usuarios (final) | MRR | Churns | CAC | LTV | **Tasa de churn**<br>(churns ÷ usuarios) | **Tasa de crecimiento**<br>((Usuariosₜ - Usuariosₜ₋₁) ÷ Usuariosₜ₋₁) | **LTV ÷ CAC** | ARPU (MRR ÷ usuarios) |
|-----|------------------|-----|--------|-----|-----|------------------------------|---------------------------------------------------|--------------|-------------------|
| **Enero** | 1,200 | $18,000 | 45 | $85 | $420 | **3.75 %** | – (base) | **4.94×** | **$15** |
| **Febrero** | 1,350 | $20,250 | 52 | $92 | $415 | **3.85 %** | **12.5 %** | **4.51×** | **$15** |
| **Marzo** | 1,480 | $22,200 | 68 | $78 | $408 | **4.59 %** | **9.6 %** | **5.23×** | **$15** |

### Retención de ingresos netos (NRR) – cálculo aproximado
*(Suponiendo que cada usuario genera $15 de MRR y que no hay contracciones; la “expansión” se toma como el incremento mensual del MRR.)*

\[
\textNRR = \frac{\text{MRR inicial} + \text{Ingreso por expansión} - \text{Ingreso por churn}}{\text{MRR inicial}}
\]

| Período | MRR inicial | Ingreso por expansión (Δ MRR) | Ingreso por churn (churns × $15) | **NRR** |
|--------|-------------|---------------------------|---------------------------|--------|
| Ene → Feb | $18,000 | $2,250 | $675 | **108.8 %** |
| Feb → Mar | $20,250 | $1,950 | $780 | **105.8 %** |

*Una NRR > 100 % indica que estás generando ingresos más allá de la pérdida por churn, lo cual es saludable, aunque la tasa está disminuyendo ligeramente.*

---

## 2️⃣ Tendencias preocupantes

| Tendencia | Por qué es importante | Dirección de la señal |
|-------|----------------|--------------------|
| **Tasa de churn** ↑ (3.75 % → 4.59 %) | Un aumento constante del 0.8 pp en tres meses significa que los usuarios abandonan más rápido de lo previsto. | ❌ |
| **Tasa de crecimiento** ↓ (12.5 % → 9.6 %) | El ritmo de adquisición de nuevos usuarios se está desacelerando, lo que reduce el potencial de expansión. | ❌ |
| **LTV** ↓ ligeramente ($