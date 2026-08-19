# DeepSeek V4 Pro (0813) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.14 | quality: 9.6
- latency_total: 85.362s | tokens_per_second: 59.4
- input_tokens: 231 | output_tokens: 5074
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, cumpliendo con todos los requisitos especificados en la instrucción original.

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

Aquí tienes una query SQL que cumple con los requisitos. Está escrita en PostgreSQL/MySQL 8+ (usa CTEs, funciones de ventana e `INTERVAL`).

```sql
WITH completed_orders AS (
    SELECT
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS category_qty
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),
category_rank AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY category_qty DESC, category
        ) AS rn
    FROM category_totals
)
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN category_rank cr
    ON cr.customer_id = cs.customer_id
   AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Notas:
- `categoria_mas_comprada` se calcula por la **cantidad total de artículos comprados** en cada categoría.
- Si prefieres calcularla por ingresos por categoría, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)`.
- Si usas SQL Server, cambia `LIMIT 10` por `TOP 10` y `CURRENT_DATE - INTERVAL '6 months'` por `DATEADD(MONTH, -6, GETDATE())`.