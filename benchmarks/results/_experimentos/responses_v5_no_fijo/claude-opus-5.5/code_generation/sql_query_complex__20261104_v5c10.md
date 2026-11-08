# Claude Opus 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 21.64s | tokens_per_second: 123.8
- input_tokens: 223 | output_tokens: 2679
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

# Top 10 clientes por revenue (últimos 6 meses)

```sql
WITH completed_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

top_customers AS (
    -- Métricas por cliente, filtrando los que tienen al menos 3 órdenes
    SELECT
        customer_id,
        COUNT(*)    AS total_orders,
        SUM(total)  AS total_revenue,
        AVG(total)  AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
    ORDER BY total_revenue DESC
    LIMIT 10
),

category_ranking AS (
    -- Categoría más comprada por cliente (solo para el top 10)
    SELECT
        co.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC,                    -- criterio principal: unidades
                     SUM(oi.quantity * oi.unit_price) DESC,    -- desempate: gasto
                     p.category                                -- desempate final: alfabético
        ) AS rn
    FROM completed_orders co
    JOIN top_customers tc ON tc.customer_id = co.customer_id
    JOIN order_items oi   ON oi.order_id   = co.id
    JOIN products p       ON p.id          = oi.product_id
    GROUP BY co.customer_id, p.category
)

SELECT
    c.name                       AS nombre,
    c.email,
    c.country                    AS pais,
    tc.total_orders,
    ROUND(tc.total_revenue, 2)   AS total_revenue,
    ROUND(tc.avg_order_value, 2) AS avg_order_value,
    cr.category                  AS categoria_mas_comprada
FROM top_customers tc
JOIN customers c            ON c.id = tc.customer_id
LEFT JOIN category_ranking cr
       ON cr.customer_id = tc.customer_id
      AND cr.rn = 1
ORDER BY tc.total_revenue DESC;
```

## Decisiones de diseño

1. **Revenue = `orders.total`**: se usa el total de la orden. Si `total` incluye impuestos o envío y quieres solo el valor de productos, usa `SUM(oi.quantity * oi.unit_price)`.
2. **"Categoría más comprada" = más unidades** (`SUM(quantity)`). Si prefieres la categoría en la que más gastó, cambia el orden del `ROW_NUMBER()` para poner primero `SUM(oi.quantity * oi.unit_price)`.
3. **Las 3 órdenes mínimas se cuentan dentro de la ventana de 6 meses.** Si la regla es "3 órdenes completadas en toda su historia", hay que separar ese filtro en otro CTE.
4. **El top 10 se calcula antes que la categoría**, así el `ROW_NUMBER()` solo procesa 10 clientes en lugar de todos.
5. **`LEFT JOIN` en categoría**: si una orden no tuviera items, el cliente sigue apareciendo (con `NULL` en la categoría).
6. **Empates**: el `ROW_NUMBER()` tiene desempates explícitos para que el resultado sea determinista.

## Adaptaciones según el motor

La query está escrita para **PostgreSQL**. Para otros motores:

| Motor | Fecha | Límite |
|---|---|---|
| **MySQL 8+** | `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` | `LIMIT 10` |
| **SQL Server** | `o.created_at >= DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))` | `SELECT TOP 10 ...` (y quitar `LIMIT`) |
| **BigQuery** | `o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)` | `LIMIT 10` |

En PostgreSQL, si `total` es de tipo `double precision`, `ROUND(x, 2)` da error. En ese caso usa `ROUND(tc.total_revenue::numeric, 2)`.

## Índices recomendados

```sql
CREATE INDEX idx_orders_status_created ON orders (status, created_at, customer_id);
CREATE INDEX idx_order_items_order     ON order_items (order_id, product_id);
```