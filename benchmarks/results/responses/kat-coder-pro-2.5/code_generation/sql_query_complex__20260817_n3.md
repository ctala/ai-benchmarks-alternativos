# KAT Coder Pro v2.5 — code_generation/sql_query_complex

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.4 | quality: 9.4
- latency_total: 6.482s | tokens_per_second: 95.8
- input_tokens: 161 | output_tokens: 621
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, cumpliendo con todos los requisitos de la consulta SQL compleja.

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')


## Respuesta completa



WITH completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
),
order_revenue AS (
    SELECT 
        co.customer_id,
        co.order_id,
        SUM(oi.quantity * oi.unit_price) AS order_item_revenue
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.order_id
    GROUP BY co.customer_id, co.order_id
),
customer_stats AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT orr.order_id) AS total_orders,
        SUM(orr.order_item_revenue) AS total_revenue,
        ROUND(AVG(orr.order_item_revenue), 2) AS avg_order_value
    FROM customers c
    JOIN order_revenue orr ON orr.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT orr.order_id) >= 3
),
category_counts AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customers c
    JOIN completed_orders co ON co.customer_id = c.id
    JOIN order_items oi ON oi.order_id = co.order_id
    JOIN products p ON p.id = oi.product_id
    GROUP BY c.id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    cs.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_counts cc ON cc.customer_id = cs.customer_id AND cc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;