# Kimi K3 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.87 | quality: 9.8
- latency_total: 69.927s | tokens_per_second: 36.0
- input_tokens: 236 | output_tokens: 2518
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí está la query (sintaxis PostgreSQL, con notas para otros motores abajo):

```sql
WITH ordenes_validas AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),
stats_clientes AS (
    -- Métricas por cliente, filtrando los que tienen 3+ órdenes
    SELECT
        customer_id,
        COUNT(*)             AS total_orders,
        SUM(total)           AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM ordenes_validas
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
categorias_cliente AS (
    -- Ranking de categorías por cliente (por unidades compradas)
    SELECT
        ov.customer_id,
        p.category,
        SUM(oi.quantity) AS unidades,
        ROW_NUMBER() OVER (
            PARTITION BY ov.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM ordenes_validas ov
    JOIN order_items oi ON oi.order_id = ov.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY ov.customer_id, p.category
)
SELECT
    c.name        AS nombre,
    c.email,
    c.country     AS pais,
    sc.total_orders,
    sc.total_revenue,
    sc.avg_order_value,
    cc.category   AS categoria_mas_comprada
FROM stats_clientes sc
JOIN customers c ON c.id = sc.customer_id
LEFT JOIN categorias_cliente cc
       ON cc.customer_id = sc.customer_id
      AND cc.rn = 1
ORDER BY sc.total_revenue DESC
LIMIT 10;
```

**Cómo funciona:**

1. `ordenes_validas`: filtra una sola vez las órdenes completadas de los últimos 6 meses; el resto de CTEs reutilizan este filtro.
2. `stats_clientes`: calcula totales por cliente y aplica el requisito de mínimo 3 órdenes con `HAVING COUNT(*) >= 3`.
3. `categorias_cliente`: usa `ROW_NUMBER()` para rankear las categorías de cada cliente por unidades compradas; el `rn = 1` en el join final toma la más comprada.

**Decisiones de diseño (ajústalas según tu caso):**

- **"Más comprada" por unidades**: usé `SUM(quantity)`. Si prefieres por revenue, cambia a `SUM(oi.quantity * oi.unit_price)` en el `ORDER BY` del window function.
- **Empates en categoría**: `ROW_NUMBER()` elige una arbitrariamente. Si quieres manejar empates explícitamente, usa `DENSE_RANK()` o agrega un criterio de desempate (ej: `ORDER BY SUM(oi.quantity) DESC, p.category`).
- **LEFT JOIN** a categorías por si algún cliente no tuviera items registrados (caso borde), así no pierdes la fila.

**Adaptaciones por motor:**

| Motor | Fecha (6 meses) | Top 10 |
|---|---|---|
| PostgreSQL | `NOW() - INTERVAL '6 months'` | `LIMIT 10` |
| MySQL 8+ | `DATE_SUB(NOW(), INTERVAL 6 MONTH)` | `LIMIT 10` |
| SQL Server | `DATEADD(MONTH, -6, GETDATE())` | `SELECT TOP 10` |
| Oracle | `ADD_MONTHS(SYSDATE, -6)` | `FETCH FIRST 10 ROWS ONLY` |

Si estás en MySQL 5.7 (sin CTEs ni window functions), avísame y te escribo la versión con subqueries anidadas.