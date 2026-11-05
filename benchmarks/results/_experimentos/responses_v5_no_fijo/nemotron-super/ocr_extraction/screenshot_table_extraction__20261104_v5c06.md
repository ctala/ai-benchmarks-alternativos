# Nemotron 3 Super — ocr_extraction/screenshot_table_extraction

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 16.246s | tokens_per_second: 97.7
- input_tokens: 435 | output_tokens: 1587

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

{
  "datos_metricas": {
    "MRR": {
      "Enero": "$45.2K",
      "Feb": "$48.7K",
      "Marzo": "$52.1K",
      "Var_M_M": "+7.0%"
    },
    "Churn_Rate": {
      "Enero": "4.2%",
      "Feb": "3.8%",
      "Marzo": "3.1%",
      "Var_M_M": "-0.7pp"
    },
    "NPS": {
      "Enero": "42",
      "Feb": "45",
      "Marzo": "51",
      "Var_M_M": "+6"
    },
    "CAC": {
      "Enero": "$234",
      "Feb": "$198",
      "Marzo": "$187",
      "Var_M_M": "-$11"
    },
    "LTV": {
      "Enero": "$1,890",
      "Feb": "$2,010",
      "Marzo": "$2,340",
      "Var_M_M": "+$330"
    },
    "Active_Users": {
      "Enero": "1,234",
      "Feb": "1,456",
      "Marzo": "1,678",
      "Var_M_M": "+15.3%"
    },
    "Support_Tickets": {
      "Enero": "89",
      "Feb": "76",
      "Marzo": "63",
      "Var_M_M": "-17.1%"
    },
    "Avg_Response_h": {
      "Enero": "4.2",
      "Feb": "3.1",
      "Marzo": "2.4",
      "Var_M_M": "-0.7"
    }
  },
  "LTV_CAC_ratio": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "metrica_mayor_mejora_porcentual": {
    "metrica": "Active Users",
    "valor_actual": "1,678",
    "mejora_porcentual": "+15.3%",
    "nota": "Aunque Support Tickets tiene una mejora del -17.1% (reducción), se interpreta como mejora positiva, pero la pregunta pide 'mejora porcentual' en sentido absoluto de crecimiento positivo. Active Users es la única con crecimiento positivo explícito y el más alto entre las métricas que mejoran en valor absoluto (MRR, NPS, LTV, Active Users). Si se considera reducción como mejora, entonces Support Tickets (-17.1%) sería la mayor mejora. Sin embargo, en contextos de KPIs, 'mejora' suele referirse a dirección deseada: para Support Tickets, menos es mejor, por lo que -17.1% es una mejora del 17.1% en magnitud. Por lo tanto, se toma el valor absoluto de la mejora: 17.1% > 15.3%. Revisando: la tendencia general es '↑ Positiva en todas las métricas', lo que implica que incluso las métricas que disminuyen (Churn, CAC, Support Tickets, Avg Response) están mejorando porque van en la dirección deseada. Por lo tanto, se debe comparar la magnitud del cambio en la dirección de mejora. Entonces: Support Tickets: 17.1% de mejora (reducción), Active Users: 15.3% de mejora (aumento). Por lo tanto, Support Tickets tiene la mayor mejora porcentual."
    ,
    "correccion": "Tras reevaluar la instrucción 'Tendencia general: ↑ Positiva en todas las métricas', se interpreta que todas las variaciones mostradas representan mejoras en la dirección deseada. Por lo tanto, se compara el valor absoluto del cambio porcentual (ignorando el signo, ya que todos son mejoras). Las mejoras porcentuales en magnitud son: MRR: 7.0%, Churn Rate: 0.7pp (no porcentual, se ignora para comparación directa), NPS: +6 puntos (no porcentual), CAC: -$11 (absoluto), LTV: +$330 (absoluto), Active Users: +15.3%, Support Tickets: 17.1%, Avg Response: -0.7h (absoluto). Solo MRR y Active Users tienen cambios porcentuales explícitos. Support Tickets tiene -17.1%, lo que equivale a una mejora del 17.1% en magnitud. Por lo tanto, Support Tickets tiene la mayor mejora porcentual en magnitud: 17.1%."
  },
  "proyeccion_Abril": {
    "MRR": "$55.7K",
    "Churn_Rate": "2.5%",
    "NPS": "57",
    "CAC": "$176",
    "LTV": "$2,670",
    "Active_Users": "1,935",
    "Support_Tickets": "52",
    "Avg_Response_h": "1.7"
  },
  "notas": {
    "LTV_CAC_ratio_calculo": "LTV dividido por CAC, valores convertidos a números (ej: $1,890 → 1890, $234 → 234). Enero: 1890/234 ≈ 8.08; Feb: 2010/198 ≈ 10.15; Marzo: 2340/187 ≈ 12.51",
    "metrica_mayor_mejora_porcentual_explicacion": "Se consideró la magnitud del cambio en la dirección de mejora deseada. Support Tickets mostró una reducción del 17.1%, lo que representa una mejora del 17.1% en magnitud, mayor que el 15.3% de Active Users. Otras métricas no tenían cambios porcentuales explícitos (usaban puntos porcentuales, dólares o horas), por lo que no se compararon directamente en porcentaje.",
    "proyeccion_metodologia": "Se aplicó la tasa de cambio mensual relativa (Var M/M) observada en febrero a marzo para proyectar abril. Para métricas con cambio porcentual: se aplicó el mismo % al valor de marzo. Para métricas con cambio absoluto (como CAC, LTV, Avg Response): se asumió que el cambio absoluto mensual se mantiene constante (ej: CAC disminuye $11/mes). Para Support Tickets: se aplicó el mismo % de reducción (-17.1%) al valor de marzo. Para NPS y Churn Rate (que usan puntos porcentuales o puntos): se asumió que el cambio absoluto observado (+6 para NSS, -0.7pp para Churn) se mantiene constante."
  }
}