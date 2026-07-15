# Claude Fable 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 17.318s | tokens_per_second: 76.9
- input_tokens: 221 | output_tokens: 1332
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

stats_clientes AS (
    -- Métricas agregadas por cliente
    SELECT
        customer_id,
        COUNT(*)            AS total_orders,
        SUM(total)          AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_top AS (
    -- Categoría más comprada por cliente (por revenue de items)
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            orr.customer_id,
            p.category,
            SUM(oi.quantity * oi.unit_price) AS revenue_categoria,
            ROW_NUMBER() OVER (
                PARTITION BY orr.customer_id
                ORDER BY SUM(oi.quantity * oi.unit_price) DESC
            ) AS rn
        FROM ordenes_recientes orr
        JOIN order_items oi ON oi.order_id = orr.id
        JOIN products p     ON p.id = oi.product_id
        GROUP BY orr.customer_id, p.category
    ) ranked
    WHERE rn = 1
)

SELECT
    c.name              AS nombre,
    c.email,
    c.country           AS pais,
    sc.total_orders,
    sc.total_revenue,
    sc.avg_order_value,
    ct.categoria_mas_comprada
FROM stats_clientes sc
JOIN customers c      ON c.id = sc.customer_id
LEFT JOIN categoria_top ct ON ct.customer_id = sc.customer_id
ORDER BY sc.total_revenue DESC
LIMIT 10;
```

### Notas sobre la query

1. **`ordenes_recientes`**: filtro base (status y fecha) en un solo lugar para no repetirlo y garantizar consistencia entre los CTEs.

2. **`stats_clientes`**: el `HAVING COUNT(*) >= 3` aplica el mínimo de 3 órdenes completadas.

3. **`categoria_top`**: uso `ROW_NUMBER()` para quedarme con la categoría de mayor revenue por cliente. Si prefieres decidir por **cantidad de unidades** en vez de revenue, cambia el `ORDER BY` a `SUM(oi.quantity) DESC`.

4. **`LEFT JOIN` en categoria_top**: por si algún cliente tiene órdenes sin items (dato inconsistente), no lo excluye del resultado.

### Ajustes según tu motor de BD

- **MySQL**: cambia el intervalo a `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`.
- **SQL Server**: usa `DATEADD(MONTH, -6, GETDATE())` y reemplaza `LIMIT 10` por `SELECT TOP 10`.
- **Empates en categoría**: `ROW_NUMBER()` elige una arbitrariamente; si quieres desempate determinista, agrega un segundo criterio como `p.category ASC` al `ORDER BY` de la ventana.