# Muse Glimmer 30B — code_generation/sql_query_complex

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.47 | quality: 9.52
- latency_total: 14.905s | tokens_per_second: 134.8
- input_tokens: 197 | output_tokens: 2009
- judge_score: 4.8 | justificación: 

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

Aquí tienes una versión en PostgreSQL. La lógica es:

1. Filtrar órdenes `completed` de los últimos 6 meses
2. Agrupar por cliente y quedarte con los que tienen >=3 órdenes
3. Calcular la categoría más comprada por cliente con `ROW_NUMBER`

```sql
WITH recent_orders AS (
  SELECT o.id, o.customer_id, o.total
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= NOW() - INTERVAL '6 months'
),
customer_stats AS (
  SELECT 
    c.id,
    c.name  AS nombre,
    c.email,
    c.country AS pais,
    COUNT(ro.id) AS total_orders,
    SUM(ro.total) AS total_revenue,
    AVG(ro.total) AS avg_order_value
  FROM customers c
  JOIN recent_orders ro ON ro.customer_id = c.id
  GROUP BY c.id
  HAVING COUNT(ro.id) >= 3
),
customer_category AS (
  SELECT 
    o.customer_id,
    p.category,
    SUM(oi.quantity * oi.unit_price) AS revenue_cat
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.id
  JOIN products p ON p.id = oi.product_id
  WHERE o.status = 'completed'
    AND o.created_at >= NOW() - INTERVAL '6 months'
  GROUP BY o.customer_id, p.category
),
ranked_category AS (
  SELECT 
    customer_id,
    category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id 
      ORDER BY revenue_cat DESC
    ) AS rn
  FROM customer_category
)
SELECT 
  cs.nombre,
  cs.email,
  cs.pais,
  cs.total_orders,
  cs.total_revenue,
  ROUND(cs.avg_order_value,2) AS avg_order_value,
  rc.categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN ranked_category rc 
  ON rc.customer_id = cs.id AND rc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Notas**

* `categoria_mas_comprada` se calcula por revenue de categoría `SUM(quantity * unit_price)`. Si prefieres por unidades, cambia `SUM(oi.quantity * oi.unit_price)` por `SUM(oi.quantity)`.
* Para MySQL cambia `NOW() - INTERVAL '6 months'` por `NOW() - INTERVAL 6 MONTH`.

El resultado cumple: últimos 6 meses, solo `status = 'completed'`, mínimo 3 órdenes por cliente, top 10 por `total_revenue DESC` con las columnas solicitadas.