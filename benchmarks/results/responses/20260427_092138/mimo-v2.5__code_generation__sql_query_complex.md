# MiMo V2.5 (Xiaomi) — code_generation/sql_query_complex

- model_id: `mimo-v2.5`
- success: True  | final: 7.11 | quality: 7.16
- latency_total: 21.32s | tokens_per_second: 96.1
- input_tokens: 392 | output_tokens: 2048
- judge_score: 3.4 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH customer_metrics AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_preferences AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS