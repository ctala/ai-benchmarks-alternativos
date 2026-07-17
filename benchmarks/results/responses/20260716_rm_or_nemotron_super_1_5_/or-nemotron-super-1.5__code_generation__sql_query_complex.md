# Nemotron Super 49B v1.5 — code_generation/sql_query_complex

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.58 | quality: 9.76
- latency_total: 90.165s | tokens_per_second: 50.2
- input_tokens: 163 | output_tokens: 4529
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí está la consulta SQL que cumple con los requisitos especificados:

```sql
WITH customer_data AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id AS order_id,
        oi.quantity,
        oi.unit_price,
        p.category
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),
totals AS (
    SELECT 
        customer_id,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customer_data
    GROUP BY customer_id
),
category_summary AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS total_quantity
    FROM customer_data
    GROUP BY customer_id, category
),
most_purchased_category AS (
    SELECT 
        customer_id,
        category AS most_purchased_category
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
        FROM category_summary
    ) AS ranked
    WHERE rn = 1
)
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    t.total_orders,
    t.total_revenue,
    t.total_revenue / t.total_orders AS avg_order_value,
    mpc.most_purchased_category AS categoria_mas_comprada
FROM customers c
JOIN totals t ON c.id = t.customer_id
LEFT JOIN most_purchased_category mpc ON c.id = mpc.customer_id
WHERE t.total_orders >= 3
ORDER BY t.total_revenue DESC
LIMIT 10;
```

### Explicación:

1. **CTE `customer_data`**:
   - Une las tablas `customers`, `orders`, `order_items` y `products`.
   - Filtra órdenes completadas (`status = 'completed'`) y creadas en los últimos 6 meses.

2. **CTE `totals`**:
   - Calcula el número total de órdenes (`total_orders`) y el ingreso total (`total_revenue`) por cliente.

3. **CTE `category_summary`**:
   - Calcula la cantidad total de productos comprados por categoría para cada cliente.

4. **CTE `most_purchased_category`**:
   - Utiliza `ROW_NUMBER()` para identificar la categoría con mayor cantidad de productos comprados por cliente.

5. **Consulta final**:
   - Combina los datos de clientes, totales y categoría más comprada.
   - Filtra clientes con al menos 3 órdenes completadas.
   - Ordena por ingreso total en descenso y limita a los 10 primeros.

Esta consulta proporciona los resultados deseados con las columnas especificadas y cumple con todos los requisitos del problema.