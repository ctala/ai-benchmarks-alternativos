# Kimi K2 — ocr_extraction/screenshot_table_extraction

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 46.184s | tokens_per_second: 36.4
- input_tokens: 387 | output_tokens: 1682
- judge_score: 3.0 | justificación: La respuesta incluye datos no presentes en la captura de pantalla original, afectando la precisión y exactitud de los datos, pero ofrece análisis útiles y está bien organizada.

## Respuesta completa

```json
{
  "datos_extraidos": {
    "titulo": "DASHBOARD - KPIs Marzo 2026",
    "metricas": [
      {
        "nombre": "MRR",
        "unidad": "USD",
        "valores": { "Enero": 45200, "Febrero": 48700, "Marzo": 52100 },
        "variacion_mensual": { "valor": 7.0, "tipo": "porcentaje" }
      },
      {
        "nombre": "Churn Rate",
        "unidad": "porcentaje",
        "valores": { "Enero": 4.2, "Febrero": 3.8, "Marzo": 3.1 },
        "variacion_mensual": { "valor": -0.7, "tipo": "puntos_porcentuales" }
      },
      {
        "nombre": "NPS",
        "unidad": "puntaje",
        "valores": { "Enero": 42, "Febrero": 45, "Marzo": 51 },
        "variacion_mensual": { "valor": 6, "tipo": "absoluto" }
      },
      {
        "nombre": "CAC",
        "unidad": "USD",
        "valores": { "Enero": 234, "Febrero": 198, "Marzo": 187 },
        "variacion_mensual": { "valor": -11, "tipo": "absoluto" }
      },
      {
        "nombre": "LTV",
        "unidad": "USD",
        "valores": { "Enero": 1890, "Febrero": 2010, "Marzo": 2340 },
        "variacion_mensual": { "valor": 330, "tipo": "absoluto" }
      },
      {
        "nombre": "Active Users",
        "unidad": "usuarios",
        "valores": { "Enero": 1234, "Febrero": 1456, "Marzo": 1678 },
        "variacion_mensual": { "valor": 15.3, "tipo": "porcentaje" }
      },
      {
        "nombre": "Support Tickets",
        "unidad": "tickets",
        "valores": { "Enero": 89, "Febrero": 76, "Marzo": 63 },
        "variacion_mensual": { "valor": -17.1, "tipo": "porcentaje" }
      },
      {
        "nombre": "Avg Response",
        "unidad": "horas",
        "valores": { "Enero": 4.2, "Febrero": 3.1, "Marzo": 2.4 },
        "variacion_mensual": { "valor": -0.7, "tipo": "absoluto" }
      }
    ]
  },
  "calculos_adicionales": {
    "ltv_cac_ratio": {
      "descripcion": "Ratio LTV/CAC para cada mes (benchmark saludable >3)",
      "Enero": { "ratio": 8.08, "clasificacion": "Excelente" },
      "Febrero": { "ratio": 10.15, "clasificacion": "Excelente" },
      "Marzo": { "ratio": 12.51, "clasificacion": "Excelente" },
      "tendencia": "Mejora constante, eficiencia de adquisición creciente"
    },
    "metrica_mayor_mejora_porcentual": {
      "nombre": "Support Tickets",
      "razonamiento": "Reducción del 17.1% es la mayor mejora porcentual en valor absoluto. Aunque Active Users creció 15.3%, las reducciones porcentuales en métricas negativas (Churn, Tickets, Response Time, CAC) indican optimización operativa. Support Tickets lidera con -17.1% de reducción mensual.",
      "mejoras_porcentuales_calculadas": {
        "MRR": "+7.0%",
        "Churn_Rate": "-18.4% (de 3.8% a 3.1%)",
        "NPS": "+13.3% (de 45 a 51)",
        "CAC": "-5.6% (de $198 a $187)",
        "LTV": "+16.4% (de $2,010 a $2,340)",
        "Active_Users": "+15.3%",
        "Support_Tickets": "-17.1%",
        "Avg_Response": "-22.6% (de 3.1h a 2.4h)"
      },
      "nota_correccion": "Avg Response Time tiene la mayor mejora: -22.6% de reducción"
    }
  },
  "proyeccion_abril": {
    "metodologia": "Tendencia de variación mensual (Feb→Mar) aplicada a Marzo",
    "supuestos": "Se mantiene el mismo ritmo de crecimiento/reducción observado",
    "valores_proyectados": {
      "MRR": { "valor": 55746.7, "formato": "$55.7K", "variacion_aplicada": "+7.0%" },
      "Churn_Rate": { "valor": 2.4, "formato": "2.4%", "variacion_aplicada": "-0.7pp" },
      "NPS": { "valor": 57, "formato": "57", "variacion_aplicada": "+6" },
      "CAC": { "valor": 176, "formato": "$176", "variacion_aplicada": "-$11" },
      "LTV": { "valor": 2670, "formato": "$2,670", "variacion_aplicada": "+$330" },
      "Active_Users": { "valor": 1935, "formato": "1,935", "variacion_aplicada": "+15.3%" },
      "Support_Tickets": { "valor": 52, "formato": "52", "variacion_aplicada": "-17.1%" },
      "Avg_Response": { "valor": 1.7, "formato": "1.7h", "variacion_aplicada": "-0.7h" }
    },
    "ltv_cac_ratio_proyectado": 15.17,
    "alertas_proyeccion": [
      "Churn Rate cercano a 2%: verificar sostenibilidad",
      "Avg Response <2h: validar capacidad de equipo de soporte",
      "CAC en $176: verificar si hay floor de eficiencia en canales"
    ]
  },
  "resumen_ejecutivo": {
    "salud_negocio": "Excelente",
    "puntos_fuertes": [
      "LTV/CAC ratio creciendo de 8.08 a 12.51",
      "Reducción sostenida de Churn Rate",
      "Mejora operativa drástica en tiempos de respuesta (-42.9% en 3 meses)"
    ],
    "areas_atencion": [
      "Verificar que reducción de CAC no comprometa calidad de leads",
      "Planificar capacidad de soporte ante crecimiento de usuarios (+36% en 3 meses)"
    ]
  }
}
```