# Claude Sonnet 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 12.506s | tokens_per_second: 168.5
- input_tokens: 223 | output_tokens: 2107
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
    -- Órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_stats AS (
    -- Métricas por cliente (≥ 3 órdenes completadas)
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_rank AS (
    -- Categoría más comprada por cliente (por unidades)
    SELECT
        co.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)

SELECT
    c.name                           AS nombre,
    c.email,
    c.country                        AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2)       AS total_revenue,
    ROUND(cs.avg_order_value, 2)     AS avg_order_value,
    cr.category                      AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c           ON c.id = cs.customer_id
LEFT JOIN category_rank cr ON cr.customer_id = cs.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Decisiones de diseño

1. **Evita duplicar el revenue:** las métricas (`total_orders`, `total_revenue`, `avg_order_value`) se calculan solo desde `orders`. Si hicieras el JOIN con `order_items` en la misma query, `orders.total` se repetiría por cada item e inflaría los números.
2. **Categoría más comprada en un CTE aparte:** usa `ROW_NUMBER()` para quedarse con una sola categoría por cliente. En caso de empate, desempata alfabéticamente, así el resultado es determinista.
3. **Filtro de 3+ órdenes:** el `HAVING` aplica solo a órdenes completadas dentro de los últimos 6 meses.

## Supuestos y adaptaciones

- **Dialecto:** está escrita para PostgreSQL. Para otros motores cambia lo siguiente:
  - **MySQL 8+:** `created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`
  - **SQL Server:** `created_at >= DATEADD(MONTH, -6, GETDATE())` y `SELECT TOP 10` en lugar de `LIMIT 10`
- **"Más comprada":** la medí por unidades (`quantity`). Si prefieres por gasto, cambia el `ORDER BY` del `ROW_NUMBER()` a `SUM(oi.quantity * oi.unit_price) DESC`.
- **Revenue:** uso `orders.total`. Si ese campo incluye envío o impuestos y quieres solo productos, usa `SUM(oi.quantity * oi.unit_price)` en un CTE separado.

## Índices recomendados

```sql
CREATE INDEX idx_orders_status_created ON orders (status, created_at) INCLUDE (customer_id, total);
CREATE INDEX idx_order_items_order ON order_items (order_id);
```