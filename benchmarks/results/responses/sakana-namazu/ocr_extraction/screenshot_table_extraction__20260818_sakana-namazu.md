# Sakana Namazu — ocr_extraction/screenshot_table_extraction

- model_id: `sakana/sakana-namazu`
- success: True  | final: 4.4 | quality: 4.0
- latency_total: 10.648s | tokens_per_second: 192.3
- input_tokens: 461 | output_tokens: 2048

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

El usuario quiere que extraiga datos de una tabla de KPIs en formato JSON, calcule LTV/CAC, identifique la métrica con mayor mejora porcentual, y proyecte valores para abril. Todo debe estar en JSON estructurado y debo responder en español (ya que el usuario escribió en español).

Primero, extraigamos los datos:
- MRR: Enero $45.2K, Feb $48.7K, Marzo $52.1K, Var +7.0%
- Churn Rate: Enero 4.2%, Feb 3.8%, Marzo 3.1%, Var -0.7pp
- NPS: Enero 42, Feb 45, Marzo 51, Var +6
- CAC: Enero $234, Feb $198, Marzo $187, Var -$11
- LTV: Enero $1,890, Feb $2,010, Marzo $2,340, Var +$330
- Active Users: Enero 1,234, Feb 1,456, Marzo 1,678, Var +15.3%
- Support Tickets: Enero 89, Feb 76, Marzo 63, Var -17.1%
- Avg Response (h): Enero 4.2, Feb 3.1, Marzo 2.4, Var -0.7

Ahora calculos:
1. LTV/CAC ratio para cada mes:
   - Enero: 1890 / 234 = 8.0769... ≈ 8.08
   - Febrero: 2010 / 198 = 10.1515... ≈ 10.15
   - Marzo: 2340 / 187 = 12.5133... ≈ 12.51

2. Métrica con mayor mejora porcentual:
   Necesito calcular la mejora porcentual de febrero a marzo para cada métrica (ya que la var M/M es la variación de marzo vs febrero).
   
   - MRR: (52.1 - 48.7) / 48.7 = 3.4 / 48.7 = 0.0698... = 6.98% ≈ 7.0% (coincide con la tabla)
   - Churn Rate: es una reducción, pero como es porcentaje de porcentaje o pp? La tabla dice -0.7pp (puntos porcentuales). Si hablamos de mejora porcentual relativa: (3.8 - 3.1) / 3.8 = 0.7 / 3.8 = 18.42% de reducción. O podría interpretarse como cambio porcentual: (3.1 - 3.8) / 3.8 = -18.42%. La "mejora" es 18.42%.
   - NPS: (51 - 45) / 45 = 6/45 = 13.33%
   - CAC: reducción. (187 - 198) / 198 = -11/198 = -5.56%. Mejora del 5.56%.
   - LTV: (2340 - 2010) / 2010 = 330/2010 = 16.42%
   - Active Users: (1678 - 1456) / 1456 = 222/1456 = 15.24% (coincide aprox con 15.3%)
   - Support Tickets: reducción. (63 - 76) / 76 = -13/76 = -17.11%. Mejora del 17.11%.
   - Avg Response: reducción. (2.4 - 3.1) / 3.1 = -0.7/3.1 = -22.58%. Mejora del 22.58%.

   Entonces la mayor mejora porcentual es Avg Response (tiempo de respuesta) con ~22.58% de reducción. Si consideramos mejora absoluta en términos de porcentaje de cambio, es -22.58%, pero como "mejora" es positiva, 22.58%.
   
   Espera, debo verificar si hay alguna métrica con mayor mejora:
   - Avg Response: 22.58% mejora (reducción)
   - Churn Rate: 18.42% mejora (reducción relativa)
   - Support Tickets: 17.11% mejora (reducción)
   - LTV: 16.42% aumento
   - NPS: 13.33% aumento
   - Active Users: 15.24% aumento
   - MRR: 6.98% aumento
   - CAC: 5.56% mejora (reducción)

   Sí, Avg Response (h) es la ganadora.

3. Proyección de Abril si la tendencia se mantiene:
   Hay varias formas de proyectar: usando el crecimiento porcentual de marzo vs febrero, o usando la diferencia absoluta promedio, o la tasa de cambio. La instrucción dice "si la tendencia se mantiene", lo más lógico es aplicar la misma variación porcentual (o absoluta donde aplique) de marzo respecto a febrero.

   Veamos:
   - MRR: Feb->Mar +7.0%. Abril = 52.1 * 1.07 = 55.747K ≈ $55.7K
   - Churn Rate: Feb->Mar -0.7pp. Abril = 3.1 - 0.7 = 2.4%. Alternativamente podría ser reducción porcentual 18.4%, pero la tabla muestra variación en pp, así que usar la tendencia absoluta de pp es más consistente con la data presentada. Proyecto: 2.4%.
   - NPS: Feb->Mar +6. Abril = 51 + 6 = 57. O si es porcentual sería 51 * (1 + 13.33%) = 57.8, pero como es índice entero, mejor +6 absoluto. O alternativamente +13.33%. Usaré +6 por simplicidad y consistencia con la var M/M mostrada como +6 absoluto.
   - CAC: Feb->Mar -$11. Abril = 187 - 11 = $176.
   - LTV: Feb->Mar +$330. Abril = 2340 + 330 = $2,670. O si es porcentual: 2340 * 1.1642 = 2724. La tabla mueja Var M/M +$330 (absoluto), así que usaré tendencia absoluta.
   - Active Users: Feb->Mar +15.3%. Abril = 1678 * 1.153 = 1934.73 ≈ 1,935.
   - Support Tickets: Feb->Mar -17.1%. Abril = 63 * (1 - 0.171) = 63 * 0.829 = 52.23 ≈ 52.
   - Avg Response: Feb->Mar -0.7h. Abril = 2.4 - 0.7 = 1.7h.

   Pero debo ser cuidadoso. Para consistencia, podría usar el mismo método de variación que la tabla. La tabla muestra:
   - Para monetarias y conteos absolutos en var M/M: algunos son porcentaje (MRR, Active Users, Support Tickets) y otros absolutos (CAC, LTV, NPS, Avg Response, Churn Rate en pp).
   
   Para la proyección, aplicaré la variación mes a mes de forma coherente:
   - Si la var es %, proyecto con ese %.
   - Si la var es absoluta, proyecto con esa diferencia absoluta.
   - Para Churn Rate, como es en pp, proyecto restando 0.7pp.

   Espera, Churn Rate: es una métrica donde aplicar pp tiene sentido. Pero también podría interpretarse como tendencia de reducción relativa. Sin embargo, al mostrar -0.7pp la tabla sugiere que el método esperado es restar 0.7.

   Ahora, para el JSON estructurado. El usuario quiere todo en JSON. Debo crear un JSON válido con:
   - datos_extraidos (array de objetos o objeto con métricas)
   - calculos_ltv_cac (objeto con ratios mensuales)
   - mayor_mejora (objeto con nombre métrica, valor mejora, etc.)
   - proyecciones_abril (objeto con valores proyectados)

   Necesito asegurarme de que el JSON esté bien formado. Usaré números con decimidos apropiados.

   Detalles del JSON:
   ```json
   {
     "datos_extraidos": {
       "meses": ["Enero", "Febrero",