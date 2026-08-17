# DeepSeek R1 (reasoning) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.96 | quality: 9.8
- latency_total: 233.858s | tokens_per_second: 19.9
- input_tokens: 151 | output_tokens: 4652
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH recent_orders AS (
    SELECT 
        o.id, 
        o.customer_id, 
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(ro.id) AS total_orders,
        SUM(ro.total) AS total_revenue,
        AVG(ro.total) AS avg_order_value
    FROM customers c
    JOIN recent_orders ro ON c.id = ro.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(ro.id) >= 3
),
top_customers AS (
    SELECT
        customer_id,
        total_orders,
        total_revenue,
        avg_order_value,
        ROW_NUMBER() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM customer_metrics
),
customer_categories AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC, p.category) AS category_rank
    FROM recent_orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
),
top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM customer_categories
    WHERE category_rank = 1
)
SELECT
    cm.name AS nombre,
    cm.email,
    cm.country AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    tc.categoria_mas_comprada
FROM customer_metrics cm
JOIN top_customers tc ON cm.customer_id = tc.customer_id
JOIN top_category tcat ON cm.customer_id = tcat.customer_id
WHERE tc.revenue_rank <= 10
ORDER BY cm.total_revenue DESC;
```

**Explicación:**

1. **CTE `recent_orders`**:
   - Filtra órdenes completadas en los últimos 6 meses.

2. **CTE `customer_metrics`**:
   - Calcula métricas clave por cliente (total de órdenes, revenue total y valor promedio por orden).
   - Filtra clientes con al menos 3 órdenes completadas (`HAVING COUNT(ro.id) >= 3`).

3. **CTE `top_customers`**:
   - Clasifica clientes por revenue total usando `ROW_NUMBER()`.
   - Mantiene solo el top 10 mediante `revenue_rank <= 10`.

4. **CTE `customer_categories`**:
   - Calcula la cantidad total comprada por cada categoría por cliente.
   - Clasifica categorías usando `ROW_NUMBER()` (prioriza mayor cantidad y en empates usa orden alfabético).

5. **CTE `top_category`**:
   - Selecciona la categoría más comprada para cada cliente (`category_rank = 1`).

6. **Consulta final**:
   - Combina todas las métricas y la categoría más comprada.
   - Ordena por revenue total descendente.

**Notas importantes:**
- La función `CURRENT_DATE - INTERVAL '6 months'` puede variar según el RDBMS (en PostgreSQL funciona así, en MySQL sería similar).
- Si hay empates en la categoría más comprada, se selecciona la primera alfabéticamente.
- El cálculo de `avg_order_value` es el promedio del valor total de las órdenes.
- Se asume que el campo `total` en `orders` representa el revenue total de la orden.