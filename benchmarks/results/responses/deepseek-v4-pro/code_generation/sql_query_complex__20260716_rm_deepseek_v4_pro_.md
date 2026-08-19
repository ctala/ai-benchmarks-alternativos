# DeepSeek V4 Pro — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.27 | quality: 9.4
- latency_total: 34.662s | tokens_per_second: 82.7
- input_tokens: 152 | output_tokens: 2865
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

## Respuesta completa

```sql
-- Asumiendo PostgreSQL. Para MySQL, usa DATE_SUB(CURDATE(), INTERVAL 6 MONTH) en lugar de CURRENT_DATE - INTERVAL '6 months'.

WITH 
-- Pedidos completados de los últimos 6 meses con sus líneas y categorías
completed_orders AS (
  SELECT 
    o.id AS order_id,
    o.customer_id,
    oi.quantity,
    oi.unit_price,
    p.category
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'   -- ajusta según tu motor
),

-- Ingresos y número de pedidos por cliente
customer_revenue AS (
  SELECT 
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity * unit_price) AS total_revenue
  FROM completed_orders
  GROUP BY customer_id
  HAVING COUNT(DISTINCT order_id) >= 3
),

-- Cantidad total comprada por categoría y cliente
customer_category_qtys AS (
  SELECT 
    customer_id,
    category,
    SUM(quantity) AS cat_qty
  FROM completed_orders
  GROUP BY customer_id, category
),

-- Categoría principal (más unidades) por cliente, desempate alfabético
ranked_categories AS (
  SELECT 
    customer_id,
    category,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY cat_qty DESC, category ASC) AS rn
  FROM customer_category_qtys
),

top_category AS (
  SELECT customer_id, category
  FROM ranked_categories
  WHERE rn = 1
)

-- Consulta final: top 10 clientes
SELECT 
  c.name AS nombre,
  c.email,
  c.country AS pais,
  cr.total_orders,
  cr.total_revenue,
  ROUND(cr.total_revenue / cr.total_orders, 2) AS avg_order_value,
  tc.category AS categoria_mas_comprada
FROM customer_revenue cr
JOIN customers c ON cr.customer_id = c.id
LEFT JOIN top_category tc ON cr.customer_id = tc.customer_id
ORDER BY cr.total_revenue DESC
LIMIT 10;
```