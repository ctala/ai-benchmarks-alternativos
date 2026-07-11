# GPT-5.6 Sol — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.99 | quality: 9.4
- latency_total: 8.258s | tokens_per_second: 60.7
- input_tokens: 147 | output_tokens: 501
- judge_score: 5.0 | justificación: 

## Respuesta completa

```sql
-- PostgreSQL
WITH completed_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_ranking AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS units_purchased,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY
                SUM(oi.quantity) DESC,
                SUM(oi.quantity * oi.unit_price) DESC,
                p.category
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON c.id = cm.customer_id
LEFT JOIN category_ranking cr
       ON cr.customer_id = cm.customer_id
      AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

`categoria_mas_comprada` se determina por la mayor cantidad total de unidades compradas. En caso de empate, se prioriza la categoría con mayor revenue.