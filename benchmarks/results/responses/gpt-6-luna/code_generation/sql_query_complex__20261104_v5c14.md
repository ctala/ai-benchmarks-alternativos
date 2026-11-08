# GPT-6 Luna — code_generation/sql_query_complex

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.84 | quality: 9.6
- latency_total: 8.651s | tokens_per_second: 92.7
- input_tokens: 147 | output_tokens: 802
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

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

Asumiendo que el revenue corresponde a `orders.total` y que la categoría más comprada se determina por la **cantidad de unidades**, en PostgreSQL:

```sql
WITH recent_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
      AND created_at < CURRENT_TIMESTAMP
),
customer_metrics AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM recent_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_units AS (
    SELECT
        ro.customer_id,
        p.category,
        SUM(oi.quantity) AS units_bought
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY units_bought DESC, category
        ) AS category_rank
    FROM category_units
)
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON c.id = cm.customer_id
LEFT JOIN ranked_categories rc
    ON rc.customer_id = cm.customer_id
   AND rc.category_rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

En caso de empate en unidades, se elige la categoría cuyo nombre aparece primero.