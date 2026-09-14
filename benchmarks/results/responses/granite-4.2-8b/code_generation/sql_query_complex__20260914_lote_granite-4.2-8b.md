# Granite 4.2 8B — code_generation/sql_query_complex

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.61 | quality: 9.56
- latency_total: 53.274s | tokens_per_second: 129.7
- input_tokens: 180 | output_tokens: 6907
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
    SELECT o.id, o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_orders AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT fo.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    JOIN order_items oi ON fo.id = oi.order_id
    GROUP BY c.id, c.name, c.email, c.country
),
customer_categories AS (
    SELECT 
        c.id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.id, p.category
),
customer_top_category AS (
    SELECT cc.id, cc.category
    FROM (
        SELECT 
            cc.*,
            ROW_NUMBER() OVER (PARTITION BY cc.id ORDER BY cc.total_qty DESC) AS rn
        FROM customer_categories cc
    ) cc
    WHERE cc.rn = 1
)
SELECT 
    co.name AS nombre,
    co.email,
    co.country AS pais,
    co.total_orders,
    co.total_revenue,
    (co.total_revenue / co.total_orders) AS avg_order_value,
    ct.category AS categoria_mas_comprada
FROM customer_orders co
JOIN customer_top_category ct ON co.id = ct.id
WHERE co.total_orders >= 3
ORDER BY co.total_revenue DESC
LIMIT 10;
```

**Explicación breve (para cumplir con el requisito de claridad):**

1. **`filtered_orders`**: Filtra solo órdenes con `status = 'completed'` dentro de los últimos 6 meses (usando `CURRENT_DATE - INTERVAL '6 months'`; en PostgreSQL/MySQL 8+; si usas otra base, adapta el cálculo de fecha, ej. `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` en MySQL).

2. **`customer_orders`**: Agrupa por cliente para calcular:
   - `total_orders`: conteo de órdenes completadas (usando `COUNT(DISTINCT fo.id)` para evitar contar órdenes múltiples).
   - `total_revenue`: suma de `quantity * unit_price` de los ítems de las órdenes (el campo correcto para ingresos por ítem, ya que `products.price` podría no coincidir con el precio en la línea de pedido).

3. **`customer_categories`**: Agrupa por cliente y categoría para calcular `total_qty` (suma de cantidades compradas por categoría), lo que permite determinar la categoría más frecuentemente comprada en términos de volumen (no solo número de órdenes).

4. **`customer_top_category`**: Usa `ROW_NUMBER()` para seleccionar la categoría con mayor `total_qty` por cliente (el empate se resuelve tomando la primera en caso de empate, lo cual es aceptable para "categoria_mas_comprada").

5. **Consulta final**:
   - Une `customer_orders` con `customer_top_category` para obtener la categoría principal de cada cliente.
   - Aplica el filtro `WHERE co.total_orders >= 3` (solo clientes con ≥3 órdenes completadas).
   - Calcula `avg_order_value` como `total_revenue / total_orders` (valor promedio por orden, no por ítem).
   - Ordena por `total_revenue DESC` y limita a los **top 10** clientes.
   - Usa nombres de columna según el requisito (`nombre`, `email`, `pais`, `total_orders`, `total_revenue`, `avg_order_value`, `categoria_mas_comprada`).

> **Nota sobre fechas**: La expresión `CURRENT_DATE - INTERVAL '6 months'` funciona en PostgreSQL. En MySQL 8+, reemplazaría por `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`. Si tu base de datos usa otro sintaxis (ej. SQL Server), ajusta la parte de la fecha (ej. `DATEADD(month, -6, GETDATE())`). La lógica de agregación y filtros permanece idéntica.