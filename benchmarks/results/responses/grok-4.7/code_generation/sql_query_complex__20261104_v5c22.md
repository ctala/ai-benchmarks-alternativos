# Grok 4.7 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.12 | quality: 9.4
- latency_total: 14.46s | tokens_per_second: 104.7
- input_tokens: 1393 | output_tokens: 1514
- judge_score: 5.0 | justificación: 

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

Asumo que el filtro de 6 meses y el mínimo de 3 órdenes aplican a órdenes `completed` dentro de esa ventana, y que el revenue sale de `orders.total`.

```sql
WITH completed_recent AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT
        customer_id,
        COUNT(*)        AS total_orders,
        SUM(total)      AS total_revenue,
        AVG(total)      AS avg_order_value
    FROM completed_recent
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_rank AS (
    SELECT
        cr.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY cr.customer_id
            ORDER BY SUM(oi.quantity) DESC,
                     SUM(oi.quantity * oi.unit_price) DESC,
                     p.category
        ) AS rn
    FROM completed_recent cr
    JOIN order_items oi ON oi.order_id = cr.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY cr.customer_id, p.category
)
SELECT
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cat.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN category_rank cat
    ON cat.customer_id = cs.customer_id
   AND cat.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

`categoria_mas_comprada` es la categoría con mayor cantidad de unidades; si hay empate, gana la de mayor importe de líneas. En MySQL 8+ cambia el intervalo a `CURRENT_DATE - INTERVAL 6 MONTH`.