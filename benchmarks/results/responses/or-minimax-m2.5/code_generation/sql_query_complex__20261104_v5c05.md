# MiniMax M2.5 — code_generation/sql_query_complex

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.82 | quality: 9.8
- latency_total: 11.074s | tokens_per_second: 110.5
- input_tokens: 178 | output_tokens: 1224
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

# Query SQL para Top 10 Clientes por Revenue

Aquí tienes la consulta completa usando CTEs para mayor claridad:

```sql
WITH recent_orders AS (
    -- Paso 1: Órdenes de los últimos 6 meses con status 'completed'
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
),
customer_order_stats AS (
    -- Paso 2: Stats por cliente (solo los que tienen al menos 3 orders)
    SELECT 
        o.customer_id,
        COUNT(*) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM recent_orders o
    GROUP BY o.customer_id
    HAVING COUNT(*) >= 3
),
customer_categories AS (
    -- Paso 3: Obtener total gastado por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_total
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.id
    JOIN products p ON oi.product_id = p.id
    JOIN recent_orders ro ON o.id = ro.id
    GROUP BY o.customer_id, p.category
),
top_category AS (
    -- Paso 4: Quedarse con la categoría principal de cada cliente
    SELECT 
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY category_total DESC) AS rn
        FROM customer_categories
    ) ranked
    WHERE rn = 1
)
-- Paso 5: JOIN final y ordenamiento
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cos.total_orders,
    cos.total_revenue,
    cos.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_order_stats cos
JOIN customers c ON cos.customer_id = c.id
JOIN top_category tc ON cos.customer_id = tc.customer_id
ORDER BY cos.total_revenue DESC
LIMIT 10;
```

## Explicación de los pasos:

| CTE | Propósito |
|-----|-----------|
| `recent_orders` | Filtra orders de últimos 6 meses con status 'completed' |
| `customer_order_stats` | Calcula stats y filtra clientes con ≥3 órdenes |
| `customer_categories` | Suma revenue por categoría por cliente |
| `top_category` | Obtiene la categoría con más compras usando `ROW_NUMBER()` |

## Notas:

- **Para MySQL 8.0+**: La query funciona exactamente como está
- **Para MySQL 5.x**: El `ROW_NUMBER()` no está disponible, tendrías que usar una subquery con variables o un approach diferente
- **Para PostgreSQL**: Funciona igual, solo cambia `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` por `CURRENT_DATE - INTERVAL '6 months'`

¿Necesitas alguna adaptación para otra base de datos?