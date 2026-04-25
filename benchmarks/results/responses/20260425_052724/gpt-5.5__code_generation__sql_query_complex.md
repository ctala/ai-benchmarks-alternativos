# GPT-5.5 — code_generation/sql_query_complex

- model_id: `gpt-5.5`
- success: True  | final: 6.84 | quality: 8.84
- latency_total: 8.197s | tokens_per_second: 81.9
- input_tokens: 147 | output_tokens: 671
- judge_score: 4.6 | justificación: 

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
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_revenue AS (
    SELECT
        co.customer_id,
        COUNT(*) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM completed_orders co
    GROUP BY co.customer_id
    HAVING COUNT(*) >= 3
),

category_purchases AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),

top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM category_purchases
    WHERE rn = 1
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_revenue cr
JOIN customers c ON c.id = cr.customer_id
LEFT JOIN top_category tc ON tc.customer_id = cr.customer_id
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

Si usas MySQL, cambia:

```sql
CURRENT_DATE - INTERVAL '6 months'
```

por:

```sql
CURRENT_DATE - INTERVAL 6 MONTH
```