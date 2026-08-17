# DeepSeek V4 Flash (NIM) — code_generation/sql_query_complex

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.53 | quality: 9.52
- latency_total: 21.756s | tokens_per_second: 32.3
- input_tokens: 152 | output_tokens: 702
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la query SQL que resuelve tu requerimiento:

```sql
WITH customer_metrics AS (
    -- Obtener métricas básicas por cliente
    SELECT 
        c.id as customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) as total_orders,
        SUM(o.total) as total_revenue,
        AVG(o.total) as avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_categories AS (
    -- Obtener la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) as total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    ROUND(cm.total_revenue, 2) as total_revenue,
    ROUND(cm.avg_order_value, 2) as avg_order_value,
    cc.category as categoria_mas_comprada
FROM customer_metrics cm
INNER JOIN customer_categories cc ON cm.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

**Explicación de la query:**

1. **CTE `customer_metrics`**: Calcula las métricas principales por cliente:
   - Total de órdenes completadas
   - Revenue total
   - Valor promedio de orden
   - Filtra por órdenes completadas en los últimos 6 meses
   - Solo incluye clientes con 3+ órdenes completadas

2. **CTE `customer_categories`**: Determina la categoría más comprada por cada cliente:
   - Calcula la cantidad total comprada por categoría
   - Usa `ROW_NUMBER()` para rankear las categorías por cantidad
   - Selecciona la categoría con rango 1 (más comprada)

3. **Query final**: Une ambas CTEs y selecciona el Top 10 ordenado por revenue descendente

**Notas importantes:**
- La query asume que `CURRENT_DATE` es la fecha actual de tu base de datos
- Los montos se redondean a 2 decimales para mejor presentación
- Si un cliente tiene exactamente el mismo revenue que otro, el orden puede variar (podrías agregar criterios de desempate si es necesario)