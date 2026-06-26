# Kimi K2.7 Code — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.57 | quality: 9.72
- latency_total: 77.654s | tokens_per_second: 31.0
- input_tokens: 159 | output_tokens: 2411
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una query que cumple con lo que pides. Está pensada para **MySQL 8+** (por el uso de `ROW_NUMBER` y `DATE_SUB`). Si usas **PostgreSQL**, solo cambia la forma de calcular los últimos 6 meses (ver nota al final).

```sql
WITH completed_orders AS (
    -- Órdenes completadas de los últimos 6 meses
    SELECT *
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),
customer_stats AS (
    -- Métricas principales por cliente
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN completed_orders o ON o.customer_id = c.id
    JOIN order_items oi ON oi.order_id = o.id
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
category_rank AS (
    -- Categoría más comprada por cliente (por cantidad total)
    SELECT
        c.id AS customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY c.id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM customers c
    JOIN completed_orders o ON o.customer_id = c.id
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY
        c.id, p.category
)
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_rank cr
    ON cr.customer_id = cs.customer_id
    AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes

1. **Revenue**: se calcula como `quantity * unit_price` desde `order_items`. Si prefieres usar el campo `orders.total`, puedes cambiar `SUM(oi.quantity * oi.unit_price)` por `SUM(o.total)`, aunque idealmente ambos deberían coincidir.
2. **Categoría más comprada**: la define como la categoría con mayor **cantidad total de productos comprados**. Si prefieres definirla por mayor **ingreso**, cambia el `ORDER BY` de `category_rank` a:
   ```sql
   ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category ASC
   ```
3. **Filtro de 3 órdenes**: aplica solo a órdenes completadas (`status = 'completed'`) dentro de los últimos 6 meses.
4. **PostgreSQL**: reemplaza:
   ```sql
   created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
   ```
   por:
   ```sql
   created_at >= NOW() - INTERVAL '6 months'
   ```