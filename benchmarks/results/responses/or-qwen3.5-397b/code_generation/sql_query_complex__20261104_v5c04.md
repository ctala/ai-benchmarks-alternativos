# Qwen 3.5 397B — code_generation/sql_query_complex

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 72.819s | tokens_per_second: 61.5
- input_tokens: 161 | output_tokens: 4481
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')


## Respuesta completa

Aquí tienes la consulta SQL optimizada utilizando **CTEs (Common Table Expressions)** para mantener la lógica clara y evitar duplicar datos al calcular el revenue vs. la categoría.

Esta consulta está escrita en dialecto **MySQL**. Si usas PostgreSQL, verás la nota al final sobre la función de fecha.

```sql
WITH valid_orders AS (
    -- 1. Filtrar órdenes completas de los últimos 6 meses
    SELECT 
        id, 
        customer_id, 
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),
customer_metrics AS (
    -- 2. Calcular métricas por cliente (Revenue y Conteo)
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(vo.id) AS total_orders,
        SUM(vo.total) AS total_revenue
    FROM customers c
    JOIN valid_orders vo ON c.id = vo.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(vo.id) >= 3  -- Filtro de mínimas 3 órdenes
),
category_ranking AS (
    -- 3. Determinar la categoría más comprada por cliente
    SELECT
        vo.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY vo.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM valid_orders vo
    JOIN order_items oi ON vo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY vo.customer_id, p.category
)
-- 4. Unir todo y mostrar resultados finales
SELECT
    cm.name AS nombre,
    cm.email AS email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    (cm.total_revenue / cm.total_orders) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN category_ranking cr ON cm.id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`valid_orders`**: Aislamos primero las órdenes que cumplen los criterios de tiempo y estado. Esto evita tener que repetir el `WHERE` en varias partes y mejora el rendimiento.
2.  **`customer_metrics`**: Calculamos el revenue y el conteo de órdenes usando la tabla `orders` directamente. **Importante:** No unimos `order_items` aquí para evitar multiplicar el `total` de la orden si hay varios productos.
3.  **`category_ranking`**: Aquí sí unimos `order_items` y `products`. Usamos `ROW_NUMBER()` para numerar las categorías por cantidad de productos comprados (`SUM(oi.quantity)`) por cada cliente y quedarnos solo con la primera (`rn = 1`).
4.  **`SELECT` Final**: Unimos las métricas del cliente con su categoría top, calculamos el promedio y ordenamos.

### Nota para PostgreSQL:
Si tu base de datos es **PostgreSQL**, cambia la línea de la fecha en el primer CTE por:
```sql
AND created_at >= CURRENT_DATE - INTERVAL '6 months'
```
(Y asegúrate de que los cálculos de promedio manejen decimales correctamente, ej: `cm.total_revenue::NUMERIC / cm.total_orders`).