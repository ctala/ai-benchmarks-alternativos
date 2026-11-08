# GPT-6.1 Terra — code_generation/sql_query_complex

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.44 | quality: 9.6
- latency_total: 8.121s | tokens_per_second: 76.6
- input_tokens: 147 | output_tokens: 622
- judge_score: 5.0 | justificación: 

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

En PostgreSQL, tomando la categoría más comprada como la de mayor **cantidad de unidades**:

```sql
WITH completed_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
      AND created_at <= CURRENT_TIMESTAMP
),
customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_quantities AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    WHERE p.category IS NOT NULL
    GROUP BY o.customer_id, p.category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category ASC
        ) AS rn
    FROM category_quantities
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    s.total_orders,
    s.total_revenue,
    s.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_stats s
JOIN customers c ON c.id = s.customer_id
LEFT JOIN ranked_categories rc
    ON rc.customer_id = s.customer_id
   AND rc.rn = 1
ORDER BY s.total_revenue DESC
LIMIT 10;
```

El revenue se calcula con `orders.total`. Si hay empate entre categorías por cantidad, se elige la primera alfabéticamente.