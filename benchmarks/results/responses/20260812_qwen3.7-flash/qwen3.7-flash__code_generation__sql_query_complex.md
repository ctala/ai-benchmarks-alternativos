# Qwen 3.7 Flash — code_generation/sql_query_complex

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 35.787s | tokens_per_second: 136.4
- input_tokens: 161 | output_tokens: 4881
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

Aquí tienes la consulta optimizada usando **CTEs (Common Table Expressions)** para mayor legibilidad y compatibilidad con bases de datos modernas (PostgreSQL, MySQL 8+, SQL Server, SQLite):

```sql
WITH filtered_orders AS (
    -- 1. Filtrar órdenes completadas de los últimos 6 meses y unir detalles
    SELECT 
        o.id AS order_id,
        o.customer_id,
        p.category,
        oi.quantity,
        (oi.quantity * oi.unit_price) AS line_total
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6' MONTH  -- Ver nota de dialecto abajo
),
customer_metrics AS (
    -- 2. Métricas agregadas por cliente
    SELECT 
        customer_id,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(line_total) AS total_revenue,
        ROUND(SUM(line_total) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS avg_order_value
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(DISTINCT order_id) >= 3
),
category_totals AS (
    -- 3. Cantidad total comprada por categoría y cliente
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS total_qty
    FROM filtered_orders
    GROUP BY customer_id, category
),
category_ranking AS (
    -- 4. Ordenar categorías por cantidad y asignar ranking
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_qty DESC) as rn
    FROM category_totals
),
best_category AS (
    -- 5. Quedarse solo con la categoría #1 por cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_ranking
    WHERE rn = 1
)
-- 6. Consulta final
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    bc.categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
LEFT JOIN best_category bc ON cm.customer_id = bc.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **Filtro de fecha**: 
   - `CURRENT_DATE - INTERVAL '6' MONTH` funciona en **PostgreSQL** y **SQLite**.
   - Para **MySQL**, cámbialo por: `o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`
   - Para **SQL Server**: `o.created_at >= DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))`

2. **Cálculo del revenue**: Se usa `SUM(oi.quantity * oi.unit_price)` en lugar de `o.total` para garantizar precisión granular y consistencia con el cálculo de la categoría más comprada. Si prefieres usar el campo `total` de la tabla `orders`, simplemente reemplaza `line_total` por `o.total`.

3. **`categoria_mas_comprada`**: Se calcula basándose en **cantidad de unidades** (`SUM(quantity)`). Si prefieres que sea por **monto facturado** por categoría, cambia `SUM(quantity)` por `SUM(line_total)` en `category_totals` y ajusta el `ORDER BY` en `category_ranking`.

4. **Seguridad en división**: `NULLIF(COUNT(...), 0)` evita errores de división por cero en casos edge, aunque el `HAVING` ya garantiza ≥3 órdenes.

5. **Compatibilidad**: Usa `LEFT JOIN` para `best_category` por si un cliente no tiene registros en `order_items` (imposible dada la lógica actual, pero buena práctica). La ventana `ROW_NUMBER()` es estándar en SQL moderno y eficiente para este tipo de análisis.