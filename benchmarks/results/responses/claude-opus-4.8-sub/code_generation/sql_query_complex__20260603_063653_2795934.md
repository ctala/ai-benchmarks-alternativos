# Claude Opus 4.8 (suscripción) — code_generation/sql_query_complex

- model_id: `claude-opus-4-8`
- success: True  | final: 7.28 | quality: 9.52
- latency_total: 19.109s | tokens_per_second: 86.5
- input_tokens: 2026 | output_tokens: 1652
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query. La escribo para **PostgreSQL** (te aviso abajo los ajustes para MySQL):

```sql
WITH ordenes_validas AS (
    -- Órdenes completadas en los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
categoria_top AS (
    -- Categoría más comprada por cliente (por cantidad de items)
    SELECT DISTINCT ON (ov.customer_id)
        ov.customer_id,
        p.category AS categoria_mas_comprada
    FROM ordenes_validas ov
    JOIN order_items oi ON oi.order_id = ov.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY ov.customer_id, p.category
    ORDER BY ov.customer_id, SUM(oi.quantity) DESC, p.category
)
SELECT
    c.name                          AS nombre,
    c.email,
    c.country                       AS pais,
    COUNT(ov.id)                    AS total_orders,
    SUM(ov.total)                   AS total_revenue,
    ROUND(AVG(ov.total), 2)         AS avg_order_value,
    ct.categoria_mas_comprada
FROM customers c
JOIN ordenes_validas ov ON ov.customer_id = c.id
LEFT JOIN categoria_top ct ON ct.customer_id = c.id
GROUP BY c.id, c.name, c.email, c.country, ct.categoria_mas_comprada
HAVING COUNT(ov.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

### Cómo funciona
- **`ordenes_validas`**: filtra una sola vez las órdenes `completed` de los últimos 6 meses (se reutiliza y evita repetir el `WHERE`).
- **`categoria_top`**: usa `DISTINCT ON` para quedarse con la categoría de mayor cantidad (`SUM(quantity)`) por cliente. El `p.category` final en el `ORDER BY` rompe empates de forma determinista.
- **`HAVING COUNT(ov.id) >= 3`**: al menos 3 órdenes completadas (ya filtradas en el CTE).
- **`avg_order_value`**: promedio del `total` por orden.

### Decisiones que conviene que confirmes
- **"Categoría más comprada"** la interpreté como **mayor cantidad de unidades** (`SUM(quantity)`). Si la quieres por **gasto** (`SUM(quantity * unit_price)`) o por **número de órdenes distintas**, cambia el criterio del `ORDER BY` en `categoria_top`.
- **Revenue** lo tomé de `orders.total`. Si prefieres recalcularlo desde `order_items` (`SUM(quantity * unit_price)`) por consistencia con los descuentos/impuestos, avísame y lo ajusto.
- **"Últimos 6 meses"** = desde `CURRENT_DATE - 6 meses`. Si lo necesitas como "meses calendario completos", se ajusta con `date_trunc`.

### Ajustes para MySQL 8+
- Reemplaza el intervalo: `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`.
- MySQL no tiene `DISTINCT ON`. Sustituye el CTE `categoria_top` por una versión con `ROW_NUMBER()`:

```sql
categoria_top AS (
    SELECT customer_id, categoria_mas_comprada FROM (
        SELECT
            ov.customer_id,
            p.category AS categoria_mas_comprada,
            ROW_NUMBER() OVER (
                PARTITION BY ov.customer_id
                ORDER BY SUM(oi.quantity) DESC, p.category
            ) AS rn
        FROM ordenes_validas ov
        JOIN order_items oi ON oi.order_id = ov.id
        JOIN products p     ON p.id = oi.product_id
        GROUP BY ov.customer_id, p.category
    ) t
    WHERE rn = 1
)
```

¿Sobre qué motor lo vas a correr y qué criterio prefieres para "categoría más comprada"? Con eso te dejo la versión final afinada.