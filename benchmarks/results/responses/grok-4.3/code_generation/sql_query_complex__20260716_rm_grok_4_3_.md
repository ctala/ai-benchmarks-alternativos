# Grok 4.3 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.44 | quality: 9.4
- latency_total: 8.925s | tokens_per_second: 136.2
- input_tokens: 332 | output_tokens: 1216
- judge_score: 5.0 | justificación: 

## Respuesta completa

```sql
WITH filtered_orders AS (
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(fo.id) AS total_orders,
        SUM(fo.total) AS total_revenue,
        AVG(fo.total) AS avg_order_value
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(fo.id) >= 3
),
customer_categories AS (
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY fo.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM filtered_orders fo
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customer_categories cc 
    ON cs.id = cc.customer_id AND cc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```