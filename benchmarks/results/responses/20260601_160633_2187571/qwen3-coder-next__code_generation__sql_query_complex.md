# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.15 | quality: 9.8
- latency_total: 6.501s | tokens_per_second: 154.7
- input_tokens: 153 | output_tokens: 1006
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes una consulta SQL que cumple con todos los requisitos (usando sintaxis estándar SQL, compatible con PostgreSQL, MySQL 8.0+, SQL Server, etc.):

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    ROUND(SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id), 2) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi2
        JOIN orders o2 ON oi2.order_id = o2.id
        JOIN products p ON oi2.product_id = p.id
        WHERE o2.customer_id = c.id
          AND o2.status = 'completed'
          AND o2.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY p.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
WHERE 
    o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY 
    c.id, c.name, c.email, c.country
HAVING 
    COUNT(DISTINCT o.id) >= 3
ORDER BY 
    total_revenue DESC
LIMIT 10;
```

### Notas importantes:
- **Intervalo de tiempo**: `CURRENT_DATE - INTERVAL '6 months'` es estándar en PostgreSQL y MySQL 8.0+. En SQL Server usarías `DATEADD(MONTH, -6, GETDATE())`, y en SQLite `DATE('now', '-6 months')`.
- **`categoria_mas_comprada`**: Se calcula como la categoría con **mayor cantidad total de unidades vendidas** (no por ingresos), agrupando por categoría en los últimos 6 meses del cliente.
- **`total_revenue`**: Se calcula como `SUM(quantity * unit_price)`, usando el precio unitario en el momento de la compra (`unit_price` de `order_items`), que es más preciso que usar `products.price` actual.
- **Filtrado de órdenes**: Solo se consideran órdenes con `status = 'completed'`.
- **Agrupación**: Se usa `GROUP BY c.id` (y no solo `c.name`) para evitar ambigüedad si hay nombres repetidos.
- **Redondeo**: `avg_order_value` se redondea a 2 decimales.

### Alternativa para `categoria_mas_comprada` (más eficiente en algunos motores):
Si prefieres evitar subconsultas escalares (que se ejecutan por fila), puedes usar una CTE con `ROW_NUMBER()`:

```sql
WITH customer_orders AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue,
        ROUND(SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id), 2) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_counts AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS units,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, p.category
)
SELECT 
    co.*,
    cc.category AS categoria_mas_comprada
FROM customer_orders co
LEFT JOIN category_counts cc 
    ON co.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY co.total_revenue DESC
LIMIT 10;
```

Esta segunda versión es más eficiente si tienes muchos clientes, ya que evita subconsultas repetidas. Usa la que mejor se adapte a tu motor y volumen de datos.