# GLM 5 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 41.893s | tokens_per_second: 70.8
- input_tokens: 156 | output_tokens: 2965
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una solución estructurada y bien explicada para la consulta SQL compleja.

## Respuesta completa

Para resolver esta consulta de manera óptima y evitar problemas de duplicación de filas (el clásico error de sumar de más cuando se unen tablas de 1 a muchos), lo ideal es usar **CTEs (Common Table Expressions)**. 

Separaremos el cálculo de las métricas del cliente (que solo necesita `orders`) del cálculo de la categoría más comprada (que requiere `order_items` y `products`).

Aquí tienes la query:

```sql
WITH customer_metrics AS (
    -- 1. Calculamos las métricas principales por cliente usando solo la tabla orders
    SELECT 
        c.id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed' 
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months' -- Sintaxis estándar / PostgreSQL
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_ranking AS (
    -- 2. Calculamos la cantidad de productos comprados por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty_categoria,
        ROW_NUMBER() OVER(
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed' 
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unimos ambas partes y ordenamos
SELECT 
    cm.nombre,
    cm.email,
    cm.pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_ranking cr 
    ON cm.id = cr.customer_id 
    AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Notas importantes sobre la query:

1. **Prevención de duplicación (Fan-out):** Si hubiéramos hecho un solo `JOIN` de `customers`, `orders`, `order_items` y `products`, el `SUM(o.total)` se habría multiplicado por la cantidad de items en cada orden, dándote un revenue totalmente inflado. Al separar en dos CTEs, garantizamos que el revenue y el conteo de órdenes sean exactos.
2. **Función de Fecha:** Utilicé `CURRENT_DATE - INTERVAL '6 months'` que funciona en PostgreSQL y MySQL (versión 8+). Si usas **SQL Server**, debes cambiar esa línea por `o.created_at >= DATEADD(month, -6, GETDATE())`.
3. **Categoría más comprada:** Se determinó usando `SUM(oi.quantity)` asumiendo que "más comprada" se refiere a la cantidad de unidades. La función `ROW_NUMBER()` con `PARTITION BY` filtra eficientemente para quedarse solo con la categoría #1 de cada cliente.
4. **Filtro temporal en ambas CTEs:** Es crucial poner el filtro de los últimos 6 meses y `status = 'completed'` en *ambas* consultas CTE para que la categoría más comprada coincida exactamente con el mismo periodo de tiempo de las métricas.
5. **LEFT JOIN final:** Se usa un `LEFT JOIN` por si acaso (aunque en la práctica rara vez pasará) un cliente tenga órdenes completas pero no tenga items asociados en el sistema.