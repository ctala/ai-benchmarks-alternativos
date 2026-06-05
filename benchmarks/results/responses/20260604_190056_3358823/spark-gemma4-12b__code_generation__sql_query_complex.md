# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/sql_query_complex

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.98 | quality: 9.44
- latency_total: 84.304s | tokens_per_second: 25.2
- input_tokens: 176 | output_tokens: 2123
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para resolver este problema, la mejor forma es utilizar **CTEs (Common Table Expressions)**. Esto permite separar la lógica de cálculo de métricas (ventas, promedios) de la lógica de encontrar la categoría más comprada, haciendo la consulta mucho más legible y eficiente.

Aquí tienes la query en SQL (compatible con PostgreSQL, MySQL 8.0+ y SQL Server):

```sql
WITH Customer_Metrics AS (
    -- Paso 1: Calcular métricas básicas por cliente
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
Category_Ranking AS (
    -- Paso 2: Contar productos por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(oi.id) AS category_count,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(oi.id) DESC) as rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- Paso 3: Unir todo y filtrar el Top 10
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM Customer_Metrics cm
JOIN Category_Ranking cr ON cm.customer_id = cr.customer_id
WHERE cr.rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la solución:

1.  **`Customer_Metrics` (CTE):**
    *   Filtra las órdenes por `status = 'completed'` y las limita a los últimos 6 meses.
    *   Agrupa por cliente para obtener el conteo de órdenes, la suma de ingresos (`SUM`) y el promedio (`AVG`).
    *   Utiliza `HAVING COUNT(o.id) >= 3` para cumplir con el requisito de mínimo 3 órdenes.

2.  **`Category_Ranking` (CTE):**
    *   Esta es la parte más compleja: necesitamos saber cuál es la categoría que más veces aparece en las órdenes de cada cliente.
    *   Unimos `orders`, `order_items` y `products`.
    *   Usamos la función de ventana `ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(oi.id) DESC)`. Esto asigna el número "1" a la categoría que más se repite para cada cliente.

3.  **Query Final:**
    *   Unimos ambas tablas usando el `customer_id`.
    *   Filtramos por `rank = 1` para asegurarnos de traer solo la categoría más comprada de cada cliente.
    *   Ordenamos por `total_revenue DESC` y limitamos a los 10 mejores.

**Nota sobre el intervalo de tiempo:** 
Dependiendo de tu motor de base de datos, la sintaxis de fecha puede variar ligeramente:
*   **PostgreSQL:** `CURRENT_DATE - INTERVAL '6 months'`
*   **MySQL:** `DATE_SUB(NOW(), INTERVAL 6 MONTH)`
*   **SQL Server:** `DATEADD(month, -6, GETDATE())`