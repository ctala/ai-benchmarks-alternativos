# MiMo-V2.5 Pro — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.38 | quality: 9.8
- latency_total: 26.712s | tokens_per_second: 74.1
- input_tokens: 396 | output_tokens: 1980
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL compleja que cumple con todos los requisitos especificados.

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue (Últimos 6 Meses)

## La Query

```sql
WITH customer_stats AS (
    -- Estadísticas generales del cliente
    SELECT
        c.id            AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)    AS total_orders,
        SUM(o.total)            AS total_revenue,
        ROUND(SUM(o.total) / COUNT(DISTINCT o.id), 2) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_top_category AS (
    -- Categoría más comprada por cliente (por cantidad de items)
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi ON oi.order_id  = o.id
    INNER JOIN products p     ON p.id         = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_top_category ctc
       ON ctc.customer_id = cs.customer_id
      AND ctc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

---

## Cómo funciona paso a paso

```
┌─────────────────────────────────────────────────────────────────┐
│  CTE 1: customer_stats                                          │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ orders (status = 'completed', últimos 6 meses)           │  │
│  │         INNER JOIN customers                              │  │
│  │         GROUP BY customer                                 │  │
│  │         HAVING COUNT(*) >= 3   ← mínimo 3 órdenes        │  │
│  └───────────────────────────────────────────────────────────┘  │
│              │                                                  │
│              ▼                                                  │
│  CTE 2: customer_top_category                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ orders → order_items → products                           │  │
│  │ GROUP BY customer, category → SUM(quantity)               │  │
│  │ ROW_NUMBER() partitioned by customer                      │  │
│  │ ... ORDER BY SUM(quantity) DESC                           │  │
│  └───────────────────────────────────────────────────────────┘  │
│              │                                                  │
│              ▼                                                  │
│  SELECT principal: LEFT JOIN cte1 ← cte2 (solo rn = 1)        │
│  ORDER BY total_revenue DESC LIMIT 10                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ejemplo de resultado

| name | email | country | total\_orders | total\_revenue | avg\_order\_value | categoria\_mas\_comprada |
|---|---|---|---|---|---|---|
| Ana García | ana@ejemplo.com | MX | 12 | 15,420.00 | 1,285.00 | Electronics |
| Carlos Ruiz | carlos@ejemplo.com | ES | 8 | 9,870.00 | 1,233.75 | Sports |
| María López | maria@ejemplo.com | AR | 5 | 4,350.00 | 870.00 | Home & Garden |

---

## Notas importantes

| Aspecto | Detalle |
|---|---|
| **Ventana temporal** | `CURRENT_DATE - INTERVAL '6 months'` es sintaxis **PostgreSQL**. Para MySQL usa `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)` |
| **Revenue** | Se usa `SUM(o.total)` de la tabla `orders` (no se recalcula desde `order_items`) |
| **Categoría más comprada** | Se determina por **cantidad de items** (`SUM(quantity)`). Si prefieres por **monto gastado**, cambia a `SUM(oi.quantity * oi.unit_price)` |
| **LEFT JOIN** | Se usa LEFT JOIN en la categoría por si algún cliente no tuviera items (edge case improbable) |
| **DISTINCT** | `COUNT(DISTINCT o.id)` evita duplicados si un JOIN multiplicara filas |