# Kimi K2.6 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.09 | quality: 8.0
- latency_total: 25.914s | tokens_per_second: 66.2
- input_tokens: 387 | output_tokens: 1716

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
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "periodos": ["Enero", "Febrero", "Marzo"],
    "metricas": {
      "MRR": {
        "valores": [45200, 48700, 52100],
        "unidad": "USD",
        "formato": "moneda",
        "variacion_mes_a_mes": "+7.0%"
      },
      "Churn_Rate": {
        "valores": [4.2, 3.8, 3.1],
        "unidad": "porcentaje",
        "formato": "porcentaje",
        "variacion_mes_a_mes": "-0.7pp"
      },
      "NPS": {
        "valores": [42, 45, 51],
        "unidad": "puntos",
        "formato": "entero",
        "variacion_mes_a_mes": "+6"
      },
      "CAC": {
        "valores": [234, 198, 187],
        "unidad": "USD",
        "formato": "moneda",
        "variacion_mes_a_mes": "-$11"
      },
      "LTV": {
        "valores": [1890, 2010, 2340],
        "unidad": "USD",
        "formato": "moneda",
        "variacion_mes_a_mes": "+$330"
      },
      "Active_Users": {
        "valores": [1234, 1456, 1678],
        "unidad": "usuarios",
        "formato": "entero",
        "variacion_mes_a_mes": "+15.3%"
      },
      "Support_Tickets": {
        "valores": [89, 76, 63],
        "unidad": "tickets",
        "formato": "entero",
        "variacion_mes_a_mes": "-17.1%"
      },
      "Avg_Response": {
        "valores": [4.2, 3.1, 2.4],
        "unidad": "horas",
        "formato": "decimal",
        "variacion_mes_a_mes": "-0.7"
      }
    }
  },
  "analisis": {
    "ltv_cac_ratio": {
      "descripcion": "Relación entre Lifetime Value y Costo de Adquisición de Clientes",
      "valores": {
        "Enero": 8.08,
        "Febrero": 10.15,
        "Marzo": 12.51
      },
      "interpretacion": "Cada dólar invertido en adquisición genera $12.51 en valor a largo plazo (Marzo). Ratio saludable (>3x) y en mejora constante."
    },
    "metrica_mayor_mejora_porcentual": {
      "metrica": "LTV",
      "mejora_porcentual": "16.42%",
      "calculo": "(2340 - 2010) / 2010 * 100 = 16.42%",
      "detalle_mensual": {
        "Enero_a_Febrero": "6.35%",
        "Febrero_a_Marzo": "16.42%"
      },
      "nota": "Considerando métricas donde el aumento es positivo. Si se consideran reducciones favorables: Support Tickets tuvo -17.1% en el último mes"
    },
    "ranking_mejoras_periodo_Feb_Mar": [
      {"metrica": "LTV", "mejora": "+16.42%", "direccion": "positiva"},
      {"metrica": "Support_Tickets", "mejora": "-17.1% (reducción favorable)", "direccion": "positiva_reduccion"},
      {"metrica": "Active_Users", "mejora": "+15.2%", "direccion": "positiva"},
      {"metrica": "NPS", "mejora": "+13.3%", "direccion": "positiva"},
      {"metrica": "MRR", "mejora": "+7.0%", "direccion": "positiva"}
    ]
  },
  "proyeccion_abril": {
    "metodologia": "Aplicar la tasa de crecimiento/reducción del último mes (Feb→Mar) a los valores de Marzo",
    "supuesto": "Se mantiene la tendencia más reciente (variación mes a mes de Marzo)",
    "valores_proyectados": {
      "MRR": {
        "valor_abril": 55747,
        "formula": "52100 * 1.07",
        "nota": "Crecimiento del 7.0% mensual"
      },
      "Churn_Rate": {
        "valor_abril": 2.4,
        "formula": "3.1 - 0.7",
        "unidad": "%",
        "nota": "Reducción de 0.7 puntos porcentuales"
      },
      "NPS": {
        "valor_abril": 57,
        "formula": "51 + 6",
        "nota": "Incremento de 6 puntos"
      },
      "CAC": {
        "valor_abril": 176,
        "formula": "187 - 11",
        "nota": "Reducción de $11"
      },
      "LTV": {
        "valor_abril": 2670,
        "formula": "2340 + 330",
        "nota": "Incremento de $330"
      },
      "Active_Users": {
        "valor_abril": 1935,
        "formula": "1678 * 1.153",
        "nota": "Crecimiento del 15.3%"
      },
      "Support_Tickets": {
        "valor_abril": 52,
        "formula": "63 * 0.829",
        "nota": "Reducción del 17.1%"
      },
      "Avg_Response": {
        "valor_abril": 1.7,
        "formula": "2.4 - 0.7",
        "nota": "Reducción de 0.7 horas"
      }
    },
    "ltv_cac_ratio_proyectado_abril": 15.17,
    "alertas_proyeccion": [
      "Churn Rate proyectado (2.4%) podría ser optimista si se acerca a límites naturales del mercado",
      "CAC en $176 requiere verificar sostenibilidad de canales de adquisición",
      "Avg Response de 1.7h podría requerir inversión en infraestructura de soporte"
    ]
  },
  "resumen_ejecutivo": {
    "salud_negocio": "Excelente",
    "indicadores_clave": {
      "ltv_cac_ratio_tendencia": "Creciente (8.08 → 10.15 → 12.51)",
      "payback_period_estimado": "Mejorando significativamente",
      "eficiencia_soporte": "Mejorando (menos tickets, menor tiempo de respuesta)",
      "retencion": "Mejorando (churn decreciente)"
    },
    "recomendacion": "Acelerar inversión en adquisición mientras CAC se mantiene controlado y LTV crece; el ratio LTV/CAC de 12.5x permite mayor agresividad en marketing"
  }
}
```