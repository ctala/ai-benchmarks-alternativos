# GPT-5.6 Sol — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.0 | quality: 9.4
- latency_total: 7.602s | tokens_per_second: 62.5
- input_tokens: 147 | output_tokens: 475
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

## Respuesta completa

```sql
WITH customer_metrics AS (
    SELECT
        o.customer_id,
        COUNT(*) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id
    HAVING COUNT(*) >= 3
),
category_ranking AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
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

`categoria_mas_comprada` se determina por la suma de unidades (`quantity`) compradas. En caso de empate, se elige la categoría alfabéticamente. La sintaxis de fechas corresponde a PostgreSQL.