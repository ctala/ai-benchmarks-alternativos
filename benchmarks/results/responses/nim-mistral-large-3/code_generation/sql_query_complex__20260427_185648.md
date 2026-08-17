# Mistral Large 3 675B (NIM) — code_generation/sql_query_complex

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 7.3 | quality: 9.44
- latency_total: 60.487s | tokens_per_second: 10.6
- input_tokens: 144 | output_tokens: 639
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Query SQL para Top 10 Clientes por Revenue en los Últimos 6 Meses

Aquí tienes la consulta SQL que cumple con tus requerimientos:

```sql
WITH customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / COUNT(DISTINCT o.id) AS avg_order_value,
        o.created_at
    FROM
        customers c
    JOIN
        orders o ON c.id = o.customer_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(DISTINCT o.id) >= 3
),

category_ranking AS (
    SELECT
        oi.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        RANK() OVER (PARTITION BY oi.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS category_rank
    FROM
        order_items oi
    JOIN
        orders o ON oi.order_id = o.id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        oi.customer_id, p.category
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM
    customer_stats cs
JOIN
    category_ranking cr ON cs.customer_id = cr.customer_id AND cr.category_rank = 1
ORDER BY
    cs.total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **customer_stats**:
   - Calcula estadísticas básicas por cliente: total de órdenes, revenue total y valor promedio por orden
   - Filtra órdenes completadas en los últimos 6 meses
   - Aplica el filtro de al menos 3 órdenes completadas

2. **category_ranking**:
   - Calcula el revenue por categoría para cada cliente
   - Usa RANK() para identificar la categoría más comprada por cada cliente

3. **Resultado final**:
   - Une las dos CTEs para obtener la categoría más comprada por cada cliente
   - Ordena por revenue total descendente
   - Limita a los top 10 clientes

Nota: Si algún cliente tiene empate en categorías (misma cantidad de revenue en varias categorías), la consulta seleccionará una de ellas arbitrariamente. Si necesitas manejar empates de manera específica, podríamos modificar la consulta.