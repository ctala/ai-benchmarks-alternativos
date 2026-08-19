# Devstral 2 123B (NIM) — code_generation/sql_query_complex

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 7.6 | quality: 9.72
- latency_total: 15.757s | tokens_per_second: 40.6
- input_tokens: 147 | output_tokens: 640
- judge_score: 4.8 | justificación: 

## Respuesta completa

# SQL Query para Top 10 Clientes por Revenue en los últimos 6 meses

```sql
WITH customer_orders AS (
    -- Obtenemos las órdenes completadas en los últimos 6 meses
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM
        orders o
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        o.customer_id
    HAVING
        COUNT(DISTINCT o.id) >= 3
),

top_categories AS (
    -- Encontramos la categoría más comprada por cada cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS category_rank
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

-- Combinamos toda la información
SELECT
    c.name,
    c.email,
    c.country,
    co.total_orders,
    co.total_revenue,
    ROUND(co.avg_order_value, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM
    customers c
JOIN
    customer_orders co ON c.id = co.customer_id
JOIN
    top_categories tc ON c.id = tc.customer_id AND tc.category_rank = 1
ORDER BY
    co.total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **Primera CTE (`customer_orders`)**:
   - Calcula el total de órdenes, revenue y valor promedio de orden para cada cliente
   - Filtra solo órdenes completadas en los últimos 6 meses
   - Excluye clientes con menos de 3 órdenes

2. **Segunda CTE (`top_categories`)**:
   - Identifica la categoría más comprada por cada cliente (por cantidad)
   - Usa ROW_NUMBER() para seleccionar solo la categoría con mayor cantidad

3. **Consulta principal**:
   - Combina la información de clientes con los datos calculados
   - Muestra todas las columnas solicitadas
   - Ordena por total_revenue en orden descendente
   - Limita a los top 10 clientes

La consulta devuelve exactamente lo solicitado: nombre, email, país, total de órdenes, revenue total, valor promedio de orden y categoría más comprada, para los 10 clientes con mayor revenue en los últimos 6 meses que hayan completado al menos 3 órdenes.