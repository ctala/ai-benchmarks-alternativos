# DeepSeek V4 Pro — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.19 | quality: 9.6
- latency_total: 32.971s | tokens_per_second: 72.9
- input_tokens: 152 | output_tokens: 2402
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
WITH 
-- 1. Completed orders in the last 6 months
completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'   -- Ajustar según tu SGBD
),

-- 2. Revenue and order count per customer
customer_metrics AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country AS pais,
        COUNT(DISTINCT co.order_id) AS total_orders,
        SUM(co.total) AS total_revenue
    FROM customers c
    INNER JOIN completed_orders co ON co.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT co.order_id) >= 3            -- al menos 3 órdenes completadas
),

-- 3. Category quantity per customer (only from completed orders in the period)
customer_category_quantities AS (
    SELECT 
        co.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM completed_orders co
    INNER JOIN order_items oi ON oi.order_id = co.order_id
    INNER JOIN products p ON p.id = oi.product_id
    GROUP BY co.customer_id, p.category
),

-- 4. Most purchased category per customer (by total quantity; breaks ties alphabetically)
customer_top_category AS (
    SELECT 
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id 
                ORDER BY total_quantity DESC, category ASC
            ) AS rn
        FROM customer_category_quantities
    ) ranked
    WHERE rn = 1
)

-- 5. Final result: top 10 customers
SELECT 
    cm.name,
    cm.email,
    cm.pais,
    cm.total_orders,
    cm.total_revenue,
    ROUND(cm.total_revenue / cm.total_orders, 2) AS avg_order_value,
    ctc.categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN customer_top_category ctc ON ctc.customer_id = cm.customer_id
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

**Explicación breve**  
- Se filtran solo las órdenes con `status = 'completed'` de los últimos 6 meses.  
- Se calcula para cada cliente: número de órdenes, ingresos totales y ticket promedio (solo órdenes completas).  
- Se obtiene la categoría más comprada por el cliente (suma de cantidades, sin contar productos de órdenes no completadas).  
- Solo se muestran clientes con al menos 3 órdenes completadas en el período.  
- Los resultados se ordenan por `total_revenue` descendente y se limitan a los 10 primeros.

**Nota sobre la fecha**  
La expresión `CURRENT_DATE - INTERVAL '6 months'` funciona en PostgreSQL. Para otros motores, adáptala:  
- MySQL: `CURDATE() - INTERVAL 6 MONTH` o `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`  
- SQL Server: `DATEADD(MONTH, -6, GETDATE())`  
- Oracle: `ADD_MONTHS(SYSDATE, -6)`