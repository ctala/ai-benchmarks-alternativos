# DeepSeek V4.1 Flash — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.46 | quality: 9.4
- latency_total: 21.571s | tokens_per_second: 164.2
- input_tokens: 178 | output_tokens: 3542
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

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

Asumiendo PostgreSQL, la query sería:

```sql
WITH ordenes_completadas AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
revenue_cliente AS (
    SELECT
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(oc.order_id) AS total_orders,
        SUM(oc.total) AS total_revenue,
        AVG(oc.total) AS avg_order_value
    FROM customers c
    JOIN ordenes_completadas oc ON oc.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(oc.order_id) >= 3
),
categoria_cantidad AS (
    SELECT
        oc.customer_id,
        p.category,
        SUM(oi.quantity) AS cantidad,
        ROW_NUMBER() OVER (
            PARTITION BY oc.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM ordenes_completadas oc
    JOIN order_items oi ON oi.order_id = oc.order_id
    JOIN products p ON p.id = oi.product_id
    GROUP BY oc.customer_id, p.category
),
categoria_top AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM categoria_cantidad
    WHERE rn = 1
)
SELECT
    rc.nombre,
    rc.email,
    rc.pais,
    rc.total_orders,
    rc.total_revenue,
    rc.avg_order_value,
    ct.categoria_mas_comprada
FROM revenue_cliente rc
LEFT JOIN categoria_top ct ON ct.customer_id = rc.customer_id
ORDER BY rc.total_revenue DESC
LIMIT 10;
```

Notas:
- `total_revenue` se calcula con `orders.total` de órdenes `completed` en los últimos 6 meses.
- `categoria_mas_comprada` se calcula sumando `quantity` por categoría.
- Si usas MySQL, cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`.