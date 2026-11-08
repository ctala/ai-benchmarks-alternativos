# GLM 5.3 Flash — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.65 | quality: 9.6
- latency_total: 19.226s | tokens_per_second: 78.3
- input_tokens: 156 | output_tokens: 1505
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
WITH filtered_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id)                          AS total_orders,
        SUM(o.total)                         AS total_revenue,
        ROUND(AVG(o.total), 2)               AS avg_order_value
    FROM customers c
    INNER JOIN filtered_orders o ON o.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_purchases AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM filtered_orders o
    INNER JOIN order_items oi ON oi.order_id = o.id
    INNER JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),
top_category AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
    FROM category_purchases
)
SELECT
    cs.name           AS nombre,
    cs.email,
    cs.country        AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.category       AS categoria_mas_comprada
FROM customer_stats cs
INNER JOIN top_category tc
    ON tc.customer_id = cs.customer_id AND tc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Notas sobre decisiones que tomé (ajústalas si tu lógica de negocio es distinta):**

- **"Categoría más comprada"**: la definí por cantidad total de unidades (`SUM(oi.quantity)`). Si prefieres por revenue, cambia a `SUM(oi.quantity * oi.unit_price)` en el CTE `category_purchases`.
- **Empates en categoría**: `ROW_NUMBER` elige una al azar en caso de empate. Si quieres ver todas las categorías empatadas, usa `RANK()` en lugar de `ROW_NUMBER()`.
- **El filtro de ≥3 órdenes se aplica antes del LIMIT 10**, así que el top 10 solo incluye clientes que cumplen esa condición.
- **Sintaxis de fecha**: `CURRENT_DATE - INTERVAL '6 months'` es PostgreSQL. Para MySQL usa `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
- Uso `INNER JOIN` con `filtered_orders` para que solo aparezcan clientes con al menos una orden completada en el período (no hace falta `LEFT JOIN`).