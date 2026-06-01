# DeepSeek R1 (reasoning) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.4 | quality: 9.8
- latency_total: 128.143s | tokens_per_second: 23.6
- input_tokens: 153 | output_tokens: 3022
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con los requisitos solicitados:

```sql
WITH recent_orders AS (
    SELECT 
        o.id,
        o.customer_id,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
        AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_orders AS (
    SELECT
        ro.customer_id,
        COUNT(DISTINCT ro.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM recent_orders ro
    JOIN order_items oi ON ro.id = oi.order_id
    GROUP BY ro.customer_id
    HAVING COUNT(DISTINCT ro.id) >= 3
),
customer_categories AS (
    SELECT
        ro.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY ro.customer_id 
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category
        ) AS category_rank
    FROM recent_orders ro
    JOIN order_items oi ON ro.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY ro.customer_id, p.category
),
top_customers AS (
    SELECT
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        co.total_orders,
        co.total_revenue,
        (co.total_revenue / co.total_orders) AS avg_order_value,
        (SELECT cc.category 
         FROM customer_categories cc 
         WHERE cc.customer_id = c.id AND cc.category_rank = 1) AS categoria_mas_comprada
    FROM customer_orders co
    JOIN customers c ON co.customer_id = c.id
    ORDER BY co.total_revenue DESC
    LIMIT 10
)

SELECT *
FROM top_customers
ORDER BY total_revenue DESC;
```

**Explicación:**

1. **CTE `recent_orders`:**
   - Filtra órdenes completadas en los últimos 6 meses.

2. **CTE `customer_orders`:**
   - Calcula `total_orders` y `total_revenue` por cliente.
   - Filtra clientes con al menos 3 órdenes (`HAVING COUNT`).

3. **CTE `customer_categories`:**
   - Calcula el revenue por categoría para cada cliente.
   - Usa `ROW_NUMBER()` para rankear categorías por revenue (y alfabéticamente en empates).

4. **CTE `top_customers`:**
   - Combina todos los datos con la tabla `customers`.
   - Obtiene la categoría más comprada mediante subconsulta correlacionada.
   - Selecciona el top 10 por revenue total.

5. **Consulta final:**
   - Ordena los resultados por `total_revenue DESC`.

**Notas:**
- Usa `quantity * unit_price` para calcular el revenue (más preciso que el campo `total`).
- En empates de categoría, selecciona la que tiene nombre alfabético menor.
- Asume función de fecha `CURRENT_DATE` (ajustar según tu DB si es necesario).
- La categoría más comprada se basa en el mayor revenue generado por categoría.