# Claude Opus 5 Fast — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.99 | quality: 10.0
- latency_total: 14.093s | tokens_per_second: 278.2
- input_tokens: 221 | output_tokens: 3920
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

## Query principal (PostgreSQL)

```sql
WITH ordenes_recientes AS (
    -- Filtramos una sola vez: reutilizable y evita repetir predicados
    SELECT o.id,
           o.customer_id,
           o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas_cliente AS (
    SELECT customer_id,
           COUNT(*)     AS total_orders,
           SUM(total)   AS total_revenue,
           AVG(total)   AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_top AS (
    -- DISTINCT ON se aplica DESPUÉS del GROUP BY: 1 fila por cliente
    SELECT DISTINCT ON (o.customer_id)
           o.customer_id,
           p.category,
           SUM(oi.quantity) AS unidades
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id   = o.id
    JOIN products    p  ON p.id          = oi.product_id
    GROUP BY o.customer_id, p.category
    ORDER BY o.customer_id, SUM(oi.quantity) DESC, p.category  -- category desempata de forma determinista
)

SELECT c.name                        AS nombre,
       c.email,
       c.country                     AS pais,
       m.total_orders,
       ROUND(m.total_revenue, 2)     AS total_revenue,
       ROUND(m.avg_order_value, 2)   AS avg_order_value,
       ct.category                   AS categoria_mas_comprada
FROM metricas_cliente m
JOIN customers c        ON c.id = m.customer_id
LEFT JOIN categoria_top ct ON ct.customer_id = m.customer_id
ORDER BY m.total_revenue DESC
LIMIT 10;
```

**Punto clave:** las métricas de `orders` y las de `order_items` se calculan en CTEs **separadas**. Si unes `orders` con `order_items` en una sola agregación, `SUM(o.total)` se multiplica por el número de líneas de cada orden (fan-out del join) y el revenue sale inflado.

---

## Versión portable (MySQL 8+, SQL Server, Snowflake, BigQuery)

Cambia `DISTINCT ON` por `ROW_NUMBER()`:

```sql
WITH ordenes_recientes AS (
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)   -- MySQL
),

metricas_cliente AS (
    SELECT customer_id,
           COUNT(*)   AS total_orders,
           SUM(total) AS total_revenue,
           AVG(total) AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

cat_ranked AS (
    SELECT o.customer_id,
           p.category,
           ROW_NUMBER() OVER (
               PARTITION BY o.customer_id
               ORDER BY SUM(oi.quantity) DESC, p.category
           ) AS rn
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products    p  ON p.id        = oi.product_id
    GROUP BY o.customer_id, p.category
)

SELECT c.name  AS nombre,
       c.email,
       c.country AS pais,
       m.total_orders,
       ROUND(m.total_revenue, 2)   AS total_revenue,
       ROUND(m.avg_order_value, 2) AS avg_order_value,
       ct.category AS categoria_mas_comprada
FROM metricas_cliente m
JOIN customers c ON c.id = m.customer_id
LEFT JOIN cat_ranked ct ON ct.customer_id = m.customer_id AND ct.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

Ajustes por motor:
- **SQL Server:** `DATEADD(MONTH, -6, CAST(GETDATE() AS date))`, y `SELECT TOP 10 ...` en vez de `LIMIT`.
- **BigQuery:** `DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`.
- **Oracle:** `ADD_MONTHS(TRUNC(SYSDATE), -6)` y `FETCH FIRST 10 ROWS ONLY`.

---

## Decisiones que conviene que valides

1. **Fuente del revenue.** Usé `orders.total` (incluye impuestos/envío/descuentos según cómo lo calcules). Si el negocio define revenue como valor de línea, reemplaza la CTE de métricas:

```sql
metricas_cliente AS (
    SELECT o.customer_id,
           COUNT(DISTINCT o.id) AS total_orders,
           SUM(oi.quantity * oi.unit_price) AS total_revenue,
           SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id = o.id
    GROUP BY o.customer_id
    HAVING COUNT(DISTINCT o.id) >= 3
)
```

2. **"Categoría más comprada" = más unidades.** Si prefieres "en la que más gastó", cambia el criterio de orden a `SUM(oi.quantity * oi.unit_price) DESC`. Son métricas distintas: productos baratos ganan por volumen, caros por gasto.

3. **`created_at` con timezone.** Si es `timestamptz`, `CURRENT_DATE - INTERVAL '6 months'` se evalúa en la zona de la sesión. Para reportes fija la zona explícitamente: `o.created_at >= (CURRENT_DATE - INTERVAL '6 months') AT TIME ZONE 'America/Mexico_City'`.

4. **Empates en la categoría.** El desempate por `p.category` alfabético es arbitrario pero determinista (evita que el reporte cambie entre ejecuciones). Si te importa el empate real, puedes usar `STRING_AGG` con `RANK()` para mostrar todas las empatadas.

5. **`LEFT JOIN` en categoria_top.** Defensivo: si un cliente calificado tuviera órdenes sin líneas (datos inconsistentes), aparece igual con `NULL` en vez de desaparecer del top 10.

---

## Índices recomendados

```sql
CREATE INDEX idx_orders_status_created_customer
    ON orders (status, created_at, customer_id) INCLUDE (total);  -- PG 11+ / SQL Server

CREATE INDEX idx_order_items_order ON order_items (order_id, product_id);
```

El primero es el que más importa: convierte el filtro en un index range scan y, con el `INCLUDE (total)`, permite resolver la agregación sin tocar la tabla. En MySQL, el índice compuesto `(status, created_at, customer_id, total)` logra el mismo efecto de covering index.