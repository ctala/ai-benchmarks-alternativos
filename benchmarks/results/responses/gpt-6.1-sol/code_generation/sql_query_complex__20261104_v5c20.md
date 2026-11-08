# GPT-6.1 Sol — code_generation/sql_query_complex

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.36 | quality: 9.6
- latency_total: 7.241s | tokens_per_second: 64.9
- input_tokens: 147 | output_tokens: 470
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

En **PostgreSQL**, tomando “categoría más comprada” como la de **mayor cantidad de unidades** en órdenes completadas durante los últimos 6 meses:

```sql
WITH completed_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_TIMESTAMP - INTERVAL '6 months'
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
category_ranking AS (
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM completed_orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    s.total_orders,
    s.total_revenue,
    s.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats s
JOIN customers c ON c.id = s.customer_id
LEFT JOIN category_ranking cr
    ON cr.customer_id = s.customer_id
   AND cr.rn = 1
ORDER BY s.total_revenue DESC, c.id ASC
LIMIT 10;
```

El revenue se calcula desde `orders.total` antes de unir los ítems, para evitar duplicarlo cuando una orden tiene varios productos. Si dos categorías empatan en unidades, se elige la primera alfabéticamente.