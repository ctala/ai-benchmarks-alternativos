# GPT-5.6 Sol — code_generation/sql_query_complex

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.17 | quality: 9.4
- latency_total: 6.606s | tokens_per_second: 88.9
- input_tokens: 147 | output_tokens: 587
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la lógica de la consulta SQL, proporcionando insights útiles y claridad en su estructura, lo que la hace directamente utilizable por un emprendedor.

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
        id,
        customer_id,
        total
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
category_stats AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY
                SUM(oi.quantity) DESC,
                SUM(oi.quantity * oi.unit_price) DESC,
                p.category
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cat.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN category_stats cat
       ON cat.customer_id = cs.customer_id
      AND cat.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

La categoría más comprada se determina por la cantidad total de unidades. En caso de empate, se prioriza la categoría con mayor revenue y después el nombre de la categoría. La sintaxis del intervalo corresponde a PostgreSQL.