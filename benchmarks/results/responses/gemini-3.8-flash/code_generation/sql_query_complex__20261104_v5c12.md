# Gemini 3.8 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 13.975s | tokens_per_second: 139.5
- input_tokens: 160 | output_tokens: 1950
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

Aquí tienes la consulta en SQL estándar (compatible con PostgreSQL). 

Se utilizan CTEs (*Common Table Expressions*) y funciones de ventana para calcular la categoría más comprada (por cantidad de unidades) sin duplicar los totales de las órdenes:

```sql
WITH completed_orders AS (
    -- 1. Filtramos órdenes completadas de los últimos 6 meses
    SELECT 
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 month'
),
customer_stats AS (
    -- 2. Calculamos métricas por cliente y filtramos los que tienen >= 3 órdenes
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    JOIN completed_orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_ranking AS (
    -- 3. Obtenemos el ranking de la categoría más comprada (por suma de cantidad)
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM completed_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
-- 4. Unimos todo y limitamos al Top 10
SELECT 
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_ranking cr 
       ON cs.customer_id = cr.customer_id 
      AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Puntos clave considerados:
1. **Separación de métricas:** Se calculan las métricas monetarias a nivel de `orders` y la categoría a nivel de `order_items` para evitar el problema del *fan-out* (que las sumas de `orders.total` se dupliquen al hacer JOIN con los items).
2. **Criterio de categoría más comprada:** Se determina mediante `SUM(oi.quantity)` (mayor volumen de unidades compradas). En caso de empate, `ROW_NUMBER()` toma una de ellas.
3. **Compatibilidad:** Si utilizas **MySQL**, cambia `CURRENT_DATE - INTERVAL '6 month'` por `NOW() - INTERVAL 6 MONTH`. En **SQL Server**, usa `DATEADD(month, -6, GETDATE())`.