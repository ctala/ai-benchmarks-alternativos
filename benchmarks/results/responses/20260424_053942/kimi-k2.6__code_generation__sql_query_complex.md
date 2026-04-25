# Kimi K2.6 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.93 | quality: 9.52
- latency_total: 102.215s | tokens_per_second: 37.6
- input_tokens: 158 | output_tokens: 3844
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query. Usa **CTEs** para mayor claridad y está escrita en sintaxis **PostgreSQL/MySQL 8.0+**.

```sql
WITH filtered_orders AS (
    /* 1. Órdenes completadas de los últimos 6 meses con datos del cliente */
    SELECT 
        o.id AS order_id,
        o.customer_id,
        c.name,
        c.email,
        c.country
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
      -- MySQL: o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
      -- SQL Server: o.created_at >= DATEADD(month, -6, GETDATE())
),
customer_stats AS (
    /* 2. Métricas por cliente: órdenes, revenue y filtro de mínimo 3 órdenes */
    SELECT 
        fo.customer_id,
        fo.name,
        fo.email,
        fo.country,
        COUNT(DISTINCT fo.order_id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM filtered_orders fo
    JOIN order_items oi ON fo.order_id = oi.order_id
    GROUP BY 
        fo.customer_id, fo.name, fo.email, fo.country
    HAVING COUNT(DISTINCT fo.order_id) >= 3
),
category_ranking AS (
    /* 3. Categorías ordenadas por cantidad total comprada por cada cliente */
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY fo.customer_id 
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM filtered_orders fo
    JOIN order_items oi ON fo.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY 
        fo.customer_id, p.category
)
/* 4. Resultado final */
SELECT 
    cs.name AS nombre,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_ranking cr 
    ON cs.customer_id = cr.customer_id 
    AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes

| Aspecto | Detalle |
|---------|---------|
| **Ventana temporal** | Los filtros de fecha (`created_at`) aplican a **todo** el análisis: revenue, conteo de órdenes y categoría se calculan solo sobre los últimos 6 meses. |
| **Revenue** | Se calcula a partir de `order_items (quantity * unit_price)` para mantener consistencia con el análisis de categorías. |
| **Mínimo 3 órdenes** | El `HAVING` garantiza que solo aparezcan clientes con **3 o más órdenes completadas dentro de esos 6 meses**. |
| **Categoría más comprada** | Se define como la categoría con mayor **cantidad total de productos comprados** (`SUM(quantity)`). Si hay empate, elige la categoría alfabéticamente primera. |
| **Compatibilidad** | Si usas **MySQL < 8.0** o **MariaDB**, las CTE no están disponibles; si usas **SQL Server**, cambia `LIMIT 10` por `TOP 10` y ajusta la función de fecha. |

¿Te gustaría que adapte la sintaxis para algún motor específico (MySQL 5.7, SQL Server, Oracle, etc.) o que cambie la lógica de la categoría más comprada (por ejemplo, por revenue en lugar de cantidad)?