# Qwen 3.7 Max — code_generation/sql_query_complex

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.31 | quality: 9.44
- latency_total: 61.487s | tokens_per_second: 57.6
- input_tokens: 161 | output_tokens: 3542
- judge_score: 4.6 | justificación: 

## Respuesta completa

Para resolver este problema de manera limpia y eficiente, lo ideal es utilizar **CTEs (Common Table Expressions o cláusulas `WITH`)**. Esto nos permite separar el cálculo de las métricas generales del cliente y el cálculo de la categoría más comprada (que requiere funciones de ventana).

Aquí tienes la query (escrita en sintaxis estándar/PostgreSQL):

```sql
WITH CustomerMetrics AS (
    -- 1. Calculamos las métricas principales y filtramos las condiciones base
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months' 
    GROUP BY 
        c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryRanking AS (
    -- 2. Calculamos la categoría más comprada por cada cliente en el mismo periodo
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY 
        o.customer_id, p.category
)
-- 3. Unimos todo y formateamos el resultado final
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM CustomerMetrics cm
LEFT JOIN CategoryRanking cr 
    ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY 
    cm.total_revenue DESC
LIMIT 10;
```

### 💡 Notas importantes sobre la Query:

1. **Fechas (Dialectos SQL):** 
   La función para restar 6 meses varía según el motor de base de datos que estés usando. En la query usé la sintaxis de **PostgreSQL**. Si usas otro motor, cambia la línea del `WHERE`:
   * **MySQL:** `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   * **SQL Server:** `o.created_at >= DATEADD(month, -6, GETDATE())`
   * **BigQuery:** `o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`

2. **Cálculo del Revenue:** 
   He utilizado `SUM(o.total)` asumiendo que la columna `total` en la tabla `orders` es la fuente de la verdad para los ingresos (revenue). Si en tu modelo de negocio `orders.total` incluye impuestos/envíos y prefieres el ingreso neto por productos, deberías cambiarlo por `SUM(oi.quantity * oi.unit_price)` uniendo las tablas de items.

3. **Empates en Categorías (`ROW_NUMBER`):**
   En el CTE `CategoryRanking`, si un cliente compra exactamente la misma cantidad de productos en dos categorías distintas, `ROW_NUMBER()` forzará que se elija solo una (en este caso, la que venga primero alfabéticamente gracias al `p.category ASC` en el `ORDER BY`).

4. **Filtro de 3 órdenes:**
   Se aplica en el primer CTE usando `HAVING COUNT(o.id) >= 3`. Esto asegura que el cliente se descarte *antes* de intentar calcular su categoría favorita, optimizando el rendimiento de la query.