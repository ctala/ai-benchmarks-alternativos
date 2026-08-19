# GPT-OSS 20B — reasoning/business_analysis

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.64 | quality: 9.32
- latency_total: 20.837s | tokens_per_second: 98.3
- input_tokens: 229 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando cálculos detallados y análisis de tendencias con sugerencias prácticas.

## Respuesta completa

## 1. Métricas clave (cálculos mensuales)

| Mes | Usuarios (Inicio) | MRR (Inicio) | Churns | Churn Rate | Crecimiento de Usuarios | Crecimiento de MRR | LTV/CAC | NRR (Net Revenue Retention) |
|-----|------------------|--------------|--------|-----------|------------------------|--------------------|---------|-----------------------------|
| **Enero** | 1 200 | $18 000 | 45 | **3.75 %** | – | – | 420 / 85 = **4.94** | (18 000–675)/18 000 = **96.3 %** |
| **Febrero** | 1 350 | 20 250 | 52 | **3.85 %** | **12.5 %** | **12.5 %** | 415 / 92 = **4.51** | (20 250–780)/20 250 = **96.2 %** |
| **Marzo** | 1 480 | 22 200 | 68 | **4.60 %** | **9.6 %** | **9.6 %** | 408 / 78 = **5.23** | (22 200–1 020)/22 200 = **95.4 %** |

**Notas de cálculo**

- **Churn Rate** = Churns ÷ Usuarios (Inicio).  
- **Churned MRR** se estima como *Churns × (MRR ÷ Usuarios)* (promedio de MRR por usuario ≈ $15).  
- **NRR** = (MRR (Inicio) – Churned MRR) ÷ MRR (Inicio).  
- Se asume que no hubo expansión de MRR (upsells), por lo que NRR ≈ Retention Rate.

---

## 2. Tendencias preocupantes

| Indicador | Tendencia | Comentario |
|-----------|-----------|------------|
| **Churn Rate** | ↑ 3.75 % → 4.60 % | La caída de usuarios se está acelerando; sin intervención, la base quedará cada vez más frágil. |
| **Crecimiento de Usuarios / MRR** | ↓ 12.5 % → 9.6 % | El ritmo de adquisición se está desacelerando, reflejando una saturación de mercado o una propuesta de valor que no crece proporcionalmente. |
| **LTV/CAC** | 4.94 → 4.51 → 5.23 | El descenso de Febrero indica que los costos de adquisición están superando en parte el valor que generan los clientes, aunque marzo recupera ese valor. No es sostenible si la tendencia de CAC sigue subiendo. |
| **NRR** | 96.3 % → 95.4 % | La retención de ingresos (incluidos los ingresos perdidos por churn) está deteriorándose; sin mejoras, la empresa perderá ingresos recurrentes. |

**Conclusión:**  
El mayor riesgo es el *increase* sostenido en la tasa de churn y la caída en crecimiento y NRR. Si la CAC sigue al alza, el margen LTV/CAC se reducirá