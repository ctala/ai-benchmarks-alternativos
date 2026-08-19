# Seed 2.0 Code — ocr_extraction/screenshot_table_extraction

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 35.535s | tokens_per_second: 57.6
- input_tokens: 462 | output_tokens: 2048

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


El usuario quiere una respuesta en JSON estructurado, primero voy a organizar todos los datos que me dio, luego agregar los cálculos que pide.

Primero, voy a listar los pasos:

1. Extraer los datos originales del dashboard: metadata (nombre, mes de referencia), luego las métricas con sus valores por mes y variación mes a mes.

2. Calcular LTV/CAC por cada mes:
   - Enero: LTV Enero ($1890) / CAC Enero ($234) = aproximadamente 8.08 (voy a calcular bien: 1890 / 234 = 8.0769... así que 8.08)
   - Febrero: 2010 / 198 = 10.1515... → 10.15
   - Marzo: 2340 / 187 = 12.5133... → 12.51

3. Identificar la métrica con mayor mejora porcentual. Primero, tengo que convertir todas las variaciones a porcentaje equivalente para comparar, teniendo en cuenta que algunas son puntos porcentuales, dólares, etc. Wait, el usuario dijo "mayor mejora porcentual". Primero, las métricas que tienen variación porcentual explícita, o calcular la variación porcentual para todas?

Wait, veamos las variaciones que trae el dashboard:
- MRR: +7.0%
- Churn: -0.7pp (pero es mejora porque bajar el churn es bueno)
- NPS: +6 (puntos, no porcentaje)
- CAC: -$11 (mejora por que baja)
- LTV: +$330
- Active Users: +15.3%
- Support Tickets: -17.1% (mejora porque bajan)
- Avg Response: -0.7hs (mejora)

Ahora, para calcular la mejora porcentual de cada una, para poder comparar igualitariamente, porque no es lo mismo +6 puntos de NPS que +15.3% de usuarios activos. La mejora porcentual se calcula como (Valor Marzo - Valor Febrero) / Valor Febrero * 100, teniendo en cuenta la dirección de mejora:

Para métricas que QUEREMOS que SUBAN (positivas): MRR, NPS, LTV, Active Users → mejora porcentual = ((Mar - Feb)/Feb)*100

Para métricas que QUEREMOS que BAJEN (negativas): Churn Rate, CAC, Support Tickets, Avg Response → mejora porcentual = ((Feb - Mar)/Feb)*100 (así el valor es positivo si mejora)

Vamos a calcular cada una:

1. MRR: (52.1K - 48.7K)/48.7K *100 = (3.4/48.7)*100 ≈ 7.0% (coincide con la var dada)
2. Churn Rate: (3.8% - 3.1%)/3.8% *100 = (0.7/3.8)*100 ≈ 18.42% (mejora, porque baja)
3. NPS: (51-45)/45 *100 = 6/45*100 = 13.33%
4. CAC: (198 - 187)/198 *100 = 11/198*100 ≈ 5.56%
5. LTV: (2340 - 2010)/2010 *100 = 330/2010*100 ≈ 16.42%
6. Active Users: (1678 - 1456)/1456 *100 = 222/1456*100 ≈ 15.25% (coincide con el +15.3% dado, redondeado)
7. Support Tickets: (76 - 63)/76 *100 =13/76*100≈17.11% (coincide con el -17.1% dado, que es la var, la mejora es ~17.11%)
8. Avg Response (h): (3.1 - 2.4)/3.1 *100 =0.7/3.1*100≈22.58%

Oh! La mayor mejora porcentual es Avg Response Time (Tiempo Medio de Respuesta) con ~22.58% de mejora. Wait, voy a confirmar: sí, 0.7 hs menos sobre 3.1 hs originales es (3.1-2.4)/3.1 = 0.2258 → 22.58%, que es mayor que churn (18.42), support tickets (17.11), etc. Esa es la que tiene mayor mejora porcentual.

4. Proyección de Abril, manteniendo la tendencia. ¿Cuál es la tendencia? La tendencia es la variación mes a mes, pero ¿usamos la variación porcentual o la variación absoluta? Wait, el dashboard dice "Tendencia general: ↑ Positiva en todas las metricas" y las variaciones son Var M/M. Para proyectar, es mejor usar la variación porcentual mensual (Var M/M) cuando sea aplicable, o la variación absoluta? Wait, veamos las Var M/M que hay:

Algunas son porcentuales (MRR: +7.0%, Active Users: +15.3%, Support Tickets: -17.1%), otras son puntos porcentuales (Churn: -0.7pp), otras son unidades (NPS: +6), otras son dólares (CAC: -$11, LTV: +$330), otras son horas (Avg Response: -0.7h).

Para proyectar Abril, vamos a aplicar LA MISMA VARIACIÓN M/M QUE TUVO MARZO RESPECTO A FEBRERO, porque la tendencia se mantiene. Eso es lo más coherente, ya que la Var M/M es la variación de Mar vs Feb, así que Abr tendrá la misma variación respecto a Mar.

Vamos a calcular cada proyección:

1. MRR: Marzo = $52.1K, Var M/M = +7.0% → 52.1 * 1.07 = 55.747 → $55.7K (o $55.75K, pero vamos a redondear como los originales, que son 1 decimal en K)
2. Churn Rate: Marzo = 3.1%, Var M/M = -0.7pp → 3.1 - 0.7 = 2.4% (porque es puntos porcentuales, no porcentaje de variación)
3. NPS: Marzo = 51, Var M/M = +6 → 51 +6 = 57
4. CAC: Marzo = $187, Var M/M = -$11 → 187 -11 = $176
5. LTV: Marzo = $2340, Var M/M = +$330 → 2340 + 330 = $2670
6. Active Users: Marzo = 1678, Var M/M = +15.3% → 1678 * 1.153 ≈ 1934.734 → 1935 (redondeado a entero, como los originales: 1234, 1456, 1678 son enteros)
7. Support Tickets: Marzo = 63, Var M/M = -17.1% → 63 * (1 - 0.171) = 63 * 0.829 ≈ 52.227 → 52 (enteros, originales son 89,76,63)
8. Avg Response (h): Marzo = 2.4, Var M/M = -0.7 → 2.4 - 0.7 = 1.7 hs (mismo decimal que originales: 4.2, 3.1, 2.4 son 1 decimal)

Ahora, organizar todo en JSON estructurado. ¿Qué secciones debería tener?

- metadata: información del dashboard (nombre, mes_referencia, tendencia_general)
- metricas_originales