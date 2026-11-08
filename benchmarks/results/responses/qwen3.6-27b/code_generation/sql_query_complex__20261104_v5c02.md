# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/sql_query_complex

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 70.564s | tokens_per_second: 64.7
- input_tokens: 161 | output_tokens: 4568
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

Aquí tienes una query optimizada usando **CTEs (Common Table Expressions)** para mantener la legibilidad y el rendimiento. Está escrita en sintaxis estándar compatible con PostgreSQL/MySQL, con notas al final para ajustes de dialecto.

```sql
WITH recent_completed_orders AS (
    -- 1. Filtramos solo órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Calculamos métricas agregadas por cliente
    SELECT 
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM recent_completed_orders
    GROUP BY customer_id
    HAVING COUNT(id) >= 3  -- Filtro: mínimo 3 órdenes completadas
),
customer_category_stats AS (
    -- 3. Calculamos la cantidad total comprada por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM recent_completed_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
),
top_category AS (
    -- 4. Seleccionamos la categoría con mayor cantidad comprada por cliente
    SELECT 
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY total_qty DESC) as rn
        FROM customer_category_stats
    ) ranked
    WHERE rn = 1
)
-- 5. Unimos todo y devolvemos el Top 10
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    ROUND(cm.total_revenue, 2) AS total_revenue,
    ROUND(cm.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
LEFT JOIN top_category tc ON cm.customer_id = tc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **Filtro de tiempo**: `NOW() - INTERVAL '6 months'` es sintaxis **PostgreSQL**. Si usas **MySQL**, cámbialo por:  
   `AND created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`
2. **`categoria_mas_comprada`**: Se calcula como la categoría con mayor **cantidad total de unidades** (`SUM(quantity)`). Si prefieres que sea por **ingresos**, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en el CTE `customer_category_stats`.
3. **`ROW_NUMBER()`**: En caso de empate exacto en la categoría más comprada, esta función elige una de forma determinista. Si prefieres incluir todas las empatadas, usa `RANK()` y ajusta el `WHERE rn = 1`.
4. **`LEFT JOIN` en `top_category`**: Se usa para evitar que clientes válidos desaparezcan si por alguna razón no tienen registros en `order_items` o `products`.
5. **Rendimiento**: Asegúrate de tener índices en:
   - `orders(customer_id, status, created_at)`
   - `order_items(order_id, product_id)`
   - `products(id)`

¿Necesitas adaptarla a un motor específico (MySQL, SQL Server, Oracle, etc.) o ajustar la lógica de "categoría más comprada"?