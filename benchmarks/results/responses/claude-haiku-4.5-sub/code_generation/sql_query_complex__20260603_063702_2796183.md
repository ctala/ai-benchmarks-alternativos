# Claude Haiku 4.5 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.72 | quality: 9.8
- latency_total: 14.35s | tokens_per_second: 170.1
- input_tokens: 10 | output_tokens: 2441
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Query SQL - Top 10 Clientes por Revenue

Aquí está la query usando **CTEs** (Common Table Expressions) para máxima claridad:

```sql
WITH last_6_months_orders AS (
  -- Filtra órdenes completadas en los últimos 6 meses
  SELECT *
  FROM orders
  WHERE status = 'completed'
    AND created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),
customer_revenue AS (
  -- Calcula métricas por cliente (al menos 3 órdenes)
  SELECT
    c.id,
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) as total_orders,
    SUM(o.total) as total_revenue
  FROM customers c
  INNER JOIN last_6_months_orders o ON c.id = o.customer_id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(DISTINCT o.id) >= 3
),
top_categories_per_customer AS (
  -- Encuentra la categoría más comprada por cada cliente
  SELECT
    o.customer_id,
    p.category,
    SUM(oi.quantity) as total_qty,
    ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
  FROM last_6_months_orders o
  INNER JOIN order_items oi ON o.id = oi.order_id
  INNER JOIN products p ON oi.product_id = p.id
  GROUP BY o.customer_id, p.category
)
SELECT
  cr.name,
  cr.email,
  cr.country,
  cr.total_orders,
  ROUND(cr.total_revenue, 2) as total_revenue,
  ROUND(cr.total_revenue / cr.total_orders, 2) as avg_order_value,
  tc.category as categoria_mas_comprada
FROM customer_revenue cr
LEFT JOIN top_categories_per_customer tc 
  ON cr.id = tc.customer_id 
  AND tc.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

---

## 📝 Explicación por sección:

| Sección | Qué hace |
|---------|----------|
| **last_6_months_orders** | Filtra solo órdenes con status='completed' de los últimos 6 meses |
| **customer_revenue** | Agrupa por cliente, cuenta órdenes, suma revenue total. HAVING filtra ≥3 órdenes |
| **top_categories_per_customer** | Usa `ROW_NUMBER()` para ranking — la categoría con más cantidad comprada (rn=1) |
| **SELECT final** | Joinea todo y calcula avg_order_value (total_revenue ÷ total_orders) |

---

## 🔄 Variantes por motor BD:

**PostgreSQL** (cambia el cálculo de fecha):
```sql
AND created_at >= CURRENT_DATE - INTERVAL '6 months'
```

**SQL Server**:
```sql
AND created_at >= DATEADD(month, -6, CAST(GETDATE() AS DATE))
```

**SQLite**:
```sql
AND created_at >= datetime('now', '-6 months')
```

---

## 💡 Notas:

- ✅ Si hay **empate** en cantidad de items comprados, toma la primera categoría alfabéticamente (por ROW_NUMBER)
- ✅ **LEFT JOIN** en categorías → si no hay items, aparece NULL
- ✅ Si quieres **todas las categorías** del cliente (no solo top 1), reemplaza `ROW_NUMBER()` con `RANK()`
- ✅ Usa `o.total` de la tabla **orders** (si ya suma items) en lugar de recalcular desde `order_items`