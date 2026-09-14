# Qwen 3.8 Max 0902 — code_generation/sql_query_complex

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.54 | quality: 9.4
- latency_total: 180.354s | tokens_per_second: 45.8
- input_tokens: 212 | output_tokens: 8263
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes una query usando CTEs y window functions. Asumo que:

- El revenue se calcula con `orders.total`.
- Solo se consideran órdenes `completed` de los últimos 6 meses.
- “Categoría más comprada” = categoría con mayor cantidad total de unidades compradas.

```sql
WITH completed_orders AS (
    SELECT
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
      -- En MySQL puedes usar:
      -- AND created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),

customer_metrics AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN completed_orders o
        ON o.customer_id = c.id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(o.id) >= 3
),

category_totals AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders o
    INNER JOIN order_items oi
        ON oi.order_id = o.id
    INNER JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        o.customer_id,
        p.category
),

top_category AS (
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
    cm.name AS nombre,
    cm.email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN top_category tc
    ON tc.customer_id = cm.customer_id
   AND tc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

Nota: si quieres que la categoría más comprada se calcule por revenue generado por categoría en lugar de cantidad de unidades, cambia en `category_totals`:

```sql
SUM(oi.quantity) AS total_quantity
```

por:

```sql
SUM(oi.quantity * oi.unit_price) AS total_category_revenue
```

Y luego ordena por ese campo en `top_category`.