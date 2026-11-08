# GLM 5.2 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 23.023s | tokens_per_second: 102.4
- input_tokens: 156 | output_tokens: 2357
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

Aquí tienes la query SQL para obtener el resultado que buscas. 

Para resolver el desafío de obtener la "categoría más comprada", utilicé CTEs (Common Table Expressions) y la función de ventana `ROW_NUMBER()`. Además, usé la columna `orders.total` para calcular los ingresos, asumiendo que ya contiene el total correcto de la orden.

```sql
WITH CustomerMetrics AS (
    -- Calculamos las métricas base por cliente en los últimos 6 meses
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / COUNT(o.id) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months' -- Sintaxis estándar (PostgreSQL/MySQL)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryRanking AS (
    -- Calculamos la cantidad de productos comprados por categoría para cada cliente
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER(
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
TopCategory AS (
    -- Seleccionamos solo la categoría número 1 (la más comprada) por cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM CategoryRanking
    WHERE rn = 1
)
-- Unimos todo y aplicamos el límite final
SELECT
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM CustomerMetrics cm
LEFT JOIN TopCategory tc ON cm.customer_id = tc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Notas sobre la implementación:
1. **Filtro de fechas:** La sintaxis `NOW() - INTERVAL '6 months'` funciona en PostgreSQL y MySQL. Si usas **SQL Server**, debes cambiar esa línea por `o.created_at >= DATEADD(month, -6, GETDATE())`.
2. **Cálculo de Revenue:** Se utilizó `SUM(o.total)` directamente de la tabla `orders`. Si por algún motivo el campo `total` no fuera confiable y debieras calcularlo desde cero, habría que hacer un `JOIN` con `order_items` y sumar `quantity * unit_price`.
3. **Categoría más comprada:** Se definió "más comprada" como aquella categoría donde el cliente adquirió la mayor cantidad de unidades totales (`SUM(oi.quantity)`). Si dos categorías empatan, `ROW_NUMBER()` elegirá una arbitrariamente. 
4. **LEFT JOIN final:** Se usa un `LEFT JOIN` con la categoría por si existiera un cliente que cumple los requisitos pero, por algún motivo de integridad de datos, no tiene items en sus órdenes (aunque en la práctica no debería pasar).