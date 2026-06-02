# MiniMax M3 — code_generation/sql_query_complex

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.76 | quality: 9.8
- latency_total: 84.269s | tokens_per_second: 31.7
- input_tokens: 316 | output_tokens: 2673
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Query SQL — Top 10 clientes por revenue (últimos 6 meses)

```sql
WITH 
-- 1) Órdenes completadas en los últimos 6 meses
completed_orders AS (
  SELECT 
    o.id,
    o.customer_id,
    o.created_at
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

-- 2) Revenue por orden calculado desde los items (más fiable que orders.total)
order_revenue AS (
  SELECT 
    co.id,
    co.customer_id,
    SUM(oi.quantity * oi.unit_price) AS revenue
  FROM completed_orders co
  JOIN order_items oi ON oi.order_id = co.id
  GROUP BY co.id, co.customer_id
),

-- 3) Métricas agregadas por cliente (con filtro de mínimo 3 órdenes)
customer_summary AS (
  SELECT
    c.id,
    c.name,
    c.email,
    c.country,
    COUNT(orv.id)            AS total_orders,
    SUM(orv.revenue)         AS total_revenue,
    AVG(orv.revenue)         AS avg_order_value
  FROM customers c
  JOIN order_revenue orv ON orv.customer_id = c.id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(orv.id) >= 3
),

-- 4) Cantidad comprada por categoría por cliente
category_purchases AS (
  SELECT
    co.customer_id,
    p.category,
    SUM(oi.quantity) AS qty
  FROM completed_orders co
  JOIN order_items oi ON oi.order_id = co.id
  JOIN products p     ON p.id = oi.product_id
  GROUP BY co.customer_id, p.category
),

-- 5) Ranking de categorías por cliente (1 = la más comprada)
ranked_categories AS (
  SELECT
    customer_id,
    category,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY qty DESC
    ) AS rnk
  FROM category_purchases
)

-- 6) Resultado final
SELECT
  cs.name,
  cs.email,
  cs.country,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  rc.category AS categoria_mas_comprada
FROM customer_summary cs
JOIN ranked_categories rc
  ON rc.customer_id = cs.id
 AND rc.rnk = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Notas de diseño

| Decisión | Motivo |
|---|---|
| **CTEs separados** | Hace el flujo legible: filtrar → agregar → rankear → unir. |
| **Revenue desde `order_items`** | Evita inconsistencias si `orders.total` no coincide con la suma de los items. Si prefieres usar `orders.total`, sustituye `SUM(oi.quantity * oi.unit_price)` por `o.total` y agrupa por `o.id`. |
| **Categorización por cantidad (`SUM(quantity)`)** | Interpretación literal de "más comprada". Si quieres **categoría con mayor gasto**, cambia `qty` por `SUM(oi.quantity * oi.unit_price)`. |
| **`ROW_NUMBER` en vez de `RANK`** | Evita empates que devuelvan varias filas por cliente. Si hay empate entre dos categorías, se queda con una sola (cualquiera de las empatadas). |
| **Filtro de ≥3 órdenes en `HAVING`** | Se evalúa antes del `LIMIT 10`, así que el top 10 es realmente los que más gastan *cumpliendo* la condición. |
| **`INNER JOIN` con `ranked_categories`** | Garantiza que todo cliente del top tenga al menos una categoría (improbable fallar, pero evita nulos en el resultado). |

## Adaptación por motor

- **MySQL**: cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`.
- **SQL Server**: usa `DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))`.
- **Oracle**: usa `ADD_MONTHS(TRUNC(SYSDATE), -6)`.