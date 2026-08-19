# Gemini 3.5 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 6.69 | quality: 7.96
- latency_total: 11.201s | tokens_per_second: 182.5
- input_tokens: 160 | output_tokens: 2044
- judge_score: 4.0 | justificación: 

## Respuesta completa

Esta consulta requiere calcular métricas agregadas (órdenes, ingresos, promedio) y, al mismo tiempo, identificar de forma dinámica cuál es la categoría más comprada por cada cliente. 

Para resolverlo de forma limpia y eficiente, utilizaremos **CTEs (Common Table Expressions)** y una **función de ventana (`ROW_NUMBER`)**.

Aquí tienes la query en SQL estándar (compatible con PostgreSQL, MySQL 8.0+, SQL Server y Oracle):

```sql
WITH customer_metrics AS (
    -- 1. Calculamos las métricas principales de los clientes en los últimos 6 meses
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 month'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_ranking AS (
    -- 2. Determinamos la cantidad comprada por categoría para cada cliente
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER