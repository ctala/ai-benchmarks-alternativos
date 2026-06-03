# Claude Sonnet 4.6 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.37 | quality: 9.8
- latency_total: 26.604s | tokens_per_second: 68.1
- input_tokens: 3 | output_tokens: 1812
- judge_score: 5.0 | justificación: 

## Respuesta completa

## Query SQL — Top 10 Clientes por Revenue

```sql
WITH customer_stats AS (
    -- Métricas base por cliente (solo órdenes completadas, últimos 6 meses)
    SELECT
        c.id          AS customer_id,
        c.name        AS nombre,
        c.email,
        c.country     AS pais,
        COUNT(DISTINCT o.id)        AS total_orders,
        SUM(o.total)                AS total_revenue,
        AVG(o.total)                AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status     = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),

category_per_customer AS (
    -- Cantidad total comprada por cliente × categoría (mismo filtro de período)
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS qty_total,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON o.id    = oi.order_id
    JOIN products    p  ON p.id    = oi.product_id
    WHERE o.status     = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

SELECT
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    ROUND(cs.total_revenue::NUMERIC,    2) AS total_revenue,
    ROUND(cs.avg_order_value::NUMERIC,  2) AS avg_order_value,
    cp.category                            AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_per_customer cp
     ON cp.customer_id = cs.customer_id
    AND cp.rn          = 1          -- solo la categoría #1 por cliente
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

---

### Cómo funciona

| CTE | Qué hace |
|---|---|
| `customer_stats` | Agrega revenue, conteo y promedio por cliente. El `HAVING` aplica el mínimo de 3 órdenes. |
| `category_per_customer` | Rankea categorías por cantidad comprada usando `ROW_NUMBER()` particionado por cliente. |
| Query final | Une ambos CTEs tomando solo `rn = 1` (categoría top) y toma el TOP 10. |

---

### Notas importantes

**`categoria_mas_comprada`** — se calcula por **unidades (quantity)**. Si preferís por **revenue**, cambiá la línea del `ORDER BY` dentro del `ROW_NUMBER`:
```sql
-- Por revenue en lugar de cantidad:
ORDER BY SUM(oi.quantity * oi.unit_price) DESC
```

**Empates de categoría** — `ROW_NUMBER()` elige una arbitrariamente. Si querés exponer empates usá `RANK()` y ajustá el JOIN a `cp.rn <= 1` con `DISTINCT`.

**Dialecto SQL** — la query es estándar **PostgreSQL**. Ajustes por motor:

```sql
-- MySQL
AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
-- y quitar el ::NUMERIC cast, usar ROUND(valor, 2)

-- SQL Server
AND o.created_at >= DATEADD(MONTH, -6, GETDATE())
-- y reemplazar ::NUMERIC por CAST(valor AS DECIMAL(10,2))
```