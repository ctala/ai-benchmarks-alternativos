# Claude Haiku 5.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.63 | quality: 9.32
- latency_total: 7.231s | tokens_per_second: 259.0
- input_tokens: 223 | output_tokens: 1873
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

Esta query usa **PostgreSQL**. Asumo que `orders.total` es el importe de la orden, que la categoría más comprada se mide por unidades, y que el empate en la categoría se resuelve alfabéticamente.

```sql
WITH ordenes_completadas AS (
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
),
stats_cliente AS (
    SELECT
        customer_id,
        COUNT(*)              AS total_orders,
        SUM(total)            AS total_revenue,
        AVG(total)            AS avg_order_value
    FROM ordenes_completadas
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
categoria_por_cliente AS (
    SELECT
        oc.customer_id,
        p.category,
        SUM(oi.quantity) AS unidades,
        ROW_NUMBER() OVER (
            PARTITION BY oc.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM ordenes_completadas oc
    JOIN order_items oi ON oi.order_id = oc.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY oc.customer_id, p.category
)
SELECT
    c.name           AS nombre,
    c.email,
    c.country        AS pais,
    sc.total_orders,
    sc.total_revenue,
    ROUND(sc.avg_order_value, 2) AS avg_order_value,
    cat.category     AS categoria_mas_comprada
FROM stats_cliente sc
JOIN customers c ON c.id = sc.customer_id
LEFT JOIN categoria_por_cliente cat
       ON cat.customer_id = sc.customer_id
      AND cat.rn = 1
ORDER BY sc.total_revenue DESC
LIMIT 10;
```

**Notas:**

- **Ventana de 6 meses:** en MySQL usa `created_at >= CURDATE() - INTERVAL 6 MONTH`. En SQL Server usa `created_at >= DATEADD(MONTH, -6, GETDATE())`.
- **Revenue:** si `orders.total` incluye envío o impuestos y quieres solo el valor de los productos, calcula `SUM(oi.quantity * oi.unit_price)` en lugar de `SUM(o.total)`.
- **Categoría más comprada:** se calcula por unidades. Si prefieres por importe, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en `categoria_por_cliente`.
- **Filtro de órdenes:** el `HAVING COUNT(*) >= 3` se aplica sobre órdenes completadas de los últimos 6 meses. Si el criterio de 3 órdenes debe ser histórico, habría que ajustarlo.