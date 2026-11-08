# Fugu Max — code_generation/sql_query_complex

- model_id: `sakana/fugu-max`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 8.845s | tokens_per_second: 240.7
- input_tokens: 270 | output_tokens: 2129
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

# Query (PostgreSQL)

```sql
WITH period_orders AS (
    -- Órdenes completadas en los últimos 6 meses
    SELECT o.id,
           o.customer_id,
           o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= now() - interval '6 months'
),
customer_totals AS (
    -- Agregados por cliente + filtro de mínimo 3 órdenes
    SELECT po.customer_id,
           COUNT(*)                 AS total_orders,
           SUM(po.total)            AS total_revenue,
           ROUND(AVG(po.total), 2)  AS avg_order_value
    FROM period_orders po
    GROUP BY po.customer_id
    HAVING COUNT(*) >= 3
),
category_qty AS (
    -- Cantidad comprada por cliente y categoría (en el mismo período)
    SELECT po.customer_id,
           p.category,
           SUM(oi.quantity) AS qty
    FROM period_orders po
    JOIN order_items oi ON oi.order_id   = po.id
    JOIN products    p  ON p.id          = oi.product_id
    GROUP BY po.customer_id, p.category
),
top_category AS (
    -- Categoría más comprada por cliente (desempate alfabético estable)
    SELECT DISTINCT ON (customer_id)
           customer_id,
           category
    FROM category_qty
    ORDER BY customer_id, qty DESC, category
)
SELECT c.name                                   AS nombre,
       c.email                                  AS email,
       c.country                                AS pais,
       ct.total_orders                          AS total_orders,
       ct.total_revenue                         AS total_revenue,
       ct.avg_order_value                       AS avg_order_value,
       COALESCE(tc.category, 'sin categoría')   AS categoria_mas_comprada
FROM customer_totals ct
JOIN customers   c  ON c.id  = ct.customer_id
LEFT JOIN top_category tc ON tc.customer_id = ct.customer_id
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

## Decisiones de interpretación (revísalas según tu caso)

1. **Ventana temporal**: tanto el revenue como el conteo de órdenes y la categoría más comprada se calculan sobre los últimos 6 meses. Si "al menos 3 órdenes completadas" debe ser histórico (no del período), mueve ese `HAVING` a un CTE separado sin el filtro de fecha.
2. **Revenue**: uso `orders.total`. Si tu `total` no es confiable o quieres el revenue "real" por líneas, cambia `SUM(po.total)` por `SUM(oi.quantity * oi.unit_price)` haciendo el join a `order_items` dentro de `customer_totals`.
3. **`avg_order_value`** = `AVG(orders.total)` = `total_revenue / total_orders`, consistente con la métrica anterior.
4. **`categoria_mas_comprada`**: se mide por **unidades** (`SUM(quantity)`). Si la quieres por **revenue** de esa categoría, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en `category_qty` (el resto no cambia).
5. `top_category` usa `DISTINCT ON` (Postgres). En MySQL 8 / SQL Server se reemplaza por `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY qty DESC, category)` filtrando `rn = 1`.

## Versión MySQL 8 (por si aplica)

```sql
WITH period_orders AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL 6 MONTH
),
customer_totals AS (
    SELECT customer_id,
           COUNT(*)            AS total_orders,
           SUM(total)          AS total_revenue,
           ROUND(AVG(total),2) AS avg_order_value
    FROM period_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_qty AS (
    SELECT po.customer_id, p.category, SUM(oi.quantity) AS qty
    FROM period_orders po
    JOIN order_items oi ON oi.order_id  = po.id
    JOIN products    p  ON p.id         = oi.product_id
    GROUP BY po.customer_id, p.category
),
top_category AS (
    SELECT customer_id, category
    FROM (
        SELECT customer_id, category,
               ROW_NUMBER() OVER (PARTITION BY customer_id
                                  ORDER BY qty DESC, category) AS rn
        FROM category_qty
    ) t
    WHERE rn = 1
)
SELECT c.name, c.email, c.country,
       ct.total_orders, ct.total_revenue, ct.avg_order_value,
       COALESCE(tc.category, 'sin categoría') AS categoria_mas_comprada
FROM customer_totals ct
JOIN customers c ON c.id = ct.customer_id
LEFT JOIN top_category tc ON tc.customer_id = ct.customer_id
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

## Índices recomendados para que esto vuele

```sql
CREATE INDEX idx_orders_status_created ON orders (status, created_at) INCLUDE (customer_id, total);
CREATE INDEX idx_orders_customer       ON orders (customer_id);
CREATE INDEX idx_items_order           ON order_items (order_id);
CREATE INDEX idx_items_product         ON order_items (product_id);
```

El `LIMIT 10` se aplica **después** del filtro `HAVING COUNT(*) >= 3`, así que siempre obtienes los 10 mejores clientes que cumplen el mínimo (o menos si no hay suficientes).