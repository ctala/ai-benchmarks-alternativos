# Gemini 3.1 Flash Lite (GA) — ocr_extraction/screenshot_table_extraction

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 7.81 | quality: 8.0
- latency_total: 2.783s | tokens_per_second: 275.2
- input_tokens: 418 | output_tokens: 766

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo una captura de pantalla de un dashboard de metricas. El contenido visible es:

DASHBOARD - KPIs Marzo 2026

+------------------+--------+--------+--------+---------+
| Metrica          | Enero  | Feb    | Marzo  | Var M/M |
+------------------+--------+--------+--------+---------+
| MRR              | $45.2K | $48.7K | $52.1K | +7.0%   |
| Churn Rate       | 4.2%   | 3.8%   | 3.1%   | -0.7pp  |
| NPS              | 42     | 45     | 51     | +6      |
| CAC              | $234   | $198   | $187   | -$11    |
| LTV              | $1,890 | $2,010 | $2,340 | +$330   |
| Active Users     | 1,234  | 1,456  | 1,678  | +15.3%  |
| Support Tickets  | 89     | 76     | 63     | -17.1%  |
| Avg Response (h) | 4.2    | 3.1    | 2.4    | -0.7    |
+------------------+--------+--------+--------+---------+

Tendencia general: ↑ Positiva en todas las metricas

Extrae los datos en formato JSON y ademas:
1. Calcula el LTV/CAC ratio para cada mes
2. Identifica la metrica con mayor mejora porcentual
3. Proyecta los valores de Abril si la tendencia se mantiene

Responde en JSON estructurado.


## Respuesta completa

Aquí tienes la información procesada y estructurada en formato JSON:

```json
{
  "datos_dashboard": {
    "enero": {
      "MRR": 45200,
      "Churn_Rate": 0.042,
      "NPS": 42,
      "CAC": 234,
      "LTV": 1890,
      "Active_Users": 1234,
      "Support_Tickets": 89,
      "Avg_Response_h": 4.2,
      "LTV_CAC_Ratio": 8.08
    },
    "febrero": {
      "MRR": 48700,
      "Churn_Rate": 0.038,
      "NPS": 45,
      "CAC": 198,
      "LTV": 2010,
      "Active_Users": 1456,
      "Support_Tickets": 76,
      "Avg_Response_h": 3.1,
      "LTV_CAC_Ratio": 10.15
    },
    "marzo": {
      "MRR": 52100,
      "Churn_Rate": 0.031,
      "NPS": 51,
      "CAC": 187,
      "LTV": 2340,
      "Active_Users": 1678,
      "Support_Tickets": 63,
      "Avg_Response_h": 2.4,
      "LTV_CAC_Ratio": 12.51
    }
  },
  "analisis": {
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Active Users",
      "mejora_marzo": "15.3%"
    },
    "proyeccion_abril": {
      "metodologia": "Basada en la variación absoluta o porcentual media de los últimos 2 meses",
      "valores_estimados": {
        "MRR": 55747,
        "Churn_Rate": 0.026,
        "NPS": 57,
        "CAC": 178,
        "LTV": 2505,
        "Active_Users": 1935,
        "Support_Tickets": 52,
        "Avg_Response_h": 1.9
      }
    }
  }
}
```

### Notas sobre los cálculos:
1.  **LTV/CAC Ratio:** Se calculó dividiendo el LTV entre el CAC para cada mes. Se observa una mejora constante en la eficiencia del capital (de 8.08x a 12.51x).
2.  **Mayor mejora:** *Active Users* presenta el crecimiento porcentual más agresivo (+15.3% en el último mes).
3.  **Proyecciones de Abril:** 
    *   Para métricas de crecimiento (MRR, Usuarios) se aplicó la tasa de crecimiento del último mes.
    *   Para métricas de eficiencia (CAC, Churn, Tickets, Response) se aplicó la tendencia de reducción constante observada entre febrero y marzo.