# Kimi K2.5 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.41 | quality: 8.4
- latency_total: 24.841s | tokens_per_second: 82.4
- input_tokens: 159 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

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

El usuario quiere una consulta SQL que muestre el top 10 de clientes por ingresos totales en los últimos 6 meses. Necesito analizar los requisitos:

1. **Tablas involucradas**:
   - orders (id, customer_id, total, status, created_at)
   - customers (id, name, email, country, created_at)
   - order_items (id, order_id, product_id, quantity, unit_price)
   - products (id, name, category, price)

2. **Requisitos de la consulta**:
   - Top 10 clientes por revenue total en últimos 6 meses
   - Columnas: nombre, email, país, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
   - Ordenar por total_revenue DESC
   - Solo clientes con al menos 3 órdenes completadas (status = 'completed')

3. **Consideraciones**:
   - Necesito calcular el revenue. Puedo usar `orders.total` o calcularlo desde `order_items` (quantity * unit_price). Como la tabla orders ya tiene un campo `total`, usaré ese para simplificar, pero también podría calcularse desde order_items para mayor precisión. Sin embargo, el campo `total` en orders probablemente ya sea la suma de los items.
   - Para la categoría más comprada, necesito unir con order_items y products, agrupar por categoría y encontrar la más frecuente (o la que más revenue tenga, o la que más cantidad tenga). El usuario no especifica el criterio para "más comprada", así que asumiré por cantidad de items o por frecuencia. Usaré MODE() si está disponible, o una subconsulta con ROW_NUMBER().

4. **Estructura de la query**:
   - Filtrar órdenes de los últimos 6 meses: `created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)` (MySQL) o `created_at >= NOW() - INTERVAL '6 months'` (PostgreSQL). Como no especifica el motor SQL, usaré sintaxis estándar o MySQL/PostgreSQL compatible.
   - Filtrar status = 'completed'
   - Agrupar por customer_id
   - Tener HAVING COUNT(*) >= 3
   - Calcular métricas: COUNT(*) as total_orders, SUM(total) as total_revenue, AVG(total) as avg_order_value
   - Para la categoría más comprada, necesito una subconsulta o CTE que determine esto.

5. **La categoría más comprada**:
   - Esto es complejo. Necesito contar cuántos items de cada categoría compró cada cliente.
   - Opción A: Usar una subconsulta correlacionada
   - Opción B: Usar window functions (ROW_NUMBER) en una CTE
   - Opción C: Usar GROUP_CONCAT/GROUP_BY con ordenamiento (MySQL)

   Voy a usar una CTE para calcular las categorías por cliente y luego seleccionar la top 1.

   Estructura:
   ```sql
   WITH customer_stats AS (
     SELECT 
       c.id,
       c.name,
       c.email,
       c.country,
       COUNT(o.id) as total_orders,
       SUM(o.total) as total_revenue,
       AVG(o.total) as avg_order_value
     FROM customers c
     JOIN orders o ON c.id = o.customer_id
     WHERE o.status = 'completed'
       AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
     GROUP BY c.id, c.name, c.email, c.country
     HAVING COUNT(o.id) >= 3
   ),
   category_stats AS (
     SELECT 
       c.id as customer_id,
       p.category,
       SUM(oi.quantity) as total_quantity,
       ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) as rn
     FROM customers c
     JOIN orders o ON c.id = o.customer_id
     JOIN order_items oi ON o.id = oi.order_id
     JOIN products p ON oi.product_id = p.id
     WHERE o.status = 'completed'
       AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
     GROUP BY c.id, p.category
   )
   SELECT 
     cs.name,
     cs.email,
     cs.country,
     cs.total_orders,
     cs.total_revenue,
     cs.avg_order_value,
     cat.category as categoria_mas_comprada
   FROM customer_stats cs
   LEFT JOIN category_stats cat ON cs.id = cat.customer_id AND cat.rn = 1
   ORDER BY cs.total_revenue DESC
   LIMIT 10;
   ```

   Nota: Estoy asumiendo MySQL 8.0+ o PostgreSQL para las window functions. Si fuera MySQL antiguo, sería más complejo.

   También podría calcular el revenue desde order_items en lugar de usar orders.total para consistencia, pero el ejercicio permite usar orders.total.

   Ajustes:
   - Usar CURRENT_DATE o NOW() dependiendo del motor.
   - Asegurar que los joins sean correctos.
   - La condición de últimos 6 meses debe aplicarse tanto en customer_stats como en category_stats para consistencia.

   Alternativa más simple para categoría más comprada (si no se permite window functions):
   ```sql
   SELECT 
     c.id,
     SUBSTRING_INDEX(GROUP_CONCAT(p.category ORDER BY SUM(oi.quantity) DESC SEPARATOR ','), ',', 1) as categoria_mas_comprada
   FROM ...
   GROUP BY c.id
   ```
   Pero esto es truco de MySQL y no estándar.

   Mejor usar la versión con ROW_NUMBER para claridad.

   También debo considerar que si hay empates en la categoría más comprada, ROW_NUMBER elegirá uno arbitrariamente. Si quiero manejar empates, usaría RANK o DENSE_RANK, pero el usuario pide "la" categoría más comprada, implicando una sola.

   Revisión final de la query:
   1. Filtro de fecha: `o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)` (MySQL)
   2. Filtro status: `o.status = 'completed'`
   3. Group by customer
   4. Having count >= 3
   5. Cálculo de métricas
   6. Join con la subquery de categoría top

   Si el usuario usa PostgreSQL, cambiaría `DATE_SUB(NOW(), INTERVAL 6 MONTH)` por `NOW() - INTERVAL '6 months'`.

   Como no especifica el dialecto SQL, proporcionaré la versión estándar ANSI SQL o PostgreSQL que es más estándar, o mencionaré ambas.

   Voy a escribir la query usando sintaxis compatible con PostgreSQL/MySQL 8.0 (que es lo más común):

   ```sql
   WITH customer_revenue AS (
     SELECT 
       c.id,
       c.name,
       c.email,
       c.country,
       COUNT(o.id) as total_orders,
       SUM(o.total) as total_revenue,
       AVG(o.total) as avg_order_value
     FROM customers c
     INNER JOIN orders o ON c.id = o.customer_id
     WHERE o.status = 'completed'
       AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
     GROUP BY c.id, c.name, c.email, c.country
     HAVING COUNT(o.id) >= 3
   ),
   customer_categories AS (
     SELECT 
       c.id as customer_id,
       p.category,
       SUM(oi.quantity) as items_count,
       ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) as rn
     FROM customers c
     INNER JOIN orders o ON c.id = o.customer_id
     INNER JOIN order_items oi ON o.id = oi.order_id
     INNER JOIN products p ON oi.product_id = p.id
     WHERE o.status = 'completed'
       AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
     GROUP BY c.id, p.category
   )
   SELECT 
     cr.name,
     cr.email,
     cr.country,
     cr.total_orders,
     cr.total_revenue,
     ROUND(cr.avg_order_value, 2) as avg_order_value,
     cc.category as categoria_mas_comprada
   FROM customer_revenue cr
   LEFT JOIN customer_categories cc ON cr.id = cc.customer_id AND cc.rn = 1
   ORDER BY cr.total_revenue DESC
   LIMIT 10;
   ```

   Notas:
   - Uso `CURRENT_DATE - INTERVAL '6 months'` que funciona en PostgreSQL.
   - Para MySQL sería `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
   - Uso `ROUND` para el promedio.
   - El LEFT JOIN en la categoría es por si acaso un cliente no tiene items (aunque improbable si tiene órdenes completadas), pero INNER JOIN también funcionaría si estamos seguros de la integridad referencial.

   También podría