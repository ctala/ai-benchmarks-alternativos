# Ministral 14B (NIM) — code_generation/sql_query_complex

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.4 | quality: 9.44
- latency_total: 52.564s | tokens_per_second: 15.1
- input_tokens: 147 | output_tokens: 792
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Query SQL para Top 10 clientes por revenue en los últimos 6 meses

```sql
WITH order_revenue AS (
    -- Cálculo del revenue por cliente solo para órdenes completadas en los últimos 6 meses
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        SUM(oi.quantity * oi.unit_price) AS order_revenue
    FROM
        orders o
    JOIN
        customers c ON o.customer_id = c.id
    JOIN
        order_items oi ON o.id = oi.order_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        c.id, c.name, c.email, c.country
),

customer_stats AS (
    -- Estadísticas de los clientes con al menos 3 órdenes completadas
    SELECT
        customer_id,
        name,
        email,
        country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue,
        AVG(oi.quantity * oi.unit_price) AS avg_order_value,
        -- Categoría más comprada (por valor total)
        (
            SELECT p.category
            FROM order_items oi2
            JOIN products p ON oi2.product_id = p.id
            JOIN orders o2 ON oi2.order_id = o2.id
            WHERE o2.customer_id = c.customer_id
              AND o2.status = 'completed'
              AND o2.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
            GROUP BY p.category
            ORDER BY SUM(oi2.quantity * oi2.unit_price) DESC
            LIMIT 1
        ) AS categoria_mas_comprada
    FROM
        orders o
    JOIN
        customers c ON o.customer_id = c.id
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        order_revenue orev ON c.id = orev.customer_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        c.id, c.name, c.email, c.country, orev.order_revenue
    HAVING
        COUNT(DISTINCT o.id) >= 3
)

-- Resultado final con las columnas solicitadas
SELECT
    name,
    email,
    country,
    total_orders,
    total_revenue,
    avg_order_value,
    categoria_mas_comprada
FROM
    customer_stats
ORDER BY
    total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **CTE `order_revenue`**:
   - Calcula el revenue por cliente solo para órdenes completadas en los últimos 6 meses
   - Filtra por status='completed' y fecha de creación en los últimos 6 meses

2. **CTE `customer_stats`**:
   - Obtiene estadísticas detalladas de los clientes
   - Cuenta el total de órdenes (distintas) y calcula revenue total y valor promedio
   - Determina la categoría más comprada (por valor total gastado)
   - Aplica el filtro de al menos 3 órdenes completadas con HAVING

3. **Consulta final**:
   - Selecciona las columnas solicitadas
   - Ordena por revenue total en descendenete
   - Limita a los 10 clientes con mayor revenue

La consulta asegura que solo se consideran órdenes completadas (`status = 'completed'`) en el período de los últimos 6 meses y clientes con al menos 3 órdenes.