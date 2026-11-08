# Qwen 3.6 35B base (OpenRouter FP8) — ocr_extraction/screenshot_table_extraction

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.99 | quality: 10.0
- latency_total: 10.36s | tokens_per_second: 122.0
- input_tokens: 429 | output_tokens: 1264

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

Aquí tienes el análisis estructurado en JSON, incluyendo los datos extraídos, el cálculo del LTV/CAC, la identificación de la métrica con mayor mejora y la proyección para abril basada en la tendencia mensual (Month-over-Month).

```json
{
  "dashboard_info": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "Positiva"
  },
  "datos_base": {
    "mrr": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "var_mom_pct": 7.0
    },
    "churn_rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "var_mom_pct": -0.7
    },
    "nps": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "var_mom_abs": 6
    },
    "cac": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "var_mom_abs": -11
    },
    "ltv": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "var_mom_abs": 330
    },
    "active_users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "var_mom_pct": 15.3
    },
    "support_tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "var_mom_pct": -17.1
    },
    "avg_response_hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "var_mom_abs": -0.7
    }
  },
  "analisis_adicional": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51
    },
    "metrica_mayor_mejora_pct": {
      "metrica": "Support Tickets",
      "valor_mejora": -17.1,
      "nota": "Reducción del 17.1% en tickets (mejora positiva en eficiencia)"
    },
    "proyeccion_abril_2026": {
      "metodo": "Tendencia MoM (Month-over-Month) de Marzo",
      "valores_proyectados": {
        "mrr": 55748.10,
        "churn_rate": 2.72,
        "nps": 57,
        "cac": 176.89,
        "ltv": 2723.40,
        "active_users": 1934.34,
        "support_tickets": 52.25,
        "avg_response_hours": 1.73
      },
      "notas_proyeccion": [
        "MRR: +7.0% MoM",
        "Churn: -0.7pp (asumiendo decremento lineal de puntos porcentuales)",
        "NPS: +6 puntos (tendencia lineal)",
        "CAC: -$10.11 (tendencia decreciente)",
        "LTV: +$383.40 (tendencia creciente)",
        "Usuarios: +15.3% MoM",
        "Tickets: -17.1% MoM",
        "Respuesta: -0.7h (asumiendo decremento lineal)"
      ]
    }
  }
}
```

### Notas sobre el cálculo:
1. **LTV/CAC Ratio**: Se calculó dividiendo `LTV / CAC` para cada mes.
   - Enero: 1890 / 234 ≈ 8.08
   - Febrero: 2010 / 198 ≈ 10.15
   - Marzo: 2340 / 187 ≈ 12.51
2. **Mayor mejora porcentual**: Se evaluó la variación porcentual (Var M/M). Aunque el NPS subió 6 puntos, la reducción del 17.1% en **Support Tickets** es el mayor cambio porcentual absoluto en la tabla, lo que indica una mejora significativa en la eficiencia del soporte.
3. **Proyección Abril**:
   - Para métricas con `%`: Se aplicó la misma tasa de crecimiento/decadencia de Marzo sobre el valor de Marzo.
   - Para métricas con valores absolutos (pp, $, h): Se asumió que el cambio absoluto mensual se mantiene constante (tendencia lineal), ya que no se proporcionaron tasas de crecimiento exponencial para ellas.