# GLM 5 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 119.389s | tokens_per_second: 29.8
- input_tokens: 149 | output_tokens: 3556
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la query SQL para resolver tu solicitud. He utilizado **Common Table Expressions (CTEs)** para hacer el código más legible y modular, separando el cálculo de métricas de la lógica de la categoría más comprada.

Esta query está escrita en sintaxis estándar de SQL (compatible con PostgreSQL).

```sql
WITH metricas_clientes AS (
    -- 1. Calculamos las métricas principales y filtramos por fecha y estado
    SELECT
        o.customer_id,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months' -- En MySQL usar: DATE_SUB(NOW(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id
    HAVING COUNT(o.id) >= 3 -- Filtro: Al menos 3 órdenes
),
categoria_top AS (
    -- 2. Calculamos la categoría más comprada por volumen de unidades
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        -- Numeramos para obtener solo la categoría con mayor cantidad (Rank 1)
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unimos todo y mostramos el Top 10
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    mc.total_orders,
    mc.total_revenue,
    mc.avg_order_value,
    ct.category AS categoria_mas_comprada
FROM metricas_clientes mc
JOIN customers c ON mc.customer_id = c.id
LEFT JOIN categoria_top ct ON mc.customer_id = ct.customer_id AND ct.rn = 1
ORDER BY mc.total_revenue DESC
LIMIT 10;
```

### Puntos clave de la solución:

1.  **Filtro de tiempo y estado**: En el CTE `metricas_clientes`, filtramos directamente por `status = 'completed'` y la fecha de los últimos 6 meses.
2.  **Having Clause**: Usamos `HAVING COUNT(o.id) >= 3` para excluir clientes con menos de 3 órdenes completadas, tal como pediste.
3.  **Categoría más comprada**: En el CTE `categoria_top`, agrupamos por cliente y categoría sumando la cantidad (`quantity`). Usamos `ROW_NUMBER()` para asignar el ranking 1 a la categoría con más unidades compradas por cada cliente.
4.  **LEFT JOIN**: Usamos un `LEFT JOIN` para unir la categoría top, por si acaso un cliente cumple con los requisitos de órdenes pero no tiene ítems asociados (caso borde), el cliente no desaparezca del reporte.
5.  **Orden y Límite**: Finalmente, ordenamos por `total_revenue` de forma descendente y limitamos a 10 resultados.