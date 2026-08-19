# Gemini 3.7 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.63 | quality: 9.8
- latency_total: 12.679s | tokens_per_second: 153.2
- input_tokens: 160 | output_tokens: 1942
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, cumpliendo con todos los requisitos de la consulta SQL compleja solicitada.

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

Aquí tienes la consulta en **SQL estándar / PostgreSQL** (utilizando Common Table Expressions y funciones de ventana para evitar duplicaciones al cruzar con los ítems):

```sql
WITH customer_orders AS (
    -- 1. Métricas de órdenes a nivel de cliente en los últimos 6 meses
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 month'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
customer_top_category AS (
    -- 2. Ranking de la categoría más comprada (por cantidad de unidades)
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 month'
    GROUP BY o.customer_id, p.category
)
-- 3. Consulta final combinando métricas y la categoría top
SELECT 
    co.nombre,
    co.email,
    co.pais,
    co.total_orders,
    co.total_revenue,
    co.avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_orders co
LEFT JOIN customer_top_category ctc 
    ON co.customer_id = ctc.customer_id 
   AND ctc.rn = 1
ORDER BY co.total_revenue DESC
LIMIT 10;
```

---

### Notas de adaptación por motor (si aplica):
* **MySQL:** Cambia `INTERVAL '6 month'` por `INTERVAL 6 MONTH`.
* **SQL Server:** 
  * Reemplaza el filtro de fecha por `o.created_at >= DATEADD(month, -6, GETDATE())`.
  * Reemplaza `LIMIT 10` al final por `SELECT TOP 10` al inicio de la query principal.