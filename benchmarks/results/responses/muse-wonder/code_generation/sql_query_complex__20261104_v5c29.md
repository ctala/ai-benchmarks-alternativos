# Muse Wonder — code_generation/sql_query_complex

- model_id: `meta/muse-wonder`
- success: True  | final: 8.18 | quality: 9.6
- latency_total: 9.467s | tokens_per_second: 135.4
- input_tokens: 149 | output_tokens: 1282
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

```sql
WITH customer_stats AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders o 
        ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_stats AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi 
        ON oi.order_id = o.id
    INNER JOIN products p 
        ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT
    cs.name AS nombre,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cat.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_stats cat
    ON cat.customer_id = cs.id
   AND cat.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Notas:**
- Sintaxis para **PostgreSQL**. Para MySQL usa `CURRENT_DATE - INTERVAL 6 MONTH`.
- `categoria_mas_comprada` se calcula por mayor cantidad total comprada (`SUM(quantity)`). Si la quieres por mayor gasto, cambia el `ORDER BY` de la ventana a `SUM(oi.quantity * oi.unit_price) DESC`.