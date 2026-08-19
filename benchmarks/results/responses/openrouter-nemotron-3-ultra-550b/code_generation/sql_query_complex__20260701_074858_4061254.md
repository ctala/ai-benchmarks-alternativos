# Nemotron 3 Ultra 550B — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 9.544s | tokens_per_second: 100.7
- input_tokens: 160 | output_tokens: 961

## Respuesta completa

```sql
WITH 
-- 1. Órdenes completadas en los últimos 6 meses (anclado a la fecha máxima para reproducibilidad)
filtered_orders AS (
    SELECT 
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (SELECT max(created_at) FROM orders) - INTERVAL '6 months'
),

-- 2. Agregados por cliente (filtro mínimo 3 órdenes)
customer_agg AS (
    SELECT 
        fo.customer_id,
        COUNT(fo.id) AS total_orders,
        SUM(fo.total) AS total_revenue,
        AVG(fo.total) AS avg_order_value
    FROM filtered_orders fo
    GROUP BY fo.customer_id
    HAVING COUNT(fo.id) >= 3
),

-- 3. Categoría más comprada por cliente (basado en cantidad de items)
category_rank AS (
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY fo.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM filtered_orders fo
    JOIN order_items oi ON oi.order_id = fo.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY fo.customer_id, p.category
)

-- 4. Resultado final
SELECT 
    c.name,
    c.email,
    c.country,
    ca.total_orders,
    ca.total_revenue,
    ROUND(ca.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_agg ca
JOIN customers c ON c.id = ca.customer_id
LEFT JOIN category_rank cr ON cr.customer_id = ca.customer_id AND cr.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

### Notas clave:
1. **Ventana de 6 meses**: Usa `max(created_at)` de la tabla `orders` en lugar de `NOW()` para que sea determinista y funcione en réplicas/analytics.
2. **Categoria más comprada**: Se calcula sumando `quantity` de `order_items` (no revenue). Si prefieres por revenue, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en el CTE `category_rank`.
3. **LEFT JOIN en category_rank**: Por si un cliente tiene órdenes pero sin items (edge case), no se pierda el cliente.
4. **Performance**: Índices recomendados:
   - `orders(status, created_at, customer_id)`
   - `order_items(order_id, product_id)`
   - `products(id, category)`