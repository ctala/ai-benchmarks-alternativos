# MiMo-V2-Pro — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 6.23 | quality: 6.36
- latency_total: 32.625s | tokens_per_second: 62.8
- input_tokens: 394 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

Aquí tienes la query SQL que cumple con todos los requisitos:

```sql
WITH customer_stats AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
top_categories AS (
    SELECT 
        cs.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW