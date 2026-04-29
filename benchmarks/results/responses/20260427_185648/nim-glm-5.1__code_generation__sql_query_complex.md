# GLM 5.1 (NIM) — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.5 | quality: 9.72
- latency_total: 35.414s | tokens_per_second: 24.6
- input_tokens: 146 | output_tokens: 870
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query SQL. Para obtener la **categoría más comprada**, utilizamos un CTE (Common Table Expression) con la función `ROW_NUMBER()` para identificar la categoría con mayor cantidad de productos comprados por cada cliente, y luego lo unimos al cálculo principal.

```sql
WITH ClientRevenue AS (
    -- Cálculo de las métricas financieras y conteo de órdenes
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue,
        SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
TopCategory AS (
    -- Cálculo de la categoría más comprada (por volumen de unidades) en los últimos 6 meses
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER(PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, p.category
)
-- Query principal que une todo y aplica el Top 10
SELECT 
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM ClientRevenue cr
LEFT JOIN TopCategory tc ON cr.customer_id = tc.customer_id AND tc.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

### Explicación de la query:

1. **CTE `ClientRevenue`**: 
   - Filtra las órdenes por `status = 'completed'` y por los últimos 6 meses usando `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`. *(Nota: si usas PostgreSQL, cambia `DATE_SUB` por `CURRENT_DATE - INTERVAL '6 months'`)*.
   - Agrupa por cliente y calcula el `total_revenue` multiplicando la cantidad por el precio unitario.
   - Calcula el `avg_order_value` dividiendo el revenue total entre el número distinto de órdenes (es más preciso que hacer un `AVG` del total de la orden).
   - Usa `HAVING COUNT(DISTINCT o.id) >= 3` para asegurar que solo se incluyan clientes con al menos 3 órdenes completadas.

2. **CTE `TopCategory`**:
   - Agrupa por cliente y categoría, sumando la cantidad de items (`quantity`).
   - Usa `ROW_NUMBER() OVER(...)` para rankear las categorías por cliente. La categoría con mayor `SUM(oi.quantity)` obtiene el rango 1 (`rn = 1`). Si hay empate, elegirá una arbitrariamente (si quisieras que en caso de empate eligiera la de mayor revenue, añadirías `SUM(oi.quantity * oi.unit_price) DESC` al `ORDER BY` del Window Function).

3. **Query Principal**:
   - Hace un `LEFT JOIN` entre los ingresos del cliente y su categoría top (filtrando `tc.rn = 1`).
   - Ordena por `total_revenue DESC`.
   - Aplica el `LIMIT 10` para obtener solo el Top 10.