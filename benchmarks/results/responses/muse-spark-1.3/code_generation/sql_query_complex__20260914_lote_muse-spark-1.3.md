# Muse Spark 1.3 — code_generation/sql_query_complex

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 11.567s | tokens_per_second: 197.1
- input_tokens: 148 | output_tokens: 2280
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes una query optimizada para **MySQL**. Usa CTEs + `ROW_NUMBER()` para sacar la categoría favorita por cliente:

```sql
WITH filtered_orders AS (
    -- Solo órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL 6 MONTH
),
customer_totals AS (
    -- Agregado por cliente, solo los que tienen >= 3 órdenes
    SELECT
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),
category_sales AS (
    -- Revenue por cliente y categoría
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM filtered_orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),
top_category AS (
    -- Ranking de categorías por cliente, nos quedamos con la #1
    SELECT
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY category_revenue DESC
        ) AS rn
    FROM category_sales
)
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ROUND(ct.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_totals ct
JOIN customers c ON c.id = ct.customer_id
LEFT JOIN top_category tc 
    ON tc.customer_id = ct.customer_id 
    AND tc.rn = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

### Cómo funciona:

1.  **`filtered_orders`:** Filtra desde el inicio por `status = 'completed'` y `created_at` de los últimos 6 meses. Esto es clave para performance.
2.  **`customer_totals`:** Calcula `total_orders`, `total_revenue`, `avg_order_value` y aplica el `HAVING COUNT(id) >= 3`.
3.  **`category_sales`:** Une `filtered_orders -> order_items -> products` para sumar el revenue por cada `customer_id, category`.
4.  **`top_category`:** Con `ROW_NUMBER() PARTITION BY customer_id ORDER BY category_revenue DESC` nos quedamos con la categoría que más dinero generó para ese cliente.
5.  **SELECT final:** Une todo y ordena por `total_revenue DESC` con `LIMIT 10`.

> Nota: Definí `categoria_mas_comprada` como la de **mayor revenue**. Si la quieres por **mayor cantidad de unidades**, cambia `SUM(oi.quantity * oi.unit_price)` por `SUM(oi.quantity)` en el CTE `category_sales`.

Para Postgres solo cambia el filtro de fecha a: `created_at >= NOW() - INTERVAL '6 months'`.