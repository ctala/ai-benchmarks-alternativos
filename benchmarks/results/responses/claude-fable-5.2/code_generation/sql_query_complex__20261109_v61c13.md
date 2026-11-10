# Claude Fable 5.2 — code_generation/sql_query_complex

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.86 | quality: 9.6
- latency_total: 19.257s | tokens_per_second: 117.7
- input_tokens: 223 | output_tokens: 2266
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución SQL compleja que aborda todos los requisitos especificados, con una estructura clara y útil para un emprendedor.

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

Query en sintaxis PostgreSQL:

```sql
WITH completed_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    -- Métricas por cliente y top 10
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
    ORDER BY total_revenue DESC
    LIMIT 10
),
category_ranked AS (
    -- Ranking de categorías por cliente (solo para el top 10)
    SELECT
        co.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity) DESC,
                     SUM(oi.quantity * oi.unit_price) DESC,
                     p.category
        ) AS rn
    FROM completed_orders co
    JOIN customer_stats cs ON cs.customer_id = co.customer_id
    JOIN order_items oi    ON oi.order_id = co.id
    JOIN products p        ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
SELECT
    c.name                       AS nombre,
    c.email,
    c.country                    AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category                  AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN category_ranked cr
       ON cr.customer_id = cs.customer_id
      AND cr.rn = 1
ORDER BY cs.total_revenue DESC;
```

**Supuestos que hice:**

- **Revenue:** se calcula con `orders.total`, en un CTE separado de `order_items`. Si se uniera todo en un solo `JOIN`, cada orden se repetiría por cada item y se inflarían el conteo y el revenue.
- **Mínimo de 3 órdenes:** cuento solo las completadas dentro de los últimos 6 meses. Si el mínimo debe aplicar sobre todo el historial, hay que mover ese filtro a un CTE aparte.
- **Categoría más comprada:** es la de mayor cantidad de unidades (`SUM(quantity)`). Si hay empate, gana la de mayor importe y luego el orden alfabético.

**Otros motores:**

- **MySQL 8+:** cambia el filtro de fecha a `CURDATE() - INTERVAL 6 MONTH`.
- **SQL Server:** usa `DATEADD(MONTH, -6, GETDATE())` y `SELECT TOP 10` en lugar de `LIMIT 10`.