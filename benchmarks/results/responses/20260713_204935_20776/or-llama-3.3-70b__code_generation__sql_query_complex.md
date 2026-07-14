# Llama 3.3 70B — code_generation/sql_query_complex

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 8.43 | quality: 9.36
- latency_total: 31.17s | tokens_per_second: 19.3
- input_tokens: 155 | output_tokens: 603
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Para lograr esto, necesitamos hacer varias cosas:

1. Calcular el total de revenue por cliente.
2. Calcular el número total de órdenes por cliente.
3. Calcular el valor promedio de las órdenes por cliente.
4. Determinar la categoría más comprada por cada cliente.
5. Filtrar solo los clientes con al menos 3 órdenes completadas en los últimos 6 meses.

La query SQL para lograr esto sería:

```sql
WITH 
-- Calcula el total de revenue y el número de órdenes por cliente
cliente_ordenes AS (
  SELECT 
    c.id,
    c.name,
    c.email,
    c.country,
    COUNT(o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    AVG(oi.quantity * oi.unit_price) AS avg_order_value
  FROM customers c
  JOIN orders o ON c.id = o.customer_id
  JOIN order_items oi ON o.id = oi.order_id
  WHERE o.status = 'completed' AND o.created_at >= NOW() - INTERVAL 6 MONTH
  GROUP BY c.id, c.name, c.email, c.country
),

-- Determina la categoría más comprada por cada cliente
categoria_mas_comprada AS (
  SELECT 
    c.id AS customer_id,
    p.category,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS row_num
  FROM customers c
  JOIN orders o ON c.id = o.customer_id
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed' AND o.created_at >= NOW() - INTERVAL 6 MONTH
  GROUP BY c.id, p.category
)

SELECT 
  co.name,
  co.email,
  co.country,
  co.total_orders,
  co.total_revenue,
  co.avg_order_value,
  cmc.category AS categoria_mas_comprada
FROM cliente_ordenes co
JOIN categoria_mas_comprada cmc ON co.id = cmc.customer_id AND cmc.row_num = 1
WHERE co.total_orders >= 3
ORDER BY co.total_revenue DESC
LIMIT 10;
```

Esta query utiliza dos Common Table Expressions (CTE) para calcular el total de revenue y el número de órdenes por cliente, y para determinar la categoría más comprada por cada cliente. Luego, se unen estas CTE para obtener los resultados finales.

Ten en cuenta que esta query asume que la base de datos es PostgreSQL, ya que utiliza la función `NOW()` y el operador `INTERVAL`. Si estás utilizando otra base de datos, es posible que debas adaptar la query a sus funciones y operadores específicos.