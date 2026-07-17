# GPT-5.6 Terra — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.11 | quality: 9.4
- latency_total: 6.351s | tokens_per_second: 85.7
- input_tokens: 147 | output_tokens: 544
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_totals AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_purchases AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS category_rank
    FROM completed_orders co
    INNER JOIN order_items oi
        ON oi.order_id = co.id
    INNER JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),

top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM category_purchases
    WHERE category_rank = 1
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_totals ct
INNER JOIN customers c
    ON c.id = ct.customer_id
LEFT JOIN top_category tc
    ON tc.customer_id = ct.customer_id
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

La categoría más comprada se calcula por la suma de `quantity` de los productos adquiridos en órdenes completadas durante los últimos 6 meses.