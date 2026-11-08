# Gemini 3.1 Pro — code_generation/sql_query_complex

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 25.92s | tokens_per_second: 110.6
- input_tokens: 160 | output_tokens: 2866
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

Aquí tienes la query SQL. Para resolverlo de la forma más limpia y eficiente, he utilizado **CTEs (Common Table Expressions)**. 

La query se divide en dos partes principales: calcular las métricas base por cliente y calcular cuál es la categoría más comprada por cada uno.

```sql
WITH CustomerMetrics AS (
    -- 1. Calculamos las métricas principales (órdenes, revenue, AOV) y filtramos
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months' -- (Ver nota sobre fechas abajo)
    GROUP BY 
        c.id, c.name, c.email, c.country
    HAVING 
        COUNT(o.id) >= 3
),
CustomerCategories AS (
    -- 2. Calculamos la cantidad de productos comprados por categoría para cada cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        -- Asignamos un número de fila ordenado por la cantidad comprada (el 1 será el más comprado)
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY 
        o.customer_id, p.category
),
TopCategoryPerCustomer AS (
    -- 3. Nos quedamos únicamente con la categoría top (rn = 1) de cada cliente
    SELECT 
        customer_id, 
        category AS categoria_mas_comprada
    FROM CustomerCategories
    WHERE rn = 1
)

-- 4. Unimos todo, ordenamos y limitamos al Top 10
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM CustomerMetrics cm
JOIN TopCategoryPerCustomer tc ON cm.customer_id = tc.customer_id
ORDER BY 
    cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:
1. **`CustomerMetrics`**: Agrupa a los clientes, suma sus ingresos (`total_revenue`), cuenta sus órdenes y saca el promedio (`avg_order_value`). Aquí aplicamos los filtros de los últimos 6 meses, estatus 'completed' y el `HAVING COUNT >= 3`.
2. **`CustomerCategories`**: Une las tablas de órdenes, items y productos. Suma las cantidades compradas por categoría para cada cliente. Usa la función de ventana `ROW_NUMBER()` para hacer un ranking interno por cliente, donde `1` es la categoría con más artículos comprados.
3. **`TopCategoryPerCustomer`**: Filtra el paso anterior para quedarse solo con la fila `rn = 1` (la categoría ganadora).
4. **Query Final**: Une las métricas del cliente con su categoría favorita, ordena por revenue de mayor a menor y extrae solo los primeros 10.

### ⚠️ Nota sobre la sintaxis de fechas según tu motor SQL:
La sintaxis `CURRENT_DATE - INTERVAL '6 months'` funciona en **PostgreSQL** y **MySQL**. Si usas otro motor de base de datos, deberás cambiar esa línea:
* **SQL Server (T-SQL)**: `o.created_at >= DATEADD(month, -6, GETDATE())`
* **Oracle**: `o.created_at >= ADD_MONTHS(SYSDATE, -6)`
* **Snowflake / BigQuery**: `o.created_at >= DATEADD(month, -6, CURRENT_DATE())`