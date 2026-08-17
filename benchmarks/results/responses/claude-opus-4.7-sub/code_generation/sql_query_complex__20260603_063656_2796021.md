# Claude Opus 4.7 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-opus-4-7`
- success: True  | final: 7.33 | quality: 10.0
- latency_total: 23.709s | tokens_per_second: 78.2
- input_tokens: 6 | output_tokens: 1854
- judge_score: 5.0 | justificación: 

## Respuesta completa

```sql
WITH last_6_months AS (
    -- Filtro base: ordenes completadas en los ultimos 6 meses
    SELECT
        o.id              AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    -- Agregados por cliente (revenue, ordenes, AOV)
    SELECT
        l.customer_id,
        COUNT(DISTINCT l.order_id)                       AS total_orders,
        SUM(l.total)                                     AS total_revenue,
        AVG(l.total)                                     AS avg_order_value
    FROM last_6_months l
    GROUP BY l.customer_id
    HAVING COUNT(DISTINCT l.order_id) >= 3
),
category_revenue AS (
    -- Revenue por cliente y categoria (usando line items, no order.total)
    SELECT
        l.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM last_6_months l
    JOIN order_items oi ON oi.order_id   = l.order_id
    JOIN products    p  ON p.id          = oi.product_id
    GROUP BY l.customer_id, p.category
),
top_category AS (
    -- Categoria con mayor revenue por cliente (rank 1)
    SELECT
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY category_revenue DESC, category ASC  -- desempate determinista
        ) AS rn
    FROM category_revenue
)
SELECT
    c.name                                AS nombre,
    c.email,
    c.country                             AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue::numeric, 2)   AS total_revenue,
    ROUND(cs.avg_order_value::numeric, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c  ON c.id           = cs.customer_id
LEFT JOIN top_category tc
       ON tc.customer_id = cs.customer_id
      AND tc.rn          = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas de diseño

**1. Por que CTEs y no subqueries inline**
- `last_6_months` se reutiliza en `customer_stats` y `category_revenue` → evita escanear `orders` dos veces.
- Hace la query auditable: cada paso tiene un nombre.

**2. Filtro temporal**
- `CURRENT_DATE - INTERVAL '6 months'` → PostgreSQL/MySQL 8+.
- Si usas otro motor cambia a: `DATEADD(month, -6, GETDATE())` (SQL Server) o `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` (MySQL clasico).

**3. `total_revenue`: 2 fuentes posibles**
- Uso `orders.total` para revenue/AOV (consistente con como facturas al cliente: incluye envio, descuentos, impuestos).
- Uso `SUM(quantity * unit_price)` SOLO para decidir la categoria favorita (necesito desagregar por producto).
- Si tu negocio define revenue puro como suma de line items, cambia `customer_stats` para sumar desde `order_items`.

**4. Categoria mas comprada: por revenue, no por cantidad**
- `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY category_revenue DESC, category ASC)`.
- El segundo criterio (`category ASC`) rompe empates de forma determinista → mismo resultado en cada corrida.
- Si prefieres "mas comprada por unidades" cambia a `SUM(oi.quantity)`.

**5. `HAVING COUNT >= 3` dentro del CTE**
- Filtra a nivel cliente antes del JOIN final → menos filas que joinear con `customers` y `top_category`.

**6. `LEFT JOIN top_category`**
- Defensivo: si un cliente tiene ordenes pero sin `order_items` (datos sucios), aun aparece con `categoria_mas_comprada = NULL` en vez de desaparecer del top 10.

**7. `ROUND(... ::numeric, 2)`**
- Sintaxis PostgreSQL. En MySQL: `ROUND(cs.total_revenue, 2)`. En SQL Server: `ROUND(cs.total_revenue, 2)`.

### Indices recomendados para que rinda

```sql
CREATE INDEX idx_orders_status_created ON orders(status, created_at) WHERE status = 'completed';
CREATE INDEX idx_orders_customer        ON orders(customer_id);
CREATE INDEX idx_order_items_order      ON order_items(order_id);
CREATE INDEX idx_products_id_category   ON products(id, category);
```

El primero es un indice parcial (PostgreSQL) — si el 80% de tus ordenes no estan `completed`, ahorra mucho I/O.