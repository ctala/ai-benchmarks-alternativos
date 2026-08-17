# DeepSeek V4 Flash 0731 — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.12 | quality: 9.16
- latency_total: 163.782s | tokens_per_second: 16.5
- input_tokens: 152 | output_tokens: 2696
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, cumpliendo con todos los requisitos de la consulta SQL compleja.

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

```sql
WITH 
-- Órdenes completadas en los últimos 6 meses
recent_orders AS (
    SELECT id AS order_id, customer_id
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

-- Items de esas órdenes con su categoría
order_items_with_cat AS (
    SELECT 
        oi.order_id,
        oi.product_id,
        oi.quantity,
        oi.unit_price,
        p.category
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
),

-- Métricas por cliente: total de órdenes, revenue total y ticket promedio
customer_metrics AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT ro.order_id) AS total_orders,
        SUM(oiw.quantity * oiw.unit_price) AS total_revenue,
        SUM(oiw.quantity * oiw.unit_price) / COUNT(DISTINCT ro.order_id) AS avg_order_value
    FROM customers c
    JOIN recent_orders ro ON c.id = ro.customer_id
    JOIN order_items_with_cat oiw ON ro.order_id = oiw.order_id
    GROUP BY c.id, c.name, c.email, c.country
),

-- Cantidad comprada por cliente y categoría
category_totals AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        SUM(oi.quantity * oi.unit_price) AS total_rev_cat
    FROM customers c
    JOIN recent_orders ro ON c.id = ro.customer_id
    JOIN order_items oi ON ro.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.id, p.category
),

-- Ranking de categorías por cliente (mayor cantidad, desempate por revenue)
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY total_qty DESC, total_rev_cat DESC
        ) AS rn
    FROM category_totals
)

-- Selección final
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN ranked_categories rc ON cm.id = rc.customer_id AND rc.rn = 1
WHERE cm.total_orders >= 3
ORDER BY cm.total_revenue DESC
LIMIT 10;
```