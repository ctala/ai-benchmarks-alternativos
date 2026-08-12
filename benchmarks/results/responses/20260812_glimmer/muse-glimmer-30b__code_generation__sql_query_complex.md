# Muse Glimmer 30B — code_generation/sql_query_complex

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.49 | quality: 9.8
- latency_total: 38.727s | tokens_per_second: 59.4
- input_tokens: 197 | output_tokens: 2299
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada y detallada que cumple con los requisitos especificados.

## Respuesta completa

Aquí tienes una versión en PostgreSQL. La lógica es:

1. Filtrar `orders` completadas de los últimos 6 meses
2. Agregar por cliente con HAVING >= 3 pedidos
3. Sacar la categoría más comprada por cliente con `ROW_NUMBER`

```sql
WITH orders_recent AS (
  SELECT id, customer_id, total
  FROM orders
  WHERE status = 'completed'
    AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
  SELECT
    c.id AS customer_id,
    c.name  AS nombre,
    c.email,
    c.country AS pais,
    COUNT(or_.id) AS total_orders,
    SUM(or_.total) AS total_revenue,
    ROUND(SUM(or_.total)::numeric / COUNT(or_.id), 2) AS avg_order_value
  FROM customers c
  JOIN orders_recent or_ ON or_.customer_id = c.id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(or_.id) >= 3
),
category_qty AS (
  SELECT
    or_.customer_id,
    p.category,
    SUM(oi.quantity) AS qty
    -- Si quieres por revenue: SUM(oi.quantity * oi.unit_price) AS revenue
  FROM orders_recent or_
  JOIN order_items oi ON oi.order_id = or_.id
  JOIN products p ON p.id = oi.product_id
  GROUP BY or_.customer_id, p.category
),
ranked_category AS (
  SELECT
    customer_id,
    category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id 
      ORDER BY qty DESC
    ) AS rn
  FROM category_qty
)
SELECT
  cs.nombre,
  cs.email,
  cs.pais,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  rc.categoria_mas_comprada
FROM customer_stats cs
JOIN ranked_category rc 
  ON rc.customer_id = cs.customer_id AND rc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Notas**
* `CURRENT_DATE - INTERVAL '6 months'` = últimos 6 meses. En MySQL usa `created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
* `categoria_mas_comprada` se calcula por cantidad total. Si lo quieres por revenue cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en `category_qty` y en el `ORDER BY` del `ROW_NUMBER`.
* `total_revenue` usa `orders.total`. Si prefieres recalcularlo desde `order_items` usa `SUM(oi.quantity * oi.unit_price)`.