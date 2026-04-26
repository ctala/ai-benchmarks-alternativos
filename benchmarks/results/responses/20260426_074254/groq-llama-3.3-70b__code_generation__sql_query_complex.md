# Llama 3.3 70B (Groq) — code_generation/sql_query_complex

- model_id: `llama-3.3-70b-versatile`
- success: True  | final: 7.86 | quality: 8.6
- latency_total: 2.336s | tokens_per_second: 296.7
- input_tokens: 179 | output_tokens: 693
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para obtener la información solicitada, necesitamos realizar algunas operaciones en las tablas proporcionadas. A continuación, te presento la query SQL que debería resolver el problema:

```sql
WITH 
-- Obtenemos las ordenes completadas de los ultimos 6 meses
ultimas_ordenes AS (
  SELECT 
    o.customer_id, 
    o.id AS order_id,
    o.total,
    oi.product_id,
    oi.quantity,
    oi.unit_price
  FROM 
    orders o
  JOIN 
    order_items oi ON o.id = oi.order_id
  WHERE 
    o.status = 'completed' 
    AND o.created_at >= NOW() - INTERVAL 6 MONTH
),

-- Obtenemos el total de revenue por cliente
total_revenue_por_cliente AS (
  SELECT 
    customer_id, 
    SUM(total) AS total_revenue
  FROM 
    ultimas_ordenes
  GROUP BY 
    customer_id
),

-- Obtenemos el total de ordenes por cliente
total_ordenes_por_cliente AS (
  SELECT 
    customer_id, 
    COUNT(order_id) AS total_orders
  FROM 
    ultimas_ordenes
  GROUP BY 
    customer_id
),

-- Obtenemos el valor promedio de las ordenes por cliente
avg_order_value_por_cliente AS (
  SELECT 
    customer_id, 
    AVG(total) AS avg_order_value
  FROM 
    ultimas_ordenes
  GROUP BY 
    customer_id
),

-- Obtenemos la categoria mas comprada por cliente
categoria_mas_comprada_por_cliente AS (
  SELECT 
    uo.customer_id, 
    p.category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (PARTITION BY uo.customer_id ORDER BY SUM(uo.quantity) DESC) AS row_num
  FROM 
    ultimas_ordenes uo
  JOIN 
    products p ON uo.product_id = p.id
  GROUP BY 
    uo.customer_id, p.category
)

SELECT 
  c.name, 
  c.email, 
  c.country, 
  top.total_orders, 
  tr.total_revenue, 
  aov.avg_order_value, 
  cmc.categoria_mas_comprada
FROM 
  customers c
JOIN 
  total_revenue_por_cliente tr ON c.id = tr.customer_id
JOIN 
  total_ordenes_por_cliente top ON c.id = top.customer_id
JOIN 
  avg_order_value_por_cliente aov ON c.id = aov.customer_id
JOIN 
  categoria_mas_comprada_por_cliente cmc ON c.id = cmc.customer_id AND cmc.row_num = 1
WHERE 
  top.total_orders >= 3
ORDER BY 
  tr.total_revenue DESC
LIMIT 10;
```

Esta query utiliza Common Table Expressions (CTEs) para calcular el total de revenue por cliente, el total de ordenes por cliente, el valor promedio de las ordenes por cliente y la categoria mas comprada por cliente. Luego, une estas CTEs con la tabla de clientes para obtener la información solicitada. La query ordena los resultados por el total de revenue en forma descendente y limita los resultados a los primeros 10 clientes con al menos 3 ordenes completadas en los ultimos 6 meses.