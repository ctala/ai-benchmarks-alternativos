# Grok 4.3 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.39 | quality: 8.0
- latency_total: 11.39s | tokens_per_second: 105.3
- input_tokens: 271 | output_tokens: 1199

## Respuesta completa

```sql
WITH completed_orders AS (
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),
customer_stats AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        ROUND(SUM(co.total) / COUNT(DISTINCT co.id), 2) AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.id) >= 3
),
category_revenue AS (
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS revenue,
        ROW_NUMBER() OVER (PARTITION BY co.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS rn
    FROM completed_orders co
    JOIN order_items oi ON co.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY co.customer_id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_revenue cr 
    ON cs.id = cr.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```