# Claude Sonnet 5 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-sonnet-5`
- success: True  | final: 8.08 | quality: 9.8
- latency_total: 36.356s | tokens_per_second: 77.9
- input_tokens: 2 | output_tokens: 2831
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, proporcionando una consulta SQL bien estructurada y detallada que cumple con los requisitos especificados.

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

Aquí está la query, estructurada con CTEs para que sea legible y fácil de mantener:

```sql
WITH filtered_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT *
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_summary AS (
    -- Métricas agregadas por cliente, solo con 3+ órdenes
    SELECT
        customer_id,
        COUNT(*)          AS total_orders,
        SUM(total)         AS total_revenue,
        AVG(total)          AS avg_order_value
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_ranking AS (
    -- Categoría más comprada por cliente (por cantidad de unidades)
    SELECT
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY fo.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM filtered_orders fo
    JOIN order_items oi ON oi.order_id = fo.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY fo.customer_id, p.category
)

SELECT
    c.name                          AS nombre,
    c.email,
    c.country                       AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2)    AS avg_order_value,
    cr.category                     AS categoria_mas_comprada
FROM customer_summary cs
JOIN customers c        ON c.id = cs.customer_id
JOIN category_ranking cr ON cr.customer_id = cs.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Decisiones a validar contigo:**

1. **"Categoría más comprada"** — la definí por *cantidad de unidades* (`SUM(quantity)`), no por revenue. Si prefieres que sea por dinero gastado en esa categoría, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en el CTE `category_ranking`.

2. **Sintaxis de fecha** — `CURRENT_DATE - INTERVAL '6 months'` es PostgreSQL. Si es MySQL, cambia a:
   ```sql
   created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
   ```
   Si es SQL Server: `created_at >= DATEADD(MONTH, -6, GETDATE())`

3. **Empates en categoría** — si un cliente compró igual cantidad en 2 categorías, `ROW_NUMBER()` elige una arbitrariamente (según orden de desempate del motor). Si necesitas determinismo, agrega un criterio de desempate, ej. `ORDER BY SUM(oi.quantity) DESC, p.category ASC`.

4. **Índices recomendados** para que esto no escanee tablas completas: `orders(status, created_at, customer_id)` y `order_items(order_id)`.

¿Qué motor de base de datos usas (Postgres/MySQL/SQL Server)? Así te dejo la sintaxis exacta sin necesidad de que ajustes nada.