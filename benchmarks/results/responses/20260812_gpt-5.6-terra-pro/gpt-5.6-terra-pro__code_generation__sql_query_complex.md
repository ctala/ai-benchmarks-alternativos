# GPT-5.6 Terra Pro — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.09 | quality: 9.4
- latency_total: 10.326s | tokens_per_second: 166.6
- input_tokens: 3557 | output_tokens: 1720
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la lógica de la consulta SQL, proporcionando una solución clara y directamente utilizable para un emprendedor.

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
        o.id,
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
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co
        ON co.customer_id = c.id
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),

category_sales AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_units
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
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_units DESC, category ASC
        ) AS category_rank
    FROM category_sales
)

SELECT
    ct.name AS nombre,
    ct.email,
    ct.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_totals ct
LEFT JOIN ranked_categories rc
    ON rc.customer_id = ct.customer_id
   AND rc.category_rank = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

`categoria_mas_comprada` se determina por la mayor suma de `quantity` comprada por el cliente durante el mismo período de 6 meses.