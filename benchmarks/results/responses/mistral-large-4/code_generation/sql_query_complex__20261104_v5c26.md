# Mistral Large 4.0 — code_generation/sql_query_complex

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 39.271s | tokens_per_second: 81.0
- input_tokens: 156 | output_tokens: 3180
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

Aquí tienes la query usando **CTEs** (Common Table Expressions) y **window functions**, compatible con PostgreSQL 8.4+, MySQL 8.0+, SQL Server y Oracle (con ajustes de fecha según tu motor):

```sql
WITH ordenes_recientes AS (
    -- 1. Filtrar solo órdenes completadas de los últimos 6 meses
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'  -- PostgreSQL
      -- AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH) -- MySQL
      -- AND o.created_at >= DATEADD(month, -6, GETDATE())     -- SQL Server
      -- AND o.created_at >= ADD_MONTHS(SYSDATE, -6)            -- Oracle
),

estadisticas_clientes AS (
    -- 2. Calcular métricas por cliente (solo los que tienen >= 3 órdenes)
    SELECT
        customer_id,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(DISTINCT order_id) >= 3
),

categorias_por_cliente AS (
    -- 3. Calcular cuánto compró de cada categoría (por cantidad de items)
    SELECT
        or_.customer_id,
        p.category,
        SUM(oi.quantity) AS total_items,
        -- Si prefieres medir por revenue en lugar de cantidad, usa:
        -- SUM(oi.quantity * oi.unit_price) AS total_spent,
        ROW_NUMBER() OVER (
            PARTITION BY or_.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM ordenes_recientes or_
    JOIN order_items oi ON or_.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY or_.customer_id, p.category
),

categoria_top AS (
    -- 4. Seleccionar solo la categoría #1 de cada cliente
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM categorias_por_cliente
    WHERE rn = 1
)

-- 5. Query final con los datos del cliente
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    ec.total_orders,
    ROUND(ec.total_revenue, 2) AS total_revenue,
    ROUND(ec.avg_order_value, 2) AS avg_order_value,
    ct.categoria_mas_comprada
FROM estadisticas_clientes ec
JOIN customers c ON ec.customer_id = c.id
LEFT JOIN categoria_top ct ON ec.customer_id = ct.customer_id
ORDER BY ec.total_revenue DESC
LIMIT 10;
```

### Notas importantes:

1. **Filtro de tiempo**: El filtro de "últimos 6 meses" se aplica **antes** de contar las órdenes, por lo que los clientes necesitan 3+ órdenes completadas *dentro de ese período*.

2. **Cálculo de revenue**: Usé `orders.total` directamente. Si prefieres calcularlo desde los items (más preciso si hay descuentos aplicados a nivel de item), reemplaza `SUM(total)` por:
   ```sql
   SUM((SELECT SUM(quantity * unit_price) FROM order_items WHERE order_id = o.id))
   ```
   O mejor, haz el cálculo en el CTE `estadisticas_clientes` haciendo join con `order_items`.

3. **Categoría más comprada**: Está calculada por **cantidad de items** (`SUM(quantity)`). Si quieres por **dinero gastado**, cambia el `ORDER BY` en la window function a `SUM(oi.quantity * oi.unit_price) DESC`.

4. **Empates en categorías**: Si un cliente tiene dos categorías con la misma cantidad, `ROW_NUMBER()` elegirá una arbitrariamente. Si quieres mostrar todas las empatadas, usa `RANK()` en lugar de `ROW_NUMBER()` (pero esto devolvería múltiples filas por cliente).

5. **Redondeo**: Usé `ROUND(..., 2)` para que los valores monetarios se vean limpios. Quítalo si necesitas precisión decimal completa.