# Kimi K2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 12.863s | tokens_per_second: 96.6
- input_tokens: 405 | output_tokens: 1242

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

 ```json
{
  "datos_extraidos": {
    "periodo": "Marzo 2026",
    "metricas": {
      "MRR": {"enero": 45200, "febrero": 48700, "marzo": 52100, "unidad": "USD", "var_mm": 0.07},
      "Churn_Rate": {"enero": 4.2, "febrero": 3.8, "marzo": 3.1, "unidad": "porcentaje", "var_mm_pp": -0.7},
      "NPS": {"enero": 42, "febrero": 45, "marzo": 51, "unidad": "puntos", "var_mm": 6},
      "CAC": {"enero": 234, "febrero": 198, "marzo": 187, "unidad": "USD", "var_mm": -11},
      "LTV": {"enero": 1890, "febrero": 2010, "marzo": 2340, "unidad": "USD", "var_mm": 330},
      "Active_Users": {"enero": 1234, "febrero": 1456, "marzo": 1678, "unidad": "usuarios", "var_mm": 0.153},
      "Support_Tickets": {"enero": 89, "febrero": 76, "marzo": 63, "unidad": "tickets", "var_mm": -0.171},
      "Avg_Response_Time": {"enero": 4.2, "febrero": 3.1, "marzo": 2.4, "unidad": "horas", "var_mm": -0.7}
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "tendencia": "creciente",
      "interpretacion": "Excelente salud unitaria; cada dolar invertido en adquisicion genera 12.5x en valor de vida"
    },
    "mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_marzo_sobre_febrero": "16.4%",
      "mejora_acumulada_ene_mar": "23.8%",
      "nota": "Si consideramos mejoras donde menor es mejor, Support Tickets mejoró -17.1% M/M"
    },
    "ranking_mejoras_marzo": [
      {"metrica": "LTV", "mejora": "+16.4%"},
      {"metrica": "Support_Tickets", "mejora": "-17.1% (reducción positiva)"},
      {"metrica": "Active_Users", "mejora": "+15.3%"},
      {"metrica": "NPS", "mejora": "+13.3%"},
      {"metrica": "MRR", "mejora": "+7.0%"}
    ]
  },
  "proyeccion_abril_2026": {
    "metodo": "tendencia lineal ultimos 2 meses",
    "valores_proyectados": {
      "MRR": {"valor": 55450, "unidad": "USD", "crecimiento_esperado": "+6.4%"},
      "Churn_Rate": {"valor": 2.4, "unidad": "%", "nota": "si se mantiene reduccion de 0.7pp"},
      "NPS": {"valor": 57, "unidad": "puntos", "nota": "si se mantiene incremento de +6"},
      "CAC": {"valor": 176, "unidad": "USD", "nota": "si se mantiene reduccion de -$11"},
      "LTV": {"valor": 2670, "unidad": "USD", "crecimiento_esperado": "+14.1%"},
      "Active_Users": {"valor": 1900, "unidad": "usuarios", "crecimiento_esperado": "+13.2%"},
      "Support_Tickets": {"valor": 50, "unidad": "tickets", "nota": "si se mantiene reduccion de -13"},
      "Avg_Response_Time": {"valor": 1.7, "unidad": "horas", "nota": "si se mantiene reduccion de -0.7h"}
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "alertas_proyeccion": [
      "Churn Rate proyectado al 2.4% seria muy bajo; verificar sostenibilidad",
      "LTV creciendo mas rapido que MRR puede indicar concentracion en clientes enterprise"
    ]
  },
  "resumen_ejecutivo": {
    "salud_negocio": "Excelente",
    "drivers_positivos": ["Eficiencia en adquisicion (CAC ↓)", "Retencion mejorando (Churn ↓)", "Satisfaccion creciente (NPS ↑)", "Operaciones mas eficientes (Tickets ↓, Response ↓)"],
    "metrica_clave_a_seguir": "LTV/CAC ratio ya en 12.5x con tendencia a 15x - monitorear calidad de nuevos clientes"
  }
}
```