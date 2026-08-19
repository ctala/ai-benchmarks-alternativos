# Devstral Medium — code_generation/sql_query_complex

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.35 | quality: 9.72
- latency_total: 216.967s | tokens_per_second: 3.0
- input_tokens: 147 | output_tokens: 643
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para obtener el top 10 de clientes por revenue total en los últimos 6 meses, con las columnas especificadas y ordenados por `total_revenue` en orden descendente, puedes usar la siguiente consulta SQL:

```sql
WITH recent_orders AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.status,
        o.created_at
    FROM
        orders o
    WHERE
        o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
        AND o.status = 'completed'
),
customer_revenue AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(ro.order_id) AS total_orders,
        SUM(ro.total) AS total_revenue,
        AVG(ro.total) AS avg_order_value
    FROM
        customers c
    JOIN
        recent_orders ro ON c.id = ro.customer_id
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(ro.order_id) >= 3
),
customer_categories AS (
    SELECT
        ro.customer_id,
        p.category,
        COUNT(oi.product_id) AS category_count
    FROM
        recent_orders ro
    JOIN
        order_items oi ON ro.order_id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    GROUP BY
        ro.customer_id, p.category
),
top_category AS (
    SELECT
        cc.customer_id,
        cc.category,
        ROW_NUMBER() OVER (PARTITION BY cc.customer_id ORDER BY cc.category_count DESC) AS rn
    FROM
        customer_categories cc
)
SELECT
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM
    customer_revenue cr
JOIN
    top_category tc ON cr.customer_id = tc.customer_id
WHERE
    tc.rn = 1
ORDER BY
    cr.total_revenue DESC
LIMIT 10;
```

### Explicación:

1. **recent_orders**: Filtra las órdenes completadas en los últimos 6 meses.
2. **customer_revenue**: Calcula el total de órdenes, revenue total y valor promedio de orden para cada cliente que tiene al menos 3 órdenes completadas.
3. **customer_categories**: Cuenta cuántas veces cada cliente ha comprado productos de cada categoría.
4. **top_category**: Usa `ROW_NUMBER()` para encontrar la categoría más comprada por cada cliente.
5. **Final SELECT**: Une las tablas `customer_revenue` y `top_category` para obtener los datos finales y ordena por `total_revenue` en orden descendente, limitando a los top 10 clientes.

Esta consulta asegura que solo se consideren clientes con al menos 3 órdenes completadas y muestra la categoría más comprada por cada cliente.