# Mercury 2.5 — code_generation/sql_query_complex

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.89 | quality: 9.4
- latency_total: 5.144s | tokens_per_second: 443.4
- input_tokens: 144 | output_tokens: 2281
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución completa y bien estructurada para la consulta SQL compleja, con consideraciones útiles para diferentes motores de base de datos.

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



Aquí tienes una query SQL utilizando CTEs para calcular las métricas solicitadas:

```sql
WITH order_stats AS (
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
category_counts AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS items_count
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
top_category AS (
    SELECT customer_id, category
    FROM (
        SELECT
            customer_id,
            category,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY items_count DESC) as rn
        FROM category_counts
    ) sub
    WHERE rn = 1
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    os.total_orders,
    os.total_revenue,
    os.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customers c
JOIN order_stats os ON c.id = os.customer_id
LEFT JOIN top_category tc ON c.id = tc.customer_id
ORDER BY os.total_revenue DESC
LIMIT 10;
```

Nota: La función de fecha (`CURRENT_DATE - INTERVAL '6 months'`) puede variar según el motor de base de datos (MySQL, PostgreSQL, BigQuery, etc.). Ajusta la sintaxis temporal según sea necesario.