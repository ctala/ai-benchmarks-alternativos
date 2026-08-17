# Tencent Hy3 — code_generation/sql_query_complex

- model_id: `tencent/hy3`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 175.035s | tokens_per_second: 26.5
- input_tokens: 163 | output_tokens: 4634
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

Aquí tienes una consulta SQL que cumple con todos tus requisitos utilizando Common Table Expressions (CTEs) para mantener la lógica organizada y legible.

```sql
WITH ordenes_recientes AS (
    -- 1. Filtramos las órdenes completadas de los últimos 6 meses
    SELECT 
        id, 
        customer_id, 
        total
    FROM orders
    WHERE status = 'completed'
      -- Nota: La función de fecha puede variar según tu motor de base de datos:
      -- MySQL: created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
      -- PostgreSQL / SQL Estándar: created_at >= CURRENT_DATE - INTERVAL '6 months'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
resumen_clientes AS (
    -- 2. Calculamos métricas por cliente y filtramos los que tienen al menos 3 órdenes
    SELECT 
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),
categoria_preferida AS (
    -- 3. Determinamos la categoría más comprada por cada cliente (por valor monetario)
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC
        ) AS rn
    FROM ordenes_recientes o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
-- 4. Unimos todo y seleccionamos las columnas requeridas
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    rc.total_orders,
    rc.total_revenue,
    ROUND(rc.total_revenue / rc.total_orders, 2) AS avg_order_value,
    cp.category AS categoria_mas_comprada
FROM resumen_clientes rc
JOIN customers c ON rc.customer_id = c.id
LEFT JOIN categoria_preferida cp 
    ON rc.customer_id = cp.customer_id 
    AND cp.rn = 1
ORDER BY rc.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:
1. **`ordenes_recientes`**: Filtra las órdenes que están en estado `'completed'` y fueron creadas en los últimos 6 meses.
2. **`resumen_clientes`**: Agrupa por cliente para contar el número de órdenes y sumar el revenue total. La cláusula `HAVING` asegura que solo se incluyan clientes con 3 órdenes o más.
3. **`categoria_preferida`**: Cruza las órdenes con `order_items` y `products` para sumar el gasto por categoría de cada cliente. Usamos `ROW_NUMBER()` para rankear las categorías y quedarnos con la #1 (`rn = 1`).
4. **Consulta final**: Unimos las métricas con la tabla `customers` para obtener nombre, email y país. Se calcula el `avg_order_value` (ticket promedio) dividiendo el revenue total entre la cantidad de órdenes, y se ordena por revenue descendente limitando a 10 resultados.

### Notas:
* **`categoria_mas_comprada`**: En este ejemplo se define como la categoría en la que el cliente gastó más dinero (suma de `quantity * unit_price`). Si quieres definirla por *cantidad de unidades* en lugar de dinero, cambia `ORDER BY SUM(oi.quantity * oi.unit_price) DESC` por `ORDER BY SUM(oi.quantity) DESC` en el CTE `categoria_preferida`.
* **Compatibilidad**: Ajusta la condición de fecha (`created_at >= ...`) según el dialecto SQL que estés utilizando (MySQL, PostgreSQL, SQL Server, etc.).