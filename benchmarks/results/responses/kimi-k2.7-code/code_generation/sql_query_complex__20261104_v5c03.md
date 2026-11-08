# Kimi K2.7 Code — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.33 | quality: 9.8
- latency_total: 45.64s | tokens_per_second: 50.4
- input_tokens: 158 | output_tokens: 2298
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

Aquí tienes una query usando **CTEs** para que sea legible. Funciona en **PostgreSQL** y **MySQL 8.0+**:

```sql
WITH recent_orders AS (
    -- Órdenes completadas de los últimos 6 meses con sus líneas
    SELECT 
        o.id AS order_id,
        o.customer_id,
        oi.product_id,
        oi.quantity,
        oi.unit_price
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_category_qty AS (
    -- Cantidad comprada por cliente y categoría
    SELECT 
        ro.customer_id,
        p.category,
        SUM(ro.quantity) AS total_qty
    FROM recent_orders ro
    JOIN products p ON ro.product_id = p.id
    GROUP BY ro.customer_id, p.category
),
top_category AS (
    -- Categoría más comprada por cada cliente (en caso de empate, alfabética)
    SELECT 
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id 
                ORDER BY total_qty DESC, category ASC
            ) AS rn
        FROM customer_category_qty
    ) ranked
    WHERE rn = 1
),
customer_stats AS (
    -- Métricas agregadas por cliente
    SELECT 
        customer_id,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(quantity * unit_price) AS total_revenue,
        SUM(quantity * unit_price) / NULLIF(COUNT(DISTINCT order_id), 0) AS avg_order_value
    FROM recent_orders
    GROUP BY customer_id
    HAVING COUNT(DISTINCT order_id) >= 3
)
SELECT 
    c.name,
    c.email,
    c.country AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON cs.customer_id = c.id
JOIN top_category tc ON cs.customer_id = tc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación clave:

- **`recent_orders`**: filtra solo órdenes `completed` de los últimos 6 meses y une con sus líneas.
- **`customer_stats`**: calcula `total_orders`, `total_revenue` y `avg_order_value`. El `HAVING` garantiza al menos 3 órdenes completadas en ese período.
- **`top_category`**: usa `ROW_NUMBER()` para obtener la categoría con mayor cantidad comprada por cliente. Si hay empate, elige la primera alfabéticamente.
- El revenue se calcula desde `order_items` para mantener coherencia con el análisis por categoría.

### Notas por motor de base de datos:

| Motor | Cambios necesarios |
|-------|--------------------|
| **MySQL 8.0+** | Funciona casi igual. Usa `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` si prefieres ser explícito. |
| **SQL Server** | Cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATEADD(MONTH, -6, GETDATE())` y `LIMIT 10` por `TOP 10`. |
| **SQLite** | Usa `date('now', '-6 months')` para el filtro de fecha. |
| **MySQL 5.7** | No tiene `ROW_NUMBER()`; avísame y te doy una alternativa con variables o subqueries. |