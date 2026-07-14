# DeepSeek V4 Pro — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.59 | quality: 9.8
- latency_total: 38.035s | tokens_per_second: 62.2
- input_tokens: 152 | output_tokens: 2365
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos. Está escrita en un estilo compatible con PostgreSQL (usa `CURRENT_DATE - INTERVAL '6 months'`; para MySQL cambiarías por `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`).

```sql
WITH 
-- Período de tiempo (últimos 6 meses)
recent_orders AS (
    SELECT *
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'  -- Ajusta según tu SGBD
),

-- Estadísticas básicas por cliente
customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        SUM(total) / COUNT(*) AS avg_order_value
    FROM recent_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3                -- Al menos 3 órdenes completadas
),

-- Cantidad total comprada por cliente y categoría
category_qty AS (
    SELECT
        ro.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),

-- Seleccionar la categoría más comprada de cada cliente (en caso de empate, la primera alfabéticamente)
top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id 
                ORDER BY total_quantity DESC, category ASC
            ) AS rn
        FROM category_qty
    ) ranked
    WHERE rn = 1
)

-- Resultado final
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN top_category tc ON tc.customer_id = cs.customer_id   -- Por si algún cliente no tiene items (poco probable)
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Explicación breve:**
1. **recent_orders**: filtra todas las órdenes completadas de los últimos 6 meses.
2. **customer_stats**: agrupa por cliente, calcula `total_orders`, `total_revenue` y `avg_order_value`, y aplica el filtro de al menos 3 órdenes.
3. **category_qty**: suma las cantidades de cada categoría comprada por el cliente en ese período.
4. **top_category**: usa `ROW_NUMBER()` para quedarse con la categoría que más unidades acumula; en caso de empate se elige la primera alfabéticamente.
5. La consulta final une los datos del cliente con sus estadísticas y su categoría favorita, y devuelve los 10 primeros por `total_revenue` descendente.

Si tu base de datos es MySQL, cambia la línea del filtro de fecha por:
```sql
AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
```
Para SQL Server, usa:
```sql
AND created_at >= DATEADD(MONTH, -6, GETDATE())
```