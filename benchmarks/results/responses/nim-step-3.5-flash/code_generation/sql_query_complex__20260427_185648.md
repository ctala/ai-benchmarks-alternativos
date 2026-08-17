# Step 3.5 Flash (NIM) — code_generation/sql_query_complex

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 6.6 | quality: 8.0
- latency_total: 117.493s | tokens_per_second: 17.4
- input_tokens: 160 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

## Respuesta completa

```sql
WITH 
-- Órdenes completadas en los últimos 6 meses
filtered_orders AS (
    SELECT 
        o.id, 
        o.customer_id, 
        o.total, 
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
),

-- Datos agregados por cliente (mínimo 3 órdenes)
customer_summary AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT fo.id) AS total_orders,
        SUM(fo.total) AS total_revenue,
        AVG(fo.total) AS avg_order_value
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT fo.id) >= 3
),

-- Cantidad total de productos por categoría para cada cliente
category_purchases AS (
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM filtered_orders fo
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
),

-- Rank de categorías por cantidad comprada por cliente
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY total_quantity DESC, category
        ) AS rank
    FROM category_purchases
)

-- Resultado final
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
