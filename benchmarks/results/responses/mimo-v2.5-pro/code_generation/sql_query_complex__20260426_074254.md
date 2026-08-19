# MiMo-V2.5 Pro — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.33 | quality: 9.52
- latency_total: 19.988s | tokens_per_second: 83.7
- input_tokens: 396 | output_tokens: 1672
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue (Últimos 6 Meses)

```sql
WITH customer_stats AS (
    -- Estadísticas generales del cliente
    SELECT 
        c.id            AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)  AS total_orders,
        SUM(o.total)          AS total_revenue,
        AVG(o.total)          AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_top_category AS (
    -- Categoría más comprada por cliente (por cantidad de items)
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p     ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    ROUND(cs.total_revenue, 2)   AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    ctc.category                 AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_top_category ctc 
       ON cs.customer_id = ctc.customer_id 
      AND ctc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

---

## Explicación paso a paso

```
┌─────────────────────────────────────────────────────────────┐
│  CTE 1: customer_stats                                      │
│  ───────────────────                                        │
│  • JOIN customers ↔ orders                                  │
│  • Filtra: status = 'completed' + últimos 6 meses           │
│  • Agrupa por cliente → total_orders, total_revenue, avg    │
│  • HAVING total_orders >= 3                                 │
├─────────────────────────────────────────────────────────────┤
│  CTE 2: customer_top_category                               │
│  ────────────────────────────                               │
│  • JOIN orders ↔ order_items ↔ products                     │
│  • Mismos filtros de fecha y status                         │
│  • Agrupa por cliente + categoría → SUM(quantity)           │
│  • ROW_NUMBER() → ranking de categorías por cliente         │
│  • rn = 1 → la categoría más comprada                       │
├─────────────────────────────────────────────────────────────┤
│  Query principal                                            │
│  ───────────────                                           │
│  • LEFT JOIN ambos CTEs por customer_id (rn=1)              │
│  • ORDER BY total_revenue DESC                              │
│  • LIMIT 10                                                 │
└─────────────────────────────────────────────────────────────┘
```

## Notas importantes

| Punto | Detalle |
|-------|---------|
| **`DATE_SUB`** | Compatible con MySQL. Para PostgreSQL usa `CURRENT_DATE - INTERVAL '6 months'` |
| **`ROW_NUMBER()`** | Si hay empate en cantidad entre categorías, elige **una sola** (la primera alfabéticamente). Usa `RANK()` si prefieres mostrar todas las empatadas |
| **`LEFT JOIN`** en categoría | Garantiza que el cliente aparezca aunque por algún motivo no tenga items registrados |
| **`ROUND(..., 2)`** | Formatea revenue y avg a 2 decimales |
| **`DISTINCT`** en `COUNT` | Protege contra posibles duplicados en el join |