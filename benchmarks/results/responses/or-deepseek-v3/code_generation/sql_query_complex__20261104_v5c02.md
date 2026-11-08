# DeepSeek V3 — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.8 | quality: 9.8
- latency_total: 19.423s | tokens_per_second: 37.1
- input_tokens: 152 | output_tokens: 721
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

Aquí tienes la consulta SQL solicitada:

```sql
WITH 
-- Filtramos órdenes de los últimos 6 meses completadas
recent_orders AS (
    SELECT 
        id,
        customer_id,
        total,
        created_at
    FROM orders
    WHERE status = 'completed'
      AND created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),

-- Calculamos estadísticas por cliente
customer_stats AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT ro.id) AS total_orders,
        SUM(ro.total) AS total_revenue,
        AVG(ro.total) AS avg_order_value
    FROM customers c
    LEFT JOIN recent_orders ro ON c.id = ro.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT ro.id) >= 3
),

-- Encontramos la categoría más comprada por cliente
customer_top_category AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rank
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    JOIN orders o ON oi.order_id = o.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)

-- Resultado final
SELECT 
    cs.name AS nombre,
    cs.email AS email,
    cs.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    COALESCE(ctc.category, 'Sin compras') AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_top_category ctc ON cs.id = ctc.customer_id AND ctc.rank = 1
WHERE cs.total_revenue IS NOT NULL
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Explicación de la consulta:**

1. **CTE `recent_orders`**: Filtra las órdenes completadas en los últimos 6 meses.
2. **CTE `customer_stats`**: Calcula las estadísticas principales por cliente y filtra aquellos con al menos 3 órdenes completadas.
3. **CTE `customer_top_category`**: Determina la categoría más comprada por cada cliente basándose en la cantidad total de productos.
4. **Consulta final**: Combina todas las estadísticas y muestra el top 10 clientes ordenados por revenue total.

**Notas importantes:**
- Asume que la columna `created_at` es de tipo fecha/hora
- Considera que `total` en la tabla `orders` ya representa el revenue total de la orden
- La categoría más comprada se basa en la cantidad total de productos comprados en esa categoría
- Si hay empate en cantidad entre categorías, se toma la primera por orden alfabético
- Solo incluye clientes con revenue total (excluye clientes sin compras en el período)