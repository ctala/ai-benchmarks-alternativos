# Ling 3.0 Flash — code_generation/sql_query_complex

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.41 | quality: 9.8
- latency_total: 4.47s | tokens_per_second: 406.2
- input_tokens: 177 | output_tokens: 1816
- judge_score: 5.0 | justificación: 

## Respuesta completa

```sql
WITH customer_stats AS (
    SELECT
        c.id           AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)  AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN orders o
        ON o.customer_id = c.id
    JOIN order_items oi
        ON oi.order_id = o.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_ranking AS (
    SELECT
        c.id        AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY c.id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM customers c
    JOIN orders o
        ON o.customer_id = c.id
    JOIN order_items oi
        ON oi.order_id = o.id
    JOIN products p
        ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY c.id, p.category
)
SELECT
    cs.name          AS nombre,
    cs.email         AS email,
    cs.country       AS pais,
    cs.total_orders  AS total_orders,
    cs.total_revenue AS total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    cr.category      AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_ranking cr
    ON cr.customer_id = cs.customer_id
   AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de cada parte:

| CTE / Sección | Qué hace |
|---|---|
| `customer_stats` | Agrupa por cliente, calcula `total_orders`, `total_revenue` y filtra con `HAVING >= 3` órdenes completadas en los últimos 6 meses. |
| `category_ranking` | Agrupa por cliente + categoría, suma las cantidades y usa `ROW_NUMBER()` para rankear las categorías por volumen de compra dentro de cada cliente. |
| `SELECT` final | Une ambas CTEs quedándose solo con la categoría #1 (`rn = 1`) de cada cliente, calcula el `avg_order_value` y ordena por `total_revenue DESC` con `LIMIT 10`. |

> **Nota:** Si usas **PostgreSQL**, reemplaza `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` por `CURRENT_DATE - INTERVAL '6 months'`. Si usas **SQL Server**, usa `DATEADD(MONTH, -6, GETDATE())`.