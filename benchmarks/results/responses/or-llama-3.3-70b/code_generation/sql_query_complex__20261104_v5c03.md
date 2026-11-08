# Llama 3.3 70B — code_generation/sql_query_complex

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 8.75 | quality: 9.36
- latency_total: 8.769s | tokens_per_second: 94.3
- input_tokens: 154 | output_tokens: 827
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una solución SQL completa y bien estructurada que aborda todos los requisitos del problema.

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

Para resolver este problema, necesitamos realizar varias operaciones en la base de datos:

1. Calcular el total de ingresos (`total_revenue`) para cada cliente en los últimos 6 meses.
2. Calcular el número total de órdenes (`total_orders`) para cada cliente en los últimos 6 meses.
3. Calcular el valor promedio de la orden (`avg_order_value`) para cada cliente en los últimos 6 meses.
4. Determinar la categoría más comprada (`categoria_mas_comprada`) para cada cliente en los últimos 6 meses.
5. Filtrar solo a los clientes con al menos 3 órdenes completadas (`status = 'completed'`) en los últimos 6 meses.

A continuación, te proporciono una posible solución en SQL. Ten en cuenta que la implementación exacta puede variar dependiendo del sistema de gestión de base de datos que estés utilizando (por ejemplo, MySQL, PostgreSQL, SQL Server, etc.). La siguiente query está escrita en un estilo genérico que debería ser adaptable a la mayoría de los sistemas de gestión de bases de datos relacionales.

```sql
WITH 
-- Calcula el total de ingresos, número de órdenes y valor promedio por cliente
cliente_ordenes AS (
  SELECT 
    c.id AS customer_id,
    c.name,
    c.email,
    c.country,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    COUNT(DISTINCT o.id) AS total_orders,
    AVG(o.total) AS avg_order_value
  FROM 
    customers c
  JOIN 
    orders o ON c.id = o.customer_id
  JOIN 
    order_items oi ON o.id = oi.order_id
  WHERE 
    o.status = 'completed' AND o.created_at >= NOW() - INTERVAL 6 MONTH
  GROUP BY 
    c.id, c.name, c.email, c.country
),
-- Determina la categoría más comprada por cliente
categoria_mas_comprada AS (
  SELECT 
    c.id AS customer_id,
    p.category,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS row_num
  FROM 
    customers c
  JOIN 
    orders o ON c.id = o.customer_id
  JOIN 
    order_items oi ON o.id = oi.order_id
  JOIN 
    products p ON oi.product_id = p.id
  WHERE 
    o.status = 'completed' AND o.created_at >= NOW() - INTERVAL 6 MONTH
  GROUP BY 
    c.id, p.category
)

SELECT 
  co.name,
  co.email,
  co.country,
  co.total_orders,
  co.total_revenue,
  co.avg_order_value,
  cmc.category AS categoria_mas_comprada
FROM 
  cliente_ordenes co
JOIN 
  categoria_mas_comprada cmc ON co.customer_id = cmc.customer_id AND cmc.row_num = 1
WHERE 
  co.total_orders >= 3
ORDER BY 
  co.total_revenue DESC
LIMIT 10;
```

Esta query utiliza dos Common Table Expressions (CTEs):

1. `cliente_ordenes`: Calcula el total de ingresos, el número de órdenes y el valor promedio de la orden para cada cliente en los últimos 6 meses, siempre que el estado de la orden sea 'completed'.
2. `categoria_mas_comprada`: Determina la categoría más comprada por cada cliente en los últimos 6 meses, considerando solo las órdenes completadas.

Finalmente, se unen estas dos CTEs para obtener la información completa por cliente, se filtra para incluir solo a los clientes con al menos 3 órdenes completadas, y se ordena el resultado por el total de ingresos en descenso, limitando la salida a los primeros 10 clientes.