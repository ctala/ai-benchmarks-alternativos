# Claude Opus 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 22.807s | tokens_per_second: 89.8
- input_tokens: 221 | output_tokens: 2048
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
    -- Filtro base: una sola vez, reutilizado abajo
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas AS (
    -- Agregados a nivel orden (SIN join a items para no duplicar filas)
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categorias_ranked AS (
    -- Categoría dominante por cliente
    SELECT
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC,                      -- criterio 1: unidades
                     SUM(oi.quantity * oi.unit_price) DESC,      -- desempate: gasto
                     p.category ASC                              -- desempate estable
        ) AS rn
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products    p  ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)

SELECT
    c.name                          AS nombre,
    c.email,
    c.country                       AS pais,
    m.total_orders,
    ROUND(m.total_revenue, 2)       AS total_revenue,
    ROUND(m.avg_order_value, 2)     AS avg_order_value,
    cr.category                     AS categoria_mas_comprada
FROM metricas m
JOIN customers c        ON c.id = m.customer_id
LEFT JOIN categorias_ranked cr
       ON cr.customer_id = m.customer_id
      AND cr.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

## Por qué está estructurada así

**1. El bug clásico que evita:** si haces `orders JOIN order_items` y luego `SUM(o.total)`, el total se multiplica por el número de items de cada orden. Por eso separo los agregados de orden (`metricas`) de los agregados de items (`categorias_ranked`).

**2. `LEFT JOIN` en la categoría:** un cliente podría tener órdenes completadas sin filas en `order_items` (datos sucios, órdenes de servicio, etc.). Con `INNER JOIN` lo perderías del top 10 silenciosamente.

**3. Desempate explícito:** sin el `ORDER BY` de 3 niveles, un cliente con empate entre categorías devolvería un resultado no determinista que cambia entre ejecuciones.

## Dos decisiones que deberías confirmar

**¿"Más comprada" = unidades o gasto?** Puse unidades primero. Si tu negocio la mide por revenue (más común en reportes de e-commerce), invierte las dos primeras lí