# MiMo-V2.5 Pro — ocr_extraction/screenshot_table_extraction

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 6.16 | quality: 6.16
- latency_total: 23.515s | tokens_per_second: 87.1
- input_tokens: 667 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "dashboard": "KPIs Marzo 2026",
  "tendencia_general": "↑ Positiva en todas las métricas",
  
  "datos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD"
    },
    "Churn_Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "porcentaje"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD"
    },
    "Active_Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios"
    },
    "Support_Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets"
    },
    "Avg_Response_Time": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas"
    }
  },

  "analisis": {
    "ltv_cac_ratio": {
      "enero": 8.08,
      "febrero": 10.15,
      "marzo": 12.51,
      "interpretacion": "Ratio excelente y en mejora continua. Un LTV/CAC > 3 se considera saludable; 12.51 indica altísima eficiencia en adquisición."
    },

    "metrica_mayor_mejora_porcentual": {
      "metrica": "Avg Response Time",
      "cambio_enero_a_marzo": "-42.9%",
      "valores": "4.2h → 2.4h",
      "nota": "Es la métrica con mayor mejora porcentual. Se redujo casi a la mitad en dos meses, lo que probablemente explica la mejora en NPS y reducción de tickets."
    },

    "ranking_mejora_porcentual": [
      {"metrica": "Avg Response Time", "cambio": "-42.9%", "tipo": "reducción = mejora"},
      {"metrica": "Support Tickets", "cambio": "-29.2%", "tipo": "