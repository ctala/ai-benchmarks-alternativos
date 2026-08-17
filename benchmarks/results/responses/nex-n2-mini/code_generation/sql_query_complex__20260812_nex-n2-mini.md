# Nex-N2-Mini — code_generation/sql_query_complex

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 8.72 | quality: 9.4
- latency_total: 28.595s | tokens_per_second: 194.6
- input_tokens: 160 | output_tokens: 5564
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

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
        o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_totals AS (
    SELECT
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN completed_orders co
        ON co.customer_id = c.id
    JOIN order_items oi
        ON oi.order_id = co.order_id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
),
category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.order_id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category
        ) AS rn
    FROM category_totals
)
SELECT
    ct.nombre,
    ct.email,
    ct.pais,
    ct.total_orders,
    ROUND(CAST(ct.total_revenue AS DECIMAL(18, 2)), 2) AS total_revenue,
    ROUND(
        CAST(ct.total_revenue / NULLIF(ct.total_orders, 0) AS DECIMAL(18, 2)),
        2
    ) AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_totals ct
JOIN ranked_categories rc
    ON rc.customer_id = ct.customer_id
   AND rc.rn = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

Esta versión considera como `categoria_mas_comprada` la categoría con más unidades compradas. Si quieres que sea la categoría con mayor revenue, cambia en `ranked_categories` el `ORDER BY total_quantity DESC` por `ORDER BY SUM(oi.quantity * oi.unit_price) DESC`.