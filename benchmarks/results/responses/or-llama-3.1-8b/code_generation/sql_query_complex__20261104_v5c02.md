# Llama 3.1 8B Instant — code_generation/sql_query_complex

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 6.22 | quality: 5.24
- latency_total: 3.954s | tokens_per_second: 144.1
- input_tokens: 155 | output_tokens: 570
- judge_score: 2.2 | justificación: 

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

Aquí te dejo la consulta SQL que resuelve el problema:
```sql
WITH 
  -- Cálculo del total de ingresos por cliente
  cliente_revenue AS (
    SELECT 
      c.id, 
      c.name, 
      c.email, 
      c.country, 
      COUNT(o.id) AS total_orders, 
      SUM(o.total) AS total_revenue, 
      AVG(o.total) AS avg_order_value
    FROM 
      customers c
    JOIN 
      orders o ON c.id = o.customer_id
    WHERE 
      o.status = 'completed' AND 
      o.created_at > NOW() - INTERVAL '6 month'
    GROUP BY 
      c.id, c.name, c.email, c.country
  ),
  -- Cálculo de la categoría más comprada por cliente
  categoria_mas_comprada AS (
    SELECT 
      cr.id, 
      cr.name, 
      cr.email, 
      cr.country, 
      cr.total_orders, 
      cr.total_revenue, 
      MAX(CASE WHEN ci.category = p.category THEN 1 ELSE 0 END) AS max_categoria_comprada
    FROM 
      cliente_revenue cr
    JOIN 
      order_items oi ON cr.id = oi.order_id
    JOIN 
      products p ON oi.product_id = p.id
    GROUP BY 
      cr.id, cr.name, cr.email, cr.country, cr.total_orders, cr.total_revenue
  )
SELECT 
  name, 
  email, 
  country, 
  total_orders, 
  total_revenue, 
  avg_order_value, 
  MAX(categoria_mas_comprada) AS categoria_mas_comprada
FROM 
  categoria_mas_comprada
GROUP BY 
  name, email, country, total_orders, total_revenue, avg_order_value
ORDER BY 
  total_revenue DESC
LIMIT 10;
```
Esta consulta utiliza dos subconsultas con CTE (Common Table Expressions) para calcular el total de ingresos y la categoría más comprada por cada cliente. Luego, se agrupa los resultados y se ordena por el total de ingresos en descenso para obtener los 10 clientes con mayor ingresos.

Nota que la función `NOW()` devuelve la fecha y hora actual, y `INTERVAL '6 month'` es un intervalo de 6 meses. También se utiliza la función `MAX` con `CASE` para calcular la categoría más comprada, ya que la función `GROUP BY` no permite utilizar funciones de agregación en las columnas no agrupadas.

Espero que esto te ayude. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!