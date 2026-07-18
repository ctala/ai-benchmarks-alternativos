# Kimi K3 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.43 | quality: 8.0
- latency_total: 135.285s | tokens_per_second: 47.3
- input_tokens: 463 | output_tokens: 6403
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí está el análisis completo en JSON:

```json
{
  "dashboard": "KPIs Marzo 2026",
  "tendencia_general": "Positiva en todas las metricas",
  "datos_extraidos": {
    "MRR":              {"unidad": "USD_miles", "enero": 45.2, "febrero": 48.7, "marzo": 52.1, "var_mom": "+7.0%"},
    "Churn_Rate":       {"unidad": "%",         "enero": 4.2,  "febrero": 3.8,  "marzo": 3.1,  "var_mom": "-0.7pp"},
    "NPS":              {"unidad": "puntos",    "enero": 42,   "febrero": 45,   "marzo": 51,   "var_mom": "+6"},
    "CAC":              {"unidad": "USD",       "enero": 234,  "febrero": 198,  "marzo": 187,  "var_mom": "-11"},
    "LTV":              {"unidad": "USD",       "enero": 1890, "febrero": 2010, "marzo": 2340, "var_mom": "+330"},
    "Active_Users":     {"unidad": "usuarios",  "enero": 1234, "febrero": 1456, "marzo": 1678, "var_mom": "+15.3%"},
    "Support_Tickets":  {"unidad": "tickets",   "enero": 89,   "febrero": 76,   "marzo": 63,   "var_mom": "-17.1%"},
    "Avg_Response_h":   {"unidad": "horas",     "enero": 4.2,  "febrero": 3.1,  "marzo": 2.4,  "var_mom": "-0.7"}
  },
  "1_ltv_cac_ratio": {
    "formula": "LTV / CAC",
    "enero": 8.08,
    "febrero": 10.15,
    "marzo": 12.51,
    "tendencia": "creciente (+54.9% en el trimestre)",
    "interpretacion": "Excelente salud del negocio: el benchmark SaaS considera saludable un ratio >3. En marzo, cada $1 invertido en adquisicion genera ~$12.5 de valor de vida del cliente."
  },
  "2_mayor_mejora_porcentual": {
    "metrica_ganadora": "Avg_Response_h",
    "mejora_feb_mar": "22.6%",
    "detalle": "De 3.1h a 2.4h. Para esta metrica una reduccion constituye mejora.",
    "ranking_completo_mejora_pct_feb_mar": [
      {"metrica": "Avg_Response_h",  "mejora_pct": 22.6, "tipo": "reduccion favorable"},
      {"metrica": "Churn_Rate",      "mejora_pct": 18.4, "tipo": "reduccion favorable"},
      {"metrica": "Support_Tickets", "mejora_pct": 17.1, "tipo": "reduccion favorable"},
      {"metrica": "LTV",             "mejora_pct": 16.4, "tipo": "incremento favorable"},
      {"metrica": "Active_Users",    "mejora_pct": 15.2, "tipo": "incremento favorable"},
      {"metrica": "NPS",             "mejora_pct": 13.3, "tipo": "incremento favorable"},
      {"metrica": "MRR",             "mejora_pct": 7.0,  "tipo": "incremento favorable"},
      {"metrica": "CAC",             "mejora_pct": 5.6,  "tipo": "reduccion favorable"}
    ]
  },
  "3_proyeccion_abril_2026": {
    "metodologia": "Extrapolacion de la Var M/M reportada (Feb->Mar) sobre Marzo: porcentual donde el dashboard expresa % y absoluta donde expresa pp/unidades.",
    "valores_proyectados": {
      "MRR":             {"valor": 55.7, "unidad": "USD_miles", "calculo": "52.1 x 1.07"},
      "Churn_Rate":      {"valor": 2.4,  "unidad": "%",         "calculo": "3.1 - 0.7pp"},
      "NPS":             {"valor": 57,   "unidad": "puntos",    "calculo": "51 + 6"},
      "CAC":             {"valor": 176,  "unidad": "USD",       "calculo": "187 - 11"},
      "LTV":             {"valor": 2670, "unidad": "USD",       "calculo": "2340 + 330"},
      "Active_Users":    {"valor": 1935, "unidad": "usuarios",  "calculo": "1678 x 1.153"},
      "Support_Tickets": {"valor": 52,   "unidad": "tickets",   "calculo": "63 x 0.829"},
      "Avg_Response_h":  {"valor": 1.7,  "unidad": "horas",     "calculo": "2.4 - 0.7"}
    },
    "ltv_cac_ratio_proyectado_abril": 15.17,
    "advertencias": [
      "Extrapolacion lineal simple: no considera estacionalidad, saturacion de mercado ni efectos compuestos.",
      "Churn y Support Tickets tienen piso natural en 0; la tasa de mejora tendera a desacelerarse.",
      "NPS tiene techo de 100 puntos.",
      "A mayor horizonte de proyeccion, mayor incertidumbre."
    ]
  }
}
```

**Notas clave del análisis:**
- El ratio **LTV/CAC pasó de 8.1 a 12.5** en el trimestre, impulsado simultáneamente por la suba del LTV (+$330) y la baja del CAC (-$11) — una combinación muy favorable.
- La mayor mejora porcentual fue el **tiempo de respuesta de soporte (-22.6%)**, lo cual es consistente con la caída de tickets (-17.1%): menos carga permite responder más rápido.
- Si querés la proyección de abril con método compuesto (aplicando % a todas las métricas) o a 3 meses, avísame y la genero.