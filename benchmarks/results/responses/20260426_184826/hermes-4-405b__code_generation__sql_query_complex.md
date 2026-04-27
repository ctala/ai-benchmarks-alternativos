# Hermes 4 405B — code_generation/sql_query_complex

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 7.17 | quality: 8.48
- latency_total: 19.399s | tokens_per_second: 36.3
- input_tokens: 168 | output_tokens: 704
- judge_score: 4.2 | justificación: 

## Respuesta completa

Para obtener el resultado deseado, podemos dividir la consulta en varias subconsultas y combinarlas. Aquí está la consulta SQL completa:

```sql
WITH completed_orders AS (
  SELECT o.customer_id, COUNT(DISTINCT o.id) AS total_orders
  FROM orders o
  WHERE o.status = 'completed' 
    AND o.created_at >= DATEADD(MONTH, -6, GETDATE())
  GROUP BY o.customer_id
  HAVING COUNT(DISTINCT o.id) >= 3
),

customer_revenue AS (
  SELECT 
    o.customer_id,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    AVG(SUM(oi.quantity * oi.unit_price)) OVER (PARTITION BY o.customer_id) AS avg_order_value
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  WHERE o.status = 'completed'
    AND o.created_at >= DATEADD(MONTH, -6, GETDATE())
  GROUP BY o.customer_id, o.id
),

category_counts AS (
  SELECT 
    o.customer_id,
    p.category,
    COUNT(*) AS category_count,
    ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) AS rn
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= DATEADD(MONTH, -6, GETDATE())
  GROUP BY o.customer_id, p.category
),

top_category AS (
  SELECT customer_id, category AS categoria_mas_comprada
  FROM category_counts
  WHERE rn = 1
),

final AS (
  SELECT 
    c.name,
    c.email,
    c.country AS pais,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    tc.categoria_mas_comprada
  FROM customer_revenue cr
  JOIN customers c ON cr.customer_id = c.id
  JOIN completed_orders co ON cr.customer_id = co.customer_id
  JOIN top_category tc ON cr.customer_id = tc.customer_id
  ORDER BY cr.total_revenue DESC
  LIMIT 10
)

SELECT * FROM final;
```

Esta consulta consta de varias partes:

1. `completed_orders`: Filtra las órdenes completadas en los últimos 6 meses y selecciona solo clientes con al menos 3 órdenes completadas.

2. `customer_revenue`: Calcula el total de órdenes, el total de ingresos y el valor promedio del pedido para cada cliente en los últimos 6 meses.

3. `category_counts`: Cuenta la cantidad de productos comprados en cada categoría para cada cliente.

4. `top_category`: Selecciona la categoría más comprada para cada cliente.

5. `final`: Combina todas las subconsultas anteriores para obtener el resultado final, que incluye el nombre, correo electrónico, país, total de órdenes, total de ingresos, valor promedio del pedido y la categoría más comprada para los 10 clientes principales por ingresos totales en los últimos 6 meses.

Esta consulta debería proporcionar el resultado deseado según los requisitos especificados.