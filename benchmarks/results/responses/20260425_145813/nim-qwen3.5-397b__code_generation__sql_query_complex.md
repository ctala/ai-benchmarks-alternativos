# Qwen 3.5 397B (NIM) — code_generation/sql_query_complex

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.6 | quality: 9.72
- latency_total: 26.237s | tokens_per_second: 35.4
- input_tokens: 154 | output_tokens: 928
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL optimizada para resolver tu requerimiento.

### Lógica de la solución:
1.  **Filtrado de tiempo y estado**: Se filtran las órdenes con `status = 'completed'` y cuya fecha (`created_at`) sea dentro de los últimos 6 meses.
2.  **Agregación por cliente**: Se calcula el total de órdenes, el ingreso total (sumando el total de la orden) y el valor promedio por orden.
3.  **Categoría más comprada**: Se utiliza una subconsulta o CTE intermedia para contar cuántos ítems de cada categoría ha comprado cada cliente y seleccionar la de mayor frecuencia (`ROW_NUMBER` o `LIMIT 1` por grupo).
4.  **Filtro final**: Se aplica `HAVING` para asegurar que solo aparezcan clientes con 3 o más órdenes.
5.  **Ordenamiento y Limite**: Se ordena por ingresos descendentes y se toma el Top 10.

*Nota: La sintaxis de fechas (`INTERVAL '6 MONTH'`) corresponde a PostgreSQL/MySQL. Si usas SQL Server, avísame para ajustar la función de fecha.*

```sql
WITH filtered_orders AS (
    -- Paso 1: Filtrar órdenes completadas de los últimos 6 meses
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total AS order_total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 MONTH'
),
customer_stats AS (
    -- Paso 2: Calcular métricas por cliente (Total Orders, Revenue, Avg)
    SELECT 
        fo.customer_id,
        COUNT(*) AS total_orders,
        SUM(fo.order_total) AS total_revenue,
        AVG(fo.order_total) AS avg_order_value
    FROM filtered_orders fo
    GROUP BY fo.customer_id
    HAVING COUNT(*) >= 3 -- Solo clientes con al menos 3 órdenes
),
category_counts AS (
    -- Paso 3: Contar cantidad de items por categoría para cada cliente
    SELECT 
        fo.customer_id,
        p.category,
        COUNT(*) AS category_count,
        ROW_NUMBER() OVER (PARTITION BY fo.customer_id ORDER BY COUNT(*) DESC, p.category ASC) as rn
    FROM filtered_orders fo
    JOIN order_items oi ON fo.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
),
top_category_per_customer AS (
    -- Paso 4: Seleccionar solo la categoría #1 por cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_counts
    WHERE rn = 1
)
-- Consulta Final
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tcc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON cs.customer_id = c.id
LEFT JOIN top_category_per_customer tcc ON cs.customer_id = tcc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Consideraciones importantes:
*   **Sintaxis de Fechas**: La parte `NOW() - INTERVAL '6 MONTH'` es estándar en **PostgreSQL** y **MySQL**. Si estás usando **SQL Server**, cámbialo por `DATEADD(MONTH, -6, GETDATE())`. Si usas **Oracle**, usa `ADD_MONTHS(SYSDATE, -6)`.
*   **Empates en categorías**: En la columna `categoria_mas_comprada`, si un cliente tiene dos categorías con la misma cantidad de compras, la consulta selecciona la que tenga el nombre alfabéticamente menor (gracias a `p.category ASC` en el `ROW_NUMBER`) para evitar duplicados.
*   **Cálculo de Revenue**: Se asume que la columna `total` en la tabla `orders` es fiable. Si prefieres calcularlo sumando `quantity * unit_price` de `order_items`, avísame para ajustar la lógica del CTE `customer_stats`.