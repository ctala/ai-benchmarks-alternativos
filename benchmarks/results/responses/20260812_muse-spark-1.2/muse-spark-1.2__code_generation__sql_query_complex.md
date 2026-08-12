# Muse Spark 1.2 — code_generation/sql_query_complex

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 9.335s | tokens_per_second: 186.6
- input_tokens: 148 | output_tokens: 1742
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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

Esta es la query optimizada para `PostgreSQL` y `MySQL 8.0+`:

```sql
WITH completed_orders AS (
    -- 1. Filtramos solo órdenes completadas de los últimos 6 meses
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),
customer_stats AS (
    -- 2. Agregamos métricas por cliente
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
ranked_categories AS (
    -- 3. Calculamos la categoría más comprada por cliente [por cantidad]
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM completed_orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
)
-- 4. Resultado final
SELECT
    c.name,
    c.email,
    c.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN ranked_categories rc ON rc.customer_id = cs.customer_id AND rc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes:

**1. Sobre `total_revenue`:**
Usé `SUM(orders.total)` porque ya tienes el total en la orden. Si quieres calcularlo de forma más precisa desde los items usa esto en `customer_stats`:
```sql
SUM(oi.quantity * oi.unit_price) AS total_revenue
```

**2. Sobre `categoria_mas_comprada`:**
En esta query se define como la categoría con mayor `SUM(quantity)`. Si la quieres definir por mayor gasto, cambia en `ranked_categories`:
```sql
SUM(oi.quantity * oi.unit_price) AS total_spent
-- y en el ORDER BY:
ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC)
```

**3. Compatibilidad:**
* `PostgreSQL`: `NOW() - INTERVAL '6 months'`
* `MySQL`: `NOW() - INTERVAL 6 MONTH`
* `SQL Server`: `DATEADD(MONTH, -6, GETDATE())`

> Si hay empates en categorías y quieres traer todas, cambia `ROW_NUMBER()` por `RANK()` o `DENSE_RANK()`.