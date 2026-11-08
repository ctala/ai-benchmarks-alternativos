# Claude Opus 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.25 | quality: 10.0
- latency_total: 21.516s | tokens_per_second: 122.2
- input_tokens: 223 | output_tokens: 2629
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

Esta query está escrita para **PostgreSQL**. Al final indico qué cambiar para otros motores.

```sql
WITH completed_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_stats AS (
    -- Métricas por cliente (solo clientes con 3 o más órdenes)
    SELECT
        customer_id,
        COUNT(*)                         AS total_orders,
        SUM(total)                       AS total_revenue,
        ROUND(AVG(total)::numeric, 2)    AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

top_customers AS (
    SELECT *
    FROM customer_stats
    ORDER BY total_revenue DESC
    LIMIT 10
),

category_ranking AS (
    -- Categoría más comprada por cliente (por unidades)
    SELECT
        co.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC,
                     SUM(oi.quantity * oi.unit_price) DESC,  -- desempate por gasto
                     p.category                              -- desempate final
        ) AS rn
    FROM completed_orders co
    JOIN top_customers tc ON tc.customer_id = co.customer_id
    JOIN order_items oi   ON oi.order_id = co.id
    JOIN products p       ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)

SELECT
    c.name               AS nombre,
    c.email,
    c.country            AS pais,
    tc.total_orders,
    tc.total_revenue,
    tc.avg_order_value,
    cr.category          AS categoria_mas_comprada
FROM top_customers tc
JOIN customers c             ON c.id = tc.customer_id
LEFT JOIN category_ranking cr
       ON cr.customer_id = tc.customer_id
      AND cr.rn = 1
ORDER BY tc.total_revenue DESC;
```

## Decisiones de diseño

1. **Métricas y categoría se calculan por separado.** Si se hace `JOIN` de `orders` con `order_items` antes de agregar, cada orden se repite una vez por cada ítem. Eso inflaría `SUM(total)` y `COUNT(*)`. Por eso las métricas salen de `orders` y la categoría se calcula en otro CTE.

2. **La categoría se calcula solo para los 10 clientes finales**, no para todos. Así la query es más eficiente.

3. **"Categoría más comprada" se mide por unidades** (`SUM(quantity)`). Si prefieres medirla por dinero gastado, invierte el orden de los dos criterios en el `ORDER BY` del `ROW_NUMBER()`.

4. **Empates:** el `ROW_NUMBER()` garantiza una sola categoría por cliente, con un desempate determinista.

5. **Interpretación del filtro de 3 órdenes:** las 3 órdenes completadas deben estar dentro de los últimos 6 meses. Si querías 3 completadas en todo el historial, habría que filtrar aparte sobre `orders` sin restricción de fecha.

6. **Se usa `LEFT JOIN` con la categoría** para que un cliente aparezca aunque, por alguna inconsistencia, tenga órdenes sin ítems.

## Adaptaciones para otros motores

| Motor | Cambios |
|---|---|
| **MySQL 8+** | `CURRENT_DATE - INTERVAL 6 MONTH` y quitar el `::numeric` |
| **SQL Server** | `DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))`, `SELECT TOP 10` en lugar de `LIMIT 10` (en SQL Server un `ORDER BY` dentro de un CTE exige `TOP`), y `CAST(AVG(total) AS DECIMAL(12,2))` |
| **BigQuery** | `DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)` y quitar el `::numeric` |

## Índices recomendados

Para que la query rinda bien con volumen:

```sql
CREATE INDEX idx_orders_status_created ON orders (status, created_at, customer_id);
CREATE INDEX idx_order_items_order     ON order_items (order_id, product_id);
```