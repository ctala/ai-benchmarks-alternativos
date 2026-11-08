# Solar Pro 4 — code_generation/sql_query_complex

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 24.451s | tokens_per_second: 34.0
- input_tokens: 196 | output_tokens: 831
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



Aquí tienes la consulta SQL optimizada para PostgreSQL (teniendo en cuenta la función `DATE_TRUNC` y sintaxis de ventanas), que cumple con todos los requisitos:

```sql
WITH completed_orders AS (
    -- 1. Filtrar solo órdenes completadas en los últimos 6 meses
    SELECT 
        o.customer_id,
        o.id AS order_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '6 months')
),
customer_metrics AS (
    -- 2. Calcular métricas por cliente (orders, revenue, avg)
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(co.order_id) AS total_orders,
        SUM(co.total) AS total_revenue,
        AVG(co.total) AS avg_order_value
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.order_id) >= 3
),
category_metrics AS (
    -- 3. Contar unidades por categoría por cliente (basado en items)
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders co
    JOIN order_items oi ON co.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY co.customer_id, p.category
),
ranked_categories AS (
    -- 4. Asignar rango a las categorías por cliente para obtener la top 1
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) as rn
    FROM category_metrics
)
-- 5. Unir todo y filtrar el Top 10
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN ranked_categories rc ON cm.customer_id = rc.customer_id AND rc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`completed_orders` (CTE)**: Filtra las órdenes base. Es crucial hacer esto primero para asegurar que el conteo de órdenes, el revenue y las categorías provengan exclusivamente de órdenes `completed` y dentro del rango de tiempo de 6 meses.
2.  **`customer_metrics` (CTE)**: Agrupa por cliente para obtener las métricas financieras. El `HAVING COUNT(...) >= 3` asegura el requisito de mínimo 3 órdenes.
3.  **`category_metrics` (CTE)**: Unión con `order_items` y `products`. Se suma la `quantity` en lugar del precio para determinar qué categoría compró "más" (volumen), lo cual es el estándar para "más comprada".
4.  **`ranked_categories` (CTE)**: Usa `ROW_NUMBER()` para ordenar las categorías por volumen por cliente y seleccionar solo la primera (`rn = 1`).
5.  **Consulta Final**: Une las métricas del cliente con su categoría más comprada (usando `LEFT JOIN` por si acaso un cliente no tiene items, aunque es raro si tiene órdenes), ordena por revenue y limita a 10.

*Nota: La función `DATE_TRUNC` y `INTERVAL` es específica de PostgreSQL. Si usas MySQL, deberías ajustar la fecha a `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.*