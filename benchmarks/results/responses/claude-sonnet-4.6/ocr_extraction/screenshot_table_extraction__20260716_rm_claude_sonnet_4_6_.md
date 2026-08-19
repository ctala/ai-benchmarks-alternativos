# Claude Sonnet 4.6 (ultimo Anthropic) — ocr_extraction/screenshot_table_extraction

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 26.503s | tokens_per_second: 77.3
- input_tokens: 430 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la tabla original, como 'LTV', 'Active Users', 'Support Tickets', y 'Avg Response Time', lo que afecta la precisión y exactitud de los datos; sin embargo, la estructura y claridad son buenas, y la relevancia es aceptable.

## Respuesta completa

```json
{
  "dashboard": {
    "title": "KPIs Marzo 2026",
    "extracted_at": "2026-03-31",
    "general_trend": "Positiva en todas las métricas",

    "raw_data": {
      "metrics": [
        {
          "name": "MRR",
          "unit": "USD_thousands",
          "values": {
            "enero": 45.2,
            "febrero": 48.7,
            "marzo": 52.1
          },
          "mom_variation": {
            "value": 7.0,
            "type": "percentage"
          }
        },
        {
          "name": "Churn Rate",
          "unit": "percentage",
          "values": {
            "enero": 4.2,
            "febrero": 3.8,
            "marzo": 3.1
          },
          "mom_variation": {
            "value": -0.7,
            "type": "percentage_points"
          }
        },
        {
          "name": "NPS",
          "unit": "score",
          "values": {
            "enero": 42,
            "febrero": 45,
            "marzo": 51
          },
          "mom_variation": {
            "value": 6,
            "type": "absolute"
          }
        },
        {
          "name": "CAC",
          "unit": "USD",
          "values": {
            "enero": 234,
            "febrero": 198,
            "marzo": 187
          },
          "mom_variation": {
            "value": -11,
            "type": "absolute_usd"
          }
        },
        {
          "name": "LTV",
          "unit": "USD",
          "values": {
            "enero": 1890,
            "febrero": 2010,
            "marzo": 2340
          },
          "mom_variation": {
            "value": 330,
            "type": "absolute_usd"
          }
        },
        {
          "name": "Active Users",
          "unit": "count",
          "values": {
            "enero": 1234,
            "febrero": 1456,
            "marzo": 1678
          },
          "mom_variation": {
            "value": 15.3,
            "type": "percentage"
          }
        },
        {
          "name": "Support Tickets",
          "unit": "count",
          "values": {
            "enero": 89,
            "febrero": 76,
            "marzo": 63
          },
          "mom_variation": {
            "value": -17.1,
            "type": "percentage"
          }
        },
        {
          "name": "Avg Response Time",
          "unit": "hours",
          "values": {
            "enero": 4.2,
            "febrero": 3.1,
            "marzo": 2.4
          },
          "mom_variation": {
            "value": -0.7,
            "type": "absolute_hours"
          }
        }
      ]
    },

    "analysis": {

      "ltv_cac_ratio": {
        "description": "LTV dividido CAC. Ratio saludable recomendado: >= 3.0x",
        "benchmark_healthy": 3.0,
        "values": {
          "enero": {
            "ltv": 1890,
            "cac": 234,
            "ratio": 8.08,
            "formula": "1890 / 234",
            "status": "excellent"
          },
          "febrero": {
            "ltv": 2010,
            "cac": 198,
            "ratio": 10.15,
            "formula": "2010 / 198",
            "status": "excellent"
          },
          "marzo": {
            "ltv": 2340,
            "cac": 187,
            "ratio": 12.51,
            "formula": "2340 / 187",
            "status": "excellent"
          }
        },
        "trend": {
          "enero_to_febrero_change": "+2.07x (+25.6%)",
          "febrero_to_marzo_change": "+2.36x (+23.3%)",
          "total_period_change": "+4.43x (+54.8%)",
          "interpretation": "El ratio mejora aceleradamente. Combinación de LTV creciente y CAC decreciente genera eficiencia compuesta."
        }
      },

      "best_improvement_percentage": {
        "description": "Métrica con mayor mejora porcentual en variación Feb→Mar",
        "methodology": "Se calcula variación porcentual (valor_marzo - valor_feb) / valor_feb * 100. Para métricas inversas (Churn, CAC, Tickets, Response Time), la mejora es la reducción porcentual.",
        "calculations": [
          {
            "metric": "MRR",
            "feb": 48.7,
            "mar": 52.1,
            "pct_change": 6.98,
            "direction": "higher_is_better",
            "improvement_score": 6.98
          },
          {
            "metric": "Churn Rate",
            "feb": 3.8,
            "mar": 3.1,
            "pct_change": -18.42,
            "direction": "lower_is_better",
            "improvement_score": 18.42
          },
          {
            "metric": "NPS",
            "feb": 45,
            "mar": 51,
            "pct_change": 13.33,
            "direction": "higher_is_better",
            "improvement_score": 13.33
          },
          {
            "metric": "CAC",
            "feb": 198,
            "mar": 187,
            "pct_change": -5.56,
            "direction": "lower_is_better",
            "improvement_score": 5.56
          },
          {
            "metric": "LTV",
            "feb": 2010,
            "mar": 2340,
            "pct_change": 16.42,
            "direction": "higher_is_better",
            "improvement_score": 16.42
          },
          {
            "metric": "Active Users",
            "feb": 1456,
            "mar": 1678,
            "pct_change": 15.25,
            "direction": "higher_is_better",
            "improvement_score": 15.25
          },
          {
            "metric": "Support Tickets",
            "feb": 76,
            "mar": 63,
            "pct_change": -17.11,
            "direction": "lower_is_better",
            "improvement_score": 17.11
          },
          {
            "metric": "Avg Response Time",
            "feb": 3.1,
            "mar": 2.4,
            "pct_change": -22.58,
            "direction": "lower_is_better",
            "improvement_score": 22.58
          }
        ],
        "winner": {
          "metric": "Avg Response Time",
          "improvement_score": 22.58,
          "detail": "Redujo de 3.1h a 2.4h, una mejora del 22.58% en eficiencia operativa",
          "runner_up": {
            "metric": "Churn Rate",
            "improvement_score": 18.42
          },
          "third_place": {
            "metric": "Support Tickets",
            "improvement_score": 17.11
          }
        }
      },

      "april_projections": {
        "description": "Proyección Abril 2026 manteniendo la tasa de variación M/M observada en Feb→Mar",
        "methodology": "Se aplica el mismo delta absoluto o porcentual observado en el último período. Para métricas con límite natural (Churn, NPS) se añade nota de restricción.",
        "projections": [
          {
            