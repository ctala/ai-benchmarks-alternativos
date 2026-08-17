# Llama 3.1 8B Instant — code_generation/sql_query_complex

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 7.16 | quality: 7.76
- latency_total: 89.202s | tokens_per_second: 7.3
- input_tokens: 154 | output_tokens: 655
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí te dejo la consulta SQL que resuelve tu problema:
```sql
WITH 
  -- Calcula el total de revenue para cada cliente en los últimos 6 meses
  cliente_revenue AS (
    SELECT 
      c.id, c.name, c.email, c.country, 
      SUM(oi.quantity * oi.unit_price) AS total_revenue,
      COUNT(o.id) AS total_orders,
      AVG(oi.quantity * oi.unit_price) AS avg_order_value
    FROM 
      orders o
      JOIN customers c ON o.customer_id = c.id
      JOIN order_items oi ON o.id = oi.order_id
    WHERE 
      o.status = 'completed' AND
      o.created_at >= NOW() - INTERVAL '6 month'
    GROUP BY 
      c.id, c.name, c.email, c.country
  ),
  -- Calcula la categoría más comprada para cada cliente
  categoria_mas_comprada AS (
    SELECT 
      cr.id, cr.name, cr.email, cr.country, 
      MAX(cr.total_revenue) AS max_revenue,
      (SELECT 
         p.category
       FROM 
         products p
         JOIN order_items oi ON p.id = oi.product_id
       WHERE 
         oi.order_id IN (SELECT id FROM orders WHERE customer_id = cr.id AND status = 'completed')
       GROUP BY 
         p.category
       ORDER BY 
         SUM(oi.quantity * oi.unit_price) DESC
       LIMIT 1) AS categoria_mas_comprada
    FROM 
      cliente_revenue cr
    GROUP BY 
      cr.id, cr.name, cr.email, cr.country
  )
SELECT 
  cmc.name, cmc.email, cmc.country, 
  cr.total_orders, cr.total_revenue, 
  cr.avg_order_value, cmc.categoria_mas_comprada
FROM 
  categoria_mas_comprada cmc
  JOIN cliente_revenue cr ON cmc.id = cr.id
WHERE 
  cmc.max_revenue IS NOT NULL AND 
  cr.total_orders >= 3
ORDER BY 
  cr.total_revenue DESC
LIMIT 10;
```
Esta consulta utiliza dos CTE (Common Table Expressions) para calcular el total de revenue y la categoría más comprada para cada cliente.

La primera CTE, `cliente_revenue`, calcula el total de revenue para cada cliente en los últimos 6 meses, agrupando por el id del cliente, nombre, email, país y sumando el total de revenue para cada cliente.

La segunda CTE, `categoria_mas_comprada`, calcula la categoría más comprada para cada cliente, seleccionando la categoría que tiene el mayor total de revenue para cada cliente.

Finalmente, se une la tabla `categoria_mas_comprada` con la tabla `cliente_revenue` para obtener la lista de clientes con el total de revenue, total de órdenes, valor promedio de cada orden, categoría más comprada y el nombre, email y país del cliente.

La consulta se ordena por total de revenue en descenso y se limita a los 10 primeros registros.