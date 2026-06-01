# DeepSeek R1 (reasoning) — ocr_extraction/screenshot_table_extraction

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 5.21 | quality: 6.12
- latency_total: 570.613s | tokens_per_second: 11.1
- input_tokens: 387 | output_tokens: 6352
- judge_score: 3.0 | justificación: 

## Respuesta completa

```json
{
  "dashboard_data": {
    "months": ["Enero", "Feb", "Marzo"],
    "metrics": {
      "MRR": [45200, 48700, 52100],
      "Churn Rate": [4.2, 3.8, 3.1],
      "NPS": [42, 45, 51],
      "CAC": [234, 198, 187],
      "LTV": [1890, 2010, 2340],
      "Active Users": [1234, 1456, 1678],
      "Support Tickets": [89, 76, 63],
      "Avg Response (h)": [4.2, 3.1, 2.4]
    }
  },
  "ltv_cac_ratios": {
    "Enero": 8.08,
    "Feb": 10.15,
    "Marzo": 12.51
  },
  "metrica_mayor_mejora": "Avg Response (h)",
  "proyeccion_abril": {
    "MRR": 55700,
    "Churn Rate": 2.4,
    "NPS": 57,
    "CAC": 176,
    "LTV": 2670,
    "Active Users": 1935,
    "Support Tickets": 52,
    "Avg Response (h)": 1.7
  }
}
```

### Explicación:
1. **Extracción de datos**: Los valores se convirtieron a números (eliminando símbolos como `$`, `%`, `K`, y comas). Por ejemplo:
   - `$45.2K` → `45200` (se multiplicó por 1000).
   - `4.2%` → `4.2`.
   - `$1,890` → `1890` (se eliminaron comas y `$`).

2. **Cálculo de LTV/CAC ratio**:
   - **Enero**: `1890 / 234 ≈ 8.08`.
   - **Febrero**: `2010 / 198 ≈ 10.15`.
   - **Marzo**: `2340 / 187 ≈ 12.51`.
   - *Nota*: Se redondeó a dos decimales.

3. **Métrica con mayor mejora porcentual**:
   - Se calculó la mejora porcentual relativa (febrero → marzo) para cada métrica, considerando:
     - *Métricas positivas* (↑ es bueno): `(Marzo - Febrero) / Febrero`.
     - *Métricas negativas* (↓ es bueno): `(Febrero - Marzo) / Febrero`.
   - Resultados:
     - `Avg Response (h)`: `(3.1 - 2.4) / 3.1 ≈ 22.58%` (mayor mejora).
     - Otras: Churn Rate (18.42%), Support Tickets (17.11%), LTV (16.42%), etc.

4. **Proyección de abril**:
   - Se aplicó el mismo cambio observado en marzo (en la unidad original del *Var M/M*):
     - **MRR**: `+7.0%` → `52100 * 1.07 = 55700`.
     - **Churn Rate**: `-0.7 pp` → `3.1 - 0.7 = 2.4`.
     - **NPS**: `+6 puntos` → `51 + 6 = 57`.
     - **CAC**: `-$11` → `187 - 11 = 176`.
     - **LTV**: `+$330` → `2340 + 330 = 2670`.
     - **Active Users**: `+15.3%` → `1678 * 1.153 ≈ 1935`.
     - **Support Tickets**: `-17.1%` → `63 * 0.829 ≈ 52`.
     - **Avg Response (h)**: `-0.7 horas` → `2.4 - 0.7 = 1.7`.