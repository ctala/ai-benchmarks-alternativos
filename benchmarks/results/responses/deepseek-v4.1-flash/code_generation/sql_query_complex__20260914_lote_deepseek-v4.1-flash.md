# DeepSeek V4.1 Flash — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.44 | quality: 9.4
- latency_total: 16.31s | tokens_per_second: 234.2
- input_tokens: 178 | output_tokens: 3820
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profunda, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados, incluyendo el cálculo de la categoría más comprada y el filtrado de clientes con al menos 3 órdenes en los últimos 6 meses.

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
WITH completed_orders AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.order_id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.order_id) >= 3
),
category_qty AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.order_id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),
category_rank AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category
        ) AS rn
    FROM category_qty
)
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_rank cr
    ON cr.customer_id = cs.customer_id
   AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Notas:
- La fecha `CURRENT_DATE - INTERVAL '6 months'` es para PostgreSQL; en MySQL sería `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` y en SQL Server `DATEADD(month, -6, GETDATE())`.
- `categoria_mas_comprada` se calcula por cantidad total comprada (`SUM(quantity)`) en los últimos 6 meses.
- Si el revenue debe calcularse desde `order_items` en vez de `orders.total`, cambia `SUM(co.total)` por `SUM(oi.quantity * oi.unit_price)`.