# GPT-5.6 Luna Pro — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.57 | quality: 9.6
- latency_total: 16.685s | tokens_per_second: 196.5
- input_tokens: 4785 | output_tokens: 3278
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, cumpliendo con todos los requisitos de la consulta SQL compleja.

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

Asumiendo que el revenue se calcula usando `orders.total` y que todas las métricas consideran únicamente órdenes **completadas durante los últimos 6 meses**:

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
),

customer_metrics AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    INNER JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY
        c.id,
        c.name,
        c.email,
        c.country
    HAVING COUNT(co.id) >= 3
),

category_purchases AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS units_purchased
    FROM completed_orders co
    INNER JOIN order_items oi
        ON oi.order_id = co.id
    INNER JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),

most_purchased_category AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY units_purchased DESC, category
        ) AS category_rank
    FROM category_purchases
)

SELECT
    cm.name,
    cm.email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    mpc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN most_purchased_category mpc
    ON mpc.customer_id = cm.customer_id
   AND mpc.category_rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

`categoria_mas_comprada` se determina por la suma de unidades compradas (`quantity`). En caso de empate, se elige la categoría cuyo nombre aparece primero alfabéticamente.