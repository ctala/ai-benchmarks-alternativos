# Grok 4.5 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.5`
- success: True  | final: 8.16 | quality: 9.4
- latency_total: 12.223s | tokens_per_second: 122.0
- input_tokens: 357 | output_tokens: 1491
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL completa que cumple con todos los requisitos especificados.

## Respuesta completa

```sql
WITH completed_orders AS (
  SELECT
    o.id,
    o.customer_id,
    o.total
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
  SELECT
    co.customer_id,
    COUNT(*) AS total_orders,
    SUM(co.total) AS total_revenue,
    AVG(co.total) AS avg_order_value
  FROM completed_orders co
  GROUP BY co.customer_id
  HAVING COUNT(*) >= 3
),
category_qty AS (
  SELECT
    co.customer_id,
    p.category,
    SUM(oi.quantity) AS total_qty
  FROM completed_orders co
  JOIN order_items oi ON oi.order_id = co.id
  JOIN products p ON p.id = oi.product_id
  GROUP BY co.customer_id, p.category
),
ranked_categories AS (
  SELECT
    customer_id,
    category,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id
      ORDER BY total_qty DESC
    ) AS rn
  FROM category_qty
)
SELECT
  c.name AS nombre,
  c.email,
  c.country AS pais,
  cm.total_orders,
  cm.total_revenue,
  cm.avg_order_value,
  rc.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON c.id = cm.customer_id
JOIN ranked_categories rc
  ON rc.customer_id = cm.customer_id
 AND rc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```