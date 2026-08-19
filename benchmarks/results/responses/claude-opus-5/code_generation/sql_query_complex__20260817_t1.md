# Claude Opus 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 29.604s | tokens_per_second: 91.2
- input_tokens: 221 | output_tokens: 2701
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

## Query (PostgreSQL)

```sql
WITH ordenes_recientes AS (
    -- Filtramos una sola vez: base reutilizable para métricas y categorías
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
metricas_cliente AS (
    SELECT
        customer_id,
        COUNT(*)     AS total_orders,
        SUM(total)   AS total_revenue,
        AVG(total)   AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
categoria_ranking AS (
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC,
                     SUM(oi.quantity) DESC,
                     p.category ASC          -- desempate determinista
        ) AS rn
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id   = o.id
    JOIN products    p  ON p.id          = oi.product_id
    GROUP BY o.customer_id, p.category
)
SELECT
    c.name                                    AS nombre,
    c.email,
    c.country                                 AS pais,
    m.total_orders,
    ROUND(m.total_revenue::numeric, 2)        AS total_revenue,
    ROUND(m.avg_order_value::numeric, 2)      AS avg_order_value,
    cat.category                              AS categoria_mas_comprada
FROM metricas_cliente m
JOIN customers c        ON c.id = m.customer_id
LEFT JOIN categoria_ranking cat
       ON cat.customer_id = m.customer_id
      AND cat.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

## Decisiones de diseño

**1. `orders.total` vs. suma de `order_items`**
Uso `orders.total` para el revenue porque es el importe real facturado (puede incluir envío/descuentos). Los `order_items` los uso **solo** para determinar la categoría. Si en tu modelo `total` no es confiable o quieres revenue neto de producto, reemplaza `metricas_cliente` por:

```sql
metricas_cliente AS (
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.id)                    AS total_orders,
        SUM(oi.quantity * oi.unit_price)        AS total_revenue,
        SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id = o.id
    GROUP BY o.customer_id
    HAVING COUNT(DISTINCT o.id) >= 3
)
```

**2. `LEFT JOIN` en la categoría**
Evita perder clientes que tengan órdenes completadas pero sin filas en `order_items` (datos sucios). Si prefieres excluirlos, cámbialo a `JOIN`.

**3. "Más comprada" = mayor gasto**
Interpreté "más comprada" como **mayor revenue por categoría**. Si lo quieres por **unidades**, invierte el `ORDER BY` de la window function: `SUM(oi.quantity) DESC, SUM(oi.quantity * oi.unit_price) DESC`.

**4. Ventana de 6 meses**
`CURRENT_DATE - INTERVAL '6 months'` cuenta desde hoy. Si necesitas meses calendario completos: `DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '6 months'`.

## Variante MySQL 8+

Solo cambian dos cosas:

```sql
-- en ordenes_recientes:
AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)

-- en el SELECT final:
ROUND(m.total_revenue, 2)   AS total_revenue,
ROUND(m.avg_order_value, 2) AS avg_order_value,
```

## Índices recomendados

```sql
CREATE INDEX idx_orders_status_created_customer
    ON orders (status, created_at, customer_id) INCLUDE (total);  -- INCLUDE: PG 11+

CREATE INDEX idx_order_items_order_product
    ON order_items (order_id, product_id);
```

El primero permite resolver el filtro + agregación casi por index-only scan; el segundo acelera el join de items. `products(id)` y `customers(id)` ya deberían ser PK.

## Nota sobre `status`

Si `status` puede venir con distinta capitalización o espacios, considera `WHERE LOWER(TRIM(o.status)) = 'completed'` — pero eso invalida el índice, así que mejor normalizar los datos en origen o usar un índice funcional.