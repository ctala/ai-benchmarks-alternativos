# Nemotron 3 Ultra 550B — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.49 | quality: 9.6
- latency_total: 10.094s | tokens_per_second: 68.5
- input_tokens: 160 | output_tokens: 691
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
    SELECT
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (SELECT max(created_at) FROM orders) - INTERVAL '6 months'
),
customer_agg AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM completed_orders co
    JOIN customers c ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),
top_category AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY co.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    ca.name,
    ca.email,
    ca.country,
    ca.total_orders,
    ca.total_revenue,
    ROUND(ca.avg_order_value, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_agg ca
LEFT JOIN top_category tc ON tc.customer_id = ca.id AND tc.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

**Notas:**
- Uso `max(created_at)` como ancla para "últimos 6 meses" (evita depender de `CURRENT_DATE` y hace la query reproducible).
- `categoria_mas_comprada` se define por **cantidad de unidades** (`SUM(oi.quantity)`). Si prefieres por revenue, cambia el `ORDER BY` del `ROW_NUMBER()` a `SUM(oi.quantity * oi.unit_price) DESC`.
- `LEFT JOIN` en `top_category` por si un cliente tuviera orders sin items (edge case).