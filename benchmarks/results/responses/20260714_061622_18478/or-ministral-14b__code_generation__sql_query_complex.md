# Ministral 14B — code_generation/sql_query_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.42 | quality: 8.6
- latency_total: 6.348s | tokens_per_second: 110.9
- input_tokens: 147 | output_tokens: 704
- judge_score: 4.0 | justificación: 

## Respuesta completa

# Query SQL para Top 10 clientes por revenue en últimos 6 meses

```sql
WITH customer_revenue AS (
    -- Calcular revenue por cliente en los últimos 6 meses
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
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

category_counts AS (
    -- Contar compras por categoría para cada cliente
    SELECT
        oi.order_id,
        p.category,
        COUNT(*) AS item_count
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
        oi.order_id, p.category
),

top_categories AS (
    -- Encontrar la categoría más comprada por cada cliente
    SELECT
        cr.customer_id,
        p.category AS categoria_mas_comprada
    FROM
        customer_revenue cr
    JOIN
        orders o ON cr.customer_id = o.customer_id
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        cr.customer_id, p.category
    ORDER BY
        cr.customer_id, COUNT(*) DESC
    LIMIT 1 OFFSET 0 -- Solo la primera categoría por cliente
)

-- Resultado final
SELECT
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    ROUND(cr.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM
    customer_revenue cr
LEFT JOIN
    top_categories tc ON cr.customer_id = tc.customer_id
ORDER BY
    cr.total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **customer_revenue**: Calcula el revenue total, número de órdenes y valor promedio por orden para cada cliente en los últimos 6 meses, solo para órdenes completadas.

2. **category_counts**: Cuenta los items comprados por categoría para cada orden.

3. **top_categories**: Determina la categoría más comprada por cada cliente (la que aparece más veces en sus órdenes).

4. **Resultado final**: Combina la información del cliente con su categoría más comprada y ordena por revenue total descendente, mostrando solo los 10 clientes con mayor revenue.

La consulta filtra solo clientes con al menos 3 órdenes completadas en el período especificado.