# Mistral Large 3 675B — code_generation/sql_query_complex

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 9.12 | quality: 9.8
- latency_total: 4.742s | tokens_per_second: 123.8
- input_tokens: 147 | output_tokens: 587
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes la consulta SQL que cumple con todos tus requisitos:

```sql
WITH last_6_months_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total,
        oi.product_id,
        oi.quantity,
        p.category
    FROM
        orders o
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),

customer_stats AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / COUNT(DISTINCT o.id) AS avg_order_value
    FROM
        customers c
    JOIN
        last_6_months_orders o ON c.id = o.customer_id
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(DISTINCT o.id) >= 3
),

top_categories AS (
    SELECT
        customer_id,
        category,
        SUM(quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC) AS category_rank
    FROM
        last_6_months_orders
    GROUP BY
        customer_id, category
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM
    customer_stats cs
JOIN
    top_categories tc ON cs.id = tc.customer_id AND tc.category_rank = 1
ORDER BY
    cs.total_revenue DESC
LIMIT 10;
```

Explicación de la consulta:

1. **last_6_months_orders**: CTE que obtiene todas las órdenes completadas en los últimos 6 meses junto con los productos asociados.

2. **customer_stats**: CTE que calcula las estadísticas básicas de cada cliente (nombre, email, país, total de órdenes, revenue total y valor promedio de orden), filtrando solo aquellos con al menos 3 órdenes completadas.

3. **top_categories**: CTE que identifica la categoría más comprada por cada cliente (basado en la cantidad total de productos comprados en esa categoría).

4. **Consulta final**: Une los datos de los clientes con su categoría más comprada, redondea el valor promedio de orden y ordena por revenue total descendente, limitando a los 10 mejores clientes.