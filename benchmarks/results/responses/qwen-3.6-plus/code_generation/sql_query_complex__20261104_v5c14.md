# Qwen 3.6 Plus — code_generation/sql_query_complex

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 92.125s | tokens_per_second: 58.0
- input_tokens: 161 | output_tokens: 5341
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada y detallada que cumple con los requisitos especificados.

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

Aquí tienes la query optimizada y legible usando `CTEs` (Common Table Expressions). Está escrita en SQL estándar (compatible con PostgreSQL/MySQL) e incluye comentarios explicativos:

```sql
WITH CustomerMetrics AS (
    -- 1. Métricas base por cliente (últimos 6 meses, solo completadas)
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
CategoryRank AS (
    -- 2. Ranking de categorías por cliente (por cantidad comprada)
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unión final y cálculo del promedio
SELECT 
    cm.name AS nombre,
    cm.email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    ROUND(cm.total_revenue / cm.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM CustomerMetrics cm
JOIN CategoryRank cr 
  ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 🔍 Puntos clave:
1. **`COUNT(DISTINCT o.id)`**: Necesario porque el `JOIN` con `order_items` multiplica las filas por cada producto. Sin `DISTINCT`, contarías líneas de pedido, no órdenes.
2. **`HAVING COUNT(...) >= 3`**: Filtra *después* de agrupar, garantizando que solo se evalúen clientes con ≥3 órdenes completadas en el período.
3. **`ROW_NUMBER() OVER (...)`**: Asigna `1` a la categoría con mayor cantidad comprada por cliente. Si prefieres que sea por **gasto** en lugar de cantidad, cambia `ORDER BY SUM(oi.quantity) DESC` por `ORDER BY SUM(oi.quantity * oi.unit_price) DESC`.
4. **Filtro de fecha**: `CURRENT_DATE - INTERVAL '6 months'` funciona en PostgreSQL y MySQL. Si usas:
   - **SQL Server**: `DATEADD(month, -6, GETDATE())`
   - **Oracle**: `ADD_MONTHS(SYSDATE, -6)`

¿Necesitas adaptarla a un motor de base de datos específico o ajustar la lógica de "categoría más comprada"?