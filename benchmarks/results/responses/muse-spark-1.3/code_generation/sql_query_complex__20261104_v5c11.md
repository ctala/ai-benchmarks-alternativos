# Muse Spark 1.3 — code_generation/sql_query_complex

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 21.852s | tokens_per_second: 112.8
- input_tokens: 149 | output_tokens: 2464
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una solución estructurada y bien explicada que un emprendedor podría aplicar directamente.

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

Aquí tienes una solución limpia usando CTEs + `ROW_NUMBER()` para sacar la categoría favorita por cliente. Es para **MySQL 8 / PostgreSQL**:

```sql
WITH completed_orders AS (
    -- 1. Solo órdenes completadas de los últimos 6 meses
    SELECT 
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
      -- Para PostgreSQL usa: created_at >= NOW() - INTERVAL '6 months'
),
customer_stats AS (
    -- 2. Agregamos por cliente y filtramos >= 3 órdenes
    SELECT
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),
category_ranked AS (
    -- 3. Categoría más comprada por cliente (por cantidad total)
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY co.customer_id 
            ORDER BY SUM(oi.quantity) DESC, SUM(oi.quantity * oi.unit_price) DESC
        ) AS rn
    FROM completed_orders co
    JOIN order_items oi ON oi.order_id = co.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
)
-- 4. Top 10 por revenue
SELECT
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) AS total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN category_ranked cr 
    ON cr.customer_id = cs.customer_id 
    AND cr.rn = 1
ORDER BY total_revenue DESC
LIMIT 10;
```

### Cómo funciona:

1.  **`completed_orders`:** Filtra desde el inicio por `status = 'completed'` y `created_at` de los últimos 6 meses. Esto hace la query mucho más rápida.
2.  **`customer_stats`:** Calcula por `customer_id`: `total_orders = COUNT()`, `total_revenue = SUM(total)`, `avg_order_value = AVG(total)`. El `HAVING COUNT(id) >= 3` aplica tu regla de mínimo 3 órdenes completadas.
3.  **`category_ranked`:** Une esas órdenes con `order_items + products`, agrupa por cliente + categoría y usa `ROW_NUMBER() PARTITION BY customer_id ORDER BY SUM(quantity) DESC` para quedarse con el #1 de cada cliente.
4.  **SELECT final:** Une stats + datos del cliente + su categoría #1 (`rn = 1`), ordena por `total_revenue DESC` y limita a 10.

**Supuestos que tomé:**
* `total_revenue` viene de `orders.total`. Si quieres calcularlo desde el detalle, cambia `SUM(total)` por `SUM(oi.quantity * oi.unit_price)`.
* `categoria_mas_comprada` la definí como la de mayor **cantidad de unidades** `SUM(quantity)`. Si la quieres por revenue, cambia el `ORDER BY` a `SUM(oi.quantity * oi.unit_price) DESC`.