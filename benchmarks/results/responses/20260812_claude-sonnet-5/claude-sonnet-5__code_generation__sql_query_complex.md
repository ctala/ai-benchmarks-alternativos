# Claude Sonnet 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 18.347s | tokens_per_second: 111.6
- input_tokens: 221 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

# Query: Top 10 Clientes por Revenue (últimos 6 meses)

```sql
WITH recent_orders AS (
    -- Filtramos solo órdenes completadas de los últimos 6 meses
    SELECT o.id, o.customer_id, o.total, o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_stats AS (
    -- Métricas agregadas por cliente
    SELECT
        customer_id,
        COUNT(*)          AS total_orders,
        SUM(total)         AS total_revenue,
        AVG(total)         AS avg_order_value
    FROM recent_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3  -- solo clientes con al menos 3 órdenes completadas
),

category_ranking AS (
    -- Suma de cantidades comprada por categoría, por cliente
    SELECT
        ro.customer_id,
        p.category,
        SUM(oi.quantity) AS qty_total,
        ROW_NUMBER() OVER (
            PARTITION BY ro.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products     p  ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),

top_category AS (
    -- Nos quedamos con la categoría #1 por cliente
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_ranking
    WHERE rn = 1
)

SELECT
    c.name                       AS nombre,
    c.email,
    c.country                    AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    tc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c        ON c.id = cs.customer_id
LEFT JOIN top_category tc ON tc.customer_id = cs.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Notas importantes

**1. Sintaxis de fecha según motor:**
```sql
-- PostgreSQL (usada arriba)
o.created_at >= CURRENT_DATE - INTERVAL '6 months'

-- MySQL
o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)

-- SQL Server
o.created_at >= DATEADD(MONTH, -6, GETDATE())
```

**2. ¿Por qué CTEs separadas?**
- `recent_orders`: evita repetir el filtro de fecha/status en cada join
- `customer_stats`: aplica el `HAVING >= 3` antes de calcular la categoría (más eficiente)
- `category_ranking` + `top_category`: usa `ROW_NUMBER()` para desempatar y traer sol