# Inkling Small — code_generation/sql_query_complex

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.56 | quality: 9.8
- latency_total: 14.885s | tokens_per_second: 299.3
- input_tokens: 155 | output_tokens: 4455
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

Aquí tienes la query (en sintaxis **PostgreSQL**, fácil de adaptar a MySQL/SQL Server):

```sql
WITH completed_6m AS (
  /* 1. Órdenes completadas en los últimos 6 meses */
  SELECT *
  FROM orders
  WHERE status = 'completed'
    AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

/* 2. Métricas por cliente (solo los que tengan >= 3 órdenes) */
customer_stats AS (
  SELECT 
    customer_id,
    COUNT(*) AS total_orders,
    SUM(total) AS total_revenue,
    AVG(total)::numeric(12,2) AS avg_order_value
  FROM completed_6m
  GROUP BY customer_id
  HAVING COUNT(*) >= 3
),

/* 3. Ventas por cliente y categoría (basado en items) */
category_sales AS (
  SELECT 
    o.customer_id,
    p.category,
    SUM(oi.quantity) AS total_qty   -- "más comprada" = mayor cantidad comprada
  FROM completed_6m o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p     ON oi.product_id = p.id
  GROUP BY o.customer_id, p.category
),

/* 4. Ranking de categorías por cliente */
ranked_categories AS (
  SELECT 
    customer_id,
    category,
    ROW_NUMBER() OVER (
      PARTITION BY customer_id 
      ORDER BY total_qty DESC, category ASC
    ) AS rn
  FROM category_sales
),

/* 5. Solo la categoría #1 por cliente */
best_category AS (
  SELECT customer_id, category AS categoria_mas_comprada
  FROM ranked_categories
  WHERE rn = 1
)

/* 6. Resultado final: Top 10 */
SELECT 
  c.name,
  c.email,
  c.country AS pais,
  cs.total_orders,
  cs.total_revenue,
  cs.avg_order_value,
  bc.categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON cs.customer_id = c.id
LEFT JOIN best_category bc ON cs.customer_id = bc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes:

| Parte | Explicación |
|-------|-------------|
| **`completed_6m`** | Filtra `status = 'completed'` y `created_at` de los últimos 6 meses. |
| **`HAVING COUNT(*) >= 3`** | Aplica el filtro de "al menos 3 órdenes completadas". |
| **`SUM(total)`** | Usa la columna `orders.total` como revenue. Si prefieres calcularlo desde `order_items` (`quantity * unit_price`), cambia esta parte por un `SUM(oi.quantity * oi.unit_price)` y une `order_items` también ahí. |
| **`categoria_mas_comprada`** | Se determina por la **cantidad total comprada** (`SUM(quantity)`) en ese período. Si prefieres por **ingreso de categoría**, reemplaza `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en `category_sales`. |
| **Fecha** | Si usas **MySQL**: cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`. Si usas **SQL Server**: usa `DATEADD(month, -6, GETDATE())`. |
| **`LIMIT 10`** | Es para PostgreSQL/MySQL. En SQL Server usa `TOP 10` después del `SELECT`. |

¿Necesitas que calcule `total_revenue` desde `order_items` en vez de `orders.total`, o que la categoría ganadora sea por ingresos en vez de cantidad? Avísame y ajusto la query.