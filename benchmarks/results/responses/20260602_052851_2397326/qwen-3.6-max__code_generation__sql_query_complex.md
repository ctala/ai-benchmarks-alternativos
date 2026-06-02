# Qwen 3.6 Max — code_generation/sql_query_complex

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.26 | quality: 10.0
- latency_total: 116.946s | tokens_per_second: 45.5
- input_tokens: 161 | output_tokens: 5320
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes una query optimizada y compatible con SQL moderno (PostgreSQL, MySQL 8.0+, SQL Server, etc.). Utiliza CTEs para mantener la lógica clara y eficiente.

```sql
WITH filtered_orders AS (
    -- 1. Filtramos órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Agregamos métricas básicas por cliente
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(fo.id) AS total_orders,
        ROUND(SUM(fo.total), 2) AS total_revenue,
        ROUND(AVG(fo.total), 2) AS avg_order_value
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(fo.id) >= 3
),
category_stats AS (
    -- 3. Calculamos cantidad comprada por categoría y cliente
    SELECT
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM filtered_orders fo
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
),
category_ranking AS (
    -- 4. Rankeamos categorías por cliente (la más comprada queda en rn = 1)
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER(
            PARTITION BY customer_id 
            ORDER BY total_qty DESC, category ASC
        ) AS rn
    FROM category_stats
)
-- 5. Resultado final
SELECT
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_ranking cr ON cm.id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **Filtro de fecha**: 
   - `CURRENT_DATE - INTERVAL '6 months'` es sintaxis **PostgreSQL**. 
   - Para **MySQL** usa: `created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   - Para **SQL Server**: `created_at >= DATEADD(month, -6, CAST(GETDATE() AS DATE))`
2. **Cálculo de revenue**: Se usa `orders.total` como indica tu esquema. Si prefieres calcularlo desde los ítems (ej. para excluir impuestos/envíos), cambia `SUM(fo.total)` por `SUM(oi.quantity * oi.unit_price)` y ajusta los JOINs.
3. **Categoría más comprada**: Se basa en `SUM(quantity)`. Si prefieres basarla en dinero gastado por categoría, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en `category_stats`.
4. **Empates en categoría**: `ROW_NUMBER()` elige una categoría determinísticamente (orden alfabético en caso de empate). Si quieres mostrar todas las empatadas, cambia `ROW_NUMBER()` por `RANK()` y ajusta el filtro a `rn = 1`.
5. **Performance recomendada**: Asegúrate de tener índices en:
   - `orders(customer_id, status, created_at)`
   - `order_items(order_id, product_id)`
   - `products(id, category)`

¿Necesitas que la adapte a un motor específico (MySQL, PostgreSQL, SQL Server, BigQuery) o que ajuste la lógica de revenue/categoría?