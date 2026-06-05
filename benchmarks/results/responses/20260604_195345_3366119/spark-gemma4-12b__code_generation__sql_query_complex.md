# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/sql_query_complex

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.33 | quality: 9.72
- latency_total: 32.159s | tokens_per_second: 25.3
- input_tokens: 173 | output_tokens: 815
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver esta consulta, necesitamos realizar varios JOINs entre las tablas, filtrar por fecha y estado, y utilizar una **Common Table Expression (CTE)** o una subconsulta para calcular la "categoría más comprada", ya que es un valor agregado que requiere una agregación distinta a la del revenue.

Aquí tienes la query en SQL estándar:

```sql
WITH CustomerStats AS (
    -- Primero calculamos las métricas básicas por cliente
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
    -- Calculamos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as purchase_count,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank_desc
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
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
WHERE cr.rank_desc = 1  -- Nos quedamos solo con la categoría #1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`CustomerStats` (CTE):**
    *   Filtra las órdenes de los últimos 6 meses y que tengan estado `completed`.
    *   Agrupa por cliente para obtener el conteo de órdenes, la suma del revenue y el promedio.
    *   Aplica el filtro `HAVING COUNT(o.id) >= 3` para cumplir con tu requisito de mínimo 3 órdenes.

2.  **`CategoryRanking` (CTE):**
    *   Cruza las órdenes con los productos para saber qué categorías compró cada cliente.
    *   Usa una función de ventana `ROW_NUMBER() OVER(...)`. Esto asigna el número "1" a la categoría que más veces aparece en las compras de ese cliente específico.

3.  **Query Final:**
    *   Une ambas tablas.
    *   Filtra `rank_desc = 1` para asegurar que solo aparezca una categoría (la más comprada).
    *   Ordena por `total_revenue` de forma descendente y limita a los 10 mejores.

**Nota sobre dialectos:**
*   Si usas **MySQL**, el intervalo de fecha sería `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
*   Si usas **SQL Server**, sería `DATEADD(month, -6, GETDATE())`.
*   La query de arriba funciona perfectamente en **PostgreSQL**.