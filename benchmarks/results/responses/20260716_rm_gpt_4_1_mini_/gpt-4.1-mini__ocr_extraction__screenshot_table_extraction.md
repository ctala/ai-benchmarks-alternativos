# GPT-4.1 Mini — ocr_extraction/screenshot_table_extraction

- model_id: `gpt-4.1-mini`
- success: True  | final: 7.61 | quality: 8.0
- latency_total: 8.604s | tokens_per_second: 106.8
- input_tokens: 380 | output_tokens: 919
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "dashboard": "KPIs Marzo 2026",
  "metrics": {
    "MRR": {
      "Enero": 45200,
      "Febrero": 48700,
      "Marzo": 52100,
      "Var_M_M": 0.07
    },
    "Churn_Rate": {
      "Enero": 0.042,
      "Febrero": 0.038,
      "Marzo": 0.031,
      "Var_M_M_pp": -0.007
    },
    "NPS": {
      "Enero": 42,
      "Febrero": 45,
      "Marzo": 51,
      "Var_M_M": 6
    },
    "CAC": {
      "Enero": 234,
      "Febrero": 198,
      "Marzo": 187,
      "Var_M_M": -11
    },
    "LTV": {
      "Enero": 1890,
      "Febrero": 2010,
      "Marzo": 2340,
      "Var_M_M": 330
    },
    "Active_Users": {
      "Enero": 1234,
      "Febrero": 1456,
      "Marzo": 1678,
      "Var_M_M": 0.153
    },
    "Support_Tickets": {
      "Enero": 89,
      "Febrero": 76,
      "Marzo": 63,
      "Var_M_M": -0.171
    },
    "Avg_Response_h": {
      "Enero": 4.2,
      "Febrero": 3.1,
      "Marzo": 2.4,
      "Var_M_M": -0.7
    }
  },
  "ltv_cac_ratio": {
    "Enero": 8.08,
    "Febrero": 10.15,
    "Marzo": 12.52
  },
  "metric_with_greatest_percentage_improvement": {
    "metric": "Active_Users",
    "improvement_percentage": 15.3
  },
  "april_projection": {
    "MRR": 55747,
    "Churn_Rate": 0.0243,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active_Users": 1933,
    "Support_Tickets": 52,
    "Avg_Response_h": 1.7,
    "LTV_CAC_Ratio": 15.17
  }
}
```

---

### Explicación:

1. **Datos en JSON**: Se extraen los valores numéricos, se convierten a números (sin formato de moneda ni porcentaje).

2. **LTV/CAC ratio**:  
   - Enero: 1890 / 234 ≈ 8.08  
   - Febrero: 2010 / 198 ≈ 10.15  
   - Marzo: 2340 / 187 ≈ 12.52

3. **Métrica con mayor mejora porcentual**:  
   - Se consideran variaciones en %, para las métricas que ya están en porcentaje.  
   - Active Users subió +15.3% (la mayor entre todas las métricas positivas).

4. **Proyección Abril** (usando el mismo factor de crecimiento o cambio de Marzo respecto a Febrero):  
   - MRR: 52100 * (1 + 0.07) = 55747  
   - Churn Rate: 0.031 + (-0.007) = 0.024 (2.43%)  
   - NPS: 51 + 6 = 57  
   - CAC: 187 + (-11) = 176  
   - LTV: 2340 + 330 = 2670  
   - Active Users: 1678 * (1 + 0.153) = 1933  
   - Support Tickets: 63 * (1 - 0.171) = 52  
   - Avg Response (h): 2.4 + (-0.7) = 1.7  
   - LTV/CAC Abril: 2670 / 176 ≈ 15.17