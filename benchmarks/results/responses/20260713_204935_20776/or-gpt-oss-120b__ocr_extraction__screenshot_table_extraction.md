# GPT-OSS 120B — ocr_extraction/screenshot_table_extraction

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 1.91 | quality: 0.0
- latency_total: 46.307s | tokens_per_second: 44.2
- input_tokens: 438 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta extrae correctamente algunos datos de la tabla, pero incluye una métrica (LTV) que no estaba en el dashboard original y tiene un valor incorrecto para CAC en Marzo, afectando la precisión y exactitud de los datos.

## Respuesta completa

```json
{
  "title": "DASHBOARD - KPIs Marzo 2026",
  "metrics": {
    "MRR": {
      "unit": "USD",
      "values": {
        "Enero": 45200,
        "Febrero": 48700,
        "Marzo": 52100
      }
    },
    "Churn Rate": {
      "unit": "%",
      "values": {
        "Enero": 4.2,
        "Febrero": 3.8,
        "Marzo": 3.1
      }
    },
    "NPS": {
      "unit": "points",
      "values": {
        "Enero": 42,
        "Febrero": 45,
        "Marzo": 51
      }
    },
    "CAC": {
      "unit": "USD",
      "values": {
        "Enero": 234,
        "Febrero": 198,
        "Marzo": 187
      }
    },
    "LTV": {
      "unit": "USD",
      "values": {
        "Enero": 1890,
        "Febrero": 2010,
        "Marzo": 2340
      }
    },
    "