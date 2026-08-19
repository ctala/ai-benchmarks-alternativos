# MiMo V2.5-Pro (Xiaomi) — code_generation/sql_query_complex

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 32.892s | tokens_per_second: 62.3
- input_tokens: 396 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

## Query SQL — Top 10 Clientes por Revenue (Últimos 6 Meses)

```sql
WITH order_totals AS (
    -- 1) Calcula el revenue de cada orden desde order_items
    SELECT
        o.id            AS order_id,
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS order_revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY o.id, o.customer_id
),

customer_stats AS (
    -- 2) Agrega a nivel cliente: totales y promedio
    SELECT
        customer_id,
        COUNT(*)            AS total_orders,
        SUM(order_revenue)  AS total_revenue,
        AVG(order_revenue)  AS avg_order_value
    FROM order_totals
    GROUP BY customer_id
    HAVING COUNT(*) >= 3                        -- mínimo 3 órdenes
),

customer_top_category AS (
    -- 3) Ranking de categorías más compradas por cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS qty_bought,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p     ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)

-- 4) Resultado final
SELECT
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2)   AS avg_order_value,
    tc.category                    AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c             ON c.id = cs.customer_id
JOIN customer_top_category tc ON tc.customer_id = cs.customer_id
                              AND tc.rn = 1          -- solo la categoría #1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

---

### ¿Cómo funciona paso a paso?

| CTE | Propósito |
|---|---|
| **`order_totals`** | Calcula el revenue real de cada orden (`quantity × unit_price`) evitando duplicados por el