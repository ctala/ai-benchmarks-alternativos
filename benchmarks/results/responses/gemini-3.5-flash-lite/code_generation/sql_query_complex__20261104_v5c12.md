# Gemini 3.5 Flash Lite — code_generation/sql_query_complex

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 3.238s | tokens_per_second: 262.9
- input_tokens: 160 | output_tokens: 851
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

Aquí tienes la query SQL optimizada para resolver tu requerimiento. 

Asume un estándar compatible con la mayoría de bases de datos relacionales modernas (como PostgreSQL, MySQL 8.0+ o SQL Server), utilizando **CTEs** (Common Table Expressions) para mantenerla limpia y estructurada.

```sql
WITH customer_orders AS (
    -- Paso 1: Filtrar órdenes de los últimos 6 meses y completadas, 
    -- y calcular métricas básicas por orden.
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 month'
),
filtered_customers AS (
    -- Paso 2: Filtrar clientes que cumplan con el mínimo de 3 órdenes completadas
    -- en ese período y calcular sus agregados generales.
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
    -- Paso 3: Identificar la categoría más comprada por cada cliente
    -- usando una ventana de ranking (ROW_NUMBER).
    SELECT 
        c.customer_id,
        p.category,
        ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customer_orders c
    JOIN order_items oi ON c.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.customer_id, p.category
)
-- Paso 4: Unir todo con la tabla customers y seleccionar el Top 10
SELECT 
    c.name AS nombre,
    c.email,
    c.country AS pais,
    fc.total_orders,
    fc.total_revenue,
    fc.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM filtered_customers fc
JOIN customers c ON fc.customer_id = c.id
JOIN customer_categories cc ON fc.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY fc.total_revenue DESC
LIMIT 10;
```

### Explicación de la Lógica:

1. **`customer_orders` (CTE):** Aisla las órdenes de los últimos 6 meses que tienen el `status = 'completed'`. Esto evita repetir la condición de fecha y estado en múltiples lugares. *(Nota: `CURRENT_DATE - INTERVAL '6 month'` puede variar ligeramente según el motor de base de datos, por ejemplo, `DATE_SUB(NOW(), INTERVAL 6 MONTH)` en MySQL).*
2. **`filtered_customers` (CTE):** Agrupa por cliente para calcular el `total_orders`, `total_revenue` y `avg_order_value`. La cláusula `HAVING COUNT(order_id) >= 3` asegura que solo pasen los clientes que cumplen con el requisito mínimo.
3. **`customer_categories` (CTE):** Relaciona las órdenes con los productos para saber qué categorías está comprando cada cliente y en qué cantidad (`SUM(oi.quantity)`). Usamos `ROW_NUMBER()` particionado por cliente y ordenado por la cantidad descendente para quedarnos con la categoría líder (`rn = 1`).
4. **Consulta Final:** Junta los datos demográficos del cliente (`customers`), las métricas financieras y la categoría favorita, ordenando por `total_revenue DESC` y limitando a los 10 primeros resultados.