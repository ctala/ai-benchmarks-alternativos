# Claude Fable 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.72 | quality: 9.52
- latency_total: 16.901s | tokens_per_second: 76.9
- input_tokens: 221 | output_tokens: 1299
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query (sintaxis PostgreSQL):

```sql
WITH ordenes_completadas AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

metricas_cliente AS (
    SELECT
        oc.customer_id,
        COUNT(oc.id)      AS total_orders,
        SUM(oc.total)     AS total_revenue,
        AVG(oc.total)     AS avg_order_value
    FROM ordenes_completadas oc
    GROUP BY oc.customer_id
    HAVING COUNT(oc.id) >= 3
),

categoria_top AS (
    SELECT
        oc.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY oc.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC
        ) AS rn
    FROM ordenes_completadas oc
    JOIN order_items oi ON oi.order_id = oc.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY oc.customer_id, p.category
)

SELECT
    c.name                              AS nombre,
    c.email,
    c.country                           AS pais,
    mc.total_orders,
    mc.total_revenue,
    ROUND(mc.avg_order_value, 2)        AS avg_order_value,
    ct.category                         AS categoria_mas_comprada
FROM metricas_cliente mc
JOIN customers c      ON c.id = mc.customer_id
LEFT JOIN categoria_top ct ON ct.customer_id = mc.customer_id AND ct.rn = 1
ORDER BY mc.total_revenue DESC
LIMIT 10;
```

**Explicación de la estructura:**

1. **`ordenes_completadas`**: filtra una sola vez las órdenes completadas de los últimos 6 meses, para reutilizarlas en los otros CTEs y evitar repetir el filtro.

2. **`metricas_cliente`**: calcula órdenes totales, revenue y ticket promedio por cliente. El `HAVING COUNT(*) >= 3` aplica el requisito de mínimo 3 órdenes completadas.

3. **`categoria_top`**: determina la categoría más comprada por cliente usando `ROW_NUMBER()`, rankeando por el monto gastado (`quantity * unit_price`). Luego solo tomamos `rn = 1`.

**Notas / decisiones que podrías ajustar:**

- **"Categoría más comprada"**: la definí por **monto gastado**. Si prefieres definirla por **cantidad de unidades**, cambia el `ORDER BY` del window a `SUM(oi.quantity) DESC`.
- **Empates de categoría**: `ROW_NUMBER()` elige una arbitrariamente en caso de empate. Puedes agregar un desempate como `, p.category ASC` en el `ORDER BY` del window para que sea determinístico.
- **MySQL 8+**: funciona igual, solo cambia el intervalo a `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`.
- Uso `LEFT JOIN` a `categoria_top` por seguridad, aunque en la práctica todo cliente con órdenes completadas debería tener items.