# Qwen 3.5 397B — code_generation/sql_query_complex

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 68.67s | tokens_per_second: 62.7
- input_tokens: 161 | output_tokens: 4307
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la query SQL optimizada utilizando **CTEs (Common Table Expressions)** y **Window Functions** para resolver el requerimiento de manera limpia y eficiente.

*Nota: La sintaxis de fechas (`INTERVAL '6 months'`) está basada en PostgreSQL/Standard SQL. Si usas MySQL, ver la nota al final.*

```sql
WITH orders_filtered AS (
    -- 1. Filtramos las órdenes completas de los últimos 6 meses
    SELECT *
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Calculamos las métricas por cliente y filtramos los que tienen >= 3 órdenes
    SELECT
        o.customer_id,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM orders_filtered o
    GROUP BY o.customer_id
    HAVING COUNT(o.id) >= 3
),
category_ranking AS (
    -- 3. Determinamos la categoría más comprada por cada cliente (usando Window Function)
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders_filtered o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
-- 4. Unimos todo para el resultado final
SELECT
    c.name,
    c.email,
    c.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
JOIN category_ranking cr ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`orders_filtered`**: Aislamos el contexto de tiempo (6 meses) y estado ('completed') en una sola CTE para asegurarnos de que tanto los cálculos de revenue como los de categorías usen exactamente los mismos datos.
2.  **`customer_metrics`**: Agrupamos por cliente para obtener el conteo de órdenes, la suma total y el promedio. El `HAVING` asegura que solo pasen clientes con 3 o más compras.
3.  **`category_ranking`**: Esta es la parte clave para `categoria_mas_comprada`.
    *   Unimos `orders` con `order_items` y `products`.
    *   Agrupamos por cliente y categoría sumando la cantidad (`quantity`).
    *   Usamos `ROW_NUMBER()` particionado por el cliente para rankear sus categorías. La que tenga `rn = 1` es la más comprada.
4.  **Select Final**: Unimos las métricas del cliente, sus datos personales y su categoría top, ordenamos por revenue y limitamos a 10.

### Compatibilidad con Motores de Base de Datos

La función de fecha puede variar según tu motor SQL:

*   **PostgreSQL / Standard SQL:** `created_at >= NOW() - INTERVAL '6 months'`
*   **MySQL / MariaDB:** `created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`
*   **SQL Server:** `created_at >= DATEADD(month, -6, GETDATE())`
*   **SQLite:** `created_at >= DATE('now', '-6 months')`

Ajusta la línea del CTE `orders_filtered` según tu base de datos.