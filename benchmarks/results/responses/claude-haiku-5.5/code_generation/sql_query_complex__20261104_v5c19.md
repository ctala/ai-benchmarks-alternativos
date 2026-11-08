# Claude Haiku 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.61 | quality: 9.32
- latency_total: 8.39s | tokens_per_second: 255.8
- input_tokens: 223 | output_tokens: 2146
- judge_score: 4.8 | justificación: 

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

```sql
WITH pedidos_recientes AS (
    -- Pedidos completados de los últimos 6 meses
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
totales_cliente AS (
    -- Métricas por cliente; solo los que tienen al menos 3 pedidos
    SELECT
        customer_id,
        COUNT(*)                  AS total_orders,
        SUM(total)                AS total_revenue,
        AVG(total)                AS avg_order_value
    FROM pedidos_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
categoria_por_cliente AS (
    -- Unidades compradas por categoría y cliente, ranking por cliente
    SELECT
        pr.customer_id,
        p.category,
        SUM(oi.quantity) AS unidades,
        ROW_NUMBER() OVER (
            PARTITION BY pr.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM pedidos_recientes pr
    JOIN order_items oi ON oi.order_id = pr.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY pr.customer_id, p.category
)
SELECT
    c.name                            AS nombre,
    c.email                           AS email,
    c.country                         AS pais,
    tc.total_orders,
    ROUND(tc.total_revenue, 2)        AS total_revenue,
    ROUND(tc.avg_order_value, 2)      AS avg_order_value,
    cpc.category                      AS categoria_mas_comprada
FROM totales_cliente tc
JOIN customers c ON c.id = tc.customer_id
LEFT JOIN categoria_por_cliente cpc
       ON cpc.customer_id = tc.customer_id
      AND cpc.rn = 1
ORDER BY tc.total_revenue DESC
LIMIT 10;
```

**Notas:**

- **Sintaxis de fecha:** el filtro usa `CURRENT_DATE - INTERVAL '6 months'` (PostgreSQL). En MySQL sería `CURDATE() - INTERVAL 6 MONTH`, y en SQL Server `DATEADD(MONTH, -6, GETDATE())`.
- **Revenue:** se toma `orders.total`. Si ese campo no siempre coincide con la suma de `order_items.quantity * unit_price`, habría que calcular el revenue desde `order_items`.
- **Categoría más comprada:** se define por unidades (`SUM(quantity)`). Si prefieres por gasto, cambia el ORDER BY a `SUM(oi.quantity * oi.unit_price)`. En caso de empate, se elige alfabéticamente.
- **Ventana de 6 meses:** el filtro de fecha se aplica tanto a las métricas como al umbral de 3 pedidos, así que solo cuentan pedidos de ese periodo.