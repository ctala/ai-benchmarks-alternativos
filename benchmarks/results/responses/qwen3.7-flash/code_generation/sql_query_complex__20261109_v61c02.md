# Qwen 3.7 Flash — code_generation/sql_query_complex

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 44.858s | tokens_per_second: 101.0
- input_tokens: 161 | output_tokens: 4532
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

Aquí tienes la consulta optimizada usando CTEs (Common Table Expressions) y funciones de ventana para resolver el requerimiento de forma clara y eficiente:

```sql
WITH order_metrics AS (
  -- Métricas base por cliente en los últimos 6 meses
  SELECT 
    o.customer_id,
    COUNT(*) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 MONTH'
  GROUP BY o.customer_id
  HAVING COUNT(*) >= 3
),
customer_cat_qty AS (
  -- Cantidad de productos comprados por categoría y cliente
  SELECT 
    o.customer_id,
    p.category,
    SUM(oi.quantity) AS qty
  FROM orders o
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 MONTH'
  GROUP BY o.customer_id, p.category
),
ranked_cats AS (
  -- Ranking de categorías por cliente para obtener la más comprada
  SELECT 
    customer_id,
    category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY qty DESC) AS rn
  FROM customer_cat_qty
)
SELECT 
  c.name AS nombre,
  c.email,
  c.country AS pais,
  om.total_orders,
  om.total_revenue,
  ROUND(om.total_revenue / NULLIF(om.total_orders, 0), 2) AS avg_order_value,
  rc.categoria_mas_comprada
FROM order_metrics om
JOIN customers c ON om.customer_id = c.id
LEFT JOIN ranked_cats rc ON om.customer_id = rc.customer_id AND rc.rn = 1
ORDER BY om.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **Cálculo de Revenue**: Se usa `SUM(oi.quantity * oi.unit_price)` en lugar de `o.total` porque es más preciso en entornos reales (evita duplicaciones si `orders.total` incluye impuestos/envíos o está desactualizado). Si prefieres usar la columna `total` de `orders`, cámbialo a `SUM(o.total)`.
2. **Fecha dinámica**: 
   - 🟦 **PostgreSQL**: `CURRENT_DATE - INTERVAL '6 MONTH'`
   - 🟨 **MySQL**: `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   - 🟥 **SQL Server**: `DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))`
3. **Seguridad en división**: `NULLIF(om.total_orders, 0)` evita errores de división por cero si apareciera algún caso atípico.
4. **`categoria_mas_comprada`**: Se define por mayor cantidad de unidades vendidas. Si prefieres que sea por mayor facturación por categoría, cambia `ORDER BY qty DESC` por `ORDER BY SUM(oi.quantity * oi.unit_price) DESC` en el `OVER()`.
5. **Límite**: `LIMIT 10` es estándar en PostgreSQL/MySQL/SQLite. En SQL Server usa `TOP 10` al inicio del `SELECT`, y en Oracle `FETCH FIRST 10 ROWS ONLY`.

¿Necesitas que adapte la sintaxis a un motor específico o ajustar la lógica de "más comprada" (por unidad vs por monto)?