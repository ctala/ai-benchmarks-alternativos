# Muse Ember — code_generation/sql_query_complex

- model_id: `meta/muse-ember`
- success: True  | final: 9.1 | quality: 9.8
- latency_total: 3.644s | tokens_per_second: 561.8
- input_tokens: 149 | output_tokens: 2047
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes la query usando CTEs para separar el cálculo por cliente y la categoría más comprada:

```sql
WITH customer_stats AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_stats AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM category_stats
    WHERE rn = 1
)
SELECT
    cs.name AS nombre,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN top_category tc ON tc.customer_id = cs.id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Notas:**

1.  `customer_stats`: Calcula `total_orders`, `total_revenue` y `avg_order_value` solo con órdenes `completed` de los últimos 6 meses, y filtra con `HAVING COUNT(o.id) >= 3`.
2.  `category_stats` + `top_category`: Calcula la categoría con más unidades compradas (`SUM(oi.quantity)`) por cliente usando `ROW_NUMBER()`. Si prefieres definir "más comprada" por revenue, cambia el `ORDER BY` a `SUM(oi.quantity * oi.unit_price) DESC`.
3.  La sintaxis de fecha `CURRENT_DATE - INTERVAL '6 months'` es para PostgreSQL. En MySQL sería `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.