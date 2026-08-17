# Gemma 4 12B (Spark llama-server, reasoning) — code_generation/sql_query_complex

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.96 | quality: 9.44
- latency_total: 91.12s | tokens_per_second: 25.6
- input_tokens: 176 | output_tokens: 2331
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para resolver este problema, la mejor forma es utilizar **CTEs (Common Table Expressions)**. Esto nos permite separar la lógica del cálculo de métricas generales (revenue, promedio) de la lógica para determinar la "categoría más comprada", que requiere una agregación distinta.

Aquí tienes la query (escrita en un estándar compatible con PostgreSQL/MySQL):

```sql
WITH customer_base_metrics AS (
    -- Primero calculamos las métricas básicas y filtramos por tiempo y cantidad de órdenes
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
    -- Calculamos cuántas veces cada cliente compró en cada categoría
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as items_count,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank_cat
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT 
    bm.name,
    bm.email,
    bm.country,
    bm.total_orders,
    bm.total_revenue,
    bm.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_base_metrics bm
JOIN category_counts cc ON bm.customer_id = cc.customer_id
WHERE cc.rank_cat = 1 -- Nos quedamos solo con la categoría con más ventas por cliente
ORDER BY bm.total_revenue DESC
LIMIT 10;
```

### Explicación de la solución:

1.  **`customer_base_metrics` (CTE):**
    *   Une `customers` con `orders`.
    *   Filtra por `status = 'completed'` y el periodo de los últimos 6 meses.
    *   Usa `GROUP BY` para calcular el `SUM` (revenue), `COUNT` (total de órdenes) y `AVG` (valor promedio).
    *   **Filtro Crítico:** El `HAVING COUNT(o.id) >= 3` asegura que solo procesamos a clientes con al menos 3 órdenes cumplidas.

2.  **`category_counts` (CTE):**
    *   Aquí unimos las tablas de productos y artículos de orden para saber qué categorías están comprando.
    *   Utilizamos una **Window Function** (`ROW_NUMBER() OVER(...)`). Esto asigna el número "1" a la categoría que más veces aparece para cada cliente. Si un cliente compró 5 veces "Electrónica" y 2 veces "Hogar", "Electrónica" será la número 1.

3.  **Query Final:**
    *   Une ambas tablas usando el ID del cliente.
    *   Filtra por `rank_cat = 1` para que en la columna `categoria_mas_comprada` solo aparezca una (la principal).
    *   Ordena por el revenue total de forma descendente y limita el resultado a los 10 mejores.

**Nota sobre la sintaxis de fecha:**
*   Si usas **PostgreSQL**, `CURRENT_DATE - INTERVAL '6 months'` es correcto.
*   Si usas **MySQL**, podrías necesitar `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
*   Si usas **SQL Server**, sería `DATEADD(month, -6, GETDATE())`.