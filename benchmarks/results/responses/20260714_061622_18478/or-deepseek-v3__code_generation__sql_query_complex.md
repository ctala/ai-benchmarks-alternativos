# DeepSeek V3 — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 7.87 | quality: 8.4
- latency_total: 16.57s | tokens_per_second: 42.2
- input_tokens: 152 | output_tokens: 700
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH customer_stats AS (
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email AS email,
        c.country AS pais,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
top_categories AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) AS rank_cat
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
SELECT 
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN top_categories tc ON cs.customer_id = tc.customer_id
    AND tc.rank_cat = diccionario1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Explicación de la consulta:**

1. **CTE `customer_stats`**: Calcula las métricas básicas por cliente:
   - Filtra órdenes completadas en los últimos 6 meses
   - Agrupa por cliente
   - Filtra clientes con al menos 3 órdenes completadas (usando HAVING)

2. **CTE `top_categories`**: Identifica la categoría más comprada por cada cliente:
   - Calcula la cantidad total comprada por categoría
   - Usa ROW_NUMBER() para rankear categorías por cliente
   - El ranking 1 corresponde a la categoría más comprada

3. **Consulta principal**: Une ambas CTEs y selecciona las columnas requeridas:
   - Toma la categoría con rank_cat = 1 (la más comprada)
   - Ordena por total_revenue descendente
   - Limita a los 10 primeros resultados

**Notas importantes:**
- La consulta asume que `orders.total` ya representa el revenue total de la orden
- Si `orders.total` no existe o no es confiable, puedes calcularlo como `SUM(oi.quantity * oi.unit_price)` en el primer CTE
- El cálculo de "categoría más comprada" se basa en la cantidad total de productos, no en el valor monetario