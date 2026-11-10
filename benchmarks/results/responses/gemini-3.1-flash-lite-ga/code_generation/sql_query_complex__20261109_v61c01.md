# Gemini 3.1 Flash Lite (GA) — code_generation/sql_query_complex

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.22 | quality: 10.0
- latency_total: 2.733s | tokens_per_second: 271.5
- input_tokens: 160 | output_tokens: 742
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

Para resolver esta consulta, utilizaremos **CTEs (Common Table Expressions)** o subconsultas para calcular primero las métricas de los clientes y luego determinar la categoría más comprada.

Aquí tienes la query optimizada:

```sql
WITH CustomerMetrics AS (
    -- Calculamos métricas básicas de clientes y filtramos por fecha y estatus
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryRanking AS (
    -- Identificamos qué categoría compró más cada cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as purchase_count,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id, p.category
)
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM CustomerMetrics cm
JOIN CategoryRanking cr ON cm.id = cr.customer_id
WHERE cr.rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`CustomerMetrics` (CTE):**
    *   Filtra las órdenes con `status = 'completed'` y los últimos 6 meses.
    *   Realiza las agregaciones (`SUM`, `AVG`, `COUNT`).
    *   Aplica el filtro `HAVING COUNT(o.id) >= 3` para cumplir con el requerimiento de mínimo 3 órdenes.
2.  **`CategoryRanking` (CTE):**
    *   Une `orders`, `order_items` y `products` para contar cuántas veces aparece cada categoría por cliente.
    *   Usa `ROW_NUMBER()` con `PARTITION BY customer_id` para asignar el número 1 a la categoría más frecuente de cada cliente.
3.  **Consulta Final:**
    *   Une ambos resultados mediante el `customer_id`.
    *   Filtra `cr.rank = 1` para obtener solo la categoría principal.
    *   Ordena por `total_revenue DESC` y limita a los 10 mejores.

**Nota:** Esta consulta utiliza sintaxis estándar compatible con **PostgreSQL**. Si usas MySQL, el manejo de fechas puede variar ligeramente (por ejemplo, usando `DATE_SUB(NOW(), INTERVAL 6 MONTH)`).