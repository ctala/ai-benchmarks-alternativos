# MiMo V2-Pro (Xiaomi direct) — code_generation/sql_query_complex

- model_id: `mimo-v2-pro`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 36.495s | tokens_per_second: 56.1
- input_tokens: 394 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH customer_metrics AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
top_categories AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS category_rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    ROUND(cm.avg_order_value, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN top_categories tc ON cm.customer_id = tc.customer_id 
    AND tc.category_rank = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

**Explicación de la solución:**

1. **CTE `customer_metrics`**: Calcula las métricas principales por cliente
   - Filtra solo órdenes completadas en los últimos 6 meses
   - Agrupa por cliente calculando total_orders, total_revenue y avg_order_value
   - Aplica el filtro HAVING para clientes con al menos 3 órdenes

2. **CTE `top_categories`**: Encuentra la categoría más comprada por cada cliente
   - Usa `ROW_NUMBER()` para rankear categorías por cantidad total de productos comprados
   - Considera solo órdenes completadas en los últimos 6 meses

3. **Consulta principal**: Combina ambas CTEs
   - Usa `LEFT JOIN` para incluir clientes que podrían no tener items (aunque es improbable)
   - Filtra por `category_rank = 1` para obtener solo la categoría principal
   - Ordena por `total_revenue DESC` y limita a 10 resultados

**Nota