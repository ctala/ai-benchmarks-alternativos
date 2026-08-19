# KAT Coder Air v2.5 — ocr_extraction/screenshot_table_extraction

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.57 | quality: 8.0
- latency_total: 10.418s | tokens_per_second: 196.6
- input_tokens: 427 | output_tokens: 2048

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
  "dashboard": {
    "titulo": "KPIs Marzo 2026",
    "periodo": "Enero - Marzo 2026",
    "tendencia_general": "↑ Positiva en todas las métricas"
  },
  "datos_extraidos": {
    "MRR": { "Enero": 45200, "Febrero": 48700, "Marzo": 52100, "Var_M_M": "+7.0%" },
    "Churn_Rate": { "Enero": "4.2%", "Febrero": "3.8%", "Marzo": "3.1%", "Var_M_M": "-0.7pp" },
    "NPS": { "Enero": 42, "Febrero": 45, "Marzo": 51, "Var_M_M": "+6" },
    "CAC": { "Enero": 234, "Febrero": 198, "Marzo": 187, "Var_M_M": "-$11" },
    "LTV": { "Enero": 1890, "Febrero": 2010, "Marzo": 2340, "Var_M_M": "+$330" },
    "Active_Users": { "Enero": 1234, "Febrero": 1456, "Marzo": 1678, "Var_M_M": "+15.3%" },
    "Support_Tickets": { "Enero": 89, "Febrero": 76, "Marzo": 63, "Var_M_M": "-17.1%" },
    "Avg_Response_h": { "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4, "Var_M_M": "-0.7" }
  },
  "ltv_cac_ratio": {
    "Enero": {
      "LTV": 1890,
      "CAC": 234,
      "Ratio": 8.08
    },
    "Febrero": {
      "LTV": 2010,
      "CAC": 198,
      "Ratio": 10.15
    },
    "Marzo": {
      "LTV": 2340,
      "CAC": 187,
      "Ratio": 12.51
    },
    "analisis": "El ratio LTV/CAC mejora consistentemente: de 8.08x en Enero a 12.51x en Marzo (+54.8%). Un ratio >3x se considera saludable; el negocio está muy bien posicionado."
  },
  "mayor_mejora_porcentual": {
    "metrica": "Avg Response Time (horas)",
    "mejora": "-42.9%",
    "detalle": "De 4.2h a 2.4h, una reducción del 42.9% en tiempo de respuesta. Es la métrica con mayor variación porcentual relativa del dashboard.",
    "comparativa": [
      { "metrica": "Avg Response (h)", "mejora_relativa": "-42.9%" },
      { "metrica": "Support Tickets", "mejora_relativa": "-29.2%" },
      { "metrica": "LTV", "mejora_relativa": "+17.5%" },
      { "metrica": "Churn Rate", "mejora_relativa": "-16.7%" },
      { "metrica": "Active Users", "mejora_relativa": "+15.3%" },
      { "metrica": "NPS", "mejora_relativa": "+14.3%" },
      { "metrica": "MRR", "mejora_relativa": "+7.0%" },
      { "metrica": "CAC", "mejora_relativa": "-4.7%" }
    ]
  },
  "proyeccion_abril_2026": {
    "metodologia": "Tasa de variación M/M observada en Marzo extrapolada a Abril",
    "proyecciones": {
      "MRR": {
        "valor_proyectado": 55.75,
        "unidad": "K",
        "formula": "52.1 * 1.07"
      },
      "Churn_Rate": {
        "valor_proyectado": 2.9,
        "unidad": "%",
        "formula": "3.1 - 0.7pp",
        "nota": "Limitado a 0%; no puede bajar indefinidamente"
      },
      "NPS": {
        "valor_proyectado": 57,
        "unidad": "puntos",
        "formula": "51 + 6"
      },
      "CAC": {
        "valor_proyectado": 176,
        "unidad": "$",
        "formula": "187 - 11",
        "nota": "Disminución absoluta constante"
      },
      "LTV": {
        "valor_proyectado": 2700,
        "unidad": "$",
        "formula": "2340 * 1.153"
      },
      "Active_Users": {
        "valor_proyectado": 1934,
        "unidad": "usuarios",
        "formula": "1678 * 1.153"
      },
      "Support_Tickets": {
        "valor_proyectado": 52,
        "unidad": "tickets",
        "formula": "63 * 0.829"
      },
      "Avg_Response_h": {
        "valor_proyectado": 1.9,
        "unidad": "horas",
        "formula": "2.4