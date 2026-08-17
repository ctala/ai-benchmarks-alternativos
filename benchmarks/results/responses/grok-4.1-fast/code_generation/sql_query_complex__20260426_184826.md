# Grok 4.1 Fast — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.66 | quality: 9.32
- latency_total: 17.188s | tokens_per_second: 143.8
- input_tokens: 297 | output_tokens: 2471
- judge_score: 4.8 | justificación: 

## Respuesta completa

```sql
WITH qualified_orders AS (
  SELECT 
    o.customer_id, 
    o.id AS order_id, 
    o.total
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),
customer_totals AS (
  SELECT 
    c.id,
    c.name AS nombre,
    c.email,
    c.country AS pais,
    COUNT(DISTINCT qo.order_id) AS total_orders,
    SUM(qo.total) AS total_revenue,
    SUM(qo.total) / COUNT(DISTINCT qo.order_id) AS avg_order_value
  FROM customers c
  JOIN qualified_orders qo ON qo.customer_id = c.id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING total_orders >= 3
),
category_sales AS (
  SELECT 
    qo.customer_id,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS cat_revenue
  FROM qualified_orders qo
  JOIN order_items oi ON oi.order_id = qo.order_id
  JOIN products p ON p.id = oi.product_id
  GROUP BY qo.customer_id, p.category
),
top_category AS (
  SELECT 
    customer_id,
    category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY cat_revenue DESC) AS rn
  FROM category_sales
)
SELECT 
  ct.nombre,
  ct.email,
  ct.pais,
  ct.total_orders,
  ct.total_revenue,
  ct.avg_order_value,
  tc.categoria_mas_comprada
FROM customer_totals ct
JOIN top_category tc ON tc.customer_id = ct.id AND tc.rn = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

**Notas:**
- Asume MySQL 8.0+ (para CTEs y `ROW_NUMBER()`).
- Filtra órdenes completadas en los últimos 6 meses (`DATE_SUB(NOW(), INTERVAL 6 MONTH)`).
- `total_revenue`: suma de `orders.total`.
- `avg_order_value`: `total_revenue / total_orders`.
- `categoria_mas_comprada`: categoría con mayor revenue por cliente (`SUM(quantity * unit_price)` por categoría). En caso de empate, elige uno arbitrariamente.
- Solo clientes con ≥3 órdenes completadas en el período.
- Si un cliente no tiene ítems/categorías (improbable), no aparecerá en el top.