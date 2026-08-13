# Claude Opus 5 Fast — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 9.22s | tokens_per_second: 222.1
- input_tokens: 221 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, abordando todos los requisitos con una estructura bien pensada y explicaciones detalladas.

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
WITH ordenes_validas AS (
    -- Filtramos una sola vez: base común para todas las métricas
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
metricas AS (
    SELECT
        customer_id,
        COUNT(*)                            AS total_orders,
        SUM(total)                          AS total_revenue,
        ROUND(AVG(total)::numeric, 2)       AS avg_order_value
    FROM ordenes_validas
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
categorias AS (
    SELECT
        ov.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY ov.customer_id
            ORDER BY SUM(oi.quantity) DESC,                    -- criterio principal: unidades
                     SUM(oi.quantity * oi.unit_price) DESC,    -- desempate: gasto
                     p.category ASC                            -- desempate determinista
        ) AS rn
    FROM ordenes_validas ov
    JOIN order_items oi ON oi.order_id = ov.id
    JOIN products    p  ON p.id = oi.product_id
    GROUP BY ov.customer_id, p.category
)
SELECT
    c.name                    AS nombre,
    c.email,
    c.country                 AS pais,
    m.total_orders,
    m.total_revenue,
    m.avg_order_value,
    cat.category              AS categoria_mas_comprada
FROM metricas m
JOIN customers c   ON c.id = m.customer_id
LEFT JOIN categorias cat ON cat.customer_id = m.customer_id AND cat.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

---

## Decisiones de diseño (importantes)

**1. Separé las agregaciones en CTEs para evitar fan-out.**
Es el bug más común en este tipo de query: si haces `JOIN order_items` y luego `SUM(o.total)`, el total de cada orden se multiplica por su número de líneas. Los importes salen inflados y no es obvio a simple vista. Al calcular `metricas` sobre `orders` puro y las categorías por separado, cada cosa se agrega a su propia granularidad.

**2. `revenue = SUM(orders.total)`.**
Asumo que `orders.total` es la fuente de verdad. Si tu `total` incluye envío/impuestos y