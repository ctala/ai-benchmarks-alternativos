# GLM 5.3 Flash — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.51 | quality: 9.6
- latency_total: 64.924s | tokens_per_second: 42.6
- input_tokens: 156 | output_tokens: 2767
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes la query (sintaxis PostgreSQL, con notas para otros motores al final):

```sql
WITH completed_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    -- Métricas por cliente, solo con al menos 3 órdenes
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_stats AS (
    -- Cantidad comprada por categoría y cliente
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),
top_category AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY total_qty DESC
        ) AS rn
    FROM category_stats
)
SELECT
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c          ON c.id = cs.customer_id
LEFT JOIN top_category tc ON tc.customer_id = cs.customer_id AND tc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Decisiones y supuestos:**

- **Revenue**: uso `orders.total`. Si prefieres calcularlo desde los ítems, reemplaza con `SUM(oi.quantity * oi.unit_price)` agregando los joins correspondientes en `customer_stats`.
- **Ventana de tiempo**: asumí que tanto los 6 meses como el requisito de "al menos 3 órdenes" aplican a la misma ventana. Si las 3 órdenes deben contar de todos los tiempos, habría que separar el `HAVING` en otro CTE sin el filtro de fecha.
- **Categoría más comprada**: la defino por cantidad de unidades (`SUM(oi.quantity)`). Si prefieres por revenue de categoría, cambia a `SUM(oi.quantity * oi.unit_price)`. En caso de empate, `ROW_NUMBER()` elige una arbitraria; usa `RANK()` o añade un desempate si necesitas otro comportamiento.
- **LEFT JOIN** en la categoría para no excluir clientes cuyas órdenes no tengan ítems registrados.

**Variantes por motor:**

- **MySQL**: `created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` (requiere MySQL 8+ por las window functions)
- **SQL Server**: `created_at >= DATEADD(MONTH, -6, CAST(GETDATE() AS date))` y `SELECT TOP 10 ...` en lugar de `LIMIT 10`