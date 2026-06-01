# DeepSeek V4 Flash (OpenRouter) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.48 | quality: 9.8
- latency_total: 20.217s | tokens_per_second: 39.0
- input_tokens: 152 | output_tokens: 788
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la query SQL que cumple con todos los requisitos:

```sql
WITH customer_stats AS (
    -- Calculamos estadísticas por cliente
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) as total_orders,
        SUM(o.total) as total_revenue,
        AVG(o.total) as avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE 
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_categories AS (
    -- Encontramos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) as total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE 
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
-- Query final con los resultados
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    ROUND(cs.total_revenue, 2) as total_revenue,
    ROUND(cs.avg_order_value, 2) as avg_order_value,
    cc.category as categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_categories cc ON cs.id = cc.customer_id AND cc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**Explicación de la query:**

1. **CTE `customer_stats`**: Calcula las métricas principales por cliente:
   - Total de órdenes completadas
   - Revenue total (suma de totales de órdenes)
   - Valor promedio por orden
   - Filtra solo órdenes completadas en los últimos 6 meses
   - Solo clientes con 3+ órdenes completadas

2. **CTE `customer_categories`**: Determina la categoría más comprada por cada cliente:
   - Suma las cantidades por categoría
   - Usa `ROW_NUMBER()` para identificar la categoría con mayor cantidad
   - Filtra por el mismo período y estado que las órdenes

3. **Query principal**: 
   - Une ambos CTEs
   - Selecciona solo la categoría principal (rn = 1)
   - Ordena por revenue total descendente
   - Limita a los top 10 clientes

**Notas importantes:**
- La función `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)` es para MySQL. Para otros motores de BD, ajusta la sintaxis:
  - PostgreSQL: `CURRENT_DATE - INTERVAL '6 months'`
  - SQL Server: `DATEADD(MONTH, -6, GETDATE())`
  - SQLite: `DATE('now', '-6 months')`
- Se usa `ROUND()` para formatear los valores monetarios a 2 decimales
- El `LEFT JOIN` asegura que todos los clientes aparezcan incluso si no tienen categoría asignada