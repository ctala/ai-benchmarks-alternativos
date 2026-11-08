# Kimi K2 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 18.464s | tokens_per_second: 41.6
- input_tokens: 160 | output_tokens: 768
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

```sql
WITH 
-- Fecha de inicio: 6 meses atrás
date_range AS (
    SELECT DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH) AS start_date
),

-- Órdenes completadas en los últimos 6 meses con su revenue
completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total AS order_total,
        oi.product_id,
        oi.quantity,
        (oi.quantity * oi.unit_price) AS item_revenue
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
        AND o.created_at >= (SELECT start_date FROM date_range)
),

-- Resumen por cliente
customer_summary AS (
    SELECT 
        co.customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.item_revenue) AS total_revenue,
        AVG(co.order_total) AS avg_order_value
    FROM completed_orders co
    JOIN customers c ON co.customer_id = c.id
    GROUP BY co.customer_id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
),

-- Categoría más comprada por cliente (por cantidad de items)
category_ranking AS (
    SELECT 
        co.customer_id,
        p.category,
        SUM(co.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id 
            ORDER BY SUM(co.quantity) DESC
        ) AS rn
    FROM completed_orders co
    JOIN products p ON co.product_id = p.id
    GROUP BY co.customer_id, p.category
)

-- Resultado final
SELECT 
    cs.name AS nombre,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_summary cs
LEFT JOIN category_ranking cr ON cs.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Explicación del query:

| CTE | Propósito |
|-----|-----------|
| `date_range` | Define el rango de 6 meses atrás |
| `completed_orders` | Filtra órdenes completadas con sus items y revenue |
| `customer_summary` | Agrupa por cliente, calcula métricas y filtra ≥3 órdenes |
| `category_ranking` | Determina la categoría más comprada por cantidad |

## Notas importantes:

1. **Revenue calculado**: Uso `quantity * unit_price` de `order_items` (más preciso que `orders.total`)

2. **Categoría más comprada**: Se define por **cantidad de items** (no por revenue). Si prefieres por revenue, cambia el `ORDER BY` en `ROW_NUMBER()` a `SUM(co.quantity * co.unit_price) DESC`

3. **Empates en categoría**: `ROW_NUMBER()` elige uno arbitrariamente. Para incluir empates, usa `RANK()` o `DENSE_RANK()`

4. **MySQL**: Usa `DATE_SUB()` y `INTERVAL`. Para PostgreSQL: `CURRENT_DATE - INTERVAL '6 months'`

5. **avg_order_value**: Calculado sobre el total de la orden, no el promedio de items