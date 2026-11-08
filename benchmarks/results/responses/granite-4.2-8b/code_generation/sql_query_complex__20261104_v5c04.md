# Granite 4.2 8B — code_generation/sql_query_complex

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.52 | quality: 9.56
- latency_total: 57.385s | tokens_per_second: 89.0
- input_tokens: 180 | output_tokens: 5105
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
WITH filtered_orders AS (
  SELECT o.id AS order_id, o.customer_id
  FROM orders o
  WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),

order_items_with_cat AS (
  SELECT 
    fo.order_id, 
    fo.customer_id, 
    oi.quantity, 
    oi.unit_price, 
    p.category
  FROM filtered_orders fo
  JOIN order_items oi ON fo.order_id = oi.order_id
  JOIN products p ON oi.product_id = p.id
),

customer_stats AS (
  SELECT 
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity * unit_price) AS total_revenue
  FROM order_items_with_cat
  GROUP BY customer_id
),

per_category AS (
  SELECT 
    customer_id,
    category,
    SUM(quantity) AS total_quantity
  FROM order_items_with_cat
  GROUP BY customer_id, category
),

top_category AS (
  SELECT 
    customer_id,
    category,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
  FROM per_category
)

SELECT 
  c.name AS nombre,
  c.email,
  c.country AS pais,
  cs.total_orders,
  cs.total_revenue,
  ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
  tc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN customers c ON cs.customer_id = c.id
JOIN top_category tc ON cs.customer_id = tc.customer_id AND tc.rn = 1
WHERE cs.total_orders >= 3
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Explicación breve (para claridad):**

1. **`filtered_orders`**: Filtra órdenes completadas (`status = 'completed'`) dentro de los últimos 6 meses usando `DATE_SUB(NOW(), INTERVAL 6 MONTH)` (ajustable según el motor; en PostgreSQL usaría `NOW() - INTERVAL '6 months'`, en SQL Server `DATEADD(month, -6, GETDATE())`).
2. **`order_items_with_cat`**: Une órdenes → ítems → productos para obtener `quantity`, `unit_price` y `category` de cada ítem.
3. **`customer_stats`**: Calcula por cliente:
   - `total_orders` = conteo de órdenes distintas (usando `COUNT(DISTINCT order_id)`).
   - `total_revenue` = suma de `quantity * unit_price` (revenue real de la orden, no el campo `total` de `orders`, que podría incluir impuestos o variar).
4. **`per_category`**: Calcula la cantidad total comprada (`SUM(quantity)`) por categoría por cliente.
5. **`top_category`**: Usa `ROW_NUMBER()` para seleccionar la categoría con mayor cantidad comprada por cliente (en caso de empate, se elige la primera encontrada; si se necesita un criterio adicional para empates, se podría añadir `ORDER BY total_quantity DESC, category ASC`).
6. **Consulta final**:
   - Une `customer_stats` con `customers` para obtener nombre, email y país.
   - Une con `top_category` (solo `rn = 1` para la categoría más comprada del cliente).
   - Filtra clientes con `total_orders >= 3`.
   - Ordena por `total_revenue DESC` y limita a los 10 mejores.
   - Usa `ROUND(..., 2)` para `avg_order_value` para evitar decimales excesivos (opcional pero recomendado; si se prefiere exacto, eliminar `ROUND`).

> **Nota sobre el filtro de fechas**:  
> - En MySQL/MariaDB: `DATE_SUB(NOW(), INTERVAL 6 MONTH)` es correcto.  
> - En PostgreSQL: `NOW() - INTERVAL '6 months'`.  
> - En SQL Server: `DATEADD(month, -6, GETDATE())`.  
> (El query usa `NOW()` para MySQL; si el motor es diferente, ajusta el cálculo de la fecha en `filtered_orders` según corresponda. El lógico del query permanece igual.)

Este query cumple todos los requisitos: top 10 clientes por revenue total en los últimos 6 meses, solo clientes con ≥3 órdenes completadas, columnas exactas solicitadas, orden correcto y cálculo preciso de la categoría más comprada por cliente.