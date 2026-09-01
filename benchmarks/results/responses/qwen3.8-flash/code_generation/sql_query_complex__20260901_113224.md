# Qwen 3.8 Flash — code_generation/sql_query_complex

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.65 | quality: 9.8
- latency_total: 52.599s | tokens_per_second: 63.0
- input_tokens: 212 | output_tokens: 3312
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Asumiendo **PostgreSQL** o un SQL estándar, esta query devuelve los **top 10 clientes por revenue total en los últimos 6 meses**, considerando solo órdenes con `status = 'completed'` y con al menos **3 órdenes completadas**.

La columna `categoria_mas_comprada` se calcula como la categoría con mayor **cantidad total de productos comprados** (`SUM(quantity)`). Si prefieres por revenue, más abajo te dejo cómo cambiarlo.

```sql
WITH recent_completed_orders AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_totals AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(rco.order_id) AS total_orders,
        SUM(rco.total) AS total_revenue,
        SUM(rco.total) / NULLIF(COUNT(rco.order_id), 0) AS avg_order_value
    FROM customers c
    INNER JOIN recent_completed_orders rco
        ON rco.customer_id = c.id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(rco.order_id) >= 3
),

customer_category_totals AS (
    SELECT
        ct.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM customer_totals ct
    INNER JOIN recent_completed_orders rco
        ON rco.customer_id = ct.customer_id
    INNER JOIN order_items oi
        ON oi.order_id = rco.order_id
    INNER JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        ct.customer_id,
        p.category
),

category_rank AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category
        ) AS rn
    FROM customer_category_totals
)

SELECT
    ct.name AS nombre,
    ct.email AS email,
    ct.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_totals ct
LEFT JOIN category_rank cr
    ON cr.customer_id = ct.customer_id
   AND cr.rn = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

### Si usas MySQL

Cambia el filtro de fecha por:

```sql
AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
```

### Si `categoria_mas_comprada` debe ser por revenue

En la CTE `customer_category_totals`, cambia:

```sql
SUM(oi.quantity) AS total_quantity
```

por:

```sql
SUM(oi.quantity * oi.unit_price) AS total_quantity
```

o, más claramente:

```sql
SUM(oi.quantity * oi.unit_price) AS category_revenue
```

y luego ordena por ese campo.