# Mercury 3 — code_generation/sql_query_complex

- model_id: `inception/mercury-3`
- success: True  | final: 8.67 | quality: 9.4
- latency_total: 5.265s | tokens_per_second: 569.4
- input_tokens: 140 | output_tokens: 2998
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

Asumiendo que:

- El revenue se calcula sobre órdenes con `status = 'completed'`.
- Los últimos 6 meses se calculan desde la fecha actual.
- La condición de mínimo 3 órdenes completadas se aplica también a esos últimos 6 meses.
- La categoría más comprada se determina por cantidad de unidades (`SUM(quantity)`).

```sql
WITH pedidos_recientes AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
resumen_clientes AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        ROUND(SUM(total), 2) AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM pedidos_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
totales_categorias AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS cantidad
    FROM pedidos_recientes o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),
categorias_ranked AS (
    SELECT
        customer_id,
        category,
        cantidad,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY cantidad DESC, category
        ) AS rn
    FROM totales_categorias
)
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    r.total_orders,
    r.total_revenue,
    r.avg_order_value,
    cat.category AS categoria_mas_comprada
FROM resumen_clientes r
JOIN customers c ON c.id = r.customer_id
LEFT JOIN categorias_ranked cat
    ON cat.customer_id = r.customer_id
    AND cat.rn = 1
ORDER BY r.total_revenue DESC
LIMIT 10;
```

Si usas MySQL, cambia la condición de fecha por:

```sql
AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
```