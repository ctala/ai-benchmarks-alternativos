# Grok 4.6 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.97 | quality: 9.4
- latency_total: 29.997s | tokens_per_second: 63.1
- input_tokens: 357 | output_tokens: 1893
- judge_score: 5 | justificación: La respuesta es precisa y completa, abordando todos los aspectos de la consulta SQL compleja solicitada. La consulta está bien estructurada y utiliza correctamente las subconsultas y funciones de ventana para calcular métricas avanzadas como el total de ingresos y la categoría más comprada. La claridad y organización de la respuesta facilitan su comprensión y aplicación, haciéndola altamente útil para un emprendedor.

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
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / COUNT(o.id) AS avg_order_value
    FROM customers c
    JOIN recent_completed_orders o ON o.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_qty AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS qty
    FROM recent_completed_orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),
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
                ORDER BY qty DESC, category
            ) AS rn
        FROM category_qty
    ) t
    WHERE rn = 1
)
SELECT
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
JOIN top_category tc ON tc.customer_id = cs.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Si usas MySQL, cambia el filtro de fecha a `created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`.