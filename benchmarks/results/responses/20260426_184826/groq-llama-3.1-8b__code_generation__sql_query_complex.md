# Llama 3.1 8B Instant (Groq) — code_generation/sql_query_complex

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 8.06 | quality: 8.6
- latency_total: 0.815s | tokens_per_second: 493.5
- input_tokens: 179 | output_tokens: 402
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí te muestro la query SQL que busca lo que necesitas:
```sql
WITH 
  -- Calcula el total de ingresos por cliente
  customer_revenue AS (
    SELECT 
      o.customer_id,
      c.name,
      c.email,
      c.country,
      COUNT(o.id) AS total_orders,
      SUM(o.total) AS total_revenue,
      AVG(o.total) AS avg_order_value,
      -- Calcula la categoría con mayor cantidad de productos comprados
      (SELECT 
         p.category
       FROM 
         order_items oi
         JOIN products p ON oi.product_id = p.id
       WHERE 
         oi.order_id = o.id
       GROUP BY 
         p.category
       ORDER BY 
         COUNT(oi.id) DESC
       LIMIT 1) AS categoria_mas_comprada
    FROM 
      orders o
      JOIN customers c ON o.customer_id = c.id
    WHERE 
      o.status = 'completed' AND 
      o.created_at > NOW() - INTERVAL 6 MONTH
    GROUP BY 
      o.customer_id, c.name, c.email, c.country
  ),
  
  -- Selecciona los clientes con al menos 3 órdenes completadas
  top_customers AS (
    SELECT 
      *
    FROM 
      customer_revenue
    WHERE 
      total_orders >= 3
  )
  
SELECT 
  name,
  email,
  country,
  total_orders,
  total_revenue,
  avg_order_value,
  categoria_mas_comprada
FROM 
  top_customers
ORDER BY 
  total_revenue DESC
LIMIT 10;
```
Esta query utiliza dos consultas con comandos `WITH` para calcular el total de ingresos por cliente y seleccionar los clientes con al menos 3 órdenes completadas. Luego, selecciona los primeros 10 clientes con mayor total de ingresos.