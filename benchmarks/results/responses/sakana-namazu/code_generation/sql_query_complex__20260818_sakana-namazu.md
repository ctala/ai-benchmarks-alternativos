# Sakana Namazu — code_generation/sql_query_complex

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.42 | quality: 8.2
- latency_total: 7.369s | tokens_per_second: 277.9
- input_tokens: 234 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando los requisitos de la consulta SQL con una estructura clara y bien organizada. Ofrece una buena profundidad al considerar diferentes enfoques para calcular métricas y manejar la sintaxis SQL, lo que la hace útil para un emprendedor.

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

El usuario quiere una consulta SQL que muestre el top 10 de clientes por revenue total en los últimos 6 meses. Los requisitos son:

Tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Columnas requeridas:
- nombre (customers.name)
- email (customers.email)
- pais (customers.country)
- total_orders (conteo de órdenes completadas)
- total_revenue (suma del revenue, probablemente de orders.total o calcular desde order_items)
- avg_order_value (total_revenue / total_orders)
- categoria_mas_comprada (la categoría más comprada por el cliente)

Condiciones:
- Últimos 6 meses (desde created_at de orders supongo)
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')
- Ordenar por total_revenue DESC
- Top 10

Necesito considerar:
1. Cómo calcular total_revenue. Puedo usar orders.total directamente o calcular desde order_items. Como hay una columna total en orders, usaré esa para simplificar, aunque también podría calcularse desde order_items. La consulta será más eficiente usando orders.total.
2. Sin embargo, para categoria_mas_comprada, necesito unir con order_items y products para obtener las categorías y determinar cuál es la más comprada.
3. Para "últimos 6 meses", usaré `created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)` o similar dependiendo del SQL dialect. Como no especifica qué base de datos, usaré sintaxis estándar/PostgreSQL o MySQL. La más común es MySQL/PostgreSQL. Usaré `CURRENT_DATE - INTERVAL '6 months'` para PostgreSQL o `DATE_SUB(NOW(), INTERVAL 6 MONTH)` para MySQL. Mejor usar una sintaxis que funcione en ambos o especificar. Como no sé el dialecto exacto, usaré una sintaxis genérica o comentaré las opciones. De hecho, usaré sintaxis estándar SQL como `CURRENT_DATE - INTERVAL '6' MONTH` o similar. Mejor usar `NOW() - INTERVAL '6 months'` para PostgreSQL o `DATE_SUB(NOW(), INTERVAL 6 MONTH)` para MySQL. 

Voy a escribir la consulta usando CTEs para claridad.

Pasos:
1. Filtrar órdenes completadas de los últimos 6 meses.
2. Agrupar por cliente para obtener total_orders, total_revenue, avg_order_value.
3. Filtrar solo los que tengan >= 3 órdenes.
4. Encontrar la categoría más comprada por cliente. Esto requiere contar cantidad de items o número de órdenes por categoría. El usuario dice "categoría más comprada" - podría ser por cantidad de items (SUM(quantity)) o por número de órdenes. Usaré SUM(quantity) como métrica de "más comprada".
5. Unir todo y limitar a 10.

Para la categoría más comprada, puedo usar una CTE que calcule por cliente y categoría la cantidad total comprada, luego usar ROW_NUMBER() para quedarme con la primera de cada cliente.

Estructura:

```sql
WITH completed_orders AS (
  SELECT *
  FROM orders
  WHERE status = 'completed'
    AND created_at >= DATE('now', '-6 months') -- SQLite? No, mejor genérico
```

Mejor usar:
```sql
WHERE created_at >= CURRENT_DATE - INTERVAL '6 months'
```
Esto es PostgreSQL. Para MySQL sería `CURRENT_DATE - INTERVAL 6 MONTH`.

Dado que no especifica el motor, usaré una sintaxis cercana a PostgreSQL que es muy estándar, o usaré comentarios. De hecho, usaré `CURRENT_DATE - INTERVAL '6 months'` y si es MySQL se puede adaptar.

O simplemente usar `created_at >= NOW() - INTERVAL '6 months'` (PostgreSQL) o `DATE_SUB(NOW(), INTERVAL 6 MONTH)` (MySQL).

Decisión: Escribiré la consulta con sintaxis estándar SQL window functions (ROW_NUMBER) que funciona en PostgreSQL, MySQL 8.0+, SQL Server, etc. Para la fecha, usaré `CURRENT_DATE - INTERVAL '6' MONTH` (estándar SQL) o comentaré la alternativa.

Espera, en MySQL 8.0 la sintaxis `INTERVAL '6' MONTH` funciona en algunos contextos pero `INTERVAL 6 MONTH` es más común. En PostgreSQL es `INTERVAL '6 months'`.

Voy a usar `CURRENT_DATE - INTERVAL '6 months'` asumiendo PostgreSQL, pero agregaré un comentario sobre cómo adaptarlo.

Consulta detallada:

```sql
WITH completed_orders AS (
  SELECT 
    o.*,
    c.name,
    c.email,
    c.country
  FROM orders o
  JOIN customers c ON o.customer_id = c.id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
  SELECT 
    customer_id,
    name,
    email,
    country,
    COUNT(DISTINCT id) AS total_orders,
    SUM(total) AS total_revenue,
    SUM(total) / COUNT(DISTINCT id) AS avg_order_value
  FROM completed_orders
  GROUP BY customer_id, name, email, country
  HAVING COUNT(DISTINCT id) >= 3
),
category_purchases AS (
  SELECT 
    o.customer_id,
    p.category,
    SUM(oi.quantity) AS total_quantity
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
  GROUP BY o.customer_id, p.category
),
ranked_categories AS (
  SELECT 
    customer_id,
    category,
    total_quantity,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC, category ASC) AS rn
  FROM category_purchases
),
top_category AS (
  SELECT 
    customer_id,
    category AS categoria_mas_comprada
  FROM ranked_categories
  WHERE rn = 1
)
SELECT 
  cs.name AS nombre,
  cs.email,
  cs.country AS pais,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  tc.categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN top_category tc ON cs.customer_id = tc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Notas:
- `COUNT(DISTINCT id)` en customer_stats asume que `id` es de orders. Esto es correcto.
- El revenue lo tomo de `orders.total`. Esto es razonable dado que existe esa columna.
- Para avg_order_value, uso `SUM(total) / COUNT(DISTINCT id)`. Podría dar decimal.
- LEFT JOIN por si un cliente no tiene items (aunque improbable si tiene órdenes completadas), pero para evitar descartar clientes.
- `categoria_mas_comprada` determina por cantidad de unidades (SUM(oi.quantity)). Si hay empate, elige la categoría alfabéticamente primero (category ASC).

Espera, en `customer_stats` estoy seleccionando `name, email, country` de la CTE `completed_orders` que ya tiene esos campos del JOIN con customers. Eso está bien.

Sin embargo, hay una consideración: Si `orders.total` no es fiable o prefiere calcularse desde order_items, podría hacerse también. Pero como la columna existe, usarla es más eficiente. Podría mencionar esto.

También, la fecha: `CURRENT_DATE - INTERVAL '6 months'` puede variar. En MySQL 8 sería `CURRENT_DATE - INTERVAL 6 MONTH`. Pero pondré un comentario.

Voy a revisar si hay algún error:

- `completed_orders` tiene `o.*` y campos de customer. Eso incluye `o.id` como `id`. Cuando hago `COUNT(DISTINCT id)`, cuenta distinct order ids. Correcto.
- En `category_purchases`, hago JOIN directamente con orders, no con completed_orders. Puedo reutilizar la CTE completed_orders para evitar repetir la lógica de filtro. Sí, mejor.

Refining:

```sql
WITH completed_orders AS (
  SELECT 
    o.id AS order_id,
    o.customer_id,
    o.total,
    o.created_at,
    c.name,
    c.email,
    c.country
  FROM orders o
  JOIN customers c ON o.customer_id = c.id