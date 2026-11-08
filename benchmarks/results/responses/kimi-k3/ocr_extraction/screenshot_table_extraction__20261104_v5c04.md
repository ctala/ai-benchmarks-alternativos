# Kimi K3 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.91 | quality: 8.0
- latency_total: 24.376s | tokens_per_second: 51.6
- input_tokens: 396 | output_tokens: 1257

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
  "dashboard": "KPIs Marzo 2026",
  "periodo": "Enero - Marzo 2026",
  "datos_extraidos": {
    "MRR": {
      "enero": 45200,
      "febrero": 48700,
      "marzo": 52100,
      "unidad": "USD",
      "variacion_mom": "+7.0%"
    },
    "Churn_Rate": {
      "enero": 4.2,
      "febrero": 3.8,
      "marzo": 3.1,
      "unidad": "%",
      "variacion_mom": "-0.7pp"
    },
    "NPS": {
      "enero": 42,
      "febrero": 45,
      "marzo": 51,
      "unidad": "puntos",
      "variacion_mom": "+6"
    },
    "CAC": {
      "enero": 234,
      "febrero": 198,
      "marzo": 187,
      "unidad": "USD",
      "variacion_mom": "-11"
    },
    "LTV": {
      "enero": 1890,
      "febrero": 2010,
      "marzo": 2340,
      "unidad": "USD",
      "variacion_mom": "+330"
    },
    "Active_Users": {
      "enero": 1234,
      "febrero": 1456,
      "marzo": 1678,
      "unidad": "usuarios",
      "variacion_mom": "+15.3%"
    },
    "Support_Tickets": {
      "enero": 89,
      "febrero": 76,
      "marzo": 63,
      "unidad": "tickets",
      "variacion_mom": "-17.1%"
    },
    "Avg_Response_Hours": {
      "enero": 4.2,
      "febrero": 3.1,
      "marzo": 2.4,
      "unidad": "horas",
      "variacion_mom": "-0.7"
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "enero": {
        "calculo": "1890 / 234",
        "ratio": 8.08,
        "interpretacion": "Saludable (>3:1)"
      },
      "febrero": {
        "calculo": "2010 / 198",
        "ratio": 10.15,
        "interpretacion": "Muy saludable"
      },
      "marzo": {
        "calculo": "2340 / 187",
        "ratio": 12.51,
        "interpretacion": "Excelente"
      },
      "tendencia": "Mejora continua - eficiencia de adquisición creciente"
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_porcentual": "+16.4%",
      "calculo": "(2340 - 2010) / 2010 * 100",
      "valor_anterior": 2010,
      "valor_actual": 2340,
      "nota": "Aunque Active Users creció +15.3%, LTV tuvo mayor impacto porcentual"
    },
    "proyeccion_abril_2026": {
      "metodologia": "Extrapolación lineal basada en tendencia Feb-Mar",
      "MRR": {
        "proyeccion": 55800,
        "calculo": "52100 + (52100 - 48700)",
        "confianza": "Alta"
      },
      "Churn_Rate": {
        "proyeccion": 2.4,
        "calculo": "3.1 - (3.8 - 3.1)",
        "confianza": "Media-Alta"
      },
      "NPS": {
        "proyeccion": 57,
        "calculo": "51 + (51 - 45)",
        "confianza": "Media"
      },
      "CAC": {
        "proyeccion": 176,
        "calculo": "187 - (198 - 187)",
        "confianza": "Alta"
      },
      "LTV": {
        "proyeccion": 2670,
        "calculo": "2340 + (2340 - 2010)",
        "confianza": "Alta"
      },
      "Active_Users": {
        "proyeccion": 1900,
        "calculo": "1678 + (1678 - 1456)",
        "confianza": "Media-Alta"
      },
      "Support_Tickets": {
        "proyeccion": 50,
        "calculo": "63 - (76 - 63)",
        "confianza": "Media"
      },
      "Avg_Response_Hours": {
        "proyeccion": 1.7,
        "calculo": "2.4 - (3.1 - 2.4)",
        "confianza": "Media-Alta"
      }
    }
  },
  "resumen_ejecutivo": {
    "tendencia_general": "Positiva",
    "metricas_mejorando": 8,
    "metricas_empeorando": 0,
    "eficiencia_adquisicion": "LTV/CAC ratio mejoró 54.8% desde Enero",
    "alertas": "Ninguna - todas las métricas en dirección favorable"
  }
}
```