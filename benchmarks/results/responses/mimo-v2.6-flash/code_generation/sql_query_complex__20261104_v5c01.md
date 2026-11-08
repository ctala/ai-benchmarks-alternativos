# MiMo V2.6 Flash — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 55.236s | tokens_per_second: 34.8
- input_tokens: 152 | output_tokens: 1922
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

# Query SQL: Top 10 Clientes por Revenue

## Estrategia

```
1. Filtrar órdenes completadas de los últimos 6 meses
2. Calcular métricas por cliente (revenue, órdenes, AOV)
3. Usar ROW_NUMBER() para obtener la categoría más comprada
4. HAVING ≥ 3 órdenes completadas
5. LIMIT 10
```

## Query

```sql
-- ──────────────────────────────────────────────
-- CTE 1: Órdenes completadas de los últimos 6 meses
-- ──────────────────────────────────────────────
WITH ordenes_recientes AS (
    SELECT
        o.id          AS order_id,
        o.customer_id
    FROM orders o
    WHERE o.status    = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)   -- MySQL
      -- AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'   -- PostgreSQL
      -- AND o.created_at >= DATEADD(MONTH, -6, GETDATE())        -- SQL Server
),

-- ──────────────────────────────────────────────
-- CTE 2: Métricas por cliente
-- ──────────────────────────────────────────────
metricas_clientes AS (
    SELECT
        c.id                          AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.order_id)    AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN ordenes_recientes o   ON o.customer_id = c.id
    JOIN order_items oi        ON oi.order_id   = o.order_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.order_id) >= 3        -- mínimo 3 órdenes
),

-- ──────────────────────────────────────────────
-- CTE 3: Categoría más comprada por cliente
--        (usando ROW_NUMBER para asignar #1)
-- ──────────────────────────────────────────────
categorias_rank AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY     SUM(oi.quantity) DESC
        ) AS rn
    FROM ordenes_recientes o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)

-- ──────────────────────────────────────────────
-- SELECT FINAL
-- ──────────────────────────────────────────────
SELECT
    mc.name,
    mc.email,
    mc.country,
    mc.total_orders,
    ROUND(mc.total_revenue, 2)                       AS total_revenue,
    ROUND(mc.total_revenue / mc.total_orders, 2)     AS avg_order_value,
    cr.category                                       AS categoria_mas_comprada
FROM metricas_clientes mc
JOIN categorias_rank cr
    ON  cr.customer_id = mc.customer_id
    AND cr.rn = 1                                    -- solo la #1
ORDER BY mc.total_revenue DESC
LIMIT 10;
```

## Explicación visual del flujo

```
orders (completed, last 6m)
        │
        ├──► metricas_clientes ──────────────────────────┐
        │    • total_orders (HAVING ≥ 3)                 │
        │    • total_revenue                             │
        │    • avg_order_value (calculado)               │
        │                                                │
        └──► categorias_rank ───────────────────────────┤
             • ROW_NUMBER() por categoría               │
             • rn = 1 → categoría más comprada          │
                                                          │
                    ┌────────────────────────────────────┘
                    ▼
              JOIN + SELECT final
              ORDER BY total_revenue DESC
              LIMIT 10
```

## Resultado esperado

| name | email | country | total_orders | total_revenue | avg_order_value | categoria_mas_comprada |
|------|-------|---------|:------------:|:-------------:|:---------------:|:----------------------:|
| Ana García | ana@email.com | España | 12 | 8450.00 | 704.17 | Electronics |
| John Smith | john@email.com | USA | 8 | 6230.50 | 778.81 | Home & Garden |
| ... | ... | ... | ... | ... | ... | ... |

## Notas

| Concepto | Detalle |
|----------|---------|
| **total_revenue** | `SUM(quantity × unit_price)` → revenue real de los items |
| **avg_order_value** | `total_revenue ÷ total_orders` → valor promedio por orden |
| **categoria_mas_comprada** | La categoría con mayor `SUM(quantity)` acumulada |
| **HAVING ≥ 3** | Se aplica *antes* del LIMIT para respetar el filtro de negocio |
| **DATE_SUB** | Ajusta la función según tu dialecto de SQL (ver comentarios) |