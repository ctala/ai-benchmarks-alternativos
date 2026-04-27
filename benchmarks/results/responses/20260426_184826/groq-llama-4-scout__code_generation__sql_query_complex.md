# Llama 4 Scout 17B (Groq preview) — code_generation/sql_query_complex

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 8.08 | quality: 9.24
- latency_total: 2.198s | tokens_per_second: 313.9
- input_tokens: 151 | output_tokens: 690
- judge_score: 4.6 | justificación: 

## Respuesta completa

**Query SQL para obtener la información solicitada**

La siguiente query SQL utilizará las tablas proporcionadas para obtener la información solicitada:

```sql
WITH 
  -- Calculamos el revenue total por orden
  order_revenue AS (
    SELECT 
      o.customer_id,
      oi.quantity * oi.unit_price AS revenue
    FROM 
      orders o
    JOIN 
      order_items oi ON o.id = oi.order_id
    WHERE 
      o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL 6 MONTH
  ),
  
  -- Agrupamos por cliente y calculamos totales
  customer_data AS (
    SELECT 
      c.id,
      c.name,
      c.email,
      c.country,
      COUNT(DISTINCT o.id) AS total_orders,
      SUM(orv.revenue) AS total_revenue
    FROM 
      customers c
    JOIN 
      orders o ON c.id = o.customer_id
    JOIN 
      order_revenue orv ON c.id = orv.customer_id
    WHERE 
      o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
      c.id, c.name, c.email, c.country
    HAVING 
      COUNT(DISTINCT o.id) >= 3
  ),
  
  -- Encontramos la categoria mas comprada por cliente
  customer_category AS (
    SELECT 
      c.id,
      p.category,
      SUM(oi.quantity) AS total_quantity
    FROM 
      customers c
    JOIN 
      orders o ON c.id = o.customer_id
    JOIN 
      order_items oi ON o.id = oi.order_id
    JOIN 
      products p ON oi.product_id = p.id
    WHERE 
      o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
      c.id, p.category
  ),
  
  -- Obtenemos la categoria con mayor cantidad para cada cliente
  max_category AS (
    SELECT 
      id,
      category,
      total_quantity,
      ROW_NUMBER() OVER (PARTITION BY id ORDER BY total_quantity DESC) AS rn
    FROM 
      customer_category
  )

-- Seleccionamos la información final
SELECT 
  cd.name,
  cd.email,
  cd.country,
  cd.total_orders,
  cd.total_revenue,
  cd.total_revenue / cd.total_orders AS avg_order_value,
  mc.category AS categoria_mas_comprada
FROM 
  customer_data cd
JOIN 
  max_category mc ON cd.id = mc.id AND mc.rn = 1
ORDER BY 
  cd.total_revenue DESC
LIMIT 10;
```

**Explicación de la query**

La query utiliza varias Common Table Expressions (CTEs) para organizar y simplificar la lógica:

1.  `order_revenue`: Calcula el revenue total por orden.
2.  `customer_data`: Agrupa por cliente y calcula totales de órdenes y revenue.
3.  `customer_category`: Encuentra la categoría más comprada por cliente.
4.  `max_category`: Obtiene la categoría con mayor cantidad para cada cliente.

Finalmente, se seleccionan los datos finales, ordenados por `total_revenue` en orden descendente, limitados a los primeros 10 registros.