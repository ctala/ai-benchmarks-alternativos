# Mercury 2.5 — code_generation/sql_query_complex

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.99 | quality: 9.4
- latency_total: 3.547s | tokens_per_second: 799.8
- input_tokens: 146 | output_tokens: 2837
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')


## Respuesta completa



Aquí tienes la query SQL que cumple con los requerimientos. Asume un dialecto compatible (como MySQL o PostgreSQL) para la fecha:

```sql
WITH order_data AS (
  SELECT
    o.customer_id,
    o.id AS order_id,
    p.category,
    oi.quantity * oi.unit_price AS line_total
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),
customer_stats AS (
  SELECT
    c.id,
    c.name AS nombre,
    c.email,
    c.country AS pais,
    COUNT(DISTINCT od.order_id) AS total_orders,
    SUM(od.line_total) AS total_revenue,
    SUM(od.line_total) / COUNT(DISTINCT od.order_id) AS avg_order_value
  FROM customers c
  JOIN order_data od ON c.id = od.customer_id
  GROUP BY c.id
  HAVING COUNT(DISTINCT od.order_id) >= 3
),
top_category AS (
  SELECT
    customer_id,
    category,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rn
  FROM order_data
  GROUP BY customer_id, category
)
SELECT
  cs.nombre,
  cs.email,
  cs.pais,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  tc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN top_category tc ON cs.id = tc.customer_id AND tc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```