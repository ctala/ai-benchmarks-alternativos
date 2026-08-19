# Llama 4 Scout 17B — code_generation/sql_query_complex

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 8.84 | quality: 9.08
- latency_total: 2.506s | tokens_per_second: 379.0
- input_tokens: 151 | output_tokens: 950
- judge_score: 4.8 | justificación: 

## Respuesta completa

### Query SQL para obtener los datos solicitados

La siguiente query SQL utiliza varias uniones y subconsultas para obtener los datos solicitados. Se asume que la tabla `orders` tiene un campo `status` que indica si la orden fue completada.

```sql
WITH 
  -- Calcula el revenue total por orden
  order_revenue AS (
    SELECT 
      o.customer_id,
      SUM(oi.quantity * oi.unit_price) AS revenue
    FROM 
      orders o
    JOIN 
      order_items oi ON o.id = oi.order_id
    WHERE 
      o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
      o.customer_id
  ),
  
  -- Calcula el total de ordenes por cliente
  customer_orders AS (
    SELECT 
      customer_id,
      COUNT(*) AS total_orders
    FROM 
      orders
    WHERE 
      status = 'completed'
      AND created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
      customer_id
  ),
  
  -- Calcula el revenue total, total de ordenes y valor promedio de orden por cliente
  customer_revenue AS (
    SELECT 
      c.id,
      c.name,
      c.email,
      c.country,
      co.total_orders,
      SUM(orv.revenue) AS total_revenue,
      SUM(orv.revenue) / co.total_orders AS avg_order_value
    FROM 
      customers c
    JOIN 
      customer_orders co ON c.id = co.customer_id
    JOIN 
      order_revenue orv ON c.id = orv.customer_id
    GROUP BY 
      c.id, c.name, c.email, c.country, co.total_orders
  ),
  
  -- Encuentra la categoria mas comprada por cliente
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
  
  -- Encuentra la categoria mas comprada por cliente
  customer_top_category AS (
    SELECT 
      id,
      category,
      ROW_NUMBER() OVER (PARTITION BY id ORDER BY total_quantity DESC) AS row_num
    FROM 
      customer_category
  )

-- Selecciona los datos finales
SELECT 
  cr.name,
  cr.email,
  cr.country,
  cr.total_orders,
  cr.total_revenue,
  cr.avg_order_value,
  ctc.category AS categoria_mas_comprada
FROM 
  customer_revenue cr
JOIN 
  customer_top_category ctc ON cr.id = ctc.id AND ctc.row_num = 1
WHERE 
  cr.total_orders >= 3
ORDER BY 
  cr.total_revenue DESC
LIMIT 10;
```

### Explicación

La query utiliza varias Common Table Expressions (CTEs) para calcular:

*   `order_revenue`: el revenue total por orden para cada cliente en los últimos 6 meses.
*   `customer_orders`: el total de ordenes por cliente en los últimos 6 meses.
*   `customer_revenue`: el revenue total, total de ordenes y valor promedio de orden por cliente en los últimos 6 meses.
*   `customer_category`: la cantidad total de productos comprados por categoría para cada cliente en los últimos 6 meses.
*   `customer_top_category`: la categoría más comprada por cliente en los últimos 6 meses.

Finalmente, la query selecciona los datos finales uniendo las CTEs `customer_revenue` y `customer_top_category`, filtrando clientes con al menos 3 ordenes completadas y ordenando por `total_revenue` en orden descendente. La query devuelve solo las primeras 10 filas.

### Nota

La query asume que la tabla `orders` tiene un campo `status` que indica si la orden fue completada. Si este campo tiene un nombre diferente, deberá ser reemplazado en la query. Además, la query utiliza funciones de fecha y hora que pueden variar dependiendo del motor de base de datos utilizado. La query fue escrita utilizando sintaxis compatible con MySQL. Si se utiliza un motor de base de datos diferente, es posible que sea necesario realizar ajustes.