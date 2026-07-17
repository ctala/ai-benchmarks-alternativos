# Mistral Small 4 — code_generation/sql_query_complex

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 8.1 | quality: 7.72
- latency_total: 1.973s | tokens_per_second: 162.2
- input_tokens: 159 | output_tokens: 320
- judge_score: 3.8 | justificación: 

## Respuesta completa

```sql
WITH completed_orders AS (
    SELECT
        o.customer_id,
        o.id AS order_id,
        o.total AS order_total,
        o.created_at,
        oi.category AS top_category
    FROM orders o
    JOIN (
        SELECT
            order_id,
            product_id,
            quantity,
            unit_price,
            p.category
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
    ) oi ON o.order_id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),

customer_stats AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.order_total) AS total_revenue,
        AVG(co.order_total) AS avg_order_value,
        MAX(co.top_category) AS categoria_mas_comprada
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
)

SELECT
    name,
    email,
    country,
    total_orders,
    total_revenue,
    ROUND(avg_order_value, 2) AS avg_order_value,
    categoria_mas_comprada
FROM customer_stats
ORDER BY total_revenue DESC
LIMIT 10;
```