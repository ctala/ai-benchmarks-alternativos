# Gemma 4 31B (NIM) — code_generation/sql_query_complex

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 22.932s | tokens_per_second: 37.6
- input_tokens: 164 | output_tokens: 863
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para lograr este resultado, necesitamos combinar varias tablas y utilizar una **Common Table Expression (CTE)** o una subconsulta para determinar la categoría más comprada por cada cliente, ya que es un cálculo agregado distinto al del revenue.

Aquí tienes la query optimizada:

```sql
WITH CustomerStats AS (
    -- Calculamos métricas generales de ventas por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed' 
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryRanking AS (
    -- Determinamos la categoría más comprada por cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as product_count,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank_cat
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM CustomerStats cs
JOIN CategoryRanking cr ON cs.customer_id = cr.customer_id
WHERE cr.rank_cat = 1 -- Solo tomamos la categoría con el conteo más alto
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación técnica de la solución:

1.  **`CustomerStats` (CTE):** 
    *   Filtra las órdenes por estado `'completed'` y el rango de tiempo de los últimos 6 meses.
    *   Utiliza `HAVING COUNT(o.id) >= 3` para cumplir la condición de clientes recurrentes.
    *   Calcula el revenue total y el promedio por pedido.

2.  **`CategoryRanking` (CTE):**
    *   Aquí es donde resolvemos la "categoría más comprada". Como un cliente puede comprar múltiples categorías, usamos la función de ventana `ROW_NUMBER()`.
    *   `PARTITION BY o.customer_id ORDER BY COUNT(*) DESC` asigna el número `1` a la categoría que más veces aparece en los pedidos de ese cliente específico.

3.  **Consulta Final:**
    *   Une ambas tablas temporales mediante el `customer_id`.
    *   Filtra `cr.rank_cat = 1` para asegurar que solo aparezca una sola categoría (la principal) por cliente.
    *   Ordena por `total_revenue DESC` y limita los resultados a los 10 mejores.

**Nota sobre compatibilidad:**
*   He utilizado `CURRENT_DATE - INTERVAL '6 months'`, que es estándar en **PostgreSQL**. 
*   Si usas **MySQL**, cambia esa línea por: `o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
*   Si usas **SQL Server**, cambia esa línea por: `o.created_at >= DATEADD(month, -6, GETDATE())`.