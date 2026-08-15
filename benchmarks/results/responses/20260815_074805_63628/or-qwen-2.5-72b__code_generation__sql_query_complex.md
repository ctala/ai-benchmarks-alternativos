# Qwen 2.5 72B — code_generation/sql_query_complex

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 7.42 | quality: 8.04
- latency_total: 24.678s | tokens_per_second: 28.1
- input_tokens: 153 | output_tokens: 694
- judge_score: 3.6 | justificación: 

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

Para resolver este problema, necesitamos realizar varias operaciones y combinaciones de tablas. Aquí tienes la consulta SQL que cumple con los requisitos:

```sql
WITH completed_orders AS (
    SELECT o.*
    FROM orders o
    WHERE o.status = 'completed' AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
),
customer_revenue AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),
customer_order_items AS (
    SELECT 
        cri.customer_id,
        cri.product_id,
        COUNT(cri.product_id) AS product_count
    FROM (
        SELECT 
            co.customer_id,
            oi.product_id
        FROM completed_orders co
        JOIN order_items oi ON co.id = oi.order_id
    ) AS cri
    GROUP BY cri.customer_id, cri.product_id
),
customer_most_bought_category AS (
    SELECT 
        coi.customer_id,
        p.category AS most_bought_category
    FROM customer_order_items coi
    JOIN products p ON coi.product_id = p.id
    GROUP BY coi.customer_id
    ORDER BY SUM(coi.product_count) DESC
    LIMIT 1
)
SELECT 
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    cmc.most_bought_category
FROM customer_revenue cr
JOIN customer_most_bought_category cmc ON cr.customer_id = cmc.customer_id
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

### Explicación:

1. **completed_orders**: Esta CTE (Common Table Expression) selecciona todas las órdenes completadas en los últimos 6 meses.

2. **customer_revenue**: Esta CTE calcula el revenue total, el número de órdenes y el valor promedio de las órdenes para cada cliente que ha realizado al menos 3 órdenes completadas.

3. **customer_order_items**: Esta CTE cuenta cuántas veces cada producto ha sido comprado por cada cliente.

4. **customer_most_bought_category**: Esta CTE determina la categoría de producto más comprada por cada cliente.

5. **Consulta final**: Combina los resultados de las CTE anteriores para obtener el top 10 de clientes por revenue total, incluyendo el nombre, email, país, número total de órdenes, revenue total, valor promedio de las órdenes y la categoría de producto más comprada.

### Notas:
- La consulta asume que `created_at` es una columna de tipo fecha y que `CURDATE()` devuelve la fecha actual.
- La categoría más comprada se determina por la categoría del producto que ha sido comprado más veces por el cliente.
- La consulta está ordenada por `total_revenue` en orden descendente y limitada a 10 resultados.