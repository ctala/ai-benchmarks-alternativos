# Kimi K2.5 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 127.502s | tokens_per_second: 29.9
- input_tokens: 159 | output_tokens: 3812
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

Aquí tienes la query usando **CTEs** y **window functions** (SQL estándar moderno, compatible con PostgreSQL, MySQL 8.0+, SQL Server, etc.):

```sql
WITH recent_orders AS (
  /* 1. Órdenes completadas de los últimos 6 meses */
  SELECT 
    o.id,
    o.customer_id,
    o.total
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    -- MySQL: DATE_SUB(NOW(), INTERVAL 6 MONTH)
    -- SQL Server: DATEADD(month, -6, GETDATE())
),
customer_stats AS (
  /* 2. Métricas principales por cliente */
  SELECT 
    c.id AS customer_id,
    c.name,
    c.email,
    c.country,
    COUNT(ro.id) AS total_orders,
    SUM(ro.total) AS total_revenue,
    AVG(ro.total) AS avg_order_value
  FROM customers c
  INNER JOIN recent_orders ro ON c.id = ro.customer_id
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(ro.id) >= 3
),
category_stats AS (
  /* 3. Categorías rankeadas por cantidad comprada por cliente */
  SELECT 
    ro.customer_id,
    p.category,
    SUM(oi.quantity) AS total_quantity,
    ROW_NUMBER() OVER (
      PARTITION BY ro.customer_id 
      ORDER BY SUM(oi.quantity) DESC, p.category ASC
    ) AS rn
  FROM recent_orders ro
  INNER JOIN order_items oi ON ro.id = oi.order_id
  INNER JOIN products p ON oi.product_id = p.id
  GROUP BY ro.customer_id, p.category
)
/* 4. Resultado final */
SELECT 
  cs.name,
  cs.email,
  cs.country,
  cs.total_orders,
  cs.total_revenue,
  ROUND(cs.avg_order_value, 2) AS avg_order_value,
  cat.category AS categoria_mas_comprada
FROM customer_stats cs
INNER JOIN category_stats cat ON cs.customer_id = cat.customer_id
WHERE cat.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes:

1. **Fecha**: La sintaxis `CURRENT_DATE - INTERVAL '6 months'` es estándar SQL. Si usas:
   - **MySQL**: cambia a `o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`
   - **SQL Server**: cambia a `o.created_at >= DATEADD(month, -6, GETDATE())`

2. **Revenue**: Usé `orders.total` para calcular `total_revenue` y `avg_order_value`. Si prefieres calcularlo desde `order_items` (más preciso si no confías en el total guardado), reemplaza en `customer_stats`:
   ```sql
   SUM(oi.quantity * oi.unit_price) AS total_revenue,
   SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT ro.id) AS avg_order_value
   ```
   (y ajusta los JOINs correspondientes).

3. **Categoría más comprada**: Se define por **mayor cantidad de unidades** (`SUM(oi.quantity)`). Si prefieres definirla por **mayor revenue**, cambia el `ORDER BY` dentro de `ROW_NUMBER` a:
   ```sql
   ORDER BY SUM(oi.quantity * oi.unit_price) DESC
   ```

4. **Empates**: Si un cliente tiene dos categorías empatadas en primer lugar, `ROW_NUMBER` + orden alfabético (`p.category ASC`) elige una de forma determinista. Si prefieres mostrar ambas en caso de empate, cambia a `RANK()`.