# Tencent Hy4 preview — code_generation/sql_query_complex

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.02 | quality: 9.6
- latency_total: 114.854s | tokens_per_second: 66.1
- input_tokens: 168 | output_tokens: 7593
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Asumiendo **PostgreSQL** y que `revenue = orders.total` para órdenes `completed` de los últimos 6 meses:

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
),

customer_metrics AS (
    SELECT
        c.id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(*) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(*) >= 3
),

category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS units_bought,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),

top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            ct.*,
            ROW_NUMBER() OVER (
                PARTITION BY ct.customer_id
                ORDER BY
                    ct.units_bought DESC,
                    ct.category_revenue DESC,
                    ct.category
            ) AS rn
        FROM category_totals ct
    ) ranked
    WHERE rn = 1
)

SELECT
    cm.nombre,
    cm.email,
    cm.pais,
    cm.total_orders,
    ROUND(CAST(cm.total_revenue AS DECIMAL(18,2)), 2) AS total_revenue,
    ROUND(CAST(cm.avg_order_value AS DECIMAL(18,2)), 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN top_category tc
    ON tc.customer_id = cm.id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

Notas:

- `categoria_mas_comprada` se calcula por **cantidad comprada**. Si la quieres por **revenue de categoría**, cambia el `ORDER BY` del `ROW_NUMBER()` a:

```sql
ORDER BY ct.category_revenue DESC, ct.units_bought DESC
```

- En MySQL, cambia la condición de fecha por:

```sql
AND o.created_at >= NOW() - INTERVAL 6 MONTH
```