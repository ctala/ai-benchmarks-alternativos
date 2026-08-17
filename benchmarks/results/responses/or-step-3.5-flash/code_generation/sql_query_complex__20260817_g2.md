# Step 3.5 Flash — code_generation/sql_query_complex

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.71 | quality: 8.2
- latency_total: 32.978s | tokens_per_second: 62.1
- input_tokens: 160 | output_tokens: 2048
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

Primero, entiendo que necesito una consulta SQL que devuelva los 10 clientes principales por ingresos totales (revenue) en los últimos 6 meses. Además, debo incluir columnas específicas y filtrar por clientes que tengan al menos 3 órdenes completadas.

Las tablas involucradas son:
- `orders`: contiene información de las órdenes, con `id`, `customer_id`, `total`, `status`, `created_at`.
- `customers`: información del cliente, con `id`, `name`, `email`, `country`, `created_at`.
- `order_items`: ítems de cada orden, con `id`, `order_id`, `product_id`, `quantity`, `unit_price`.
- `products`: información de productos, con `id`, `name`, `category`, `price`.

Requisitos:
1. Top 10 clientes por `total_revenue` en los últimos 6 meses.
2. Columnas: `nombre` (de customers), `email` (de customers), `pais` (country de customers), `total_orders` (número de órdenes completadas en el período), `total_revenue` (suma de los totales de las órdenes completadas en el período), `avg_order_value` (promedio del valor de las órdenes completadas en el período), `categoria_mas_comprada` (la categoría de producto más comprada por ese cliente en el período).
3. Ordenar por `total_revenue` DESC.
4. Solo clientes con al menos 3 órdenes completadas (status = 'completed') en el período de 6 meses.

Pasos a seguir:

a) Definir el período de tiempo: últimos 6 meses desde la fecha actual. Asumo que `created_at` en `orders` es la fecha de la orden. Entonces, filtrar órdenes donde `created_at` >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH) y `status` = 'completed'.

b) Calcular para cada cliente:
   - `total_orders`: COUNT(DISTINCT orders.id) de órdenes completadas en el período.
   - `total_revenue`: SUM(orders.total) de órdenes completadas en el período. Nota: `orders.total` ya debe ser el total de la orden, pero también podríamos calcularlo desde `order_items` (quantity * unit_price). Sin embargo, la tabla `orders` tiene un campo `total`, que probablemente es el total de la orden. Para ser consistentes, usaré `orders.total` asumiendo que está correcto. Pero si queremos ser precisos, podríamos calcularlo desde `order_items`. El problema es que `order_items` puede tener múltiples filas por orden, y `orders.total` debería ser la suma de (quantity * unit_price) de todos los ítems. Para evitar discrepancias, usaré `orders.total` ya que es más directo y asumo que es confiable. Sin embargo, en el caso de que `orders.total` no sea confiable, podríamos calcularlo. Pero dado que el campo existe, lo usaré.

   Pero cuidado: `total_revenue` debe ser el revenue del cliente, que es la suma de los totales de sus órdenes completadas en el período. Así que SUM(orders.total) está bien.

c) `avg_order_value`: `total_revenue` / `total_orders`. Podemos calcularlo como AVG(orders.total) o como la división.

d) `categoria_mas_comprada`: la categoría de producto más comprada por el cliente en el período. Esto requiere unir `order_items` y `products` para obtener la categoría de cada ítem comprado en las órdenes completadas del cliente en el período. Luego, para cada cliente, encontrar la categoría con la mayor cantidad comprada (por cantidad o por revenue? El problema dice "categoria_mas_comprada", que generalmente se refiere a la categoría con más unidades compradas o más revenue. Pero no especifica. Asumiré que es por cantidad de productos comprados (suma de quantity). Podría ser por revenue (quantity * unit_price), pero como ya tenemos revenue por orden, quizás por cantidad. Sin embargo, "más comprada" podría interpretarse como la que tiene mayor ingreso o mayor cantidad. Dado que no se especifica, usaré la categoría con la mayor suma de `quantity` de los ítems en las órdenes del cliente en el período. Otra opción es por el número de ítems, pero `quantity` es la cantidad de unidades. Usaré SUM(quantity) para cada categoría y luego tomar la categoría con el máximo.

   Esto requerirá una subconsulta o un JOIN adicional. Como necesitamos agrupar por cliente y luego por categoría, podemos usar una subconsulta para obtener la categoría más comprada por cliente.

e) Filtrar por clientes con al menos 3 órdenes completadas en el período. Esto se puede hacer con HAVING COUNT(DISTINCT orders.id) >= 3.

f) Unir las tablas: 
   - Partir de `customers` para obtener nombre, email, country.
   - Unir con `orders` en customer_id, filtrando por fecha y estado.
   - Para `categoria_mas_comprada`, necesitamos unir `orders` con `order_items` y `products` para obtener las categorías de los productos comprados en esas órdenes.

Estructura:

Primero, filtrar órdenes completadas en los últimos 6 meses:

```sql
SELECT 
    c.id AS customer_id,
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(o.total) AS total_revenue,
    AVG(o.total) AS avg_order_value
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country
HAVING total_orders >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

Pero esto no incluye `categoria_mas_comprada`. Para obtener esa columna, necesitamos una subconsulta que calcule la categoría más comprada por cada cliente en el mismo período.

Podemos hacerlo con una subconsulta en el SELECT o con un JOIN a una subconsulta que devuelva la categoría más comprada por cliente.

Enfoque con subconsulta correlacionada:

Para cada cliente, en el contexto de las órdenes filtradas, necesitamos mirar los order_items y products de esas órdenes.

Pero en la consulta principal ya estamos agrupando por cliente. Podemos añadir una subconsulta en el SELECT que para el cliente actual, busque en order_items y products de las órdenes de ese cliente (en el período) y devuelva la categoría con la suma máxima de quantity.

Sin embargo, la subconsulta correlacionada podría ser ineficiente. Otra opción es calcular primero la categoría más comprada por cliente en una subconsulta separada y luego unirla.

Vamos a crear una subconsulta que para cada cliente (dentro del período) calcule la categoría más comprada.

Primero, necesitamos los datos de order_items y products para las órdenes completadas en el período.

Podemos hacer:

```sql
-- Subconsulta para obtener por cliente y categoría, la suma de quantity
SELECT 
    o.customer_id,
    p.category,
    SUM(oi.quantity) AS total_quantity
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY o.customer_id, p.category
```

Luego, de esto, para cada cliente, queremos la categoría con el máximo `total_quantity`. Podemos usar una función ventana o un subgrupo.

Una forma es:

```sql
SELECT customer_id, category
FROM (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        RANK() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rnk
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
) ranked
WHERE rnk = 1;
```

Esto dará la categoría con más quantity para cada cliente. En caso de empate, RANK dará múltiples filas, pero podemos usar ROW_NUMBER si queremos solo una, pero el problema no especifica. Usaré RANK y si hay empate, podría mostrar múltiples categorías, pero en el SELECT principal solo podemos elegir una. Para simplificar, usaré ROW_NUMBER para