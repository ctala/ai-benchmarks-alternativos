# GPT-5.4 — code_generation/sql_query_complex

- model_id: `gpt-5.4`
- success: True  | final: 7.51 | quality: 9.04
- latency_total: 5.238s | tokens_per_second: 80.8
- input_tokens: 147 | output_tokens: 423
- judge_score: 4.6 | justificación: 

## Respuesta completa

```sql
WITH completed_orders_last_6m AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_order_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM completed_orders_last_6m co
    JOIN customers c
      ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),
customer_category_rank AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM completed_orders_last_6m co
    JOIN order_items oi
      ON oi.order_id = co.id
    JOIN products p
      ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    s.name AS nombre,
    s.email,
    s.country AS pais,
    s.total_orders,
    s.total_revenue,
    s.avg_order_value,
    ccr.category AS categoria_mas_comprada
FROM customer_order_stats s
LEFT JOIN customer_category_rank ccr
  ON ccr.customer_id = s.customer_id
 AND ccr.rn = 1
ORDER BY s.total_revenue DESC
LIMIT 10;
```

Si quieres, también te la puedo adaptar a:
- **MySQL**
- **PostgreSQL**
- **SQL Server**
- o hacerla usando `SUM(oi.quantity * oi.unit_price)` en vez de `orders.total` para calcular revenue.