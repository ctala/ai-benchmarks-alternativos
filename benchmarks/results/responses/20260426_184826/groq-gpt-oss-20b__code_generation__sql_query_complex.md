# GPT-OSS 20B (Groq) — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.93 | quality: 8.8
- latency_total: 2.338s | tokens_per_second: 816.2
- input_tokens: 212 | output_tokens: 1908
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes una solución que funciona en PostgreSQL (puedes adaptarla a MySQL, SQL‑Server, etc. cambiando la forma de calcular el intervalo de 6 meses y las funciones de ventana).

```sql
/* 1. Seleccionamos las órdenes completadas de los últimos 6 meses   */
WITH last6m_orders AS (
    SELECT
        o.id          AS order_id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= current_date - interval '6 months'
),

/* 2. Agrupamos por cliente: nº de órdenes, revenue total, etc.     */
customer_stats AS (
    SELECT
        o.customer_id,
        COUNT(DISTINCT o.order_id)                AS total_orders,
        SUM(o.total)                              AS total_revenue
    FROM last6m_orders o
    GROUP BY o.customer_id
),

/* 3. Para cada cliente hallamos la categoría más comprada          */
customer_top_category AS (
    SELECT
        oi.order_id,
        p.category,
        SUM(oi.quantity) AS qty
    FROM order_items oi
    JOIN last6m_orders lo ON oi.order_id = lo.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY oi.order_id, p.category
),

/* 4. Sumamos las cantidades por categoría y por cliente            */
customer_category_totals AS (
    SELECT
        lo.customer_id,
        ct.category,
        SUM(ct.qty) AS total_qty
    FROM customer_top_category ct
    JOIN last6m_orders lo ON ct.order_id = lo.order_id
    GROUP BY lo.customer_id, ct.category
),

/* 5. Seleccionamos la categoría con mayor cantidad por cliente     */
customer_best_category AS (
    SELECT
        customer_id,
        category AS category_mas_comprada,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_qty DESC) AS rn
    FROM customer_category_totals
)

SELECT
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.total_revenue / NULLIF(cs.total_orders,0), 2) AS avg_order_value,
    cbc.category_mas_comprada
FROM customers c
JOIN customer_stats cs ON cs.customer_id = c.id
JOIN customer_best_category cbc
      ON cbc.customer_id = c.id
     AND cbc.rn = 1                     -- la categoría más comprada
WHERE cs.total_orders >= 3              -- al menos 3 órdenes completadas
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación rápida

| Paso | Qué hace | Tabla/CTE involucrado |
|------|----------|------------------------|
| 1 | Filtra las órdenes completadas de los últimos 6 meses | `last6m_orders` |
| 2 | Calcula para cada cliente: nº de órdenes y revenue total | `customer_stats` |
| 3 | Agrupa por categoría la cantidad comprada en cada orden | `customer_top_category` |
| 4 | Suma las cantidades por categoría y por cliente | `customer_category_totals` |
| 5 | Selecciona, por cliente, la categoría con mayor cantidad | `customer_best_category` |
| 6 | Junta todo, calcula el valor medio por orden y devuelve los 10 clientes con mayor revenue | SELECT final |

Puedes adaptar el `current_date - interval '6 months'` a tu dialecto si no es PostgreSQL (por ejemplo, `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` en MySQL). ¡Listo!