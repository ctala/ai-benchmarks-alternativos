# GLM 5 (NIM) — code_generation/sql_query_complex

- model_id: `z-ai/glm5`
- success: True  | final: 7.4 | quality: 9.72
- latency_total: 155.265s | tokens_per_second: 5.5
- input_tokens: 146 | output_tokens: 854
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query SQL. Para obtener la categoría más comprada de forma eficiente sin duplicar el revenue por cliente, utilizé una CTE (Common Table Expression) que calcula ese dato aparte y luego lo une al resto de la información.

```sql
WITH CustomerCategories AS (
    -- Subconsulta para encontrar la categoría con mayor cantidad de unidades compradas por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
CustomerStats AS (
    -- Subconsulta para calcular las métricas principales y poder filtrar antes del JOIN final
    SELECT 
        o.customer_id,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id
    HAVING COUNT(DISTINCT o.id) >= 3
)
SELECT 
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND((cs.total_revenue / cs.total_orders), 2) AS avg_order_value,
    cc.category AS categoria_mas_comprada
FROM CustomerStats cs
JOIN customers c ON cs.customer_id = c.id
LEFT JOIN CustomerCategories cc ON cs.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la query:

1. **CTE `CustomerCategories`**: Calcula el total de unidades compradas por cliente y por categoría. Usamos `ROW_NUMBER()` particionado por cliente y ordenado de forma descendente por cantidad. Al hacer `cc.rn = 1` en el JOIN final, nos aseguramos de traer solo la categoría favorita. En caso de empate, toma una aleatoriamente (si quisieras que trajera todas las empatadas, cambiarías `ROW_NUMBER` por `RANK`).
2. **CTE `CustomerStats`**: Agrupa las órdenes completadas de los últimos 6 meses para sacar el conteo de órdenes y el revenue total. Aquí aplicamos el `HAVING COUNT(DISTINCT o.id) >= 3` para descartar a los clientes con menos de 3 órdenes. *Nota: Usamos `COUNT(DISTINCT o.id)` por seguridad, en caso de que un order_id se repita por algún error en los items.*
3. **Cálculo de `avg_order_value`**: Se calcula dividiendo `total_revenue` entre `total_orders` directamente en el SELECT para no duplicar datos y redondeando a 2 decimales con `ROUND`.
4. **Filtro de fechas**: `CURRENT_DATE - INTERVAL '6 months'` filtra exactamente los últimos 6 meses desde la fecha actual. *(Nota: Si usas SQL Server, la sintaxis sería `DATEADD(month, -6, GETDATE())`)*.
5. **`LEFT JOIN` con `CustomerCategories`**: Se usa LEFT JOIN por si acaso existe un cliente que cumpla con los 3 órdenes pero no tenga items asociados a categorías (caso extremo de inconsistencia de datos), así no se excluye del Top 10.
6. **`LIMIT 10`**: Muestra solo los 10 primeros. *(Si usas SQL Server, debes cambiarlo por `TOP 10` al inicio del SELECT principal)*.