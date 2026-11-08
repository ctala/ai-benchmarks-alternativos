# DeepSeek V4 Pro (0813) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.0 | quality: 9.4
- latency_total: 51.136s | tokens_per_second: 67.6
- input_tokens: 231 | output_tokens: 3455
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en el análisis al calcular métricas clave y la categoría más comprada, todo mientras mantiene claridad y utilidad práctica para un emprendedor.

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
WITH completed_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_totals AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON co.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),

customer_category AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)

SELECT
    ct.name AS nombre,
    ct.email,
    ct.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_totals ct
LEFT JOIN customer_category cc
       ON cc.customer_id = ct.id
      AND cc.rn = 1
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

Nota: `categoria_mas_comprada` se calcula por cantidad total de unidades compradas por categoría. Si hay empate, se elige la primera alfabéticamente.  
La función de fecha `CURRENT_DATE - INTERVAL '6 months'` es compatible con PostgreSQL; en MySQL sería `CURRENT_DATE - INTERVAL 6 MONTH`.