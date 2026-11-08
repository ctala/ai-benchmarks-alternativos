# GPT-5.6 Terra — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.3 | quality: 9.4
- latency_total: 5.354s | tokens_per_second: 102.2
- input_tokens: 147 | output_tokens: 547
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución completa y bien estructurada que aborda todos los aspectos de la consulta, incluyendo el cálculo de la categoría más comprada, lo cual es útil para un emprendedor.

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
WITH customer_stats AS (
    SELECT
        o.customer_id,
        COUNT(*) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id
    HAVING COUNT(*) >= 3
),

category_sales AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi
        ON oi.order_id = o.id
    INNER JOIN products p
        ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY
        o.customer_id,
        p.category
),

top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM category_sales
    WHERE rn = 1
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
INNER JOIN customers c
    ON c.id = cs.customer_id
LEFT JOIN top_category tc
    ON tc.customer_id = cs.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

La categoría más comprada se calcula por la suma de `quantity` de los productos comprados en órdenes completadas durante los últimos 6 meses. En caso de empate, se elige la categoría alfabéticamente menor.