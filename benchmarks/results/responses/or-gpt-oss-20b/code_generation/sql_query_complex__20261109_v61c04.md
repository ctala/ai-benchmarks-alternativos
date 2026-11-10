# GPT-OSS 20B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.15 | quality: 9.8
- latency_total: 13.485s | tokens_per_second: 134.4
- input_tokens: 208 | output_tokens: 1813
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes una solución que cumple con todos los requisitos.  
El query está escrito para **MySQL** (puedes adaptarlo a PostgreSQL cambiando la función de fecha).

```sql
/* 1️⃣  Filtramos las órdenes completadas de los últimos 6 meses  */
WITH recent_orders AS (
    SELECT id            AS order_id,
           customer_id,
           total,
           created_at
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
),

/* 2️⃣  Unimos las líneas de pedido con el producto para saber la categoría  */
order_items_with_products AS (
    SELECT oi.order_id,
           oi.quantity,
           oi.unit_price,
           p.category
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
),

/* 3️⃣  Calculamos estadísticas por cliente (ordenes, ingresos, valor medio)  */
customer_stats AS (
    SELECT c.id,
           c.name,
           c.email,
           c.country,
           COUNT(DISTINCT ro.order_id)                                      AS total_orders,
           COALESCE(SUM(oi.unit_price * oi.quantity), 0)                    AS total_revenue,
           COALESCE(SUM(oi.unit_price * oi.quantity) /
                     COUNT(DISTINCT ro.order_id), 0)                       AS avg_order_value
    FROM customers c
    JOIN recent_orders ro          ON c.id = ro.customer_id
    LEFT JOIN order_items_with_products oi
           ON ro.order_id = oi.order_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT ro.order_id) >= 3        /* mínimo 3 pedidos  */
),

/* 4️⃣  Determinamos la categoría más comprada por cada cliente  */
category_counts AS (
    SELECT ro.customer_id,
           oi.category,
           SUM(oi.quantity)  AS qty
    FROM recent_orders ro
    JOIN order_items_with_products oi
          ON ro.order_id = oi.order_id
    GROUP BY ro.customer_id, oi.category
),

/* 5️⃣  Ordenamos las categorías por cantidad (y por nombre para romper empates)  */
ranked_categories AS (
    SELECT customer_id,
           category,
           RANK() OVER (PARTITION BY customer_id
                        ORDER BY qty DESC, category) AS rk
    FROM category_counts
)

/* 6️⃣  Resultado final: top 10 clientes por ingresos  */
SELECT cs.name,
       cs.email,
       cs.country,
       cs.total_orders,
       cs.total_revenue,
       cs.avg_order_value,
       rc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN ranked_categories rc
       ON cs.id = rc.customer_id
      AND rc.rk = 1          -- la categoría con más compras
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Detalles importantes

| Paso | Qué hace | Comentario |
|------|----------|------------|
| 1 | Filtra `orders` con `status = 'completed'` y `created_at` dentro de los últimos 6 meses. | Usa `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` (MySQL). |
| 2 | Une `order_items` con `products` para obtener la categoría de cada línea. | Se necesita la categoría para el cálculo del “más comprado”. |
| 3 | Agrupa por cliente: cuenta de órdenes, suma de ingresos (unit_price * quantity), promedio de valor de pedido. | Se aplica `HAVING COUNT(...) >= 3` para los clientes con al menos 3 pedidos. |
| 4 | Cuenta la cantidad total de cada categoría por cliente. | Se usa `SUM(quantity)`; si prefieres usar ingresos, cambia a `SUM(unit_price * quantity)`. |
| 5 | Usa `RANK()` para determinar la categoría con mayor cantidad (o ingresos) por cliente. | Si hay empates, se elige la categoría con nombre alfabéticamente más alto. |
| 6 | Devuelve las columnas solicitadas, ordena por `total_revenue` descendente y limita a 10 filas. | `LEFT JOIN` garantiza que un cliente sin compras de ninguna categoría (teórico) no se excluya, pero en la práctica siempre habrá al menos una categoría. |

Con este query obtendrás:

| nombre | email | país | total_orders | total_revenue | avg_order_value | categoria_mas_comprada |
|--------|-------|------|--------------|---------------|-----------------|------------------------|
| …      | …     | …    | …            | …             | …               | …                      |

¡Listo para usar! Si trabajas con otro SGBD (PostgreSQL, SQL Server…), cambia la función de fecha y la sintaxis en la cláusula `ORDER BY` si es necesario.