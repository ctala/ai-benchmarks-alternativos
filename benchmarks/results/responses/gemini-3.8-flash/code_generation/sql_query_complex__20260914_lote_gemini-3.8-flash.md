# Gemini 3.8 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 14.138s | tokens_per_second: 138.5
- input_tokens: 160 | output_tokens: 1958
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, cumpliendo con todos los requisitos de la instrucción original.

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

Aquí tienes la consulta en SQL estándar (compatible con PostgreSQL). 

Se utiliza Common Table Expressions (CTEs) para evitar el problema común del *fan-out* (duplicación de totales de las órdenes al hacer `JOIN` directo con `order_items`):

```sql
WITH customer_metrics AS (
    -- 1. Métricas de órdenes y revenue a nivel cliente
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
ranked_categories AS (
    -- 2. Ranking de categorías por cantidad comprada por cliente
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS ranking
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unión de métricas con su categoría #1 y filtrado Top 10
SELECT 
    cm.nombre,
    cm.email,
    cm.pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN ranked_categories rc 
    ON cm.customer_id = rc.customer_id 
   AND rc.ranking = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

---

### Detalles clave de la solución:
1. **Separación de granularidades:** Calculamos el revenue directamente desde `orders` en un CTE y los productos desde `order_items` en otro. Si se unieran todas las tablas en un solo `JOIN`, las filas de `orders.total` se multiplicarían por cada item de la orden, inflando el revenue.
2. **Categoría más comprada:** Usamos `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY SUM(oi.quantity) DESC)` para determinar cuál categoría tuvo mayor volumen de unidades por cliente y seleccionamos solo el puesto `1`.
3. **Filtro de 6 meses y estado:** Aplicado de forma consistente en ambos CTEs (`status = 'completed'` y `created_at >= CURRENT_DATE - INTERVAL '6 months'`).
4. **Compatibilidad:** Si utilizas **MySQL**, cambia `INTERVAL '6 months'` por `INTERVAL 6 MONTH`. En **SQL Server**, usa `DATEADD(month, -6, GETDATE())` y `TOP 10` en lugar de `LIMIT 10`.