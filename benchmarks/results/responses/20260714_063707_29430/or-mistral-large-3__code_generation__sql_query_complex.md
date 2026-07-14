# Mistral Large 3 675B — code_generation/sql_query_complex

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.81 | quality: 9.8
- latency_total: 8.715s | tokens_per_second: 71.0
- input_tokens: 147 | output_tokens: 619
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, cumpliendo con todos los requisitos especificados de manera efectiva.

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH last_6_months_orders AS (
    SELECT *
    FROM orders
    WHERE status = 'completed'
    AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),

customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / COUNT(DISTINCT o.id) AS avg_order_value
    FROM customers c
    JOIN last_6_months_orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),

customer_top_category AS (
    SELECT
        oi.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        RANK() OVER (PARTITION BY oi.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS category_rank
    FROM order_items oi
    JOIN last_6_months_orders o ON oi.order_id = o.id
    JOIN products p ON oi.product_id = p.id
    GROUP BY oi.customer_id, p.category
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customer_top_category ctc ON cs.customer_id = ctc.customer_id AND ctc.category_rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Explicación de la consulta:

1. **last_6_months_orders**: Filtra las órdenes completadas de los últimos 6 meses.
2. **customer_stats**: Calcula las estadísticas básicas de cada cliente (nombre, email, país, total de órdenes, revenue total y valor promedio de orden), filtrando solo aquellos con al menos 3 órdenes completadas.
3. **customer_top_category**: Determina la categoría más comprada para cada cliente, calculando el revenue por categoría y usando RANK() para identificar la categoría principal.
4. **Consulta final**: Une las estadísticas de clientes con su categoría más comprada y ordena por revenue total descendente, limitando a los 10 primeros resultados.

La consulta cumple con todos los requisitos especificados:
- Top 10 clientes por revenue total en los últimos 6 meses
- Columnas solicitadas (nombre, email, país, total_orders, total_revenue, avg_order_value, categoria_mas_comprada)
- Ordenado por total_revenue DESC
- Solo clientes con al menos 3 órdenes completadas