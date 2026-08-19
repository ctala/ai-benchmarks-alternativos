# Gemini 3.5 Flash Lite — code_generation/sql_query_complex

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 3.011s | tokens_per_second: 274.3
- input_tokens: 161 | output_tokens: 826
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profundiza en la consulta SQL compleja solicitada, utilizando CTEs para estructurar la lógica de manera clara y eficiente. Ofrece insights útiles para un emprendedor al identificar métricas clave de clientes y categorías de productos, lo que la hace altamente utilizable en un contexto práctico.

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

Aquí tienes la consulta SQL optimizada para resolver tu requerimiento. 

Asume un estándar de SQL moderno (como PostgreSQL, MySQL 8.0+ o SQL Server), utilizando CTEs (Common Table Expressions) para mantener el código limpio y ordenado.

```sql
WITH customer_orders AS (
    -- Paso 1: Filtrar las órdenes de los últimos 6 meses y completadas
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 month'
),
customer_metrics AS (
    -- Paso 2: Calcular métricas básicas por cliente y filtrar los que tienen >= 3 órdenes
    SELECT 
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM customer_orders
    GROUP BY customer_id
    HAVING COUNT(order_id) >= 3
),
customer_categories AS (
    -- Paso 3: Determinar la categoría más comprada por cada cliente en ese periodo
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER(PARTITION BY co.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM customer_orders co
    JOIN order_items oi ON co.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY co.customer_id, p.category
)
-- Paso 4: Unir todo con la tabla de clientes, ordenar y limitar a 10
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    m.total_orders,
    m.total_revenue,
    m.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_metrics m
JOIN customers c ON m.customer_id = c.id
JOIN customer_categories cc ON m.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

### Explicación de la Query:
1. **`customer_orders` (CTE 1):** Filtra la tabla `orders` para trabajar únicamente con las órdenes de los últimos 6 meses y que tengan el `status = 'completed'`. *(Nota: `CURRENT_DATE - INTERVAL '6 month'` puede variar ligeramente de sintaxis dependiendo del motor de base de datos, ej. en SQL Server se usa `DATEADD(month, -6, GETDATE())`).*
2. **`customer_metrics` (CTE 2):** Agrupa por cliente para calcular el número total de órdenes, el ingreso total (`SUM(total)`) y el ticket promedio (`AVG(total)`). Aquí mismo se aplica el filtro `HAVING COUNT(order_id) >= 3`.
3. **`customer_categories` (CTE 3):** Relaciona las órdenes con los productos y categorías mediante `order_items`. Usa una función de ventana (`ROW_NUMBER`) para rankear las categorías por la cantidad total de productos comprados (`SUM(quantity)`), ordenadas de mayor a menor por cliente.
4. **Consulta Final:** Junta los datos de los clientes con sus métricas y selecciona únicamente la categoría número 1 (`rn = 1`) del paso anterior. Finalmente, ordena por `total_revenue DESC` y limita el resultado a 10.