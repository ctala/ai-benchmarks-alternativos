# Ling 3.0 Flash — code_generation/sql_query_complex

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.89 | quality: 9.8
- latency_total: 35.815s | tokens_per_second: 49.8
- input_tokens: 177 | output_tokens: 1783
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')


## Respuesta completa

```sql
WITH customer_revenue AS (
    -- Calcular métricas principales por cliente (órdenes completadas en últimos 6 meses)
    SELECT
        c.id          AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)                       AS total_orders,
        SUM(o.total)                                AS total_revenue,
        SUM(o.total) / COUNT(DISTINCT o.id)         AS avg_order_value
    FROM customers c
    JOIN orders o ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_category AS (
    -- Determinar la categoría más comprada por cliente (por revenue)
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price)            AS category_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p     ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
-- Resultado final: Top 10 clientes por revenue
SELECT
    cr.name              AS nombre,
    cr.email             AS email,
    cr.country           AS pais,
    cr.total_orders      AS total_orders,
    cr.total_revenue     AS total_revenue,
    cr.avg_order_value   AS avg_order_value,
    cc.category          AS categoria_mas_comprada
FROM customer_revenue cr
JOIN customer_category cc
    ON cc.customer_id = cr.customer_id
   AND cc.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso:

| Paso | Qué hace |
|------|----------|
| **`customer_revenue`** | Agrupa por cliente, filtra solo órdenes con `status = 'completed'` de los últimos 6 meses, calcula `total_orders` (COUNT DISTINCT), `total_revenue` (SUM de `orders.total`) y `avg_order_value`. Aplica `HAVING >= 3` órdenes. |
| **`customer_category`** | Para cada cliente, calcula el revenue por categoría (sumando `order_items.quantity × order_items.unit_price`). Usa `ROW_NUMBER()` para rankear las categorías por revenue descendente; la categoría más comprada tendrá `rn = 1`. |
| **Query final** | Une ambos CTEs para obtener la categoría top de cada cliente, ordena por `total_revenue DESC` y limita a 10 resultados. |

> **Nota sobre compatibilidad:** `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` es sintaxis **MySQL**. Para **PostgreSQL**, reemplázalo por `CURRENT_DATE - INTERVAL '6 months'`. Para **SQL Server**, usa `DATEADD(MONTH, -6, GETDATE())`.