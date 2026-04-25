# Claude Opus 4.6 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.63 | quality: 9.52
- latency_total: 18.455s | tokens_per_second: 63.1
- input_tokens: 178 | output_tokens: 1164
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue (últimos 6 meses)

## La Query

```sql
WITH customer_revenue AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)  AS total_orders,
        SUM(o.total)          AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    INNER JOIN orders o
        ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),

-- Categoría más comprada por cada cliente (por cantidad de unidades)
category_ranking AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi ON oi.order_id = o.id
    INNER JOIN products p     ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

SELECT
    cr.name                    AS nombre,
    cr.email,
    cr.country                 AS pais,
    cr.total_orders,
    cr.total_revenue,
    cr.avg_order_value,
    cat.category               AS categoria_mas_comprada
FROM customer_revenue cr
LEFT JOIN category_ranking cat
    ON cat.customer_id = cr.customer_id
   AND cat.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

---

## Explicación paso a paso

### Estructura visual del flujo

```
┌─────────────────────────────────────────────────────┐
│                   CTE 1: customer_revenue           │
│                                                     │
│  customers ──JOIN── orders (completed, 6 meses)     │
│                                                     │
│  → Agrupa por cliente                               │
│  → Filtra: HAVING count >= 3                        │
│  → Calcula: total_orders, revenue, avg_order_value  │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────┴──────────────────────────────┐
│                   CTE 2: category_ranking           │
│                                                     │
│  orders ──JOIN── order_items ──JOIN── products      │
│                                                     │
│  → Agrupa por (customer_id, category)               │
│  → ROW_NUMBER() para rankear categorías por cliente │
│  → rn = 1  →  categoría más comprada               │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────┴──────────────────────────────┐
│                   SELECT FINAL                      │
│                                                     │
│  customer_revenue ──LEFT JOIN── category_ranking    │
│                                                     │
│  → ORDER BY total_revenue DESC                      │
│  → LIMIT 10                                         │
└─────────────────────────────────────────────────────┘
```

### Decisiones clave

| Decisión | Razón |
|---|---|
| **`COUNT(DISTINCT o.id)`** | Evita contar duplicados si el JOIN con items multiplica filas |
| **`ROW_NUMBER()` en vez de `RANK()`** | Garantiza **exactamente 1** categoría por cliente (sin empates) |
| **`LEFT JOIN`** con category_ranking | Protege contra edge cases donde un cliente no tenga items |
| **CTEs separados** | Evita mezclar agregaciones de distinto nivel (orden vs. item) |
| **Filtros replicados** en ambos CTEs | Asegura que la categoría se calcule sobre el **mismo período y status** |

> **Nota MySQL:** Cambia `NOW() - INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)` y `LIMIT 10` se mantiene igual.