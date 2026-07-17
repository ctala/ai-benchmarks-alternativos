# MiMo-V2.5 (omnimodal) — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 8.02 | quality: 9.6
- latency_total: 101.736s | tokens_per_second: 20.1
- input_tokens: 169 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue (Últimos 6 meses)

## Enfoque: CTEs (Common Table Expressions)

```sql
-- =====================================================================
-- Top 10 clientes por revenue (últimos 6 meses)
-- Solo clientes con al menos 3 ordenes completadas
-- =====================================================================

WITH customer_metrics AS (
    -- ═══════════════════════════════════════════════─
    -- Agrupamos métricas por cliente (solo completadas)
    -- ═══════════════════════════════════════════════─
    SELECT
        c.id                     AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)     AS total_orders,
        SUM(o.total)             AS total_revenue,
        AVG(o.total)             AS avg_order_value
    FROM customers c
    INNER JOIN orders o
        ON c.id = o.customer_id
    WHERE o.status       = 'completed'
      AND o.created_at  >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3        -- ⬅ mín. 3 ordenes
),

category_ranking AS (
    -- ═══════════════════════════════════════════════─
    -- Ranking de categorías por cantidad comprada
    -- por cada cliente
    -- ═══════════════════════════════════════════════─
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity)              AS total_bought,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        )                             AS rn
    FROM order_items oi
    INNER JOIN orders  o ON oi.order_id  = o.id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status      = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

-- ═══════════════════════════════════════════════════
--  Resultado final: métricas + categoría más comprada
-- ═══════════════════════════════════════════════════
SELECT
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    ROUND(cm.total_revenue, 2)   AS total_revenue,
    ROUND(cm.avg_order_value, 2) AS avg_order_value,
    cr.category                  AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_ranking cr
    ON cm.customer_id = cr.customer_id
   AND cr.rn = 1                          -- ⬅ solo la #1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

---

## Detalle paso a paso

```
┌─────────────────────────────────────────────────────────┐
│                   FLUJO DE LA QUERY                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1️⃣  customer_metrics (CTE 1)                           │
│  ┌───────────────────────────────────────────┐          │
│  │ • JOIN orders → customers                 │          │
│  │ • FILTRO: status = 'completed'            │          │
│  │ • FILTRO: últimos 6 meses                 │          │
│  │ • GROUP BY: customer_id                   │          │
│  │ • HAVING: COUNT >= 3 ordenes              │          │
│  │ • CALCULA: cnt_orders, revenue, avg_value  │          │
│  └───────────────────────────────────────────┘          │
│         │                                               │
│         ▼                                               │
│  2️⃣  category_ranking (CTE 2)                           │
│  ┌───────────────────────────────────────────┐          │
│  │ • JOIN order_items → orders → products    │          │
│  │ • FILTRO: status = 'completed'            │          │
│  │ • FILTRO: últimos 6 meses                 │          │
│  │ • GROUP BY: customer_id, category         │          │
│  │ • ROW_NUMBER() para ranking por cantidad  │          │
│  └───────────────────────────────────────────┘          │
│         │                                               │
│         ▼                                               │