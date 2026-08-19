# Kimi K2.6 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.83 | quality: 9.52
- latency_total: 268.465s | tokens_per_second: 16.6
- input_tokens: 159 | output_tokens: 4444
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Aquí tienes la query usando **PostgreSQL** (con notas para adaptarla a MySQL/SQL Server si es necesario):

```sql
WITH filtered_orders AS (
    /* 1. Órdenes completadas de los últimos 6 meses */
    SELECT 
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
      /* MySQL:     o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH) */
      /* SQL Server: o.created_at >= DATEADD(month, -6, GETDATE())    */
),
customer_metrics AS (
    /* 2. Métricas por cliente + filtro de mínimo 3 órdenes */
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(*) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM filtered_orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(*) >= 3
),
category_ranking AS (
    /* 3. Categoría más comprada por cantidad de unidades */
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM filtered_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
/* 4. Resultado final */
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    ROUND(cm.total_revenue::numeric / cm.total_orders, 2) AS avg_order_value,
    COALESCE(cr.category, 'Sin categoría') AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_ranking cr 
    ON cm.customer_id = cr.customer_id 
    AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Detalles importantes:

| Aspecto | Implementación |
|---------|----------------|
| **Revenue** | Usa `orders.total` (más directo). Si prefieres calcularlo desde ítems, cambia `SUM(o.total)` por `SUM(oi.quantity * oi.unit_price)` y añade el JOIN con `order_items`. |
| **Categoría más comprada** | Se define por **cantidad total de unidades** (`SUM(quantity)`). Si prefieres usar *revenue* o *número de órdenes*, cambia el `ORDER BY` dentro de `ROW_NUMBER()`. |
| **Empates** | `ROW_NUMBER()` elige una si hay empate. Si quieres mostrar todas las categorías empatadas en primer lugar, usa `RANK()` en vez de `ROW_NUMBER()`. |
| **avg_order_value** | `total_revenue / total_orders`. El `::numeric` es para PostgreSQL; en MySQL simplemente usa `ROUND(cm.total_revenue / cm.total_orders, 2)`. |
| **Seguridad** | Uso `LEFT JOIN` + `COALESCE` por si existiera algún cliente con órdenes pero sin ítems registrados (caso borde). |

¿Necesitas adaptarla para un motor específico (MySQL, SQL Server, BigQuery, etc.)?