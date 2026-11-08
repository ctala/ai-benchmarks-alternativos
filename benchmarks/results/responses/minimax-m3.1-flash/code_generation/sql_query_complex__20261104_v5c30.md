# MiniMax M3.1 Flash — code_generation/sql_query_complex

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.83 | quality: 9.4
- latency_total: 8.484s | tokens_per_second: 171.6
- input_tokens: 342 | output_tokens: 1456
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

Suponiendo PostgreSQL, que el revenue se calcula con `orders.total` y que “categoría más comprada” es la que acumula mayor cantidad de artículos:

```sql
WITH completed_orders AS (
    SELECT
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
      AND created_at <= CURRENT_TIMESTAMP
),
customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_totals AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.id
    JOIN products p
        ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_quantity DESC, category ASC
        ) AS category_rank
    FROM category_totals
)
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c
    ON c.id = cs.customer_id
LEFT JOIN ranked_categories rc
    ON rc.customer_id = cs.customer_id
   AND rc.category_rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

El filtro de seis meses se aplica sobre `orders.created_at`, ya que la tabla no incluye una fecha específica de finalización. En caso de empate entre categorías, se elige la alfabéticamente anterior.