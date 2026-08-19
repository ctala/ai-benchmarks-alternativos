# Ministral 14B — code_generation/sql_query_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 11.336s | tokens_per_second: 61.5
- input_tokens: 147 | output_tokens: 697
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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
        SUM(oi.quantity * oi.unit_price) AS total_revenue,
        AVG(oi.quantity * oi.unit_price) AS avg_order_value
    FROM
        customers c
    JOIN
        orders o ON c.id = o.customer_id
    JOIN
        order_items oi ON o.id = oi.order_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(DISTINCT o.id) >= 3
),

customer_top_category AS (
    -- Determinar la categoría más comprada por cada cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM
        orders o
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        o.customer_id, p.category
)

-- Resultado final con la categoría más comprada
SELECT
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    ROUND(cr.avg_order_value, 2) AS avg_order_value,
    COALESCE(ctc.category, 'N/A') AS categoria_mas_comprada
FROM
    customer_revenue cr
LEFT JOIN
    customer_top_category ctc ON cr.customer_id = ctc.customer_id AND ctc.rn = 1
ORDER BY
    cr.total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **CTE customer_revenue**:
   - Calcula el revenue total por cliente en los últimos 6 meses
   - Solo incluye órdenes completadas (status = 'completed')
   - Filtra clientes con al menos 3 órdenes
   - Calcula métricas: total_orders, total_revenue y avg_order_value

2. **CTE customer_top_category**:
   - Determina la categoría más comprada por cada cliente
   - Usa ROW_NUMBER() para identificar la categoría con mayor cantidad comprada

3. **Query principal**:
   - Combina ambos CTEs para mostrar el resultado final
   - Usa COALESCE para manejar casos donde no haya categoría (aunque con el filtro de 3+ órdenes esto no debería ocurrir)
   - Ordena por total_revenue DESC y limita a 10 resultados

La consulta maneja correctamente los últimos 6 meses desde la fecha actual y solo incluye clientes con al menos 3 órdenes completadas en ese período.