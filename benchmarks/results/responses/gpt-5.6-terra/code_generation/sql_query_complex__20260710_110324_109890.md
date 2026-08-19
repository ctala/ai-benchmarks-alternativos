# GPT-5.6 Terra — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.42 | quality: 9.4
- latency_total: 4.846s | tokens_per_second: 109.8
- input_tokens: 147 | output_tokens: 532
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución profunda y clara que un emprendedor podría usar directamente para obtener información valiosa sobre los clientes.

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
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),

category_quantities AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS category_rank
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
)

SELECT
    ct.name AS nombre,
    ct.email,
    ct.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    cq.category AS categoria_mas_comprada
FROM customer_totals ct
LEFT JOIN category_quantities cq
    ON cq.customer_id = ct.customer_id
   AND cq.category_rank = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

La categoría más comprada se determina por la suma de `quantity` de productos comprados en órdenes completadas durante los últimos 6 meses.