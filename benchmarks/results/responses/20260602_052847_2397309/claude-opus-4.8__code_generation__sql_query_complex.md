# Claude Opus 4.8 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.38 | quality: 10.0
- latency_total: 17.082s | tokens_per_second: 85.5
- input_tokens: 221 | output_tokens: 1461
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue

```sql
WITH ordenes_completadas AS (
    -- Filtramos órdenes completadas de los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas_cliente AS (
    -- Calculamos métricas agregadas por cliente
    SELECT
        oc.customer_id,
        COUNT(DISTINCT oc.id)        AS total_orders,
        SUM(oc.total)                AS total_revenue,
        AVG(oc.total)                AS avg_order_value
    FROM ordenes_completadas oc
    GROUP BY oc.customer_id
    HAVING COUNT(DISTINCT oc.id) >= 3   -- Al menos 3 órdenes completadas
),

categoria_top AS (
    -- Determinamos la categoría más comprada por cliente (por cantidad)
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            oc.customer_id,
            p.category,
            SUM(oi.quantity) AS total_cantidad,
            ROW_NUMBER() OVER (
                PARTITION BY oc.customer_id
                ORDER BY SUM(oi.quantity) DESC
            ) AS rn
        FROM ordenes_completadas oc
        JOIN order_items oi ON oi.order_id = oc.id
        JOIN products p     ON p.id = oi.product_id
        GROUP BY oc.customer_id, p.category
    ) ranked
    WHERE rn = 1
)

SELECT
    c.name                          AS nombre,
    c.email,
    c.country                       AS pais,
    mc.total_orders,
    mc.total_revenue,
    ROUND(mc.avg_order_value, 2)    AS avg_order_value,
    ct.categoria_mas_comprada
FROM metricas_cliente mc
JOIN customers c    ON c.id = mc.customer_id
JOIN categoria_top ct ON ct.customer_id = mc.customer_id
ORDER BY mc.total_revenue DESC
LIMIT 10;
```

## Explicación de cada CTE

| CTE | Propósito |
|-----|-----------|
| **ordenes_completadas** | Filtra solo órdenes `completed` de los últimos 6 meses. Lo aislamos para reutilizarlo y mantener consistencia. |
| **metricas_cliente** | Agrega `total_orders`, `total_revenue` y `avg_order_value`. El `HAVING` aplica el filtro de **≥ 3 órdenes**. |
| **categoria_top** | Usa `ROW_NUMBER()` para sacar la categoría más comprada (por cantidad) de cada cliente, quedándonos solo con `rn = 1`. |

## Notas importantes

**1. Sintaxis de fechas según el motor:**

```sql
-- PostgreSQL (la del ejemplo)
o.created_at >= CURRENT_DATE - INTERVAL '6 months'

-- MySQL
o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)

-- SQL Server
o.created_at >= DATEADD(MONTH, -6, GETDATE())
```

**2. Revenue desde `orders.total` vs `order_items`:**
Usé `orders.total` porque ya tienes esa columna. Si prefieres calcular el revenue real desde los items (por si `total` incluye envíos/descuentos), cambia el cálculo a:

```sql
SUM(oi.quantity * oi.unit_price)
```

**3. Empates en categoría:**
Si un cliente tiene empate en categorías, `ROW_NUMBER()` elige una arbitrariamente. Si quieres ver **todas** las empatadas, usa `RANK()` en su lugar (pero podrías obtener más de una fila por cliente).

¿Quieres que la adapte a un motor específico o que el revenue se calcule desde `order_items`?