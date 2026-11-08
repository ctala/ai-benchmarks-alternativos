# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 7.352s | tokens_per_second: 94.9
- input_tokens: 153 | output_tokens: 698
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

Aquí tienes una consulta SQL que cumple con todos los requisitos. Utiliza CTEs para mayor claridad y eficiencia, y maneja correctamente la lógica de `categoria_mas_comprada` (con empate se elige una al azar o la primera según el `ORDER BY` interno):

```sql
WITH completed_orders_last_6_months AS (
  SELECT 
    o.id AS order_id,
    o.customer_id,
    o.total,
    oi.product_id,
    p.category
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE 
    o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_summary AS (
  SELECT 
    co.customer_id,
    COUNT(DISTINCT co.order_id) AS total_orders,
    SUM(co.total) AS total_revenue,
    AVG(co.total) AS avg_order_value
  FROM completed_orders_last_6_months co
  GROUP BY co.customer_id
  HAVING COUNT(DISTINCT co.order_id) >= 3
),
top_category_per_customer AS (
  SELECT 
    co.customer_id,
    co.category,
    COUNT(*) AS category_count,
    ROW_NUMBER() OVER (
      PARTITION BY co.customer_id 
      ORDER BY COUNT(*) DESC, co.category ASC  -- para desempate determinista
    ) AS rn
  FROM completed_orders_last_6_months co
  GROUP BY co.customer_id, co.category
),
customer_top_category AS (
  SELECT customer_id, category AS categoria_mas_comprada
  FROM top_category_per_customer
  WHERE rn = 1
)
SELECT 
  c.name,
  c.email,
  c.country,
  cs.total_orders,
  ROUND(cs.total_revenue, 2) AS total_revenue,
  ROUND(cs.avg_order_value, 2) AS avg_order_value,
  ctc.categoria_mas_comprada
FROM customer_summary cs
JOIN customers c ON cs.customer_id = c.id
JOIN customer_top_category ctc ON cs.customer_id = ctc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Notas importantes:
1. **Filtro de tiempo**: `o.created_at >= CURRENT_DATE - INTERVAL '6 months'` — asume base de datos PostgreSQL. En MySQL usarías `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` y en SQL Server `DATEADD(MONTH, -6, GETDATE())`.
2. **Filtro de estado**: Solo se consideran órdenes con `status = 'completed'`.
3. **Requisito de ≥3 órdenes completadas**: Se aplica en el CTE `customer_summary`.
4. **`categoria_mas_comprada`**: Se calcula contando la cantidad de *items* por categoría (no por orden), ya que una orden puede tener múltiples productos de distintas categorías. Si hay empate, se elige alfabéticamente (para determinismo).
5. **Redondeo**: Se redondea `total_revenue` y `avg_order_value` a 2 decimales para legibilidad.

¿Quieres adaptarla a un sistema específico (MySQL, SQL Server, BigQuery)?