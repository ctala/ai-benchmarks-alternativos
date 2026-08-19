# KAT Coder Air v2.5 — code_generation/sql_query_complex

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.22 | quality: 9.8
- latency_total: 4.959s | tokens_per_second: 182.9
- input_tokens: 161 | output_tokens: 907
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



# Top 10 Clientes por Revenue — Últimos 6 Meses

```sql
WITH completed_orders AS (
    -- Solo órdenes completadas en los últimos 6 meses
    SELECT
        o.id          AS order_id,
        o.customer_id,
        o.total       AS order_total,
        oi.product_id,
        oi.quantity,
        p.category
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p     ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_stats AS (
    -- Agregación por cliente
    SELECT
        c.id            AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.order_total)         AS total_revenue,
        AVG(co.order_total)         AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON co.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3
),

category_ranking AS (
    -- Categoría más comprada por cliente (por cantidad de ítems)
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY SUM(quantity) DESC
        ) AS rn
    FROM completed_orders
    GROUP BY customer_id, category
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    ROUND(cs.total_revenue, 2)  AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_ranking cr
    ON cr.customer_id = cs.customer_id
   AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

## Explicación paso a paso

| CTE | Propósito |
|---|---|
| `completed_orders` | Filtra órdenes `completed` de los últimos 6 meses y une con items y productos |
| `customer_stats` | Agrupa por cliente: cantidad de órdenes, revenue total y valor promedio. El `HAVING` aplica el filtro de ≥ 3 órdenes |
| `category_ranking` | Usa `ROW_NUMBER()` particionado por cliente para identificar la categoría más comprada (por `SUM(quantity)`) |

## Notas

- **`categoria_mas_comprada`** se define como la categoría con mayor cantidad de unidades compradas. Si prefieres por *número de líneas de orden* distintas, cambia `SUM(quantity)` por `COUNT(*)` en el `ORDER BY` del `ROW_NUMBER()`.
- **`CURRENT_DATE - INTERVAL '6 months'`** es sintaxis PostgreSQL/MySQL. En **SQL Server** sería `DATEADD(month, -6, CAST(GETDATE() AS DATE))`.
- El `LEFT JOIN` con `category_ranking` asegura que un cliente con ≥ 3 órdenes siempre aparezca, incluso si no tuviera items asociados (caso extremo).