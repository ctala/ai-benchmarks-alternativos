# Claude Fable 5 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-fable-5`
- success: True  | final: 7.31 | quality: 9.34
- latency_total: 15.56s | tokens_per_second: 84.8
- input_tokens: 2 | output_tokens: 1320

## Respuesta completa

```sql
WITH ordenes_recientes AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas_cliente AS (
    -- Agregados por cliente
    SELECT
        customer_id,
        COUNT(*)            AS total_orders,
        SUM(total)          AS total_revenue,
        AVG(total)          AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_top AS (
    -- Categoría más comprada por cliente (por cantidad de unidades)
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            orr.customer_id,
            p.category,
            ROW_NUMBER() OVER (
                PARTITION BY orr.customer_id
                ORDER BY SUM(oi.quantity) DESC
            ) AS rn
        FROM ordenes_recientes orr
        JOIN order_items oi ON oi.order_id = orr.id
        JOIN products p     ON p.id = oi.product_id
        GROUP BY orr.customer_id, p.category
    ) ranked
    WHERE rn = 1
)

SELECT
    c.name                                  AS nombre,
    c.email,
    c.country                               AS pais,
    mc.total_orders,
    ROUND(mc.total_revenue, 2)              AS total_revenue,
    ROUND(mc.avg_order_value, 2)            AS avg_order_value,
    ct.categoria_mas_comprada
FROM metricas_cliente mc
JOIN customers c      ON c.id = mc.customer_id
LEFT JOIN categoria_top ct ON ct.customer_id = mc.customer_id
ORDER BY mc.total_revenue DESC
LIMIT 10;
```

**Notas sobre las decisiones tomadas:**

1. **CTEs separados** — `ordenes_recientes` se calcula una sola vez y se reutiliza para métricas y categoría top, evitando repetir el filtro de fecha/status.

2. **`HAVING COUNT(*) >= 3`** — el filtro de mínimo 3 órdenes se aplica *antes* del join con items, lo que reduce el trabajo de la query.

3. **Categoría más comprada** — la definí por **cantidad de unidades** (`SUM(oi.quantity)`). Si prefieres definirla por **revenue** (más gastado en esa categoría), cambia el `ORDER BY` dentro del window:
   ```sql
   ORDER BY SUM(oi.quantity * oi.unit_price) DESC
   ```

4. **`LEFT JOIN` en categoria_top** — por si existe alguna orden completada sin items (data sucia), el cliente igual aparece con categoría `NULL` en vez de desaparecer del ranking.

5. **Sintaxis PostgreSQL** — si usas MySQL, cambia el filtro de fecha a:
   ```sql
   o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
   ```

6. **Empates en categoría** — `ROW_NUMBER()` rompe empates arbitrariamente. Si quieres un desempate determinístico, agrega un segundo criterio: `ORDER BY SUM(oi.quantity) DESC, p.category ASC`.