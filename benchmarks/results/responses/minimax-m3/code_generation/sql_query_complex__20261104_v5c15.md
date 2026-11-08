# MiniMax M3 — code_generation/sql_query_complex

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.32 | quality: 9.6
- latency_total: 37.027s | tokens_per_second: 89.0
- input_tokens: 325 | output_tokens: 3294
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

Una opción para **PostgreSQL**, usando `orders.total` para el revenue y la cantidad de unidades para determinar la categoría más comprada:

```sql
WITH completed_orders AS (
    -- Órdenes completadas en los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders AS o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    -- Métricas por cliente, con al menos 3 órdenes completadas
    SELECT
        co.customer_id,
        COUNT(*)             AS total_orders,
        SUM(co.total)        AS total_revenue,
        AVG(co.total)        AS avg_order_value
    FROM completed_orders AS co
    GROUP BY co.customer_id
    HAVING COUNT(*) >= 3
),
category_ranking AS (
    -- Categoría más comprada por unidades; desempate alfabético
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS units_purchased,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS category_rank
    FROM completed_orders AS co
    JOIN order_items AS oi ON oi.order_id = co.id
    JOIN products AS p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    c.name  AS nombre,
    c.email AS email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics AS cm
JOIN customers AS c
    ON c.id = cm.customer_id
LEFT JOIN category_ranking AS cr
    ON cr.customer_id = cm.customer_id
   AND cr.category_rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

**Criterios aplicados:**
- La ventana de **6 meses** y el mínimo de **3 órdenes completadas** se aplican a las mismas órdenes.
- `total_revenue` es la suma de `orders.total`; `avg_order_value` es el promedio por orden.
- `categoria_mas_comprada` se determina por **unidades compradas** (`quantity`), no por importe. En caso de empate se elige la categoría alfabéticamente menor.
- Si un cliente tiene órdenes sin líneas en `order_items`, su categoría más comprada aparecerá como `NULL`.