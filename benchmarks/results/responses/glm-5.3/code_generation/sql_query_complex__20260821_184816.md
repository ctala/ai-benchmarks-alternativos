# GLM 5.3 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.97 | quality: 9.6
- latency_total: 65.055s | tokens_per_second: 85.0
- input_tokens: 156 | output_tokens: 5530
- judge_score: 5 | justificación: La respuesta es precisa y relevante, abordando directamente la consulta con una consulta SQL compleja que cumple con todos los requisitos especificados. Ofrece profundidad al considerar diferentes métricas y proporcionar notas sobre decisiones y ajustes para diferentes motores de base de datos. La claridad está garantizada por una estructura bien organizada y explicaciones detalladas, lo que la hace altamente útil para un emprendedor que podría usarla directamente.

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

Aquí tienes la query (sintaxis PostgreSQL):

```sql
WITH ordenes AS (
    -- Solo órdenes completadas en los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),

metricas AS (
    -- Métricas por cliente, filtrando los que tienen >= 3 órdenes
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM ordenes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_top AS (
    -- Ranking de categorías por cliente según unidades compradas
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM ordenes o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)

SELECT
    c.name    AS nombre,
    c.email   AS email,
    c.country AS pais,
    m.total_orders,
    ROUND(m.total_revenue, 2)   AS total_revenue,
    ROUND(m.avg_order_value, 2) AS avg_order_value,
    ct.category                 AS categoria_mas_comprada
FROM customers c
JOIN metricas m
  ON m.customer_id = c.id
LEFT JOIN categoria_top ct
  ON ct.customer_id = c.id
 AND ct.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

**Notas sobre las decisiones que tomé:**

- **Supuesto principal:** todas las métricas (revenue, conteo de órdenes y categoría) se calculan sobre órdenes `completed` dentro de la ventana de 6 meses. Si quieres que el revenue incluya órdenes de cualquier status pero el filtro de "mínimo 3" siga siendo solo sobre completadas, avísame y lo ajusto.

- **Sintaxis de fecha según el motor:**
  - MySQL: `created_at >= NOW() - INTERVAL 6 MONTH` (o `DATE_SUB(NOW(), INTERVAL 6 MONTH)`)
  - SQL Server: `created_at >= DATEADD(MONTH, -6, GETDATE())` y usa `SELECT TOP 10` en vez de `LIMIT`

- **Categoría más comprada:** la medí por unidades (`SUM(oi.quantity)`). Si prefieres medirla por gasto, cambia el ORDER BY del window function a `SUM(oi.quantity * oi.unit_price) DESC`. El desempate con `p.category` hace el resultado determinista cuando hay empates.

- **Revenue desde `orders.total`:** uso el campo `total` directamente en vez de calcularlo desde `order_items`. Esto es importante: si unieras `orders` con `order_items` en la misma agregación, el total se multiplicaría por el número de items de cada orden. Por eso la categoría se calcula en un CTE separado.

- Si `total` es `double precision` en Postgres, `ROUND` necesita un cast: `ROUND(m.total_revenue::numeric, 2)`.