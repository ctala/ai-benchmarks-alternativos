# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.14 | quality: 9.8
- latency_total: 7.248s | tokens_per_second: 142.5
- input_tokens: 153 | output_tokens: 1033
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes una consulta SQL que cumple con todos los requisitos:

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    ROUND(SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id), 2) AS avg_order_value,
    (
        SELECT p2.category
        FROM orders o2
        JOIN order_items oi2 ON o2.id = oi2.order_id
        JOIN products p2 ON oi2.product_id = p2.id
        WHERE o2.customer_id = c.id
          AND o2.status = 'completed'
          AND o2.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY p2.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
WHERE o.status = 'completed'
  AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

### Notas importantes:
- **`CURRENT_DATE - INTERVAL '6 months'`**: Ajusta según tu SGBD (MySQL usa `INTERVAL 6 MONTH`, PostgreSQL usa `INTERVAL '6 months'`, SQL Server usa `DATEADD(MONTH, -6, GETDATE())`).
- **`categoria_mas_comprada`**: Se calcula como la categoría con mayor **cantidad de unidades vendidas** (no por ingresos ni número de pedidos). Si prefieres por número de pedidos o ingresos, se debe ajustar el `ORDER BY`.
- **`ROUND(..., 2)`**: Para redondear el valor promedio a 2 decimales.
- **`COUNT(DISTINCT o.id)`**: Asegura contar pedidos únicos, evitando duplicados si hubiera múltiples items por pedido.
- **Filtro `status = 'completed'`**: Aplicado tanto en la cláusula `WHERE` general como en la subconsulta interna para evitar incluir pedidos no completados en el cálculo del *top* o en la categoría más comprada.

### Alternativa para `categoria_mas_comprada` (más eficiente con CTE):
Si el motor lo permite (PostgreSQL, MySQL 8+, SQL Server), puedes usar un CTE para evitar subconsultas correlacionadas (mejor rendimiento):

```sql
WITH completed_orders_last_6m AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id AS order_id,
        oi.product_id,
        oi.quantity,
        p.category
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    SELECT 
        customer_id,
        name,
        email,
        country,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(quantity) AS total_units,
        SUM(quantity * (SELECT price FROM products WHERE id = product_id)) AS total_revenue -- opcional usar unit_price de order_items
    FROM completed_orders_last_6m
    GROUP BY customer_id, name, email, country
    HAVING COUNT(DISTINCT order_id) >= 3
),
category_rank AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS qty,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC) AS rn
    FROM completed_orders_last_6m
    GROUP BY customer_id, category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_rank cr ON cs.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

> **Nota**: Usa la primera versión si necesitas compatibilidad con bases más antiguas (MySQL < 8, SQLite, etc.). La segunda es más limpia y escalable. Ajusta `CURRENT_DATE - INTERVAL '6 months'` según tu sistema (ej. en MySQL: `CURDATE() - INTERVAL 6 MONTH`).