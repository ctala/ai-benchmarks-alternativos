# Qwen 3.8 Flash — code_generation/sql_query_complex

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.43 | quality: 9.6
- latency_total: 48.258s | tokens_per_second: 99.9
- input_tokens: 212 | output_tokens: 4823
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

Suponiendo **PostgreSQL**, esta query devuelve los **top 10 clientes** por revenue total en los últimos 6 meses, considerando solo órdenes con `status = 'completed'` y mínimo 3 órdenes completadas:

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_totals AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS category_quantity,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),

top_category AS (
    SELECT
        customer_id,
        category
    FROM (
        SELECT
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY category_quantity DESC, category_revenue DESC
            ) AS rn
        FROM category_totals
    ) ranked
    WHERE rn = 1
)

SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ROUND(
        CAST(ct.total_revenue AS numeric) / NULLIF(ct.total_orders, 0),
        2
    ) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_totals ct
JOIN customers c ON c.id = ct.customer_id
LEFT JOIN top_category tc ON tc.customer_id = ct.customer_id
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

Notas:

- `total_revenue` usa la columna `orders.total`.
- `avg_order_value` se calcula como `total_revenue / total_orders`.
- `categoria_mas_comprada` está definida como la categoría con mayor cantidad comprada (`SUM(oi.quantity)`). Si quieres que sea la categoría con mayor revenue, cambia el `ORDER BY` dentro de `ROW_NUMBER()` a:

```sql
ORDER BY category_revenue DESC, category_quantity DESC
```

- Si usas **MySQL**, cambia esta línea:

```sql
AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
```

por:

```sql
AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
```