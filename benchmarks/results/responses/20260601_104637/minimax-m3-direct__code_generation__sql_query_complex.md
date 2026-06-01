# MiniMax M3 (directo / sub) — code_generation/sql_query_complex

- model_id: `MiniMax-M3`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 66.165s | tokens_per_second: 30.5
- input_tokens: 316 | output_tokens: 2020
- judge_score: 5.0 | justificación: 

## Respuesta completa

<think>
The user wants a SQL query with several specific requirements. Let me break it down:

1. Tables:
   - orders (id, customer_id, total, status, created_at)
   - customers (id, name, email, country, created_at)
   - order_items (id, order_id, product_id, quantity, unit_price)
   - products (id, name, category, price)

2. Requirements:
   - Top 10 clientes por revenue total en los últimos 6 meses
   - Columns: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
   - Order by total_revenue DESC
   - Only clients with at least 3 completed orders (status = 'completed')

Let me think about the structure:

1. First, filter orders from the last 6 months with status = 'completed'
2. Group by customer to get total_orders, total_revenue, avg_order_value
3. Join with customers to get name, email, country
4. Filter HAVING total_orders >= 3
5. For categoria_mas_comprada, we need to find the most purchased category per customer. This requires joining with order_items and products, and using a window function or subquery to find the top category per customer.

Let me write the query:

```sql
WITH completed_orders AS (
  SELECT 
    o.id,
    o.customer_id,
    o.total,
    o.created_at
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),
customer_stats AS (
  SELECT 
    c.id,
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT co.id) AS total_orders,
    SUM(co.total) AS total_revenue,
    AVG(co.total) AS avg_order_value
  FROM customers c
  INNER JOIN completed_orders co ON c.id = co.customer_id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(DISTINCT co.id) >= 3
),
category_revenue AS (
  SELECT 
    co.customer_id,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS category_revenue,
    ROW_NUMBER() OVER (
      PARTITION BY co.customer_id 
      ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS rn
  FROM completed_orders co
  INNER JOIN order_items oi ON co.id = oi.order_id
  INNER JOIN products p ON oi.product_id = p.id
  GROUP BY co.customer_id, p.category
)
SELECT 
  cs.name,
  cs.email,
  cs.country,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_revenue cr ON cs.id = cr.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

Wait, I should think about a few things:
- The "last 6 months" should be based on the current date. I used DATE_SUB which is MySQL syntax. I should mention that this is MySQL syntax and adapt for other databases.
- I should be careful about the completed orders - the category most purchased should also be from completed orders in the last 6 months? The question is a bit ambiguous. I'll assume yes since we're calculating "top customers in last 6 months".

Actually, let me re-read: "Top 10 clientes por revenue total en los ultimos 6 meses" - so the customer ranking is based on revenue in the last 6 months. The category most purchased - it's reasonable to assume this is also in the last 6 months context.

Let me also think about edge cases:
- What if a customer has no items in their orders? The LEFT JOIN handles this, but they would have NULL for categoria_mas_comprada.
- What about ties in category_revenue? ROW_NUMBER() will pick one, which is fine.

Let me also add a few notes about the query, and offer a version for other SQL dialects.

I should also think: should I use `orders.total` or calculate from order_items? The orders table has a `total` column, so using that is fine and likely more efficient. But for the category calculation, I need to use order_items.

Let me refine the query and provide good explanations in Spanish since the user wrote in Spanish.

Let me also think about whether to use window functions or a different approach for categoria_mas_comprada. The window function approach is cleaner and works in most modern databases (PostgreSQL, MySQL 8+, SQL Server, etc.).

Let me also make sure the query is well-formatted and commented. I'll respond in Spanish since the user wrote in Spanish.
</think>
# Query SQL - Top 10 Clientes por Revenue

## Análisis previo

Para resolver esto necesitamos:
1. **Filtrar** órdenes de los últimos 6 meses con status = 'completed'
2. **Agregar** métricas por cliente (orders, revenue, AOV)
3. **Obtener** la categoría más comprada por cliente (requiere ranking)
4. **Filtrar** clientes con ≥ 3 órdenes
5. **Limitar** al top 10

## Query completa

```sql
WITH completed_orders AS (
  -- 1) Órdenes completadas de los últimos 6 meses
  SELECT 
    o.id,
    o.customer_id,
    o.total,
    o.created_at
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),

customer_stats AS (
  -- 2) Métricas agregadas por cliente
  SELECT 
    c.id,
    c.name,
    c.email,
    c.country,
    COUNT(co.id)                AS total_orders,
    SUM(co.total)               AS total_revenue,
    AVG(co.total)               AS avg_order_value
  FROM customers c
  INNER JOIN completed_orders co ON c.id = co.customer_id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(co.id) >= 3
),

category_ranking AS (
  -- 3) Ranking de categorías por revenue para cada cliente
  SELECT
    co.customer_id,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS category_revenue,
    ROW_NUMBER() OVER (
      PARTITION BY co.customer_id
      ORDER BY SUM(oi.quantity * oi.unit_price) DESC
    ) AS rn
  FROM completed_orders co
  INNER JOIN order_items oi ON co.id = oi.order_id
  INNER JOIN products      p  ON oi.product_id = p.id
  GROUP BY co.customer_id, p.category
)

-- 4) Resultado final
SELECT
  cs.name                AS nombre,
  cs.email               AS email,
  cs.country             AS pais,
  cs.total_orders        AS total_orders,
  ROUND(cs.total_revenue, 2)  AS total_revenue,
  ROUND(cs.avg_order_value, 2) AS avg_order_value,
  cr.category            AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_ranking cr 
       ON cs.id = cr.customer_id 
      AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Notas importantes

| Punto | Detalle |
|-------|---------|
| **Motor SQL** | `DATE_SUB` es MySQL. Para PostgreSQL usa `CURRENT_DATE - INTERVAL '6 months'`, en SQL Server `DATEADD(MONTH, -6, GETDATE())`. |
| **Performance** | Asegúrate de tener índices en: `orders(status, created_at)`, `orders(customer_id)`, `order_items(order_id)`, `order_items(product_id)`. |
| **Empates en categoría** | `ROW_NUMBER()` toma solo 1. Si quieres todas las empatadas, usa `RANK()`. |
| **Revenue vs. items** | Uso `orders.total` para revenue/AVG (es la fuente oficial). Para la categoría sí calculo desde `order_items` porque necesito desglosar por producto. |
| **LEFT JOIN a categorías** | Si un cliente tiene órdenes pero sin `order_items`, la categoría quedará `NULL` (no debería pasar, pero es defensivo). |
| **Clientes con 0 órdenes** | Excluidos automáticamente por el `INNER JOIN` en `customer_stats`. |

## Variante más performante (subquery correlacionada)

Si la ventana de funciones da problemas de performance con muchos datos, puedes reemplazar `category_ranking` con:

```sql
-- En el SELECT final:
(SELECT p2.category
 FROM order_items oi2
 JOIN orders o2        ON oi2.order_id = o2.id
 JOIN products p2      ON oi2.product_id = p2.id
 WHERE o2.customer_id = cs.id
   AND o2.status = 'completed'
   AND o2.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
 GROUP BY p2.category
 ORDER BY SUM(oi2.quantity * oi2.unit_price) DESC
 LIMIT 1) AS categoria_mas_comprada
```

Esta versión evita el CTE de ranking pero ejecuta la subquery por cada fila del resultado final (con `LIMIT 10` son solo 10 ejecuciones, así que suele ser más rápida en datasets grandes).