# Gemini 2.5 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.68 | quality: 9.24
- latency_total: 7.707s | tokens_per_second: 179.6
- input_tokens: 161 | output_tokens: 1384
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes la query SQL que cumple con tus requisitos:

```sql
WITH CustomerRevenue AS (
    SELECT
        c.id AS customer_id,
        c.name AS customer_name,
        c.email AS customer_email,
        c.country AS customer_country,
        SUM(o.total) AS total_revenue,
        COUNT(o.id) AS total_orders,
        AVG(o.total) AS avg_order_value
    FROM
        customers c
    JOIN
        orders o ON c.id = o.customer_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE('now', '-6 months') -- Para SQLite
        -- AND o.created_at >= GETDATE() - INTERVAL '6 MONTH' -- Para PostgreSQL
        -- AND o.created_at >= DATEADD(month, -6, GETDATE()) -- Para SQL Server
        -- AND o.created_at >= CURDATE() - INTERVAL 6 MONTH -- Para MySQL
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(o.id) >= 3
),
CustomerTopCategory AS (
    SELECT
        c.id AS customer_id,
        p.category AS top_category,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY COUNT(p.category) DESC, SUM(oi.quantity * oi.unit_price) DESC) AS rn
    FROM
        customers c
    JOIN
        orders o ON c.id = o.customer_id
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE('now', '-6 months') -- Para SQLite
        -- AND o.created_at >= GETDATE() - INTERVAL '6 MONTH' -- Para PostgreSQL
        -- AND o.created_at >= DATEADD(month, -6, GETDATE()) -- Para SQL Server
        -- AND o.created_at >= CURDATE() - INTERVAL 6 MONTH -- Para MySQL
    GROUP BY
        c.id, p.category
)
SELECT
    cr.customer_name AS nombre,
    cr.customer_email AS email,
    cr.customer_country AS pais,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    ctc.top_category AS categoria_mas_comprada
FROM
    CustomerRevenue cr
LEFT JOIN
    CustomerTopCategory ctc ON cr.customer_id = ctc.customer_id AND ctc.rn = 1
ORDER BY
    cr.total_revenue DESC
LIMIT 10;
```

**Explicación de la Query:**

1.  **`CustomerRevenue` CTE (Common Table Expression):**
    *   Calcula el `total_revenue`, `total_orders` y `avg_order_value` para cada cliente.
    *   `JOIN` `customers` con `orders`.
    *   `WHERE o.status = 'completed'`: Filtra solo las órdenes completadas.
    *   `AND o.created_at >= DATE('now', '-6 months')`: Filtra las órdenes de los últimos 6 meses. **IMPORTANTE:** La sintaxis para calcular "hace 6 meses" puede variar ligeramente según el sistema de base de datos que estés utilizando (SQLite, PostgreSQL, MySQL, SQL Server, etc.). He incluido ejemplos para varios.
    *   `GROUP BY c.id, c.name, c.email, c.country`: Agrupa los resultados por cliente.
    *   `HAVING COUNT(o.id) >= 3`: Filtra solo a los clientes que tienen al menos 3 órdenes completadas en el período.

2.  **`CustomerTopCategory` CTE:**
    *   Identifica la categoría de producto más comprada por cada cliente en los últimos 6 meses (solo órdenes completadas).
    *   `JOIN` `customers`, `orders`, `order_items` y `products`.
    *   `WHERE o.status = 'completed' AND o.created_at >= DATE('now', '-6 months')`: Mismos filtros de tiempo y estado que antes.
    *   `GROUP BY c.id, p.category`: Agrupa por cliente y categoría para contar las ocurrencias.
    *   `ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY COUNT(p.category) DESC, SUM(oi.quantity * oi.unit_price) DESC) AS rn`: Esta es una función de ventana.
        *   `PARTITION BY c.id`: La numeración se reinicia para cada cliente.
        *   `ORDER BY COUNT(p.category) DESC`: Ordena las categorías de cada cliente por la frecuencia con la que se compraron (la más frecuente primero).
        *   `, SUM(oi.quantity * oi.unit_price) DESC`: En caso de empate en la frecuencia, desempata por el revenue total generado por esa categoría para el cliente.
        *   `rn = 1`: Esto nos permite seleccionar solo la categoría principal para cada cliente en el `LEFT JOIN` final.

3.  **`SELECT` final:**
    *   Selecciona todas las columnas requeridas del `CustomerRevenue` CTE.
    *   `LEFT JOIN CustomerTopCategory ctc ON cr.customer_id = ctc.customer_id AND ctc.rn = 1`: Se une con el CTE de la categoría principal para obtener la `categoria_mas_comprada`. El `LEFT JOIN` asegura que se incluyan clientes incluso si no se pudo determinar una categoría principal (aunque con los filtros actuales, todos deberían tenerla).
    *   `ORDER BY cr.total_revenue DESC`: Ordena los resultados por el revenue total de forma descendente.
    *   `LIMIT 10`: Restringe los resultados a los 10 principales clientes.

**Asegúrate de ajustar la sintaxis de la fecha (`DATE('now', '-6 months')`) según el sistema de base de datos específico que estés utilizando.** He proporcionado comentarios para los más comunes.