# Gemini 4 Argon — code_generation/sql_query_complex

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 13.646s | tokens_per_second: 71.9
- input_tokens: 187 | output_tokens: 981
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

Para resolver esto de manera óptima y evitar que el revenue se duplique al unir los pedidos con los ítems (un problema común en SQL), la mejor práctica es usar **CTEs (Common Table Expressions)** y **Funciones de Ventana**.

Aquí tienes la consulta escrita en SQL estándar (compatible con **PostgreSQL**, que es el más común). Al final te dejo notas por si usas MySQL o SQL Server.

```sql
WITH recent_completed_orders AS (
    -- 1. Filtramos solo las órdenes completadas de los últimos 6 meses
    SELECT 
        id AS order_id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Calculamos las métricas principales por cliente y filtramos los que tienen >= 3 órdenes
    SELECT 
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(total) AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM recent_completed_orders
    GROUP BY customer_id
    HAVING COUNT(order_id) >= 3
),
category_ranking AS (
    -- 3. Calculamos la categoría más comprada (por cantidad de productos) para esos órdenes
    SELECT 
        rco.customer_id,
        p.category,
        SUM(oi.quantity) AS total_items,
        ROW_NUMBER() OVER (
            PARTITION BY rco.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM recent_completed_orders rco
    JOIN order_items oi ON rco.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY rco.customer_id, p.category
)
-- 4. Unimos todo para el resultado final
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
LEFT JOIN category_ranking cr ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:
1. **`recent_completed_orders` (CTE 1):** Aísla las órdenes válidas (últimos 6 meses y `completed`). Esto hace que el resto de la consulta sea más rápida porque procesa menos datos.
2. **`customer_metrics` (CTE 2):** Calcula el total de órdenes, el revenue y el ticket promedio. Aquí aplicamos el filtro `HAVING COUNT(order_id) >= 3`. Se hace separado de `order_items` para no inflar el `SUM(total)`.
3. **`category_ranking` (CTE 3):** Une las órdenes válidas con sus ítems y productos. Usa `ROW_NUMBER()` para asignar el número `1` a la categoría de la cual el cliente ha comprado más unidades (`SUM(oi.quantity)`). *Nota: Si prefieres que la categoría más comprada sea por dinero gastado y no por cantidad de unidades, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)`.*
4. **`SELECT` Final:** Une los datos del cliente con sus métricas y su categoría número 1 (`cr.rn = 1`), ordena de mayor a menor revenue y corta en el Top 10.

### Ajustes según tu motor de Base de Datos:
* **Si usas MySQL:** Cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
* **Si usas SQL Server (T-SQL):** Cambia el filtro de fecha por `DATEADD(month, -6, GETDATE())` y en lugar de `LIMIT 10` al final, pon `SELECT TOP 10` al inicio del último bloque.
* **Si usas BigQuery:** Cambia el filtro de fecha por ` DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`.