# Claude Opus 5 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-opus-5`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 49.662s | tokens_per_second: 69.7
- input_tokens: 2 | output_tokens: 3459
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada con explicaciones detalladas y consideraciones de diseño.

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
WITH ordenes_validas AS (
    -- Base común: órdenes completadas en la ventana de 6 meses
    SELECT o.id, o.customer_id, o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas AS (
    -- Agregado a nivel orden (NO se toca order_items acá, ver nota 1)
    SELECT
        customer_id,
        COUNT(*)   AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM ordenes_validas
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_gasto AS (
    -- Gasto por categoría, rankeado dentro de cada cliente
    SELECT
        ov.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS gasto,
        ROW_NUMBER() OVER (
            PARTITION BY ov.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category ASC
        ) AS rn
    FROM ordenes_validas ov
    JOIN order_items oi ON oi.order_id = ov.id
    JOIN products    p  ON p.id = oi.product_id
    GROUP BY ov.customer_id, p.category
)

SELECT
    c.name                                  AS nombre,
    c.email,
    c.country                               AS pais,
    m.total_orders,
    ROUND(m.total_revenue::numeric, 2)      AS total_revenue,
    ROUND(m.avg_order_value::numeric, 2)    AS avg_order_value,
    cg.category                             AS categoria_mas_comprada
FROM metricas m
JOIN customers c        ON c.id = m.customer_id
LEFT JOIN categoria_gasto cg
       ON cg.customer_id = m.customer_id
      AND cg.rn = 1
ORDER BY m.total_revenue DESC, c.id
LIMIT 10;
```

## Notas de diseño (las que importan)

**1. Por qué CTEs separadas y no un solo JOIN.**
Si unes `orders → order_items` y luego haces `SUM(o.total)`, cada orden se repite una vez por línea de detalle y el revenue se infla. Una orden de $100 con 4 productos suma $400. Es el bug más común en este tipo de query. Por eso `metricas` agrega a nivel orden y `categoria_gasto` baja al detalle por separado.

**2. `orders.total` vs sumar `order_items`.**
Uso `orders.total` porque es el valor cabecera (normalmente ya incluye envío, impuestos y descuentos). Si en tu esquema `total` es sucio o querés revenue neto de productos, reemplaza el CTE `metricas` por un `SUM(oi.quantity * oi.unit_price)` agrupado primero por `order_id` y después por `customer_id`. No mezcles las dos definiciones en el mismo reporte.

**3. "Categoría más comprada" = por gasto, no por unidades.**
Un cliente que compra 50 stickers de $1 y 2 laptops de $1.500 tiene su categoría real en laptops. Si querés el criterio por volumen, cambia el `SUM(oi.quantity * oi.unit_price)` por `SUM(oi.quantity)` en las dos apariciones (el `ORDER BY` de la ventana también).

**4. Empates.** `ROW_NUMBER` con desempate alfabético (`p.category ASC`) hace la salida determinista. Sin eso, dos categorías con el mismo gasto devuelven resultado distinto en cada corrida. Igual el `ORDER BY ... , c.id` del final.

**5. `LEFT JOIN` en la categoría.** Si una orden quedó sin líneas en `order_items` (data sucia), el cliente igual aparece con su revenue y `categoria_mas_comprada = NULL`. Con `INNER JOIN` desaparecería del top silenciosamente.

**6. Índices para que no se arrastre:**
```sql
CREATE INDEX idx_orders_cust_status_date ON orders (customer_id, status, created_at);
CREATE INDEX idx_order_items_order       ON order_items (order_id);
```

## Variante MySQL 8

Cambia solo dos cosas:

```sql
-- ventana
AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)

-- redondeo (sin cast a numeric)
ROUND(m.total_revenue, 2)
```

El resto (CTEs + `ROW_NUMBER` sobre agregado) funciona igual desde MySQL 8.0.