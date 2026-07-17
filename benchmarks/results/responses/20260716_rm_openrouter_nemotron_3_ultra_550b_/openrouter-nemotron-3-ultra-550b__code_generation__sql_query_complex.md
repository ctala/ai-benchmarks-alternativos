# Nemotron 3 Ultra 550B — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.89 | quality: 9.6
- latency_total: 3.277s | tokens_per_second: 202.6
- input_tokens: 160 | output_tokens: 664
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

## Respuesta completa

```sql
WITH completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (
          SELECT DATE_SUB(MAX(created_at), INTERVAL 6 MONTH) FROM orders
      )
),
customer_aggregates AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM completed_orders co
    JOIN customers c ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
),
category_ranking AS (
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY co.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.order_id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT 
    ca.name,
    ca.email,
    ca.country,
    ca.total_orders,
    ca.total_revenue,
    ROUND(ca.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_aggregates ca
LEFT JOIN category_ranking cr 
    ON cr.customer_id = ca.customer_id AND cr.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

**Notas:**
- Usa `DATE_SUB(MAX(created_at), INTERVAL 6 MONTH)` para anclar la ventana a la fecha máxima real de la tabla (evita depender de `NOW()` y es reproducible).
- `ROW_NUMBER()` elige la categoría con más unidades vendidas (`SUM(oi.quantity)`); si hay empate, gana la que aparezca primero.
- `LEFT JOIN` en `category_ranking` por si un cliente tuviera órdenes completadas pero sin items (raro, pero seguro).
- Compatible con MySQL 8+, PostgreSQL, SQL Server, BigQuery, Snowflake.