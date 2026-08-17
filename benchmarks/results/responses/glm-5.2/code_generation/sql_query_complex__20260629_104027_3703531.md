# GLM 5.2 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.29 | quality: 9.72
- latency_total: 37.968s | tokens_per_second: 62.6
- input_tokens: 156 | output_tokens: 2376
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query SQL. He utilizado CTEs (Common Table Expressions) para mantener el código legible y modular, y funciones de ventana (Window Functions) para identificar la categoría más comprada de cada cliente.

Esta query está escrita con sintaxis estándar (compatible con PostgreSQL). Si usas MySQL, solo tendrás que cambiar la función de fecha `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`.

```sql
WITH customer_metrics AS (
    -- Calculamos las métricas principales de los clientes en los últimos 6 meses
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_purchases AS (
    -- Calculamos la cantidad total de productos comprados por categoría por cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
top_category AS (
    -- Filtramos solo la categoría número 1 (la más comprada) para cada cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_purchases
    WHERE rn = 1
)
-- Unimos todo y aplicamos el orden y límite final
SELECT
    cm.name AS nombre,
    cm.email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN top_category tc ON cm.id = tc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Notas sobre el diseño de la query:
1. **Filtrado por estado y fecha:** Se aplicó el filtro de `status = 'completed'` y la fecha de los últimos 6 meses tanto en el cálculo de ingresos como en el de categorías para asegurar que las métricas reflejen exactamente el mismo periodo y tipo de órdenes.
2. **Cálculo de Revenue:** Se utilizó la columna `orders.total` para sumar el revenue y calcular el ticket promedio (`avg_order_value`), ya que es el total final de la orden. 
3. **Categoría más comprada:** Se determinó sumando la cantidad (`quantity`) de los `order_items` agrupados por la categoría del producto. Se usó `ROW_NUMBER()` para rankear las categorías por cliente y quedarnos con la posición 1. En caso de empate en cantidades, `ROW_NUMBER()` elegirá una arbitrariamente. Si quisieras ver empates, tendrías que usar `RANK()`.
4. **LEFT JOIN en la consulta final:** Se usó un `LEFT JOIN` con la categoría principal por si un cliente cumpliera las condiciones (3+ órdenes) pero por alguna razón no tuviera items asociados en `order_items`, no desaparezca de los resultados.