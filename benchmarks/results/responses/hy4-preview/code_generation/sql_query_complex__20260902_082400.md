# Tencent Hy4 preview — code_generation/sql_query_complex

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.25 | quality: 9.6
- latency_total: 41.714s | tokens_per_second: 56.0
- input_tokens: 168 | output_tokens: 2334
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

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

Asumiendo **PostgreSQL**, puedes usar CTEs para evitar duplicar `orders.total` al unir `order_items`:

```sql
WITH filtered_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_metrics AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_totals AS (
    SELECT
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_units
    FROM filtered_orders fo
    JOIN order_items oi
        ON oi.order_id = fo.id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY fo.customer_id, p.category
),

ranked_categories AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_units DESC, category ASC
        ) AS rn
    FROM category_totals
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    ROUND(cm.total_revenue::numeric, 2) AS total_revenue,
    ROUND((cm.total_revenue / cm.total_orders)::numeric, 2) AS avg_order_value,
    rc.categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c
    ON c.id = cm.customer_id
LEFT JOIN ranked_categories rc
    ON rc.customer_id = cm.customer_id
   AND rc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

Notas:

- `categoria_mas_comprada` se calcula por **cantidad de unidades compradas**: `SUM(oi.quantity)`.
- Si quieres calcular la categoría por **revenue de categoría**, cambia:

```sql
SUM(oi.quantity)
```

por:

```sql
SUM(oi.quantity * oi.unit_price)
```

- En **MySQL**, cambia la condición de fecha por:

```sql
AND o.created_at >= NOW() - INTERVAL 6 MONTH
```