# GPT-5.6 Luna — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.33 | quality: 9.4
- latency_total: 8.181s | tokens_per_second: 120.5
- input_tokens: 147 | output_tokens: 986
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución profunda y clara que un emprendedor podría usar directamente para obtener insights valiosos sobre los clientes.

## Respuesta completa

Asumiendo PostgreSQL y que `orders.total` representa el revenue de cada orden:

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
),

customer_metrics AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    INNER JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(co.id) >= 3
),

category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_units
    FROM completed_orders co
    INNER JOIN order_items oi
        ON oi.order_id = co.id
    INNER JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),

ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_units DESC, category
        ) AS category_rank
    FROM category_totals
)

SELECT
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN ranked_categories rc
    ON rc.customer_id = cm.customer_id
   AND rc.category_rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

La `categoria_mas_comprada` se determina por la cantidad total de unidades compradas. Si se desea determinarla por revenue, se puede reemplazar:

```sql
SUM(oi.quantity) AS total_units
```

por:

```sql
SUM(oi.quantity * oi.unit_price) AS total_units
```