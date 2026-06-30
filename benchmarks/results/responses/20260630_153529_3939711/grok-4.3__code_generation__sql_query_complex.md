# Grok 4.3 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.49 | quality: 8.0
- latency_total: 8.687s | tokens_per_second: 120.3
- input_tokens: 271 | output_tokens: 1045

## Respuesta completa

```sql
WITH completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),
customer_base AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.total) AS total_revenue
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
),
customer_categories AS (
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        ROW_NUMBER() OVER (PARTITION BY co.customer_id 
                           ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS rn
    FROM completed_orders co
    JOIN order_items oi ON co.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY co.customer_id, p.category
)
SELECT 
    cb.name,
    cb.email,
    cb.country,
    cb.total_orders,
    ROUND(cb.total_revenue, 2) AS total_revenue,
    ROUND(cb.total_revenue / cb.total_orders, 2) AS avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_base cb
LEFT JOIN customer_categories cc 
    ON cb.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY cb.total_revenue DESC
LIMIT 10;
```