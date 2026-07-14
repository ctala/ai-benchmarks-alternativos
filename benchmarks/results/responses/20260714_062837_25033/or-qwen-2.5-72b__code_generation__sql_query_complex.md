# Qwen 2.5 72B — code_generation/sql_query_complex

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 17.973s | tokens_per_second: 41.6
- input_tokens: 153 | output_tokens: 748
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Para obtener el top 10 de clientes por revenue total en los últimos 6 meses, con las columnas especificadas y ordenadas por `total_revenue` en orden descendente, y solo incluyendo clientes con al menos 3 órdenes completadas, puedes usar la siguiente consulta SQL:

```sql
WITH completed_orders AS (
    SELECT 
        o.customer_id,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM 
        orders o
    WHERE 
        o.status = 'completed' 
        AND o.created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
        o.customer_id
    HAVING 
        total_orders >= 3
),
category_purchases AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM 
        customers c
        JOIN orders o ON c.id = o.customer_id
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
    WHERE 
        o.status = 'completed' 
        AND o.created_at >= NOW() - INTERVAL 6 MONTH
    GROUP BY 
        c.id, p.category
),
top_category AS (
    SELECT 
        cp.customer_id,
        cp.category AS category_mas_comprada
    FROM 
        category_purchases cp
    JOIN (
        SELECT 
            customer_id,
            MAX(total_quantity) AS max_quantity
        FROM 
            category_purchases
        GROUP BY 
            customer_id
    ) max_cp ON cp.customer_id = max_cp.customer_id AND cp.total_quantity = max_cp.max_quantity
)
SELECT 
    c.name,
    c.email,
    c.country,
    co.total_orders,
    co.total_revenue,
    co.avg_order_value,
    tc.category_mas_comprada
FROM 
    completed_orders co
JOIN 
    customers c ON co.customer_id = c.id
JOIN 
    top_category tc ON tc.customer_id = c.id
ORDER BY 
    co.total_revenue DESC
LIMIT 10;
```

### Explicación de la consulta:

1. **Subconsulta `completed_orders`**:
   - Filtra las órdenes completadas (`status = 'completed'`) en los últimos 6 meses.
   - Calcula el número total de órdenes (`total_orders`), el revenue total (`total_revenue`) y el valor promedio de cada orden (`avg_order_value`) por cliente.
   - Agrupa por `customer_id` y filtra solo los clientes con al menos 3 órdenes completadas.

2. **Subconsulta `category_purchases`**:
   - Calcula la cantidad total de productos comprados por cada cliente y categoría.
   - Filtra las órdenes completadas en los últimos 6 meses.

3. **Subconsulta `top_category`**:
   - Determina la categoría más comprada por cada cliente basándose en la cantidad total de productos.

4. **Consulta principal**:
   - Une las subconsultas `completed_orders`, `customers` y `top_category` para obtener los datos finales.
   - Selecciona las columnas requeridas y ordena por `total_revenue` en orden descendente.
   - Limita el resultado a los 10 primeros clientes.

Esta consulta proporciona el top 10 de clientes por revenue total en los últimos 6 meses, con las columnas especificadas y las condiciones requeridas.