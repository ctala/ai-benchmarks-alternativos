# DeepSeek V4 Flash 0731 — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.72 | quality: 9.4
- latency_total: 23.719s | tokens_per_second: 188.6
- input_tokens: 232 | output_tokens: 4474
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

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

```sql
WITH pedidos_periodo AS (
    SELECT id AS order_id, customer_id
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
revenue AS (
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.order_id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM pedidos_periodo o
    JOIN order_items oi ON oi.order_id = o.order_id
    GROUP BY o.customer_id
    HAVING COUNT(DISTINCT o.order_id) >= 3
),
categorias AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS cantidad,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM pedidos_periodo o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)
SELECT
    c.name,
    c.email,
    c.country,
    r.total_orders,
    r.total_revenue,
    ROUND(r.total_revenue / NULLIF(r.total_orders, 0), 2) AS avg_order_value,
    cat.category AS categoria_mas_comprada
FROM revenue r
JOIN customers c ON c.id = r.customer_id
LEFT JOIN categorias cat ON cat.customer_id = r.customer_id AND cat.rn = 1
ORDER BY r.total_revenue DESC
LIMIT 10;
```