# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — code_generation/sql_query_complex

- model_id: `nemotron-3-super:120b`
- success: True  | final: 7.29 | quality: 9.12
- latency_total: 55.165s | tokens_per_second: 18.3
- input_tokens: 160 | output_tokens: 1012
- judge_score: 4.8 | justificación: 

## Respuesta completa

```sql
WITH recent_orders AS (
    SELECT o.id, o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
order_stats AS (
    SELECT
        ro.customer_id,
        COUNT(*)                                 AS total_orders,
        SUM(oi.quantity * oi.unit_price)         AS total_revenue,
        AVG(oi.quantity * oi.unit_price)         AS avg_order_value
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    GROUP BY ro.customer_id
    HAVING COUNT(*) >= 3
),
category_stats AS (
    SELECT
        ro.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price)         AS cat_revenue
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),
best_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY cat_revenue DESC, category
            ) AS rn
        FROM category_stats
    ) sub
    WHERE rn = 1
)
SELECT
    c.name,
    c.email,
    c.country AS pais,
    os.total_orders,
    os.total_revenue,
    os.avg_order_value,
    bc.categoria_mas_comprada
FROM order_stats os
JOIN customers c ON c.id = os.customer_id
LEFT JOIN best_category bc ON bc.customer_id = os.customer_id
ORDER BY os.total_revenue DESC
LIMIT 10;
```