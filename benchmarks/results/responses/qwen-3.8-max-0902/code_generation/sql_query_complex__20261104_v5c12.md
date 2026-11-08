# Qwen 3.8 Max 0902 — code_generation/sql_query_complex

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.45 | quality: 9.4
- latency_total: 308.3s | tokens_per_second: 42.9
- input_tokens: 212 | output_tokens: 13241
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución completa y bien estructurada para la consulta SQL compleja, incluyendo consideraciones adicionales para diferentes métricas.

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

Te dejo una query usando CTEs y window functions. Supuestos:

- “Últimos 6 meses” aplica también al filtro de `status = 'completed'`.
- El mínimo de 3 órdenes completadas se cuenta dentro de esos últimos 6 meses.
- `total_revenue` y `avg_order_value` se calculan desde `orders.total`.
- `categoria_mas_comprada` se define como la categoría con mayor revenue generado por el cliente; si la quieres por cantidad de unidades, te dejo la nota abajo.

```sql
WITH completed_orders_last_6m AS (
    SELECT
        id AS order_id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
      -- En MySQL puedes usar:
      -- AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
),

customer_metrics AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders_last_6m
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_rank AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category
        ) AS rn
    FROM completed_orders_last_6m co
    JOIN customer_metrics cm
      ON cm.customer_id = co.customer_id
    JOIN order_items oi
      ON oi.order_id = co.order_id
    JOIN products p
      ON p.id = oi.product_id
    GROUP BY
        co.customer_id,
        p.category
)

SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cat.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c
  ON c.id = cm.customer_id
LEFT JOIN category_rank cat
  ON cat.customer_id = cm.customer_id
 AND cat.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

Si quieres que la “categoría más comprada” sea por unidades vendidas en vez de revenue, cambia esta parte:

```sql
SUM(oi.quantity * oi.unit_price) AS category_revenue,
ROW_NUMBER() OVER (
    PARTITION BY co.customer_id
    ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category
) AS rn
```

por esto:

```sql
SUM(oi.quantity) AS category_units,
ROW_NUMBER() OVER (
    PARTITION BY co.customer_id
    ORDER BY SUM(oi.quantity) DESC, p.category
) AS rn
```

Y si en tu caso el revenue real debe salir del detalle de ítems y no de `orders.total`, la lógica principal cambiaría a algo como:

```sql
SUM(oi.quantity * oi.unit_price) AS total_revenue
```

y:

```sql
SUM(oi.quantity * oi.unit_price) / NULLIF(COUNT(DISTINCT o.id), 0) AS avg_order_value
```