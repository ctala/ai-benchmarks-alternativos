# DeepSeek V4 Flash (OpenRouter) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.69 | quality: 9.4
- latency_total: 28.511s | tokens_per_second: 56.9
- input_tokens: 152 | output_tokens: 1622
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
-- Órdenes completadas en los últimos 6 meses
completed_orders AS (
    SELECT o.id, o.customer_id, o.total, o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

-- Agregación por cliente: total_orders, total_revenue, avg_order_value
customer_agg AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue,
        SUM(co.total) / NULLIF(COUNT(co.id), 0) AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON co.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),

-- Conteo de categorías por cliente (basado en las órdenes completadas)
category_counts AS (
    SELECT 
        co.customer_id,
        p.category,
        COUNT(*) AS cnt
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),

-- Ranking de categorías por cliente (la más comprada)
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY cnt DESC, category ASC   -- desempate alfabético
        ) AS rn
    FROM category_counts
)

-- Resultado final
SELECT 
    ca.name,
    ca.email,
    ca.country,
    ca.total_orders,
    ca.total_revenue,
    ca.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_agg ca
LEFT JOIN ranked_categories rc ON rc.customer_id = ca.id AND rc.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```