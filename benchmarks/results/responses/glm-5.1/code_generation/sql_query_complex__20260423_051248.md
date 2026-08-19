# GLM-5.1 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.2 | quality: 9.44
- latency_total: 85.172s | tokens_per_second: 32.5
- input_tokens: 149 | output_tokens: 2772
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes la query SQL. Para resolver el requerimiento de la "categoría más comprada" de forma limpia, utilicé **CTEs (Common Table Expressions)** y **Window Functions**, lo que hace el código más legible y modular.

```sql
WITH customer_metrics AS (
    -- 1. Calculamos las métricas base por cliente y filtramos por status y fecha
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed' 
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months' -- Sintaxis estándar/PostgreSQL
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_ranked AS (
    -- 2. Calculamos la cantidad total de productos comprados por categoría y cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER(
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
top_category AS (
    -- 3. Filtramos solo la categoría con el rank 1 (la más comprada) por cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_ranked
    WHERE rn = 1
)
-- 4. Unimos todo y aplicamos el límite final
SELECT 
    cm.nombre,
    cm.email,
    cm.pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN top_category tc ON cm.customer_id = tc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Notas importantes sobre la consulta:

1. **Filtro de fechas (`INTERVAL`)**: La sintaxis `CURRENT_DATE - INTERVAL '6 months'` funciona en **PostgreSQL** y **MySQL**. Si usas **SQL Server**, debes cambiar esa línea por: `AND o.created_at >= DATEADD(month, -6, GETDATE())`. Si usas **Oracle**, usa `AND o.created_at >= ADD_MONTHS(SYSDATE, -6)`.
2. **Cálculo de Revenue**: Asumí que la columna `orders.total` ya contiene el valor total pagado por la orden. Si por algún motivo necesitaras calcularlo desde los artículos, cambiarías el `SUM(o.total)` por `SUM(oi.quantity * oi.unit_price)`.
3. **Categoría más comprada (Empates)**: Usé `ROW_NUMBER()` para obtener el top 1 de categorías. Si un cliente compró exactamente la misma cantidad de productos en dos categorías distintas (un empate), `ROW_NUMBER()` elegirá arbitrariamente una. Si quisieras ver ambas en caso de empate, deberías usar `RANK()` en lugar de `ROW_NUMBER()`.
4. **LEFT JOIN final**: Hice un `LEFT JOIN` con la categoría por si acaso hay alguna anomalía en los datos (un cliente con 3 órdenes pero sin items registrados). En un escenario normal, un `INNER JOIN` también funcionaría.