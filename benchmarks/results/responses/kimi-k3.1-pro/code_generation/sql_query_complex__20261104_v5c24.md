# Kimi K3.1 Pro — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.83 | quality: 9.6
- latency_total: 75.521s | tokens_per_second: 30.7
- input_tokens: 236 | output_tokens: 2321
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la lógica necesaria para resolver el problema, proporcionando una consulta SQL bien estructurada y clara que un emprendedor podría usar directamente.

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

En **PostgreSQL**, usando únicamente órdenes completadas de los últimos 6 meses. La categoría más comprada se determina por **unidades vendidas**; en caso de empate, por revenue de la categoría:

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
customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(*) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM completed_orders co
    JOIN customers c
        ON c.id = co.customer_id
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
        SUM(oi.quantity) AS total_units,
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
ranked_categories AS (
    SELECT
        ct.customer_id,
        ct.category,
        ROW_NUMBER() OVER (
            PARTITION BY ct.customer_id
            ORDER BY
                ct.total_units DESC,
                ct.category_revenue DESC,
                ct.category ASC
        ) AS category_rank
    FROM category_totals ct
)
SELECT
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN ranked_categories rc
    ON rc.customer_id = cs.customer_id
   AND rc.category_rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Si un cliente no tiene líneas de pedido asociadas, `categoria_mas_comprada` aparecerá como `NULL`.