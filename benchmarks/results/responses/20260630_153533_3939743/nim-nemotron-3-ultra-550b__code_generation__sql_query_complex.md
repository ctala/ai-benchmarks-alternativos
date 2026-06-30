# Nemotron 3 Ultra 550B (NIM) — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 80.478s | tokens_per_second: 13.6
- input_tokens: 160 | output_tokens: 1091

## Respuesta completa

```sql
WITH filtered_orders AS (
    -- Órdenes completadas en los últimos 6 meses (anclado a la fecha máxima real)
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (
          SELECT max(created_at) - INTERVAL '6 months' FROM orders
      ),
customer_aggregates AS (
    -- Métricas base por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT fo.order_id) AS total_orders,
        SUM(fo.total) AS total_revenue,
        AVG(fo.total) AS avg_order_value
    FROM filtered_orders fo
    JOIN customers c ON c.id = fo.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT fo.order_id) >= 3
),
category_rank AS (
    -- Categoría más comprada por cliente (por cantidad de unidades)
    SELECT 
        ca.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY ca.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customer_aggregates ca
    JOIN filtered_orders fo ON fo.customer_id = ca.customer_id
    JOIN order_items oi ON oi.order_id = fo.order_id
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
FROM customer_aggregates ca
LEFT JOIN category_rank cr 
    ON cr.customer_id = ca.customer_id 
   AND cr.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

### Notas clave:
1. **Ventana de 6 meses**: Se ancla a `max(created_at)` de la tabla `orders` para que sea reproducible y no dependa de `NOW()`.
2. **Revenue**: Usa `orders.total` (asumiendo que es el monto final de la orden). Si prefieres recalcular desde `order_items`, cambia `SUM(fo.total)` por `SUM(oi.quantity * oi.unit_price)` en `customer_aggregates` y añade el join correspondiente.
3. **Categoria más comprada**: Se define por **cantidad de unidades** (`SUM(oi.quantity)`). Si quieres por revenue, cámbialo a `SUM(oi.quantity * oi.unit_price)`.
4. **Empates en categoría**: `ROW_NUMBER()` elige uno arbitrario si hay empate. Si quieres ver todos los empatados, usa `RANK()` y filtra `WHERE rk = 1` (podría devolver varias filas por cliente).
5. **Compatibilidad**: Sintaxis estándar PostgreSQL / MySQL 8+ / SQL Server / BigQuery / Snowflake.