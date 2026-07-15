# Claude Fable 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 26.79s | tokens_per_second: 58.6
- input_tokens: 295 | output_tokens: 1570
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, abordando errores clave y ofreciendo estrategias prácticas.

## Respuesta completa

No le des. El cálculo tiene dos errores que, combinados, convierten un negocio "escalable" en uno que apenas empata. Vamos por partes:

## Error 1: La vida útil del cliente no son 24 meses

Con un churn mensual del 8%, la vida promedio de un cliente es:

**1 / 0,08 = 12,5 meses**

No 24. ¿De dónde salieron los 2 años? Probablemente de intuición o de tus primeros clientes (que suelen ser los más leales y no representan a los que traerá la publicidad fría). Con 8% de churn, la mitad de tu cohorte se fue antes del mes 9.

## Error 2: El LTV se calcula sobre margen bruto, no sobre ingresos

Los $35 no son tuyos; $10,50 se van a infraestructura y procesamiento. El LTV relevante para comparar contra CAC es:

**LTV = $35 × 12,5 meses × 70% = $306,25**

## El número real

| Métrica | Tu cálculo | Realidad |
|---|---|---|
| Vida útil | 24 meses | 12,5 meses |
| LTV | $840 | $306 |
| LTV/CAC | 2,9 | **1,06** |

Un LTV/CAC de 1,06 significa que por cada $290 que inviertes, recuperas $306 en margen bruto... a lo largo de un año. Eso es antes de tu salario, soporte, herramientas, impuestos. En términos prácticos, estás comprando clientes a precio de costo.

## El payback lo confirma

Margen bruto mensual por cliente: $35 × 70% = $24,50.
Payback del CAC: $290 / $24,50 = **11,8 meses**.

Tu cliente promedio vive 12,5 meses. Recuperas la inversión 3 semanas antes de que el cliente típico se vaya. Con $10.000 comprarías ~34 clientes que te devolverían ~$10.400 de margen bruto en un año. Efectivamente cero retorno, y negativo si valoras el dinero en el tiempo.

## Qué haría yo antes de escalar

1. **Atacar el churn primero.** Es tu palanca más potente. Si bajas de 8% a 4%, la vida útil sube a 25 meses y el LTV a ~$612 → ratio de 2,1. A 3% ya estás en 2,8. Averigua *cuándo* y *por qué* se van (¿churn en mes 1-2? problema de onboarding; ¿churn tardío? problema de valor).

2. **Precio.** ¿$35 está testeado? Un aumento a $45 con el mismo churn te lleva el LTV a ~$394 y el ratio a 1,4. Combinado con menos churn, ahí sí hay negocio.

3. **CAC.** $290 para un producto de $35/mes es alto. Antes de escalar, testea si $1.000–2.000 en creativos/canales distintos bajan ese número.

4. **Cuando el ratio real (con margen y churn medidos) supere 3 y el payback baje de ~6-8 meses**, entonces sí: mete gasolina.

La buena noticia: no estás perdiendo dinero por cliente, así que tienes margen para experimentar. Pero escalar con estos números es escalar el punto de equilibrio, no las ganancias.