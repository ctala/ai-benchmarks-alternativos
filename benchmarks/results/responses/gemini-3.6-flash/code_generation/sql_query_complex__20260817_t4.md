# Gemini 3.6 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 13.453s | tokens_per_second: 180.7
- input_tokens: 161 | output_tokens: 2431
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

Aquí tienes la query SQL utilizando CTEs (*Common Table Expressions*) para mantener el código organizado, legible y eficiente.

Esta solución está optimizada para **PostgreSQL** / **MySQL 8.0+**:

```sql
WITH orders_last_6_months AS (
    -- 1. Filtramos primero las órdenes completadas de los últimos 6 meses
    SELECT 
        id AS order_id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 month'
),

customer_metrics AS (
    -- 2. Calculamos los métricos principales por cliente
    SELECT 
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM orders_last_6_months
    GROUP BY customer_id
    HAVING COUNT(order_id) >= 3 -- Solo clientes con al menos 3 órdenes
),

category_ranks AS (
    -- 3. Obtenemos la cantidad de productos comprados por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders_last_6_months o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)

-- 4. Consulta final uniendo los datos del cliente con sus métricas y categoría top
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    ROUND(cm.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
LEFT JOIN category_ranks cr ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación técnica de la Query:

1. **`orders_last_6_months`**: Aísla las órdenes que cumplen con las condiciones de fecha (`INTERVAL '6 month'`) y estado (`status = 'completed'`).
2. **`customer_metrics`**: Agrupa las órdenes filtradas por cliente, calcula el total de órdenes, el revenue, el promedio de compra (`AVG`), y aplica el filtro `HAVING >= 3`.
3. **`category_ranks`**: Calcula la suma de unidades compradas (`quantity`) por cada cliente en cada categoría. Utiliza la función de ventana `ROW_NUMBER()` para asignarle el puesto `#1` a la categoría más comprada de cada cliente.
4. **Consulta Final**: Une la tabla de clientes con las métricas calculadas y la categoría líder (`cr.rn = 1`), ordena por `total_revenue DESC` y devuelve el **Top 10**.

> **Nota de compatibilidad:** 
> - Si usas **SQL Server (T-SQL)**, cambia `CURRENT_DATE - INTERVAL '6 month'` por `DATEADD(month, -6, GETDATE())` y reemplaza `LIMIT 10` por `TOP 10` en el `SELECT` principal.
> - La categoría más comprada se mide por **cantidad total de unidades** (`quantity`). Si prefieres medirla por monto gastado en esa categoría, solo cambia `ORDER BY SUM(oi.quantity) DESC` por `ORDER BY SUM(oi.quantity * oi.unit_price) DESC` dentro del `OVER()`.