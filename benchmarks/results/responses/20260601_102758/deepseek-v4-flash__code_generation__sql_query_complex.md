# DeepSeek V4 Flash (OpenRouter) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.46 | quality: 9.4
- latency_total: 14.02s | tokens_per_second: 117.2
- input_tokens: 152 | output_tokens: 1643
- judge_score: 5.0 | justificación: 

## Respuesta completa

```sql
WITH 
-- Órdenes completadas en los últimos 6 meses
filtered_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL 6 MONTH
),

-- Métricas por cliente (mínimo 3 órdenes)
customer_metrics AS (
    SELECT 
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        SUM(total) / COUNT(id) AS avg_order_value
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),

-- Cantidad total comprada por categoría para los mismos pedidos
category_quantities AS (
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM filtered_orders fo
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
),

-- Categoría más comprada (con desempate alfabético)
top_category AS (
    SELECT 
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id 
                ORDER BY total_qty DESC, category ASC
            ) AS rn
        FROM category_quantities
    ) ranked
    WHERE rn = 1
)

-- Resultado final
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
LEFT JOIN top_category tc ON cm.customer_id = tc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```