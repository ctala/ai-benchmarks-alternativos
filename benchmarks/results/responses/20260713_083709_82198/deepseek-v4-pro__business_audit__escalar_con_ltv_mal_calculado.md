# DeepSeek V4 Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.4 | quality: 7.87
- latency_total: 17.714s | tokens_per_second: 52.7
- input_tokens: 202 | output_tokens: 934

## Respuesta completa

El plan no resiste la aritmética. Tu cálculo de LTV es incorrecto y, al corregirlo, el ratio LTV/CAC está lejos de ser sano.

**El error: asumiste 2 años de vida sin considerar el churn.**  
Con un churn mensual del 8%, la retención media se calcula como `1 / churn = 1 / 0.08 = 12.5 meses`, no 24. Eso reduce drásticamente el valor del cliente.

**Cálculo real del LTV:**  
- Ingreso bruto mensual por cliente: $35 × 70% = **$24.5**.  
- LTV = contribución mensual ÷ churn = $24.5 / 0.08 = **$306.25**.

**Relación LTV/CAC real:**  
$306.25 / $290 = **1.056x**. Prácticamente 1:1.  
Cada dólar que gastas en adquirir un cliente apenas regresa su costo directo, sin margen para otros gastos operativos ni ganancia. Escalar con este CAC destruye valor; el benchmark saludable en SaaS suele ser **≥3x**.

**Conclusión:** no le des a la inversión en publicidad con esta estructura. Meter $10.000 solo traerá ~34 clientes que, en promedio, aportarán $306 cada uno, facturando ~$10.400 marginales… y te comerás toda la utilidad en CAC.

**Antes de escalar pagado, trabajá en:**
- **Bajar el churn:** si llega al 5% mensual, el LTV sube a $490 (1.7x).  
- **Subir precio o margen:** $42/mes con el mismo churn y margen da LTV de ~$367.  
- **Optimizar CAC:** si lográs bajar a $150, el ratio actual de 2x ya empieza a ser aceptable.  

Hasta que no muevas alguna de estas palancas, el crecimiento forzado con ads solo acelera la pérdida de caja.