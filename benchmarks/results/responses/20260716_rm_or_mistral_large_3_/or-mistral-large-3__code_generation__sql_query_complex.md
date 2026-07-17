# Mistral Large 3 675B — code_generation/sql_query_complex

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.84 | quality: 9.8
- latency_total: 7.621s | tokens_per_second: 70.3
- input_tokens: 147 | output_tokens: 536
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos tus requisitos:

```sql
WITH last_6_months_orders AS (
    SELECT *
    FROM orders
    WHERE created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    AND status = 'completed'
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

customer_top_categories AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        RANK() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS category_rank
    FROM last_6_months_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
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
JOIN customer_top_categories ctc ON cs.customer_id = ctc.customer_id AND ctc.category_rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Explicación de la consulta:

1. **last_6_months_orders**: Filtra las órdenes de los últimos 6 meses con status 'completed'
2. **customer_stats**: Calcula las métricas básicas por cliente (total de órdenes, revenue total, valor promedio de orden) y filtra solo clientes con al menos 3 órdenes
3. **customer_top_categories**: Determina la categoría más comprada para cada cliente usando RANK()
4. **Consulta final**: Une los datos de clientes con su categoría más comprada y ordena por revenue total descendente, limitando a los top 10

La consulta incluye todas las columnas solicitadas y cumple con todos los requisitos especificados.