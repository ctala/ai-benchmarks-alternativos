# Devstral 2 (Dic 2025) — code_generation/sql_query_complex

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.75 | quality: 9.72
- latency_total: 9.222s | tokens_per_second: 65.1
- input_tokens: 147 | output_tokens: 600
- judge_score: 4.8 | justificación: 

## Respuesta completa

# SQL Query para Top 10 Clientes por Revenue en los Últimos 6 Meses

Aquí tienes la consulta SQL que solicitas:

```sql
WITH customer_orders AS (
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

top_category AS (
    SELECT
        o.customer_id,
        p.category,
        COUNT(oi.id) AS category_count,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(oi.id) DESC) AS rank
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

SELECT
    co.name,
    co.email,
    co.country,
    co.total_orders,
    co.total_revenue,
    ROUND(co.avg_order_value, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM
    customer_orders co
LEFT JOIN
    top_category tc ON co.customer_id = tc.customer_id AND tc.rank = 1
ORDER BY
    co.total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **Primera CTE (`customer_orders`)**:
   - Calcula métricas básicas por cliente (total de órdenes, revenue total, valor promedio de orden)
   - Filtra solo órdenes completadas en los últimos 6 meses
   - Excluye clientes con menos de 3 órdenes completadas

2. **Segunda CTE (`top_category`)**:
   - Identifica la categoría más comprada por cada cliente
   - Usa ROW_NUMBER() para seleccionar solo la categoría con mayor cantidad de compras

3. **Consulta principal**:
   - Combina los resultados de ambas CTEs
   - Formatea el valor promedio de orden a 2 decimales
   - Ordena por revenue total descendente
   - Limita a los top 10 clientes

Esta consulta proporciona exactamente la información solicitada en el formato requerido.