# Nemotron 3 Ultra 550B (NIM) — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.53 | quality: 8.67
- latency_total: 34.468s | tokens_per_second: 27.2
- input_tokens: 160 | output_tokens: 936

## Respuesta completa

```sql
WITH recent_orders AS (
    -- Órdenes completadas en los últimos 6 meses (anclado a la fecha máxima real)
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (
          SELECT max(created_at) - INTERVAL '6 months' FROM orders
      ),
customer_agg AS (
    -- Agregados principales por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(ro.id) AS total_orders,
        SUM(ro.total) AS total_revenue,
        AVG(ro.total) AS avg_order_value
    FROM recent_orders ro
    JOIN customers c ON c.id = ro.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(ro.id) >= 3
),
category_rank AS (
    -- Categoría más comprada por cliente (por cantidad de unidades)
    SELECT 
        ca.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY ca.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customer_agg ca
    JOIN recent_orders ro ON ro.customer_id = ca.customer_id
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ca.customer_id, p.category
)
SELECT 
    ca.name,
    ca.email,
    ca.country,
    ca.total_orders,
    ca.total_revenue,
    ROUND(ca.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_agg ca
LEFT JOIN category_rank cr 
    ON cr.customer_id = ca.customer_id 
   AND cr.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

**Notas:**
- Ventana de 6 meses anclada a `max(created_at)` de `orders` → reproducible y sin depender de `NOW()`.
- `categoria_mas_comprada` definida por **cantidad de unidades** (`SUM(oi.quantity)`). Si prefieres por revenue, cambia el `ORDER BY` del `ROW_NUMBER()` a `SUM(oi.quantity * oi.unit_price) DESC`.
- `LEFT JOIN` en `category_rank` por si un cliente no tuviera items (poco probable con `completed`), pero mantiene la fila.