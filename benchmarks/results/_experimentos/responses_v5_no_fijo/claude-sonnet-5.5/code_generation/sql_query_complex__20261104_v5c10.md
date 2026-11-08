# Claude Sonnet 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.18 | quality: 9.6
- latency_total: 10.339s | tokens_per_second: 166.3
- input_tokens: 223 | output_tokens: 1719
- judge_score: 5.0 | justificación: 

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
WITH completed_orders AS (
    -- Órdenes completadas en los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_stats AS (
    -- Métricas por cliente (sin hacer JOIN a order_items para no duplicar totales)
    SELECT
        customer_id,
        COUNT(*)                       AS total_orders,
        SUM(total)                     AS total_revenue,
        ROUND(AVG(total), 2)           AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_ranking AS (
    -- Categoría más comprada por cliente (por unidades)
    SELECT
        co.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category   -- desempate alfabético
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)

SELECT
    c.name                  AS nombre,
    c.email                 AS email,
    c.country               AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category             AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c           ON c.id = cs.customer_id
LEFT JOIN category_ranking cr
       ON cr.customer_id = cs.customer_id
      AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Decisiones de diseño**

- **Evita duplicar totales:** `total_revenue` y `avg_order_value` se calculan solo con `orders`. Si hicieras JOIN con `order_items` antes de sumar `orders.total`, cada orden se contaría una vez por ítem.
- **Categoría más comprada:** la definí por unidades (`SUM(quantity)`). Si prefieres por dinero, cambia el `ORDER BY` a `SUM(oi.quantity * oi.unit_price) DESC`.
- **Filtro de 3 órdenes:** se aplica dentro de los últimos 6 meses. Si quieres que sean 3 órdenes completadas en toda la historia del cliente, avísame y ajusto la query.
- **`LEFT JOIN` en categoría:** por si algún cliente no tuviera ítems asociados, no se pierde de la lista.

**Adaptaciones por motor**

- **MySQL:** usa `created_at >= CURDATE() - INTERVAL 6 MONTH`.
- **SQL Server:** usa `DATEADD(MONTH, -6, GETDATE())` y `SELECT TOP 10` en lugar de `LIMIT`.

**Índices recomendados:** `orders(status, created_at, customer_id)` y `order_items(order_id)`.