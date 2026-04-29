# Gemma 4 31B (DGX Spark Q4_K_M) — code_generation/sql_query_complex

- model_id: `gemma4:31b`
- success: True  | final: 7.0 | quality: 9.44
- latency_total: 204.325s | tokens_per_second: 9.3
- input_tokens: 176 | output_tokens: 1905
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para resolver este problema, necesitamos combinar datos de las cuatro tablas. La parte más compleja es obtener la **categoría más comprada**, ya que requiere un ranking interno por cliente.

Aquí tienes la query. He utilizado **CTEs (Common Table Expressions)** para que el código sea legible y modular.

```sql
WITH customer_metrics AS (
    -- 1. Calculamos métricas básicas de pedidos y revenue
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
category_counts AS (
    -- 2. Contamos cuántos productos de cada categoría ha comprado cada cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as items_bought,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank_category
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unimos todo para obtener el resultado final
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN category_counts cc ON cm.customer_id = cc.customer_id
WHERE cc.rank_category = 1 -- Solo nos quedamos con la categoría más comprada
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación detallada de la lógica:

1.  **`customer_metrics` (CTE):**
    *   Filtramos los pedidos por `status = 'completed'` y la fecha (`INTERVAL '6 months'`).
    *   Agrupamos por cliente para calcular la suma del revenue, el conteo de órdenes y el promedio.
    *   Aplicamos el filtro `HAVING COUNT(o.id) >= 3` para cumplir con la condición de mínimo 3 órdenes.

2.  **`category_counts` (CTE):**
    *   Hacemos un join entre `orders`, `order_items` y `products` para llegar a la categoría.
    *   Usamos la función de ventana `ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC)`. Esto le asigna el número `1` a la categoría que más veces se repite para cada cliente.

3.  **Consulta Final:**
    *   Unimos ambas tablas temporales mediante el `customer_id`.
    *   Filtramos `WHERE cc.rank_category = 1` para asegurar que solo aparezca una categoría por cliente (la principal).
    *   Ordenamos por `total_revenue DESC` y limitamos a los 10 mejores.

### Notas sobre compatibilidad:
*   **PostgreSQL:** La query funciona tal cual.
*   **MySQL:** Deberías cambiar `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
*   **SQL Server:** Deberías usar `DATEADD(month, -6, GETDATE())` y cambiar el `LIMIT 10` por un `SELECT TOP 10` al inicio.