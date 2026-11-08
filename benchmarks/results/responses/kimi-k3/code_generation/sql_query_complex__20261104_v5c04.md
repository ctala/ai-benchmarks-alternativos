# Kimi K3 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.97 | quality: 9.8
- latency_total: 46.115s | tokens_per_second: 37.9
- input_tokens: 236 | output_tokens: 1749
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes la query usando CTEs (funciona en PostgreSQL y MySQL 8+):

```sql
WITH order_stats AS (
    -- Métricas de órdenes por cliente (últimos 6 meses, solo completadas)
    SELECT
        o.customer_id,
        COUNT(o.id)        AS total_orders,
        SUM(o.total)       AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id
    HAVING COUNT(o.id) >= 3
),
category_ranking AS (
    -- Ranking de categorías por cliente según cantidad comprada
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS unidades,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, SUM(oi.quantity * oi.unit_price) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p     ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT
    c.name              AS nombre,
    c.email,
    c.country           AS pais,
    os.total_orders,
    os.total_revenue,
    os.avg_order_value,
    cr.category         AS categoria_mas_comprada
FROM order_stats os
JOIN customers c        ON c.id = os.customer_id
LEFT JOIN category_ranking cr
       ON cr.customer_id = os.customer_id
      AND cr.rn = 1
ORDER BY os.total_revenue DESC
LIMIT 10;
```

**Cómo funciona:**

1. **`order_stats`**: filtra órdenes completadas de los últimos 6 meses, calcula `total_orders`, `total_revenue` y `avg_order_value`. El `HAVING COUNT(o.id) >= 3` aplica el requisito de mínimo 3 órdenes.
2. **`category_ranking`**: une `orders → order_items → products` para contar unidades por categoría, y con `ROW_NUMBER()` rankea la categoría más comprada por cliente (con desempate por monto gastado).
3. **Query final**: une todo con `customers` y ordena por revenue descendente, limitado a 10.

**Notas según tu motor de base de datos:**

- **MySQL**: cambia el filtro de fecha a `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
- **SQL Server**: usa `o.created_at >= DATEADD(MONTH, -6, GETDATE())` y `TOP 10` en lugar de `LIMIT 10`
- Si "categoría más comprada" prefieres medirla por **revenue** en vez de unidades, cambia el `ORDER BY` del `ROW_NUMBER()` a `SUM(oi.quantity * oi.unit_price) DESC`
- El `LEFT JOIN` en la categoría evita perder clientes si alguna orden no tuviera items registrados; si tus datos son consistentes, puedes usar `INNER JOIN`