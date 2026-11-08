# GLM 5 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 23.349s | tokens_per_second: 66.8
- input_tokens: 156 | output_tokens: 1560
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
WITH customer_orders AS (
    -- Base: órdenes completadas en los últimos 6 meses con detalle de items
    SELECT 
        c.id            AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id            AS order_id,
        o.total,
        oi.quantity,
        oi.unit_price,
        oi.quantity * oi.unit_price AS item_revenue,
        p.category
    FROM customers c
    JOIN orders o       ON o.customer_id = c.id
    JOIN order_items oi ON oi.order_id   = o.id
    JOIN products p     ON p.id          = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)  -- PostgreSQL: CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    -- Métricas agregadas por cliente (filtrando >= 3 órdenes)
    SELECT 
        customer_id,
        name,
        email,
        country,
        COUNT(DISTINCT order_id)                         AS total_orders,
        SUM(item_revenue)                                AS total_revenue,
        SUM(item_revenue) / COUNT(DISTINCT order_id)     AS avg_order_value
    FROM customer_orders
    GROUP BY customer_id, name, email, country
    HAVING COUNT(DISTINCT order_id) >= 3
),
category_rank AS (
    -- Ranking de categorías por cliente según cantidad comprada
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY SUM(quantity) DESC, SUM(item_revenue) DESC
        ) AS rn
    FROM customer_orders
    GROUP BY customer_id, category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN category_rank cr 
       ON cr.customer_id = cs.customer_id 
      AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas clave del enfoque

1. **`customer_orders` (CTE base)**: hace el join completo y filtra `status = 'completed'` + últimos 6 meses. Calculo `item_revenue = quantity * unit_price` porque es más confiable que `orders.total` (que podría incluir impuestos/envío y no coincide con el detalle).

2. **`customer_stats`**: agrega por cliente y aplica el filtro `HAVING COUNT(DISTINCT order_id) >= 3` **sobre órdenes completadas** (no sobre cualquier orden). Uso `COUNT(DISTINCT order_id)` porque el join con `order_items` multiplica filas.

3. **`category_rank`**: usa `ROW_NUMBER()` con `PARTITION BY customer_id` para identificar la categoría con mayor cantidad comprada por cliente. El desempate (`SUM(item_revenue) DESC`) evita ambigüedades. Alternativamente podrías rankear por revenue en lugar de cantidad cambiando el `ORDER BY`.

4. **`LEFT JOIN`** al final: por seguridad, aunque todo cliente con órdenes tiene items y por ende categorías.

### Variantes según el motor

- **PostgreSQL**: cambia `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)` por `CURRENT_DATE - INTERVAL '6 months'`.
- **SQL Server**: usa `DATEADD(month, -6, GETDATE())` y `TOP 10` en lugar de `LIMIT 10`.
- **Oracle**: usa `ADD_MONTHS(SYSDATE, -6)` y `FETCH FIRST 10 ROWS ONLY`.

### Consideraciones de performance

Si las tablas son grandes, asegúrate de tener índices en:
- `orders(customer_id, status, created_at)`
- `order_items(order_id)`
- `products(id)` (PK, ya existe)
- `customers(id)` (PK, ya existe)