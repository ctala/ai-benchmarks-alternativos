# GLM 5.2 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.31 | quality: 9.72
- latency_total: 30.15s | tokens_per_second: 70.0
- input_tokens: 156 | output_tokens: 2110
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL. Para mantenerla legible y eficiente, utilicé **CTEs (Common Table Expressions)**. 

La consulta está escrita en sintaxis estándar (PostgreSQL). Si usas MySQL, solo tendrás que cambiar la función de fecha (`CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`).

```sql
WITH CustomerStats AS (
    -- Calcula las métricas principales de los pedidos
    SELECT
        c.id,
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
TopCategories AS (
    -- Calcula la categoría más comprada (por cantidad de unidades) por cliente
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- Consulta final que une todo y aplica el límite y ordenamiento
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM CustomerStats cs
LEFT JOIN TopCategories tc ON cs.id = tc.customer_id AND tc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la consulta:
1. **CTE `CustomerStats`**: Hace un `JOIN` entre `customers` y `orders`. Filtra por `status = 'completed'` y por los últimos 6 meses. Agrupa por cliente y calcula el total de órdenes, el revenue total y el ticket promedio. El `HAVING COUNT(o.id) >= 3` asegura que solo se incluyan clientes con al menos 3 compras.
2. **CTE `TopCategories`**: Hace un `JOIN` entre `orders`, `order_items` y `products`. Agrupa por cliente y categoría, sumando la cantidad (`quantity`) de productos. Usa la función de ventana `ROW_NUMBER()` para rankear las categorías de cada cliente (1 = la más comprada).
3. **Consulta Final**: Selecciona las columnas requeridas, hace un `LEFT JOIN` con la categoría que tenga el rango `1` (la más comprada), ordena por `total_revenue` de forma descendente y limita el resultado a los primeros 10 registros.