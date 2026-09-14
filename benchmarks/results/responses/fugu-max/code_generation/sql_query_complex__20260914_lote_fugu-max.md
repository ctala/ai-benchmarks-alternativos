# Fugu Max — code_generation/sql_query_complex

- model_id: `sakana/fugu-max`
- success: True  | final: 7.81 | quality: 9.4
- latency_total: 50.017s | tokens_per_second: 89.3
- input_tokens: 306 | output_tokens: 4468
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, cumpliendo con todos los requisitos de la consulta SQL compleja.

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

Aquí tienes una query en PostgreSQL. Calcula la categoría más comprada por cantidad total (`SUM(quantity)`) y filtra por órdenes `completed` de los últimos 6 meses.

```sql
WITH pedidos_completados AS (
    SELECT
        o.id,
        o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas_cliente AS (
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.id) AS total_orders,
        COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS total_revenue
    FROM pedidos_completados o
    LEFT JOIN order_items oi ON oi.order_id = o.id
    GROUP BY o.customer_id
    HAVING COUNT(DISTINCT o.id) >= 3
),

categoria_cliente AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM pedidos_completados o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),

categoria_rank AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category
        ) AS rn
    FROM categoria_cliente
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    m.total_orders,
    ROUND(m.total_revenue::numeric, 2) AS total_revenue,
    ROUND((m.total_revenue::numeric / m.total_orders), 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM metricas_cliente m
JOIN customers c ON c.id = m.customer_id
LEFT JOIN categoria_rank cr
       ON cr.customer_id = m.customer_id
      AND cr.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

Si tu motor es MySQL, cambia la condición de fecha por:

```sql
o.created_at >= CURDATE() - INTERVAL 6 MONTH
```