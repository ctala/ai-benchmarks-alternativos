# Grok 4.3 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.48 | quality: 8.0
- latency_total: 7.337s | tokens_per_second: 152.5
- input_tokens: 271 | output_tokens: 1119

## Respuesta completa

```sql
WITH recent_completed_orders AS (
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_base AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN recent_completed_orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_categories AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM recent_completed_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
SELECT 
    cb.name,
    cb.email,
    cb.country,
    cb.total_orders,
    cb.total_revenue,
    ROUND(cb.avg_order_value, 2) AS avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_base cb
LEFT JOIN customer_categories cc 
    ON cb.id = cc.customer_id AND cc.rn = 1
ORDER BY cb.total_revenue DESC
LIMIT 10;
```