# Grok 4.6 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.98 | quality: 9.4
- latency_total: 20.651s | tokens_per_second: 86.3
- input_tokens: 357 | output_tokens: 1782
- judge_score: 5.0 | justificación: 

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
WITH recent_completed_orders AS (
    SELECT *
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN recent_completed_orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_purchases AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM recent_completed_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_qty DESC) AS rn
    FROM category_purchases
)
SELECT
    cs.name AS nombre,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN ranked_categories rc ON cs.id = rc.customer_id AND rc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```